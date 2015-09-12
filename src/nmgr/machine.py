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
