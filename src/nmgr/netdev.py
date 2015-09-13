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
import re

_NetdevMetadata = namedtuple('_NetdevMetadata', ['type', 'name', 'action'])

def watch():
    nmgr.udev.watch()

    @nmgr.on_msg(re.compile(r'^udev/net/'))
    def broadcast_same(msg, dev):
        (action, d) = dev
        if not d.is_initialized:
            return
        data = _NetdevMetadata(
            type   = d.device_type if d.device_type else 'eth',
            name   = d.sys_name,
            action = action
        )
        msg = "net/" + data.type + "/" + data.name + "/" + data.action
        nmgr.broadcast(msg, data)
