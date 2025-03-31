myUID := $(shell id -u)

CC = gcc
CFLAGS = 
TARGET = TCase
NAME = tmpTest.txt
INPUT = stdin/scenar_1/example_1.txt
NUM=1

cases:
	@mkdir -p stdusr

create: cases build
	@timeout 5 ./$(TARGET) < $(INPUT) > stdusr/$(NAME)

build:
	@rm -f $(TARGET)
	@$(CC) $(CFLAGS) -o $(TARGET) ./z3.c 


run: build 
	@python3 tester.py

clean:
	@rm -rf stdusr

d-run: build
	@export myUID=${myUID} && \
	COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		docker compose build --build-arg SRC=$(SRC) && \
		docker compose up --build 

d-purge:
	@export myUID=${myUID} &&\
	COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		docker compose down --volumes --remove-orphans --rmi local --timeout 0 


.PHONY: build create run clean d-run d-purge
