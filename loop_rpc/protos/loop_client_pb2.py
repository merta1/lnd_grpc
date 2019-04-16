# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: loop_rpc/protos/loop_client.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
        name='loop_rpc/protos/loop_client.proto',
        package='looprpc',
        syntax='proto3',
        serialized_options=None,
        serialized_pb=_b(
            '\n!loop_rpc/protos/loop_client.proto\x12\x07looprpc\x1a\x1cgoogle/api/annotations.proto\"\xc8\x01\n\x0eLoopOutRequest\x12\x0b\n\x03\x61mt\x18\x01 \x01(\x03\x12\x0c\n\x04\x64\x65st\x18\x02 \x01(\t\x12\x1c\n\x14max_swap_routing_fee\x18\x03 \x01(\x03\x12\x1e\n\x16max_prepay_routing_fee\x18\x04 \x01(\x03\x12\x14\n\x0cmax_swap_fee\x18\x05 \x01(\x03\x12\x16\n\x0emax_prepay_amt\x18\x06 \x01(\x03\x12\x15\n\rmax_miner_fee\x18\x07 \x01(\x03\x12\x18\n\x10loop_out_channel\x18\x08 \x01(\x04\"y\n\rLoopInRequest\x12\x0b\n\x03\x61mt\x18\x01 \x01(\x03\x12\x14\n\x0cmax_swap_fee\x18\x02 \x01(\x03\x12\x15\n\rmax_miner_fee\x18\x03 \x01(\x03\x12\x17\n\x0floop_in_channel\x18\x04 \x01(\x04\x12\x15\n\rexternal_htlc\x18\x05 \x01(\x08\"0\n\x0cSwapResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x0chtlc_address\x18\x02 \x01(\t\"\x10\n\x0eMonitorRequest\"\xb2\x01\n\nSwapStatus\x12\x0b\n\x03\x61mt\x18\x01 \x01(\x03\x12\n\n\x02id\x18\x02 \x01(\t\x12\x1f\n\x04type\x18\x03 \x01(\x0e\x32\x11.looprpc.SwapType\x12!\n\x05state\x18\x04 \x01(\x0e\x32\x12.looprpc.SwapState\x12\x17\n\x0finitiation_time\x18\x05 \x01(\x03\x12\x18\n\x10last_update_time\x18\x06 \x01(\x03\x12\x14\n\x0chtlc_address\x18\x07 \x01(\t\"\x0e\n\x0cTermsRequest\"\xb2\x01\n\rTermsResponse\x12\x19\n\x11swap_payment_dest\x18\x01 \x01(\t\x12\x15\n\rswap_fee_base\x18\x02 \x01(\x03\x12\x15\n\rswap_fee_rate\x18\x03 \x01(\x03\x12\x12\n\nprepay_amt\x18\x04 \x01(\x03\x12\x17\n\x0fmin_swap_amount\x18\x05 \x01(\x03\x12\x17\n\x0fmax_swap_amount\x18\x06 \x01(\x03\x12\x12\n\ncltv_delta\x18\x07 \x01(\x05\"\x1b\n\x0cQuoteRequest\x12\x0b\n\x03\x61mt\x18\x01 \x01(\x03\"H\n\rQuoteResponse\x12\x10\n\x08swap_fee\x18\x01 \x01(\x03\x12\x12\n\nprepay_amt\x18\x02 \x01(\x03\x12\x11\n\tminer_fee\x18\x03 \x01(\x03*%\n\x08SwapType\x12\x0c\n\x08LOOP_OUT\x10\x00\x12\x0b\n\x07LOOP_IN\x10\x01*s\n\tSwapState\x12\r\n\tINITIATED\x10\x00\x12\x15\n\x11PREIMAGE_REVEALED\x10\x01\x12\x12\n\x0eHTLC_PUBLISHED\x10\x02\x12\x0b\n\x07SUCCESS\x10\x03\x12\n\n\x06\x46\x41ILED\x10\x04\x12\x13\n\x0fINVOICE_SETTLED\x10\x05\x32\x92\x04\n\nSwapClient\x12R\n\x07LoopOut\x12\x17.looprpc.LoopOutRequest\x1a\x15.looprpc.SwapResponse\"\x17\x82\xd3\xe4\x93\x02\x11\"\x0c/v1/loop/out:\x01*\x12\x37\n\x06LoopIn\x12\x16.looprpc.LoopInRequest\x1a\x15.looprpc.SwapResponse\x12\x39\n\x07Monitor\x12\x17.looprpc.MonitorRequest\x1a\x13.looprpc.SwapStatus0\x01\x12Y\n\x0cLoopOutTerms\x12\x15.looprpc.TermsRequest\x1a\x16.looprpc.TermsResponse\"\x1a\x82\xd3\xe4\x93\x02\x14\x12\x12/v1/loop/out/terms\x12_\n\x0cLoopOutQuote\x12\x15.looprpc.QuoteRequest\x1a\x16.looprpc.QuoteResponse\" \x82\xd3\xe4\x93\x02\x1a\x12\x18/v1/loop/out/quote/{amt}\x12?\n\x0eGetLoopInTerms\x12\x15.looprpc.TermsRequest\x1a\x16.looprpc.TermsResponse\x12?\n\x0eGetLoopInQuote\x12\x15.looprpc.QuoteRequest\x1a\x16.looprpc.QuoteResponseb\x06proto3')
        ,
        dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR, ])

