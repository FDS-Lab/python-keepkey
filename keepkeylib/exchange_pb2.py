# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: exchange.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='exchange.proto',
  package='',
  syntax='proto2',
  serialized_options=_b('\n\033com.keepkey.device-protocolB\017KeepKeyExchange'),
  serialized_pb=_b('\n\x0e\x65xchange.proto\"[\n\x0f\x45xchangeAddress\x12\x11\n\tcoin_type\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x12\x10\n\x08\x64\x65st_tag\x18\x03 \x01(\t\x12\x12\n\nrs_address\x18\x04 \x01(\t\"\xa9\x02\n\x12\x45xchangeResponseV2\x12)\n\x0f\x64\x65posit_address\x18\x01 \x01(\x0b\x32\x10.ExchangeAddress\x12\x16\n\x0e\x64\x65posit_amount\x18\x02 \x01(\x0c\x12\x12\n\nexpiration\x18\x03 \x01(\x03\x12\x13\n\x0bquoted_rate\x18\x04 \x01(\x0c\x12,\n\x12withdrawal_address\x18\x05 \x01(\x0b\x32\x10.ExchangeAddress\x12\x19\n\x11withdrawal_amount\x18\x06 \x01(\x0c\x12(\n\x0ereturn_address\x18\x07 \x01(\x0b\x32\x10.ExchangeAddress\x12\x0f\n\x07\x61pi_key\x18\x08 \x01(\x0c\x12\x11\n\tminer_fee\x18\t \x01(\x0c\x12\x10\n\x08order_id\x18\n \x01(\x0c\"y\n\x16SignedExchangeResponse\x12#\n\x08response\x18\x01 \x01(\x0b\x32\x11.ExchangeResponse\x12\x11\n\tsignature\x18\x02 \x01(\x0c\x12\'\n\nresponseV2\x18\x03 \x01(\x0b\x32\x13.ExchangeResponseV2\"\xa7\x02\n\x10\x45xchangeResponse\x12)\n\x0f\x64\x65posit_address\x18\x01 \x01(\x0b\x32\x10.ExchangeAddress\x12\x16\n\x0e\x64\x65posit_amount\x18\x02 \x01(\x04\x12\x12\n\nexpiration\x18\x03 \x01(\x03\x12\x13\n\x0bquoted_rate\x18\x04 \x01(\x04\x12,\n\x12withdrawal_address\x18\x05 \x01(\x0b\x32\x10.ExchangeAddress\x12\x19\n\x11withdrawal_amount\x18\x06 \x01(\x04\x12(\n\x0ereturn_address\x18\x07 \x01(\x0b\x32\x10.ExchangeAddress\x12\x0f\n\x07\x61pi_key\x18\x08 \x01(\x0c\x12\x11\n\tminer_fee\x18\t \x01(\x04\x12\x10\n\x08order_id\x18\n \x01(\x0c\x42.\n\x1b\x63om.keepkey.device-protocolB\x0fKeepKeyExchange')
)




_EXCHANGEADDRESS = _descriptor.Descriptor(
  name='ExchangeAddress',
  full_name='ExchangeAddress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='coin_type', full_name='ExchangeAddress.coin_type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='ExchangeAddress.address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dest_tag', full_name='ExchangeAddress.dest_tag', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rs_address', full_name='ExchangeAddress.rs_address', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=109,
)


_EXCHANGERESPONSEV2 = _descriptor.Descriptor(
  name='ExchangeResponseV2',
  full_name='ExchangeResponseV2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='deposit_address', full_name='ExchangeResponseV2.deposit_address', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deposit_amount', full_name='ExchangeResponseV2.deposit_amount', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expiration', full_name='ExchangeResponseV2.expiration', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quoted_rate', full_name='ExchangeResponseV2.quoted_rate', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='withdrawal_address', full_name='ExchangeResponseV2.withdrawal_address', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='withdrawal_amount', full_name='ExchangeResponseV2.withdrawal_amount', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='return_address', full_name='ExchangeResponseV2.return_address', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='api_key', full_name='ExchangeResponseV2.api_key', index=7,
      number=8, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='miner_fee', full_name='ExchangeResponseV2.miner_fee', index=8,
      number=9, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='order_id', full_name='ExchangeResponseV2.order_id', index=9,
      number=10, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=112,
  serialized_end=409,
)


