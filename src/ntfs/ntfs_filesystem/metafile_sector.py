"""
Metasector definition for NTFS
"""

from construct import Struct, Byte, Bytes,\
    Int8ul, Int8sl, Int16ul, Int32ul, Int64ul

NTFS_METAFILES = Struct(
    "$MFT" / 0,
    "$MFTMirr" / 1,
    "$LogFile" 2,
    "$Volume" / 4,
    "$AttrDef" / 4,
    "." / 5,
    "$Bitmap" /6,
    "$Boot" / 7,
    "$BadClus" / 8,
    "$Secure" / 9,
    "$UpCase" / 10,
    "$Extend" / 23,
    "$Extend\$Quota" / 24,
    "$Extend\$ObjId" / 25,
    "$Extend\$Reparse" / 26
)