_SWAPTYPE = _descriptor.EnumDescriptor(
        name='SwapType',
        full_name='looprpc.SwapType',
        filename=None,
        file=DESCRIPTOR,
        values=[
            _descriptor.EnumValueDescriptor(
                    name='LOOP_OUT', index=0, number=0,
                    serialized_options=None,
                    type=None),
            _descriptor.EnumValueDescriptor(
                    name='LOOP_IN', index=1, number=1,
                    serialized_options=None,
                    type=None),
        ],
        containing_type=None,
        serialized_options=None,
        serialized_start=951,
        serialized_end=988,
)
_sym_db.RegisterEnumDescriptor(_SWAPTYPE)

SwapType = enum_type_wrapper.EnumTypeWrapper(_SWAPTYPE)
_SWAPSTATE = _descriptor.EnumDescriptor(
        name='SwapState',
        full_name='looprpc.SwapState',
        filename=None,
        file=DESCRIPTOR,
        values=[
            _descriptor.EnumValueDescriptor(
                    name='INITIATED', index=0, number=0,
                    serialized_options=None,
                    type=None),
            _descriptor.EnumValueDescriptor(
                    name='PREIMAGE_REVEALED', index=1, number=1,
                    serialized_options=None,
                    type=None),
            _descriptor.EnumValueDescriptor(
                    name='HTLC_PUBLISHED', index=2, number=2,
                    serialized_options=None,
                    type=None),
            _descriptor.EnumValueDescriptor(
                    name='SUCCESS', index=3, number=3,
                    serialized_options=None,
                    type=None),
            _descriptor.EnumValueDescriptor(
                    name='FAILED', index=4, number=4,
                    serialized_options=None,
                    type=None),
            _descriptor.EnumValueDescriptor(
                    name='INVOICE_SETTLED', index=5, number=5,
                    serialized_options=None,
                    type=None),
        ],
        containing_type=None,
        serialized_options=None,
        serialized_start=990,
        serialized_end=1105,
)
_sym_db.RegisterEnumDescriptor(_SWAPSTATE)

SwapState = enum_type_wrapper.EnumTypeWrapper(_SWAPSTATE)
LOOP_OUT = 0
LOOP_IN = 1
INITIATED = 0
PREIMAGE_REVEALED = 1
HTLC_PUBLISHED = 2
SUCCESS = 3
FAILED = 4
INVOICE_SETTLED = 5

