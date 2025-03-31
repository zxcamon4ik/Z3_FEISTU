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
COPY --chown=${USER}:555 ./stdin stdin
COPY --chown=${USER}:777 ./stdout stdout
COPY --chown=${USER}:555 ./tester.py tester.py
COPY --chown=${USER}:555 ./z3.c z3.c

RUN chmod -R a+w ${WORKDIR}


ENTRYPOINT ["./entrypoint.sh"]
CMD ["./start.sh"]