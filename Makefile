.PHONY: all build run dev

LOG_LEVEL ?= ERROR

build:
	docker build -t cryptolytics/backend .

dev:
	docker-compose build && docker-compose up

clean-dev:
	docker-compose down -v