_LOOPOUTREQUEST = _descriptor.Descriptor(
        name='LoopOutRequest',
        full_name='looprpc.LoopOutRequest',
        filename=None,
        file=DESCRIPTOR,
        containing_type=None,
        fields=[
            _descriptor.FieldDescriptor(
                    name='amt', full_name='looprpc.LoopOutRequest.amt', index=0,
                    number=1, type=3, cpp_type=2, label=1,
                    has_default_value=False, default_value=0,
                    message_type=None, enum_type=None, containing_type=None,
                    is_extension=False, extension_scope=None,
                    serialized_options=None, file=DESCRIPTOR),
            _descriptor.FieldDescriptor(
                    name='dest', full_name='looprpc.LoopOutRequest.dest', index=1,
                    number=2, type=9, cpp_type=9, label=1,
                    has_default_value=False, default_value=_b("").decode('utf-8'),
                    message_type=None, enum_type=None, containing_type=None,
                    is_extension=False, extension_scope=None,
                    serialized_options=None, file=DESCRIPTOR),
            _descriptor.FieldDescriptor(
                    name='max_swap_routing_fee',
                    full_name='looprpc.LoopOutRequest.max_swap_routing_fee', index=2,
                    number=3, type=3, cpp_type=2, label=1,
                    has_default_value=False, default_value=0,
                    message_type=None, enum_type=None, containing_type=None,
                    is_extension=False, extension_scope=None,
                    serialized_options=None, file=DESCRIPTOR),
            _descriptor.FieldDescriptor(
                    name='max_prepay_routing_fee',
                    full_name='looprpc.LoopOutRequest.max_prepay_routing_fee', index=3,
                    number=4, type=3, cpp_type=2, label=1,
                    has_default_value=False, default_value=0,
                    message_type=None, enum_type=None, containing_type=None,
                    is_extension=False, extension_scope=None,
                    serialized_options=None, file=DESCRIPTOR),
            _descriptor.FieldDescriptor(
                    name='max_swap_fee', full_name='looprpc.LoopOutRequest.max_swap_fee', index=4,
                    number=5, type=3, cpp_type=2, label=1,
                    has_default_value=False, default_value=0,
                    message_type=None, enum_type=None, containing_type=None,
                    is_extension=False, extension_scope=None,
                    serialized_options=None, file=DESCRIPTOR),
            _descriptor.FieldDescriptor(
                    name='max_prepay_amt', full_name='looprpc.LoopOutRequest.max_prepay_amt',
                    index=5,
                    number=6, type=3, cpp_type=2, label=1,
                    has_default_value=False, default_value=0,
                    message_type=None, enum_type=None, containing_type=None,
                    is_extension=False, extension_scope=None,
                    serialized_options=None, file=DESCRIPTOR),
            _descriptor.FieldDescriptor(
                    name='max_miner_fee', full_name='looprpc.LoopOutRequest.max_miner_fee', index=6,
                    number=7, type=3, cpp_type=2, label=1,
                    has_default_value=False, default_value=0,
                    message_type=None, enum_type=None, containing_type=None,
                    is_extension=False, extension_scope=None,
                    serialized_options=None, file=DESCRIPTOR),
            _descriptor.FieldDescriptor(
                    name='loop_out_channel', full_name='looprpc.LoopOutRequest.loop_out_channel',
                    index=7,
                    number=8, type=4, cpp_type=4, label=1,
                    has_default_value=False, default_value=0,
                    message_type=None, enum_type=None, containing_type=None,
                    is_extension=False, extension_scope=None,
                    serialized_options=None, file=DESCRIPTOR),
        ],
        extensions=[
        ],
        nested_types=[],
        enum_types=[
        ],
        serialized_options=None,
        is_extendable=False,
        syntax='proto3',
        extension_ranges=[],
        oneofs=[
        ],
        serialized_start=77,
        serialized_end=277,
)


