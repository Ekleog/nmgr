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

from queue import Queue

_queue = Queue()
_matchers = []

def broadcast(msg, metadata):
    _queue.put((msg, metadata))

def on(msg, action):
    if type(msg) == str:
        _matchers.append((lambda s: msg == s, action))
    elif "match" in dir(msg):
        _matchers.append((lambda s: msg.match(s) != None, action))
    elif callable(msg):
        _matchers.append((msg, action))
    else:
        raise ValueError("unable to detect type of " + msg)

def _call_action(action, metadata):
    try:
        action(metadata)
    except TypeError:
        action()

def _dispatch_event(msg, metadata):
    for m in _matchers:
        if m[0](msg):
            _call_action(m[1], metadata)

def main_loop():
    while True:
        (msg, metadata) = _queue.get()
        _dispatch_event(msg, metadata)
