# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from loop_rpc.protos import loop_client_pb2 as loop__rpc_dot_protos_dot_loop__client__pb2


class SwapClientStub(object):
    """*
    SwapClient is a service that handles the client side process of onchain/offchain
    swaps. The service is designed for a single client.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
          channel: A grpc.Channel.
        """
        self.LoopOut = channel.unary_unary(
                '/looprpc.SwapClient/LoopOut',
                request_serializer=loop__rpc_dot_protos_dot_loop__client__pb2.LoopOutRequest.SerializeToString,
                response_deserializer=loop__rpc_dot_protos_dot_loop__client__pb2.SwapResponse.FromString,
        )
        self.LoopIn = channel.unary_unary(
                '/looprpc.SwapClient/LoopIn',
                request_serializer=loop__rpc_dot_protos_dot_loop__client__pb2.LoopInRequest.SerializeToString,
                response_deserializer=loop__rpc_dot_protos_dot_loop__client__pb2.SwapResponse.FromString,
        )
        self.Monitor = channel.unary_stream(
                '/looprpc.SwapClient/Monitor',
                request_serializer=loop__rpc_dot_protos_dot_loop__client__pb2.MonitorRequest.SerializeToString,
                response_deserializer=loop__rpc_dot_protos_dot_loop__client__pb2.SwapStatus.FromString,
        )
        self.LoopOutTerms = channel.unary_unary(
                '/looprpc.SwapClient/LoopOutTerms',
                request_serializer=loop__rpc_dot_protos_dot_loop__client__pb2.TermsRequest.SerializeToString,
                response_deserializer=loop__rpc_dot_protos_dot_loop__client__pb2.TermsResponse.FromString,
        )
        self.LoopOutQuote = channel.unary_unary(
                '/looprpc.SwapClient/LoopOutQuote',
                request_serializer=loop__rpc_dot_protos_dot_loop__client__pb2.QuoteRequest.SerializeToString,
                response_deserializer=loop__rpc_dot_protos_dot_loop__client__pb2.QuoteResponse.FromString,
        )
        self.GetLoopInTerms = channel.unary_unary(
                '/looprpc.SwapClient/GetLoopInTerms',
                request_serializer=loop__rpc_dot_protos_dot_loop__client__pb2.TermsRequest.SerializeToString,
                response_deserializer=loop__rpc_dot_protos_dot_loop__client__pb2.TermsResponse.FromString,
        )
        self.GetLoopInQuote = channel.unary_unary(
                '/looprpc.SwapClient/GetLoopInQuote',
                request_serializer=loop__rpc_dot_protos_dot_loop__client__pb2.QuoteRequest.SerializeToString,
                response_deserializer=loop__rpc_dot_protos_dot_loop__client__pb2.QuoteResponse.FromString,
        )


class SwapClientServicer(object):
    """*
    SwapClient is a service that handles the client side process of onchain/offchain
    swaps. The service is designed for a single client.
    """

    def LoopOut(self, request, context):
        """* loop: `out`
        LoopOut initiates an loop out swap with the given parameters. The call
        returns after the swap has been set up with the swap server. From that
        point onwards, progress can be tracked via the SwapStatus stream that is
        returned from Monitor().
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LoopIn(self, request, context):
        """*
        LoopIn initiates a loop in swap with the given parameters. The call
        returns after the swap has been set up with the swap server. From that
        point onwards, progress can be tracked via the SwapStatus stream
        that is returned from Monitor().
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Monitor(self, request, context):
        """* loop: `monitor`
        Monitor will return a stream of swap updates for currently active swaps.
        TODO: add MonitorSync version for REST clients.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LoopOutTerms(self, request, context):
        """* loop: `terms`
        LoopOutTerms returns the terms that the server enforces for a loop out swap.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LoopOutQuote(self, request, context):
        """* loop: `quote`
        LoopOutQuote returns a quote for a loop out swap with the provided
        parameters.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLoopInTerms(self, request, context):
        """*
        GetTerms returns the terms that the server enforces for swaps.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLoopInQuote(self, request, context):
        """*
        GetQuote returns a quote for a swap with the provided parameters.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SwapClientServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'LoopOut': grpc.unary_unary_rpc_method_handler(
                servicer.LoopOut,
                request_deserializer=loop__rpc_dot_protos_dot_loop__client__pb2.LoopOutRequest.FromString,
                response_serializer=loop__rpc_dot_protos_dot_loop__client__pb2.SwapResponse.SerializeToString,
        ),
        'LoopIn': grpc.unary_unary_rpc_method_handler(
                servicer.LoopIn,
                request_deserializer=loop__rpc_dot_protos_dot_loop__client__pb2.LoopInRequest.FromString,
                response_serializer=loop__rpc_dot_protos_dot_loop__client__pb2.SwapResponse.SerializeToString,
        ),
        'Monitor': grpc.unary_stream_rpc_method_handler(
                servicer.Monitor,
                request_deserializer=loop__rpc_dot_protos_dot_loop__client__pb2.MonitorRequest.FromString,
                response_serializer=loop__rpc_dot_protos_dot_loop__client__pb2.SwapStatus.SerializeToString,
        ),
        'LoopOutTerms': grpc.unary_unary_rpc_method_handler(
                servicer.LoopOutTerms,
                request_deserializer=loop__rpc_dot_protos_dot_loop__client__pb2.TermsRequest.FromString,
                response_serializer=loop__rpc_dot_protos_dot_loop__client__pb2.TermsResponse.SerializeToString,
        ),
        'LoopOutQuote': grpc.unary_unary_rpc_method_handler(
                servicer.LoopOutQuote,
                request_deserializer=loop__rpc_dot_protos_dot_loop__client__pb2.QuoteRequest.FromString,
                response_serializer=loop__rpc_dot_protos_dot_loop__client__pb2.QuoteResponse.SerializeToString,
        ),
        'GetLoopInTerms': grpc.unary_unary_rpc_method_handler(
                servicer.GetLoopInTerms,
                request_deserializer=loop__rpc_dot_protos_dot_loop__client__pb2.TermsRequest.FromString,
                response_serializer=loop__rpc_dot_protos_dot_loop__client__pb2.TermsResponse.SerializeToString,
        ),
        'GetLoopInQuote': grpc.unary_unary_rpc_method_handler(
                servicer.GetLoopInQuote,
                request_deserializer=loop__rpc_dot_protos_dot_loop__client__pb2.QuoteRequest.FromString,
                response_serializer=loop__rpc_dot_protos_dot_loop__client__pb2.QuoteResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'looprpc.SwapClient', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
