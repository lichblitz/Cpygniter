"""
SQLAlchemy backend for MonetDB
"""

import pkg_resources

try:
    __version__ = pkg_resources.require("cpygniter")[0].version
except pkg_resources.DistributionNotFound:
    __version__ = "dev"

from . import connections


VERSION = "0.0.1"


Connect = connect = Connection = connections.Connection

def get_client_info():
    return VERSION




