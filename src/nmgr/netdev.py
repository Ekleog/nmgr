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
import sh

_NetdevMetadata = namedtuple('_NetdevMetadata', ['type', 'name', 'action'])

def _send_message(type, name, action):
    data = _NetdevMetadata(
        type   = type,
        name   = name,
        action = action
    )
    msg = "net/" + data.type + "/" + data.name + "/" + data.action
    nmgr.broadcast(msg, data)

def watch():
    nmgr.udev.watch()

    @nmgr.on_msg(re.compile(r'^udev/net/'))
    def broadcast_same(msg, dev):
        (action, d) = dev
        if not d.is_initialized:
            return
        _send_message(d.device_type if d.device_type else 'eth', d.sys_name, action)

def up(dev):
    """ dev must have at least dev.type and dev.name set. Especially, it can be a _NetdevMetadata """
    sh.ip.link.set(dev.name, "up")
    _send_message(dev.type, dev.name, 'up')

def down(dev):
    """ dev must have at least dev.type and dev.name set. Especially, it can be a _NetdevMetadata """
    sh.ip.link.set(dev.name, 'down')
    _send_message(dev.type, dev.name, 'down')
