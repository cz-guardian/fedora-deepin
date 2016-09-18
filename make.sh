#!/bin/bash

for pkg in $(ls -1 ./SPECS/*.spec); do
  spectool -g -R $pkg
  rpmbuild -ba $pkg
done