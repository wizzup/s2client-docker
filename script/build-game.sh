#!/usr/bin/env bash

SCRIPT_PATH=${0%/*}

source ${SCRIPT_PATH}/docker-util.sh

buildImage "sc2-game" ${SCRIPT_PATH}/../game
