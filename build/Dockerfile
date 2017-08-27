FROM s2client-base

# clone api repo
WORKDIR /
RUN git clone --recursive https://github.com/Blizzard/s2client-api

# prebuid the api
WORKDIR /s2client-api
COPY api-build.sh .
RUN ./api-build.sh

ENTRYPOINT [ "/bin/bash" ]
LABEL maintainer="jrepp@blizzard.com"
