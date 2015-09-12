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

from . import *

import pyudev

_context = pyudev.Context()

for device in _context.list_devices():
    broadcast("dev/" + device.subsystem + "/" + device.sys_name, device)

_monitor = pyudev.Monitor.from_netlink(_context)

def _on_event(action, device):
    broadcast("dev/" + device.subsystem + "/" + device.sys_name + "/" + action, (action, device))

_observer = pyudev.MonitorObserver(_monitor, _on_event)
_observer.start()
