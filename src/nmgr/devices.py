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
