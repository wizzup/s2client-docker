FROM s2client-game
FROM s2client-api

WORKDIR /
COPY --from=0 /StarCraftII /StarCraftII

WORKDIR /s2client-api

ENTRYPOINT [ "/bin/bash" ]
LABEL maintainer="jrepp@blizzard.com"
