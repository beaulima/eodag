# -*- coding: utf-8 -*-
# Copyright 2020, CS GROUP - France, http://www.c-s.fr
#
# This file is part of EODAG project
#     https://www.github.com/CS-SI/EODAG
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: eodag.proto

import sys

from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="eodag.proto",
    package="eodag",
    syntax="proto3",
    serialized_pb=_b(
        '\n\x0b\x65odag.proto\x12\x05\x65odag\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x19google/protobuf/any.proto">\n\x1b\x45OProductTypeMetadataSchema\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x12\n\nvalue_type\x18\x02 \x01(\t"h\n\x13\x45OProductTypeSchema\x12\n\n\x02id\x18\x01 \x01(\t\x12\x30\n\x04meta\x18\x02 \x03(\x0b\x32".eodag.EOProductTypeMetadataSchema\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t"+\n\x1a\x45OProductTypeSearchRequest\x12\r\n\x05query\x18\x01 \x01(\t"\xae\x01\n\x16\x45OProductSearchRequest\x12\x14\n\x0cproduct_type\x18\x01 \x01(\t\x12\x11\n\tfootprint\x18\x02 \x01(\t\x12)\n\x05start\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\'\n\x03\x65nd\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x17\n\x0fmetadata_filter\x18\x05 \x01(\t"<\n\x08Metadata\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any">\n\rEOProductInfo\x12\n\n\x02id\x18\x01 \x01(\t\x12!\n\x08metadata\x18\x02 \x01(\x0b\x32\x0f.eodag.Metadata".\n\x18\x45OProductDownloadRequest\x12\x12\n\nproduct_id\x18\x02 \x01(\t"\x1f\n\x0cNetCDFBuffer\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\x0c\x32\xb3\x01\n\rEOProductType\x12J\n\x10ListProductTypes\x12\x16.google.protobuf.Empty\x1a\x1a.eodag.EOProductTypeSchema"\x00\x30\x01\x12V\n\x11SearchProductType\x12!.eodag.EOProductTypeSearchRequest\x1a\x1a.eodag.EOProductTypeSchema"\x00\x30\x01\x32\xa2\x01\n\tEOProduct\x12H\n\rSearchProduct\x12\x1d.eodag.EOProductSearchRequest\x1a\x14.eodag.EOProductInfo"\x00\x30\x01\x12K\n\x0f\x44ownloadProduct\x12\x1f.eodag.EOProductDownloadRequest\x1a\x13.eodag.NetCDFBuffer"\x00\x30\x01\x62\x06proto3'
    ),
    dependencies=[
        google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_any__pb2.DESCRIPTOR,
    ],
)


_EOPRODUCTTYPEMETADATASCHEMA = _descriptor.Descriptor(
    name="EOProductTypeMetadataSchema",
    full_name="eodag.EOProductTypeMetadataSchema",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="eodag.EOProductTypeMetadataSchema.key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="value_type",
            full_name="eodag.EOProductTypeMetadataSchema.value_type",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=111,
    serialized_end=173,
)


_EOPRODUCTTYPESCHEMA = _descriptor.Descriptor(
    name="EOProductTypeSchema",
    full_name="eodag.EOProductTypeSchema",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="eodag.EOProductTypeSchema.id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="meta",
            full_name="eodag.EOProductTypeSchema.meta",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="description",
            full_name="eodag.EOProductTypeSchema.description",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=175,
    serialized_end=279,
)


_EOPRODUCTTYPESEARCHREQUEST = _descriptor.Descriptor(
    name="EOProductTypeSearchRequest",
    full_name="eodag.EOProductTypeSearchRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="query",
            full_name="eodag.EOProductTypeSearchRequest.query",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=281,
    serialized_end=324,
)


_EOPRODUCTSEARCHREQUEST = _descriptor.Descriptor(
    name="EOProductSearchRequest",
    full_name="eodag.EOProductSearchRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="product_type",
            full_name="eodag.EOProductSearchRequest.product_type",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="footprint",
            full_name="eodag.EOProductSearchRequest.footprint",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="start",
            full_name="eodag.EOProductSearchRequest.start",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="end",
            full_name="eodag.EOProductSearchRequest.end",
            index=3,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="metadata_filter",
            full_name="eodag.EOProductSearchRequest.metadata_filter",
            index=4,
            number=5,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=327,
    serialized_end=501,
)


