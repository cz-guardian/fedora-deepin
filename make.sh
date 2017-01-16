#!/bin/bash

ARCHS=("fedora-24-i386" "fedora-24-x86_64" "fedora-25-i386" "fedora-25-x86_64" "fedora-rawhide-i386" "fedora-rawhide-x86_64")
# "fedora-24-i386 fedora-24-x86_64 fedora-25-i386 fedora-25-x86_64 fedora-rawhide-i386 fedora-rawhide-x86_64"
PACKAGE=$1
RESULT_DIR=/tmp/build_$(date +%Y%m%d_%H%M%S)
# COPR specific config
COPR_PROJECT=deepin
MOCK=0

if [ "$2" ]; then
  ARCHS=($2)
fi

if [ "$3" == "mock" ]; then
  MOCK=1
fi

if [ "$4" ]; then
  RESULT_DIR="${4}"
fi

function buildPackage()
{
  local package=$1

  # Download source for given package
  spectool -g -R ${package}
  
  if [ $? == 0 ]; then
    for arch in ${ARCHS[@]}; do
      rm -rf ${RESULT_DIR}
      mkdir -p ${RESULT_DIR} && chmod 777 "${RESULT_DIR}"
      #echo mock -r ${arch} --spec=SPECS/${package}.spec --sources=SOURCES/ --buildsrpm --resultdir=${RESULT_DIR}
      mock -r ${arch} --spec=${package} --sources=SOURCES/ --buildsrpm --resultdir=${RESULT_DIR}
      ###
      rpmfile=$(grep 'src.rpm' ${RESULT_DIR}/build.log | head -n 1 | sed -e 's#^.*/##g')

      if [ ${MOCK} -eq 1 ]; then
        mockBuild "${arch}" "${RESULT_DIR}/${rpmfile}"
      else
        upload2Copr "${arch}" "${RESULT_DIR}/${rpmfile}"
      fi
    done
  else
    echo "An error occured. Exiting..."
    exit 1
  fi
}

function upload2Copr()
{
  local arch=$1
  local package=$2

  #echo copr-cli build -r ${arch} --nowait ${COPR_PROJECT} ${package}
  copr-cli build --nowait ${COPR_PROJECT} ${package}
}

function mockBuild()
{
  local arch=$1
  local package=$2

  mock -r ${arch} ${package} --resultdir=${RESULT_DIR}
}

buildPackage $PACKAGE