_SIGNEDEXCHANGERESPONSE = _descriptor.Descriptor(
  name='SignedExchangeResponse',
  full_name='SignedExchangeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='SignedExchangeResponse.response', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signature', full_name='SignedExchangeResponse.signature', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='responseV2', full_name='SignedExchangeResponse.responseV2', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=411,
  serialized_end=532,
)


_EXCHANGERESPONSE = _descriptor.Descriptor(
  name='ExchangeResponse',
  full_name='ExchangeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='deposit_address', full_name='ExchangeResponse.deposit_address', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deposit_amount', full_name='ExchangeResponse.deposit_amount', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expiration', full_name='ExchangeResponse.expiration', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quoted_rate', full_name='ExchangeResponse.quoted_rate', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='withdrawal_address', full_name='ExchangeResponse.withdrawal_address', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='withdrawal_amount', full_name='ExchangeResponse.withdrawal_amount', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='return_address', full_name='ExchangeResponse.return_address', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='api_key', full_name='ExchangeResponse.api_key', index=7,
      number=8, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='miner_fee', full_name='ExchangeResponse.miner_fee', index=8,
      number=9, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='order_id', full_name='ExchangeResponse.order_id', index=9,
      number=10, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=535,
  serialized_end=830,
)

_EXCHANGERESPONSEV2.fields_by_name['deposit_address'].message_type = _EXCHANGEADDRESS
_EXCHANGERESPONSEV2.fields_by_name['withdrawal_address'].message_type = _EXCHANGEADDRESS
_EXCHANGERESPONSEV2.fields_by_name['return_address'].message_type = _EXCHANGEADDRESS
_SIGNEDEXCHANGERESPONSE.fields_by_name['response'].message_type = _EXCHANGERESPONSE
_SIGNEDEXCHANGERESPONSE.fields_by_name['responseV2'].message_type = _EXCHANGERESPONSEV2
_EXCHANGERESPONSE.fields_by_name['deposit_address'].message_type = _EXCHANGEADDRESS
_EXCHANGERESPONSE.fields_by_name['withdrawal_address'].message_type = _EXCHANGEADDRESS
_EXCHANGERESPONSE.fields_by_name['return_address'].message_type = _EXCHANGEADDRESS
DESCRIPTOR.message_types_by_name['ExchangeAddress'] = _EXCHANGEADDRESS
DESCRIPTOR.message_types_by_name['ExchangeResponseV2'] = _EXCHANGERESPONSEV2
DESCRIPTOR.message_types_by_name['SignedExchangeResponse'] = _SIGNEDEXCHANGERESPONSE
DESCRIPTOR.message_types_by_name['ExchangeResponse'] = _EXCHANGERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ExchangeAddress = _reflection.GeneratedProtocolMessageType('ExchangeAddress', (_message.Message,), dict(
  DESCRIPTOR = _EXCHANGEADDRESS,
  __module__ = 'exchange_pb2'
  # @@protoc_insertion_point(class_scope:ExchangeAddress)
  ))
_sym_db.RegisterMessage(ExchangeAddress)

ExchangeResponseV2 = _reflection.GeneratedProtocolMessageType('ExchangeResponseV2', (_message.Message,), dict(
  DESCRIPTOR = _EXCHANGERESPONSEV2,
  __module__ = 'exchange_pb2'
  # @@protoc_insertion_point(class_scope:ExchangeResponseV2)
  ))
_sym_db.RegisterMessage(ExchangeResponseV2)

SignedExchangeResponse = _reflection.GeneratedProtocolMessageType('SignedExchangeResponse', (_message.Message,), dict(
  DESCRIPTOR = _SIGNEDEXCHANGERESPONSE,
  __module__ = 'exchange_pb2'
  # @@protoc_insertion_point(class_scope:SignedExchangeResponse)
  ))
_sym_db.RegisterMessage(SignedExchangeResponse)

ExchangeResponse = _reflection.GeneratedProtocolMessageType('ExchangeResponse', (_message.Message,), dict(
  DESCRIPTOR = _EXCHANGERESPONSE,
  __module__ = 'exchange_pb2'
  # @@protoc_insertion_point(class_scope:ExchangeResponse)
  ))
_sym_db.RegisterMessage(ExchangeResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