_METADATA = _descriptor.Descriptor(
    name="Metadata",
    full_name="eodag.Metadata",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="eodag.Metadata.key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="eodag.Metadata.value",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=503,
    serialized_end=563,
)


_EOPRODUCTINFO = _descriptor.Descriptor(
    name="EOProductInfo",
    full_name="eodag.EOProductInfo",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="eodag.EOProductInfo.id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="metadata",
            full_name="eodag.EOProductInfo.metadata",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=565,
    serialized_end=627,
)


_EOPRODUCTDOWNLOADREQUEST = _descriptor.Descriptor(
    name="EOProductDownloadRequest",
    full_name="eodag.EOProductDownloadRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="product_id",
            full_name="eodag.EOProductDownloadRequest.product_id",
            index=0,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=629,
    serialized_end=675,
)


_NETCDFBUFFER = _descriptor.Descriptor(
    name="NetCDFBuffer",
    full_name="eodag.NetCDFBuffer",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="content",
            full_name="eodag.NetCDFBuffer.content",
            index=0,
            number=1,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b(""),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=677,
    serialized_end=708,
)

_EOPRODUCTTYPESCHEMA.fields_by_name["meta"].message_type = _EOPRODUCTTYPEMETADATASCHEMA
_EOPRODUCTSEARCHREQUEST.fields_by_name[
    "start"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_EOPRODUCTSEARCHREQUEST.fields_by_name[
    "end"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_METADATA.fields_by_name["value"].message_type = google_dot_protobuf_dot_any__pb2._ANY
_EOPRODUCTINFO.fields_by_name["metadata"].message_type = _METADATA
DESCRIPTOR.message_types_by_name[
    "EOProductTypeMetadataSchema"
] = _EOPRODUCTTYPEMETADATASCHEMA
DESCRIPTOR.message_types_by_name["EOProductTypeSchema"] = _EOPRODUCTTYPESCHEMA
DESCRIPTOR.message_types_by_name[
    "EOProductTypeSearchRequest"
] = _EOPRODUCTTYPESEARCHREQUEST
DESCRIPTOR.message_types_by_name["EOProductSearchRequest"] = _EOPRODUCTSEARCHREQUEST
DESCRIPTOR.message_types_by_name["Metadata"] = _METADATA
DESCRIPTOR.message_types_by_name["EOProductInfo"] = _EOPRODUCTINFO
DESCRIPTOR.message_types_by_name["EOProductDownloadRequest"] = _EOPRODUCTDOWNLOADREQUEST
DESCRIPTOR.message_types_by_name["NetCDFBuffer"] = _NETCDFBUFFER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EOProductTypeMetadataSchema = _reflection.GeneratedProtocolMessageType(
    "EOProductTypeMetadataSchema",
    (_message.Message,),
    dict(
        DESCRIPTOR=_EOPRODUCTTYPEMETADATASCHEMA,
        __module__="eodag_pb2"
        # @@protoc_insertion_point(class_scope:eodag.EOProductTypeMetadataSchema)
    ),
)
_sym_db.RegisterMessage(EOProductTypeMetadataSchema)

EOProductTypeSchema = _reflection.GeneratedProtocolMessageType(
    "EOProductTypeSchema",
    (_message.Message,),
    dict(
        DESCRIPTOR=_EOPRODUCTTYPESCHEMA,
        __module__="eodag_pb2"
        # @@protoc_insertion_point(class_scope:eodag.EOProductTypeSchema)
    ),
)
_sym_db.RegisterMessage(EOProductTypeSchema)

EOProductTypeSearchRequest = _reflection.GeneratedProtocolMessageType(
    "EOProductTypeSearchRequest",
    (_message.Message,),
    dict(
        DESCRIPTOR=_EOPRODUCTTYPESEARCHREQUEST,
        __module__="eodag_pb2"
        # @@protoc_insertion_point(class_scope:eodag.EOProductTypeSearchRequest)
    ),
)
_sym_db.RegisterMessage(EOProductTypeSearchRequest)

EOProductSearchRequest = _reflection.GeneratedProtocolMessageType(
    "EOProductSearchRequest",
    (_message.Message,),
    dict(
        DESCRIPTOR=_EOPRODUCTSEARCHREQUEST,
        __module__="eodag_pb2"
        # @@protoc_insertion_point(class_scope:eodag.EOProductSearchRequest)
    ),
)
_sym_db.RegisterMessage(EOProductSearchRequest)

Metadata = _reflection.GeneratedProtocolMessageType(
    "Metadata",
    (_message.Message,),
    dict(
        DESCRIPTOR=_METADATA,
        __module__="eodag_pb2"
        # @@protoc_insertion_point(class_scope:eodag.Metadata)
    ),
)
_sym_db.RegisterMessage(Metadata)

EOProductInfo = _reflection.GeneratedProtocolMessageType(
    "EOProductInfo",
    (_message.Message,),
    dict(
        DESCRIPTOR=_EOPRODUCTINFO,
        __module__="eodag_pb2"
        # @@protoc_insertion_point(class_scope:eodag.EOProductInfo)
    ),
)
_sym_db.RegisterMessage(EOProductInfo)

EOProductDownloadRequest = _reflection.GeneratedProtocolMessageType(
    "EOProductDownloadRequest",
    (_message.Message,),
    dict(
        DESCRIPTOR=_EOPRODUCTDOWNLOADREQUEST,
        __module__="eodag_pb2"
        # @@protoc_insertion_point(class_scope:eodag.EOProductDownloadRequest)
    ),
)
_sym_db.RegisterMessage(EOProductDownloadRequest)

NetCDFBuffer = _reflection.GeneratedProtocolMessageType(
    "NetCDFBuffer",
    (_message.Message,),
    dict(
        DESCRIPTOR=_NETCDFBUFFER,
        __module__="eodag_pb2"
        # @@protoc_insertion_point(class_scope:eodag.NetCDFBuffer)
    ),
)
_sym_db.RegisterMessage(NetCDFBuffer)


_EOPRODUCTTYPE = _descriptor.ServiceDescriptor(
    name="EOProductType",
    full_name="eodag.EOProductType",
    file=DESCRIPTOR,
    index=0,
    options=None,
    serialized_start=711,
    serialized_end=890,
    methods=[
        _descriptor.MethodDescriptor(
            name="ListProductTypes",
            full_name="eodag.EOProductType.ListProductTypes",
            index=0,
            containing_service=None,
            input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
            output_type=_EOPRODUCTTYPESCHEMA,
            options=None,
        ),
        _descriptor.MethodDescriptor(
            name="SearchProductType",
            full_name="eodag.EOProductType.SearchProductType",
            index=1,
            containing_service=None,
            input_type=_EOPRODUCTTYPESEARCHREQUEST,
            output_type=_EOPRODUCTTYPESCHEMA,
            options=None,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_EOPRODUCTTYPE)

DESCRIPTOR.services_by_name["EOProductType"] = _EOPRODUCTTYPE


_EOPRODUCT = _descriptor.ServiceDescriptor(
    name="EOProduct",
    full_name="eodag.EOProduct",
    file=DESCRIPTOR,
    index=1,
    options=None,
    serialized_start=893,
    serialized_end=1055,
    methods=[
        _descriptor.MethodDescriptor(
            name="SearchProduct",
            full_name="eodag.EOProduct.SearchProduct",
            index=0,
            containing_service=None,
            input_type=_EOPRODUCTSEARCHREQUEST,
            output_type=_EOPRODUCTINFO,
            options=None,
        ),
        _descriptor.MethodDescriptor(
            name="DownloadProduct",
            full_name="eodag.EOProduct.DownloadProduct",
            index=1,
            containing_service=None,
            input_type=_EOPRODUCTDOWNLOADREQUEST,
            output_type=_NETCDFBUFFER,
            options=None,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_EOPRODUCT)

DESCRIPTOR.services_by_name["EOProduct"] = _EOPRODUCT

# @@protoc_insertion_point(module_scope)
