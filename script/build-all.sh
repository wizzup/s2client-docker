#!/usr/bin/env bash

SCRIPT_PATH=${0%/*}
IMAGES="base game api dev"
pushd ${SCRIPT_PATH}

  for IMG in ${IMAGES}; do
    ./build-${IMG}.sh
  done

popd
