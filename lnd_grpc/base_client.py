import codecs
import sys
from os import environ

import grpc

import lnd_grpc.protos.rpc_pb2 as ln
from lnd_grpc.utilities import get_lnd_dir

# tell gRPC which cypher suite to use
environ["GRPC_SSL_CIPHER_SUITES"] = 'HIGH+ECDSA'


class BaseClient:
    def __init__(self,
                 lnd_dir: str = None,
                 macaroon_path: str = None,
                 tls_cert_path: str = None,
                 network: str = 'mainnet',
                 grpc_host: str = 'localhost',
                 grpc_port: str = '10009'):

        self.lnd_dir = lnd_dir
        self.macaroon_path = macaroon_path
        self.tls_cert_path = tls_cert_path
        self.network = network
        self.grpc_host = grpc_host
        self.grpc_port = grpc_port
        self.channel = None
        self.connection_status = None
        self.connection_status_change = False
        self.grpc_options = [
            ('grpc.max_receive_message_length', 33554432),
            ('grpc.max_send_message_length', 33554432),
        ]

    @property
    def lnd_dir(self):
        if self._lnd_dir:
            return self._lnd_dir
        else:
            self._lnd_dir = get_lnd_dir()
            return self._lnd_dir

    @lnd_dir.setter
    def lnd_dir(self, path):
        self._lnd_dir = path

    @property
    def tls_cert_path(self):
        if self._tls_cert_path is None:
            self._tls_cert_path = self.lnd_dir + 'tls.cert'
        return self._tls_cert_path

    @tls_cert_path.setter
    def tls_cert_path(self, path):
        self._tls_cert_path = path

    @property
    def tls_cert_key(self) -> bytes:
        try:
            with open(self.tls_cert_path, 'rb') as r:
                tls_cert_key = r.read()
        except FileNotFoundError:
            sys.stderr.write("TLS cert not found at %s" % self.tls_cert_path)
            raise
        try:
            assert tls_cert_key.startswith(b'-----BEGIN CERTIFICATE-----')
            return tls_cert_key
        except (AssertionError, AttributeError):
            sys.stderr.write("TLS cert at %s did not start with b'-----BEGIN CERTIFICATE-----')"
                             % self.tls_cert_path)
            raise

    @property
    def macaroon_path(self) -> str:
        if not self._macaroon_path:
            self._macaroon_path = self.lnd_dir + \
                                  'data/chain/bitcoin/%s/admin.macaroon' \
                                  % self.network
            return self._macaroon_path
        else:
            return self._macaroon_path

    @macaroon_path.setter
    def macaroon_path(self, path: str):
        self._macaroon_path = path

    @property
    def macaroon(self):
        try:
            with open(self.macaroon_path, 'rb') as f:
                macaroon_bytes = f.read()
                macaroon = codecs.encode(macaroon_bytes, 'hex')
                return macaroon
        except FileNotFoundError:
            sys.stderr.write(f"Could not find macaroon in {self.macaroon_path}. This might happen"
                             f"in versions of lnd < v0.5-beta or those not using default"
                             f"installation path. Set client object's macaroon_path attribute"
                             f"manually.")

    # noinspection PyUnusedLocal
    def metadata_callback(self, context, callback):
        callback([('macaroon', self.macaroon)], None)

    def connectivity_event_logger(self, channel_connectivity):
        self.connection_status = channel_connectivity._name_
        if self.connection_status == 'SHUTDOWN' or self.connection_status == 'TRANSIENT_FAILURE':
            self.connection_status_change = True

    @property
    def combined_credentials(self) -> grpc.CallCredentials:
        cert_creds = grpc.ssl_channel_credentials(self.tls_cert_key)
        auth_creds = grpc.metadata_call_credentials(self.metadata_callback)
        return grpc.composite_channel_credentials(cert_creds, auth_creds)

    @property
    def grpc_address(self) -> str:
        return str(self.grpc_host + ':' + self.grpc_port)

    @staticmethod
    def channel_point_generator(funding_txid, output_index):
        return ln.ChannelPoint(funding_txid_str=funding_txid, output_index=int(output_index))

    @staticmethod
    def lightning_address(pubkey, host):
        return ln.LightningAddress(pubkey=pubkey, host=host)

    @staticmethod
    def hex_to_bytes(hex_string: str):
        return bytes.fromhex(hex_string)

    @staticmethod
    def bytes_to_hex(bytestring: bytes):
        return bytestring.hex()

    @staticmethod
    def pack_into_channelbackups(single_backup):
        """
        This function will accept either an ln.ChannelBackup object as generated by
        export_chan_backup() or should be passed a single channel backup from
        export_all_channel_backups().single_chan_backups[index].

        It will then return a single channel backup packed into a ChannelBackups
        format as required by verify_chan_backup()
        """
        return ln.ChannelBackups(chan_backups=[single_backup])
