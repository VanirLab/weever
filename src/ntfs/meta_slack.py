"""
Implementation for allocation of additional
data runs for a file to hide data in
"""

import typing
from math import ceil
from .ntfs_filesystem.ntfs import NTFS
from .ntfs_filesystem.attributes import DATA_ID
from .ntfs_filesystem.attribute_header import ATTRIBUTE_HEADER


class AllocatorMetadata:
    """
    This class contains the metadata needed by the
    ClusterAllocator for allocating additional clusters
    to a file in ntfs
    """

    def __init__(self, d: typing.Dict = None):
        """
        Declaration of the needed attributes
        """
        if d is None:
            self.file = None
            self.size = 0
            self.new_runs = []
        else:
            self.file = d['file']
            self.size = d['size']
            self.new_runs = d['new_runs']