_LOOPINREQUEST = _descriptor.Descriptor(
        name='LoopInRequest',
        full_name='looprpc.LoopInRequest',
        filename=None,
        file=DESCRIPTOR,
        containing_type=None,
        fields=[
            _descriptor.FieldDescriptor(
                    name='amt', full_name='looprpc.LoopInRequest.amt', index=0,
                    number=1, type=3, cpp_type=2, label=1,
                    has_default_value=False, default_value=0,
                    message_type=None, enum_type=None, containing_type=None,
                    is_extension=False, extension_scope=None,
                    serialized_options=None, file=DESCRIPTOR),
            _descriptor.FieldDescriptor(
                    name='max_swap_fee', full_name='looprpc.LoopInRequest.max_swap_fee', index=1,
                    number=2, type=3, cpp_type=2, label=1,
                    has_default_value=False, default_value=0,
                    message_type=None, enum_type=None, containing_type=None,
                    is_extension=False, extension_scope=None,
                    serialized_options=None, file=DESCRIPTOR),
            _descriptor.FieldDescriptor(
                    name='max_miner_fee', full_name='looprpc.LoopInRequest.max_miner_fee', index=2,
                    number=3, type=3, cpp_type=2, label=1,
                    has_default_value=False, default_value=0,
                    message_type=None, enum_type=None, containing_type=None,
                    is_extension=False, extension_scope=None,
                    serialized_options=None, file=DESCRIPTOR),
            _descriptor.FieldDescriptor(
                    name='loop_in_channel', full_name='looprpc.LoopInRequest.loop_in_channel',
                    index=3,
                    number=4, type=4, cpp_type=4, label=1,
                    has_default_value=False, default_value=0,
                    message_type=None, enum_type=None, containing_type=None,
                    is_extension=False, extension_scope=None,
                    serialized_options=None, file=DESCRIPTOR),
            _descriptor.FieldDescriptor(
                    name='external_htlc', full_name='looprpc.LoopInRequest.external_htlc', index=4,
                    number=5, type=8, cpp_type=7, label=1,
                    has_default_value=False, default_value=False,
                    message_type=None, enum_type=None, containing_type=None,
                    is_extension=False, extension_scope=None,
                    serialized_options=None, file=DESCRIPTOR),
        ],
        extensions=[
        ],
        nested_types=[],
        enum_types=[
        ],
        serialized_options=None,
        is_extendable=False,
        syntax='proto3',
        extension_ranges=[],
        oneofs=[
        ],
        serialized_start=279,
        serialized_end=400,
)


_SWAPRESPONSE = _descriptor.Descriptor(
        name='SwapResponse',
        full_name='looprpc.SwapResponse',
        filename=None,
        file=DESCRIPTOR,
        containing_type=None,
        fields=[
            _descriptor.FieldDescriptor(
                    name='id', full_name='looprpc.SwapResponse.id', index=0,
                    number=1, type=9, cpp_type=9, label=1,
                    has_default_value=False, default_value=_b("").decode('utf-8'),
                    message_type=None, enum_type=None, containing_type=None,
                    is_extension=False, extension_scope=None,
                    serialized_options=None, file=DESCRIPTOR),
            _descriptor.FieldDescriptor(
                    name='htlc_address', full_name='looprpc.SwapResponse.htlc_address', index=1,
                    number=2, type=9, cpp_type=9, label=1,
                    has_default_value=False, default_value=_b("").decode('utf-8'),
                    message_type=None, enum_type=None, containing_type=None,
                    is_extension=False, extension_scope=None,
                    serialized_options=None, file=DESCRIPTOR),
        ],
        extensions=[
        ],
        nested_types=[],
        enum_types=[
        ],
        serialized_options=None,
        is_extendable=False,
        syntax='proto3',
        extension_ranges=[],
        oneofs=[
        ],
        serialized_start=402,
        serialized_end=450,
)


_MONITORREQUEST = _descriptor.Descriptor(
        name='MonitorRequest',
        full_name='looprpc.MonitorRequest',
        filename=None,
        file=DESCRIPTOR,
        containing_type=None,
        fields=[
        ],
        extensions=[
        ],
        nested_types=[],
        enum_types=[
        ],
        serialized_options=None,
        is_extendable=False,
        syntax='proto3',
        extension_ranges=[],
        oneofs=[
        ],
        serialized_start=452,
        serialized_end=468,
)


