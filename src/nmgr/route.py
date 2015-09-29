#
# This file is part of nmgr.
# Copyright (C) 2015 Leo Gaspard
#
# nmgr is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# nmgr is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with nmgr.  If not, see <http://www.gnu.org/licenses/>.
#

import nmgr
from collections import namedtuple
import sh

_RouteMetadata = namedtuple('_IpMetadata', ['action', 'subnet', 'meta'])

def _send_message(action, subnet, meta):
    data = _RouteMetadata(
        action = action,
        subnet = subnet,
        meta   = meta
    )
    msg = "route/" + data.action + "/" + data.subnet
    nmgr.broadcast(msg, data)

def add(subnet, **kwargs):
    args = []
    for key in kwargs:
        args.append(key)
        args.append(kwargs[key])
    sh.ip.route.add(subnet, *args)
    _send_message('add', subnet, kwargs)
