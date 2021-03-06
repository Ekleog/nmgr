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
import pyudev

_watching_udev = False

def watch():
    global _watching_udev
    if _watching_udev:
        return
    _watching_udev = True

    context = pyudev.Context()

    for device in context.list_devices():
        nmgr.broadcast("udev/" + device.subsystem + "/" + device.sys_name + "/add", ('add', device))

    monitor = pyudev.Monitor.from_netlink(context)

    def on_event(action, device):
        nmgr.broadcast("udev/" + device.subsystem + "/" + device.sys_name + "/" + action, (action, device))

    observer = pyudev.MonitorObserver(monitor, on_event)
    observer.start()
