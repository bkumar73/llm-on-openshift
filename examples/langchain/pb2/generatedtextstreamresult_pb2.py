# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: generatedtextstreamresult.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import generatedtoken_pb2 as generatedtoken__pb2
import producerid_pb2 as producerid__pb2
import tokenstreamdetails_pb2 as tokenstreamdetails__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fgeneratedtextstreamresult.proto\x12\x15\x63\x61ikit_data_model.nlp\x1a\x14generatedtoken.proto\x1a\x10producerid.proto\x1a\x18tokenstreamdetails.proto\"\xe1\x01\n\x19GeneratedTextStreamResult\x12\x16\n\x0egenerated_text\x18\x01 \x01(\t\x12\x35\n\x06tokens\x18\x02 \x03(\x0b\x32%.caikit_data_model.nlp.GeneratedToken\x12:\n\x07\x64\x65tails\x18\x03 \x01(\x0b\x32).caikit_data_model.nlp.TokenStreamDetails\x12\x39\n\x0bproducer_id\x18\x04 \x01(\x0b\x32$.caikit_data_model.common.ProducerIdb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'generatedtextstreamresult_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_GENERATEDTEXTSTREAMRESULT']._serialized_start=125
  _globals['_GENERATEDTEXTSTREAMRESULT']._serialized_end=350
# @@protoc_insertion_point(module_scope)