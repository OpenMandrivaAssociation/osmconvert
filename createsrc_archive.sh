#!/bin/bash
# Get the file
wget -O - http://m.m.i24.cc/osmconvert.c >osmconvert.c
# Determine the version number
VERSION="-"$(grep '#define VERSION' osmconvert.c |awk -F '"' '{print $2}')

echo "$VERSION"
# Put the filename into the correct directory structure using gtar's tranfor mechanism
eval gtar --transform 's,^,osmconvert"$VERSION"/,S'  -cJvf 'osmconvert-0.8.11.tar' 'osmconvert.c'

