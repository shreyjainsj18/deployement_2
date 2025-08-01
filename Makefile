IMAGE   := ghcr.io/${USER}/mlapptest

.PHONY: help fmt lint test build run push

help:  ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?##' Makefile | sort | awk 'BEGIN{FS=":.*?##"}{printf "  \033[32m%-12s\033[0m%s\n", $$1, $$2}'

fmt:   ## Format with black
	black .

lint:  ## Run flake8
	flake8 .

test:  ## Run pytest
	pytest -q

build: ## Build docker image
	docker build -t $(IMAGE):dev .

run:   ## Run container locally
	docker run -it --rm -p 5000:5000 --env-file .env $(IMAGE):dev

push:  ## Push dev tag to GHCR
	docker push $(IMAGE):dev
