FROM sc2-game
FROM sc2-api

WORKDIR /
COPY --from=0 /StarCraftII /StarCraftII

WORKDIR /build
COPY build-api.sh /build
RUN sh /build/build-api.sh

COPY builder.py /build

ENTRYPOINT [ "./builder.py" ]

LABEL maintainer="wizzup@gmail.com"
