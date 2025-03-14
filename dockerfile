FROM python:3.12

ENV PYTHONUNBUFFERED=1

ARG WORKDIR=/wd
ARG USER=user


WORKDIR ${WORKDIR}

RUN useradd --system ${USER} && \
    chown --recursive ${USER} ${WORKDIR}

RUN apt update && apt upgrade -y

COPY --chown=${USER}:555 ./docker/service/entrypoint.sh ./entrypoint.sh
COPY --chown=${USER}:555 ./docker/service/start.sh ./start.sh

RUN chmod +x ./entrypoint.sh ./start.sh

COPY --chown=${USER}:555 ./Makefile Makefile
COPY --chown=${USER}:555 ./include include
COPY --chown=${USER}:555 ./src src
COPY --chown=${USER}:777 ./z2_testing z2_testing
COPY --chown=${USER}:555 ./tester.py tester.py



ENTRYPOINT ["./entrypoint.sh"]
CMD ["./start.sh"]