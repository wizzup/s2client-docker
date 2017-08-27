#!/usr/bin/env bash

deep_clean(){
  # stop all running containers
  CONTAINERS=`docker ps -q`
  [[ ! -z ${CONTAINERS} ]] && docker kill ${CONTAINERS}

  # remove all containers
  CONTAINERS=`docker ps -aq`
  [[ ! -z ${CONTAINERS} ]] && docker rm ${CONTAINERS}

  # remove all images
  IMAGES=`docker images -qa`
  [[ ! -z ${IMAGES} ]] && docker rmi ${IMAGES}
}

# https://stackoverflow.com/a/3232082/1664572
confirm() {
    # call with a prompt string or use a default
    read -r -p "${1:-Are you sure? [y/N]} " response
    case "$response" in
        [yY][eE][sS]|[yY]) 
            true
            ;;
        *)
            false
            ;;
    esac
}

echo WARNING: this will stop any running container and remove ALL docker images from your system.
confirm && deep_clean
