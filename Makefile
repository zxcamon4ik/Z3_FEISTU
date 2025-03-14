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
	@make cases
	@$(CC) $(CFLAGS) -o $(TARGET) ./src/z2.c ./src/functions.c ./src/data.c -lm

run: build 
	python3 tester.py

.PHONY: build create run
