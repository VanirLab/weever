"""
Declaration of the attribute foot for file attributes
"""

from construct import Struct, Byte, Bytes, Int8ul, Int16ul, Int32ul, Int64ul, Padding, Flag, IfThenElse, Embedded, this

ATTR_RESIDENT = Struct(
    "length" / Int32ul,
    "offset" / Int16ul,
    "indexed_tag" / Byte,
    Padding(2)
)

ATTR_NONRESIDENT = Struct(
    "start_vcn" / Int64ul,
    "end_vcn" / Int64ul,
    "datarun_offset" / Int16ul,
    "compression_size" / Int16ul,
    Padding(8),
    "alloc_size" / Int64ul,
    "real_size" / Int64ul,
    "stream_size" / Int64ul
)

ATTRIBUTE_FOOT = Struct(
    "type" / Int32ul,
    "total_length" / Int32ul,
    "nonresident" / Flag,
    "name_length" / Int8ul,
    "name_offset" / Int16ul,
    "flags" / Bytes(4),
    "id" / Int16ul,
    Embedded(IfThenElse(this.nonresident, ATTR_NONRESIDENT, \
            ATTR_RESIDENT))
)