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

_IpMetadata = namedtuple('_IpMetadata', ['action', 'iface', 'ip'])

def _send_message(action, iface, ip):
    data = _IpMetadata(
        action = action,
        iface  = iface,
        ip     = ip
    )
    msg = "ip/" + data.action + "/" + data.iface + "/" + data.ip
    nmgr.broadcast(msg, data)

def add(iface, ip):
    sh.ip.address("add", ip, "dev", iface)
    _send_message('add', iface, ip)

def remove(iface, ip):
    sh.ip.address("del", ip, "dev", iface)
    _send_message('remove', iface, ip)
