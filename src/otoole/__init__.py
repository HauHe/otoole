# -*- coding: utf-8 -*-
from pkg_resources import get_distribution, DistributionNotFound

from otoole.input import Context
from otoole.read_strategies import (
    ReadCsv,
    ReadDatafile,
    ReadDatapackage,
    ReadExcel,
    ReadMemory,
)
from otoole.write_strategies import (
    WriteCsv,
    WriteDatafile,
    WriteDatapackage,
    WriteExcel,
)

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = __name__
    __version__ = get_distribution(dist_name).version
except DistributionNotFound:
    __version__ = "unknown"
finally:
    del get_distribution, DistributionNotFound


__all__ = [
    "Context",
    "ReadCsv",
    "ReadDatafile",
    "ReadDatapackage",
    "ReadExcel",
    "ReadMemory",
    "WriteCsv",
    "WriteDatafile",
    "WriteDatapackage",
    "WriteExcel",
]