_SWAPSTATUS = _descriptor.Descriptor(
        name='SwapStatus',
        full_name='looprpc.SwapStatus',
        filename=None,
        file=DESCRIPTOR,
        containing_type=None,
        fields=[
            _descriptor.FieldDescriptor(
                    name='amt', full_name='looprpc.SwapStatus.amt', index=0,
                    number=1, type=3, cpp_type=2, label=1,
                    has_default_value=False, default_value=0,
                    message_type=None, enum_type=None, containing_type=None,
                    is_extension=False, extension_scope=None,
                    serialized_options=None, file=DESCRIPTOR),
            _descriptor.FieldDescriptor(
                    name='id', full_name='looprpc.SwapStatus.id', index=1,
                    number=2, type=9, cpp_type=9, label=1,
                    has_default_value=False, default_value=_b("").decode('utf-8'),
                    message_type=None, enum_type=None, containing_type=None,
                    is_extension=False, extension_scope=None,
                    serialized_options=None, file=DESCRIPTOR),
            _descriptor.FieldDescriptor(
                    name='type', full_name='looprpc.SwapStatus.type', index=2,
                    number=3, type=14, cpp_type=8, label=1,
                    has_default_value=False, default_value=0,
                    message_type=None, enum_type=None, containing_type=None,
                    is_extension=False, extension_scope=None,
                    serialized_options=None, file=DESCRIPTOR),
            _descriptor.FieldDescriptor(
                    name='state', full_name='looprpc.SwapStatus.state', index=3,
                    number=4, type=14, cpp_type=8, label=1,
                    has_default_value=False, default_value=0,
                    message_type=None, enum_type=None, containing_type=None,
                    is_extension=False, extension_scope=None,
                    serialized_options=None, file=DESCRIPTOR),
            _descriptor.FieldDescriptor(
                    name='initiation_time', full_name='looprpc.SwapStatus.initiation_time', index=4,
                    number=5, type=3, cpp_type=2, label=1,
                    has_default_value=False, default_value=0,
                    message_type=None, enum_type=None, containing_type=None,
                    is_extension=False, extension_scope=None,
                    serialized_options=None, file=DESCRIPTOR),
            _descriptor.FieldDescriptor(
                    name='last_update_time', full_name='looprpc.SwapStatus.last_update_time',
                    index=5,
                    number=6, type=3, cpp_type=2, label=1,
                    has_default_value=False, default_value=0,
                    message_type=None, enum_type=None, containing_type=None,
                    is_extension=False, extension_scope=None,
                    serialized_options=None, file=DESCRIPTOR),
            _descriptor.FieldDescriptor(
                    name='htlc_address', full_name='looprpc.SwapStatus.htlc_address', index=6,
                    number=7, type=9, cpp_type=9, label=1,
                    has_default_value=False, default_value=_b("").decode('utf-8'),
                    message_type=None, enum_type=None, containing_type=None,
                    is_extension=False, extension_scope=None,
                    serialized_options=None, file=DESCRIPTOR),
        ],
        extensions=[
        ],
        nested_types=[],
        enum_types=[
        ],
        serialized_options=None,
        is_extendable=False,
        syntax='proto3',
        extension_ranges=[],
        oneofs=[
        ],
        serialized_start=471,
        serialized_end=649,
)


_TERMSREQUEST = _descriptor.Descriptor(
        name='TermsRequest',
        full_name='looprpc.TermsRequest',
        filename=None,
        file=DESCRIPTOR,
        containing_type=None,
        fields=[
        ],
        extensions=[
        ],
        nested_types=[],
        enum_types=[
        ],
        serialized_options=None,
        is_extendable=False,
        syntax='proto3',
        extension_ranges=[],
        oneofs=[
        ],
        serialized_start=651,
        serialized_end=665,
)


