#!/usr/bin/make

THIS_FILE := $(lastword $(MAKEFILE_LIST))

.PHONY : first-run up down stop restart

.DEFAULT_GOAL := help

help:
	make -pRrq  -f $(THIS_FILE) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

first-run:
	docker-compose run --rm borobot
up:
	docker-compose up -d borobot
down:
	docker-compose down borobot
stop:
	docker-compose stop borobot
restart:
	docker-compose restart borobot