.PHONY: build run bash down clean

IMAGE_NAME := website-scraper

build:
	@echo "Building the docker image..."
	docker build -t $(IMAGE_NAME) .

run:
	@echo "Running the application..."
	cat websites.txt | docker run -i $(IMAGE_NAME)

bash:
	@echo "Accessing bash inside the container..."
	docker run -it $(IMAGE_NAME) bash

down:
	@echo "Stopping containers..."
	docker stop $(shell docker ps -aq --filter ancestor=$(IMAGE_NAME))

clean:
	@echo "Cleaning up..."
	docker system prune -f
	docker rmi $(IMAGE_NAME)
