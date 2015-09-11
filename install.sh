#!/bin/sh

mkdir /opt 2> /dev/null
rm -Rf /opt/nmgr /usr/bin/nmgr
cp -R src /opt/nmgr
cp src/nmgr /usr/bin/nmgr