_TERMSRESPONSE = _descriptor.Descriptor(
        name='TermsResponse',
        full_name='looprpc.TermsResponse',
        filename=None,
        file=DESCRIPTOR,
        containing_type=None,
        fields=[
            _descriptor.FieldDescriptor(
                    name='swap_payment_dest', full_name='looprpc.TermsResponse.swap_payment_dest',
                    index=0,
                    number=1, type=9, cpp_type=9, label=1,
                    has_default_value=False, default_value=_b("").decode('utf-8'),
                    message_type=None, enum_type=None, containing_type=None,
                    is_extension=False, extension_scope=None,
                    serialized_options=None, file=DESCRIPTOR),
            _descriptor.FieldDescriptor(
                    name='swap_fee_base', full_name='looprpc.TermsResponse.swap_fee_base', index=1,
                    number=2, type=3, cpp_type=2, label=1,
                    has_default_value=False, default_value=0,
                    message_type=None, enum_type=None, containing_type=None,
                    is_extension=False, extension_scope=None,
                    serialized_options=None, file=DESCRIPTOR),
            _descriptor.FieldDescriptor(
                    name='swap_fee_rate', full_name='looprpc.TermsResponse.swap_fee_rate', index=2,
                    number=3, type=3, cpp_type=2, label=1,
                    has_default_value=False, default_value=0,
                    message_type=None, enum_type=None, containing_type=None,
                    is_extension=False, extension_scope=None,
                    serialized_options=None, file=DESCRIPTOR),
            _descriptor.FieldDescriptor(
                    name='prepay_amt', full_name='looprpc.TermsResponse.prepay_amt', index=3,
                    number=4, type=3, cpp_type=2, label=1,
                    has_default_value=False, default_value=0,
                    message_type=None, enum_type=None, containing_type=None,
                    is_extension=False, extension_scope=None,
                    serialized_options=None, file=DESCRIPTOR),
            _descriptor.FieldDescriptor(
                    name='min_swap_amount', full_name='looprpc.TermsResponse.min_swap_amount',
                    index=4,
                    number=5, type=3, cpp_type=2, label=1,
                    has_default_value=False, default_value=0,
                    message_type=None, enum_type=None, containing_type=None,
                    is_extension=False, extension_scope=None,
                    serialized_options=None, file=DESCRIPTOR),
            _descriptor.FieldDescriptor(
                    name='max_swap_amount', full_name='looprpc.TermsResponse.max_swap_amount',
                    index=5,
                    number=6, type=3, cpp_type=2, label=1,
                    has_default_value=False, default_value=0,
                    message_type=None, enum_type=None, containing_type=None,
                    is_extension=False, extension_scope=None,
                    serialized_options=None, file=DESCRIPTOR),
            _descriptor.FieldDescriptor(
                    name='cltv_delta', full_name='looprpc.TermsResponse.cltv_delta', index=6,
                    number=7, type=5, cpp_type=1, label=1,
                    has_default_value=False, default_value=0,
                    message_type=None, enum_type=None, containing_type=None,
                    is_extension=False, extension_scope=None,
                    serialized_options=None, file=DESCRIPTOR),
        ],
        extensions=[
        ],
        nested_types=[],
        enum_types=[
        ],
        serialized_options=None,
        is_extendable=False,
        syntax='proto3',
        extension_ranges=[],
        oneofs=[
        ],
        serialized_start=668,
        serialized_end=846,
)


_QUOTEREQUEST = _descriptor.Descriptor(
        name='QuoteRequest',
        full_name='looprpc.QuoteRequest',
        filename=None,
        file=DESCRIPTOR,
        containing_type=None,
        fields=[
            _descriptor.FieldDescriptor(
                    name='amt', full_name='looprpc.QuoteRequest.amt', index=0,
                    number=1, type=3, cpp_type=2, label=1,
                    has_default_value=False, default_value=0,
                    message_type=None, enum_type=None, containing_type=None,
                    is_extension=False, extension_scope=None,
                    serialized_options=None, file=DESCRIPTOR),
        ],
        extensions=[
        ],
        nested_types=[],
        enum_types=[
        ],
        serialized_options=None,
        is_extendable=False,
        syntax='proto3',
        extension_ranges=[],
        oneofs=[
        ],
        serialized_start=848,
        serialized_end=875,
)


_QUOTERESPONSE = _descriptor.Descriptor(
        name='QuoteResponse',
        full_name='looprpc.QuoteResponse',
        filename=None,
        file=DESCRIPTOR,
        containing_type=None,
        fields=[
            _descriptor.FieldDescriptor(
                    name='swap_fee', full_name='looprpc.QuoteResponse.swap_fee', index=0,
                    number=1, type=3, cpp_type=2, label=1,
                    has_default_value=False, default_value=0,
                    message_type=None, enum_type=None, containing_type=None,
                    is_extension=False, extension_scope=None,
                    serialized_options=None, file=DESCRIPTOR),
            _descriptor.FieldDescriptor(
                    name='prepay_amt', full_name='looprpc.QuoteResponse.prepay_amt', index=1,
                    number=2, type=3, cpp_type=2, label=1,
                    has_default_value=False, default_value=0,
                    message_type=None, enum_type=None, containing_type=None,
                    is_extension=False, extension_scope=None,
                    serialized_options=None, file=DESCRIPTOR),
            _descriptor.FieldDescriptor(
                    name='miner_fee', full_name='looprpc.QuoteResponse.miner_fee', index=2,
                    number=3, type=3, cpp_type=2, label=1,
                    has_default_value=False, default_value=0,
                    message_type=None, enum_type=None, containing_type=None,
                    is_extension=False, extension_scope=None,
                    serialized_options=None, file=DESCRIPTOR),
        ],
        extensions=[
        ],
        nested_types=[],
        enum_types=[
        ],
        serialized_options=None,
        is_extendable=False,
        syntax='proto3',
        extension_ranges=[],
        oneofs=[
        ],
        serialized_start=877,
        serialized_end=949,
)

