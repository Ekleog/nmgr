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

from nmgr import *
import re

netdev.watch()

@on_msg(re.compile(r'.'))
def debug(src, meta):
    print('DEBUG: ' + src + ': ' + str(meta))

@on_msg('netdev/eth/usbeth/add')
def dev_up(src, dev):
    netdev.up(dev)

@on_msg('netdev/eth/usbeth/up')
def add_ip(src, dev):
    ip.add(dev.name, "192.168.1.1")

main_loop()
