# -*- coding: utf-8 -*-

# Resource object code
#
# Created by: Storm Shadow (Qt v4.8.6)
#
# WARNING! All changes made in this file will be lost anfd file wont work!

from PyQt5 import QtCore

qt_resource_data = "\
\x00\x00\x01\x30\
\x89\
\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d\x49\x48\x44\x52\x00\
\x00\x00\x10\x00\x00\x00\x10\x08\x06\x00\x00\x00\x1f\xf3\xff\x61\
\x00\x00\x00\xf7\x49\x44\x41\x54\x38\x8d\x9d\xd3\xa1\x4e\x43\x41\
\x10\x85\xe1\x4f\x20\x2a\x2a\x2a\x10\x24\x54\x54\x20\x11\x08\x48\
\x20\x21\xa4\x8f\x50\x81\x40\x20\x10\x08\x04\x12\x81\xc4\x23\x2a\
\x90\xc8\xca\x3e\x40\x1f\xa0\x02\x59\x81\x40\x20\x10\x88\x3e\x40\
\x05\x02\x51\xc4\x9d\x92\xde\x65\xf7\x42\x38\xc9\x88\xdd\x9d\xf3\
\x67\x67\x76\x96\xbc\xfa\x18\xe1\x05\x0b\xcc\x70\x83\x4e\x21\xff\
\x5b\x2d\xdc\x63\x59\x88\x77\x1c\x37\x01\x26\x91\xf8\x86\x47\x5c\
\x67\x20\x0b\xec\x96\xae\xbd\x4a\xba\xc4\x06\xda\x38\x0c\xd3\x1d\
\xc6\x71\x3e\xc9\x01\x2e\xd6\x00\xfb\x01\x3c\xc3\x16\x6e\x63\xbd\
\xad\xea\xcb\x27\x36\x9b\x00\xc3\x48\x68\x47\x29\xc3\x00\x75\xe3\
\x36\xcb\x00\xd6\x34\x48\x6a\x9d\xaa\x9a\x76\x82\xd3\x58\x3f\xaf\
\x9d\xef\xa5\x80\x07\xf9\xae\x1f\xe0\x28\xd9\x9f\xa7\xe6\x0e\x3e\
\x32\x80\xd5\x8b\xcc\x93\xbd\xf3\x14\x00\xaf\x05\x40\x1a\xd3\x9c\
\x99\xfa\x33\x36\x45\x71\x90\x5a\x7f\x04\xf4\x4a\x00\xea\x5d\xce\
\xc5\x58\x35\x60\x45\x75\xa3\x94\x1d\x3f\xff\xc4\xaf\xe6\x9c\x9e\
\xc2\x3c\xfa\x8f\x19\xae\x54\x53\x58\xd4\x17\x2d\xb4\x73\xa5\x9a\
\x77\x13\x01\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42\x60\x82\
"

qt_resource_name = "\
\x00\x03\
\x00\x00\x6f\x9f\
\x00\x69\
\x00\x63\x00\x6f\
\x00\x08\
\x00\x47\x59\xc7\
\x00\x6d\
\x00\x69\x00\x6e\x00\x64\x00\x2e\x00\x70\x00\x6e\x00\x67\
"

qt_resource_struct = "\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