_SWAPSTATUS.fields_by_name['type'].enum_type = _SWAPTYPE
_SWAPSTATUS.fields_by_name['state'].enum_type = _SWAPSTATE
DESCRIPTOR.message_types_by_name['LoopOutRequest'] = _LOOPOUTREQUEST
DESCRIPTOR.message_types_by_name['LoopInRequest'] = _LOOPINREQUEST
DESCRIPTOR.message_types_by_name['SwapResponse'] = _SWAPRESPONSE
DESCRIPTOR.message_types_by_name['MonitorRequest'] = _MONITORREQUEST
DESCRIPTOR.message_types_by_name['SwapStatus'] = _SWAPSTATUS
DESCRIPTOR.message_types_by_name['TermsRequest'] = _TERMSREQUEST
DESCRIPTOR.message_types_by_name['TermsResponse'] = _TERMSRESPONSE
DESCRIPTOR.message_types_by_name['QuoteRequest'] = _QUOTEREQUEST
DESCRIPTOR.message_types_by_name['QuoteResponse'] = _QUOTERESPONSE
DESCRIPTOR.enum_types_by_name['SwapType'] = _SWAPTYPE
DESCRIPTOR.enum_types_by_name['SwapState'] = _SWAPSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LoopOutRequest = _reflection.GeneratedProtocolMessageType('LoopOutRequest', (_message.Message,),
                                                          dict(
                                                                  DESCRIPTOR=_LOOPOUTREQUEST,
                                                                  __module__='loop_rpc.protos.loop_client_pb2'
                                                                  # @@protoc_insertion_point(class_scope:looprpc.LoopOutRequest)
                                                          ))
_sym_db.RegisterMessage(LoopOutRequest)

LoopInRequest = _reflection.GeneratedProtocolMessageType('LoopInRequest', (_message.Message,), dict(
        DESCRIPTOR=_LOOPINREQUEST,
        __module__='loop_rpc.protos.loop_client_pb2'
        # @@protoc_insertion_point(class_scope:looprpc.LoopInRequest)
))
_sym_db.RegisterMessage(LoopInRequest)

SwapResponse = _reflection.GeneratedProtocolMessageType('SwapResponse', (_message.Message,), dict(
        DESCRIPTOR=_SWAPRESPONSE,
        __module__='loop_rpc.protos.loop_client_pb2'
        # @@protoc_insertion_point(class_scope:looprpc.SwapResponse)
))
_sym_db.RegisterMessage(SwapResponse)

MonitorRequest = _reflection.GeneratedProtocolMessageType('MonitorRequest', (_message.Message,),
                                                          dict(
                                                                  DESCRIPTOR=_MONITORREQUEST,
                                                                  __module__='loop_rpc.protos.loop_client_pb2'
                                                                  # @@protoc_insertion_point(class_scope:looprpc.MonitorRequest)
                                                          ))
_sym_db.RegisterMessage(MonitorRequest)

SwapStatus = _reflection.GeneratedProtocolMessageType('SwapStatus', (_message.Message,), dict(
        DESCRIPTOR=_SWAPSTATUS,
        __module__='loop_rpc.protos.loop_client_pb2'
        # @@protoc_insertion_point(class_scope:looprpc.SwapStatus)
))
_sym_db.RegisterMessage(SwapStatus)

TermsRequest = _reflection.GeneratedProtocolMessageType('TermsRequest', (_message.Message,), dict(
        DESCRIPTOR=_TERMSREQUEST,
        __module__='loop_rpc.protos.loop_client_pb2'
        # @@protoc_insertion_point(class_scope:looprpc.TermsRequest)
))
_sym_db.RegisterMessage(TermsRequest)

