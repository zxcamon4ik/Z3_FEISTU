myUID := $(shell id -u)

CC = gcc
CFLAGS = -Iinclude
TARGET = TCase
NAME = tmpTest.txt
INPUT = z2_testing/stdin/scenar_1/example_1.txt
NUM=1

cases:
	@mkdir -p z2_testing/stdusr

create: cases build
	@timeout 5 ./$(TARGET) < $(INPUT) > z2_testing/stdusr/$(NAME)

build:
	rm -f $(TARGET)
	@$(CC) $(CFLAGS) -o $(TARGET) ./src/z2.c ./src/functions.c ./src/data.c -lm


run: build 
	python3 tester.py

clean:
	@rm -rf z2_testing/stdusr

d-run: build
	@export myUID=${myUID} && \
	COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		docker compose build --build-arg SRC=$(SRC) && \
		docker compose up --build 



.PHONY: build create run clean d-run
