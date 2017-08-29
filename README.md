This is a quick and dirty `all-in-one` approach branch.

Use `master` branch for official way.

# Assume
* s2client-api cloned @ ./api/s2client-api
* game downloaed and extracted @ ./game/downloads/

# Building Docker Images

## Build all images at once

    ./script/build-all.sh

## Build single image

    ./script/build-base.sh
    ./script/build-game.sh
    ./script/build-api.sh
    ./script/build-dev.sh

# Images

## sc2-base

This image contains base tool like git, cmake, ect.
Usally this image only need to build once.

## sc2-game

This image contains StarCraftII game at /StarCraftII
Usally this image only need to build once.

## sc2-api

This image contains s2client-api game at /s2client-api
This image only need to be rebuild when upstream s2client-api is update.

## sc2-dev

This is the main working image. It combine game and api.
The plan is to upload my bot to running test deamon (maybe web based) and get the result back.
I don't want to use `docker volume` as `upstream` did.

# Running/Testing

    docker run -it sc2-dev

    cd /build/api
    cmake /s2client-api

TODO:
 * sc2-dev : upload bot source interface.