TermsResponse = _reflection.GeneratedProtocolMessageType('TermsResponse', (_message.Message,), dict(
        DESCRIPTOR=_TERMSRESPONSE,
        __module__='loop_rpc.protos.loop_client_pb2'
        # @@protoc_insertion_point(class_scope:looprpc.TermsResponse)
))
_sym_db.RegisterMessage(TermsResponse)

QuoteRequest = _reflection.GeneratedProtocolMessageType('QuoteRequest', (_message.Message,), dict(
        DESCRIPTOR=_QUOTEREQUEST,
        __module__='loop_rpc.protos.loop_client_pb2'
        # @@protoc_insertion_point(class_scope:looprpc.QuoteRequest)
))
_sym_db.RegisterMessage(QuoteRequest)

QuoteResponse = _reflection.GeneratedProtocolMessageType('QuoteResponse', (_message.Message,), dict(
        DESCRIPTOR=_QUOTERESPONSE,
        __module__='loop_rpc.protos.loop_client_pb2'
        # @@protoc_insertion_point(class_scope:looprpc.QuoteResponse)
))
_sym_db.RegisterMessage(QuoteResponse)

_SWAPCLIENT = _descriptor.ServiceDescriptor(
        name='SwapClient',
        full_name='looprpc.SwapClient',
        file=DESCRIPTOR,
        index=0,
        serialized_options=None,
        serialized_start=1108,
        serialized_end=1638,
        methods=[
            _descriptor.MethodDescriptor(
                    name='LoopOut',
                    full_name='looprpc.SwapClient.LoopOut',
                    index=0,
                    containing_service=None,
                    input_type=_LOOPOUTREQUEST,
                    output_type=_SWAPRESPONSE,
                    serialized_options=_b('\202\323\344\223\002\021\"\014/v1/loop/out:\001*'),
            ),
            _descriptor.MethodDescriptor(
                    name='LoopIn',
                    full_name='looprpc.SwapClient.LoopIn',
                    index=1,
                    containing_service=None,
                    input_type=_LOOPINREQUEST,
                    output_type=_SWAPRESPONSE,
                    serialized_options=None,
            ),
            _descriptor.MethodDescriptor(
                    name='Monitor',
                    full_name='looprpc.SwapClient.Monitor',
                    index=2,
                    containing_service=None,
                    input_type=_MONITORREQUEST,
                    output_type=_SWAPSTATUS,
                    serialized_options=None,
            ),
            _descriptor.MethodDescriptor(
                    name='LoopOutTerms',
                    full_name='looprpc.SwapClient.LoopOutTerms',
                    index=3,
                    containing_service=None,
                    input_type=_TERMSREQUEST,
                    output_type=_TERMSRESPONSE,
                    serialized_options=_b('\202\323\344\223\002\024\022\022/v1/loop/out/terms'),
            ),
            _descriptor.MethodDescriptor(
                    name='LoopOutQuote',
                    full_name='looprpc.SwapClient.LoopOutQuote',
                    index=4,
                    containing_service=None,
                    input_type=_QUOTEREQUEST,
                    output_type=_QUOTERESPONSE,
                    serialized_options=_b(
                        '\202\323\344\223\002\032\022\030/v1/loop/out/quote/{amt}'),
            ),
            _descriptor.MethodDescriptor(
                    name='GetLoopInTerms',
                    full_name='looprpc.SwapClient.GetLoopInTerms',
                    index=5,
                    containing_service=None,
                    input_type=_TERMSREQUEST,
                    output_type=_TERMSRESPONSE,
                    serialized_options=None,
            ),
            _descriptor.MethodDescriptor(
                    name='GetLoopInQuote',
                    full_name='looprpc.SwapClient.GetLoopInQuote',
                    index=6,
                    containing_service=None,
                    input_type=_QUOTEREQUEST,
                    output_type=_QUOTERESPONSE,
                    serialized_options=None,
            ),
        ])
_sym_db.RegisterServiceDescriptor(_SWAPCLIENT)

DESCRIPTOR.services_by_name['SwapClient'] = _SWAPCLIENT

# @@protoc_insertion_point(module_scope)
