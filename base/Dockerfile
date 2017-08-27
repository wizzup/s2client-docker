FROM ubuntu:16.04

# Update the image with required build packages
RUN \
  sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y \
    net-tools \
    build-essential \
    clang \
    cmake \
    curl  \
    git  \
    htop  \
    libidn11  \
    libz-dev \
    libssl-dev \
    make \
    python-minimal \
    software-properties-common \
    unzip \
    vim \
    wget

ENTRYPOINT [ "/bin/bash" ]
LABEL maintainer="jrepp@blizzard.com"
