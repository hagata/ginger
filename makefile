GINGER_IMAGE = hagata/ginger-scaffold

VOLUMES = -v $(shell pwd):/app/

gcloud:
	docker run -ti $(VOLUMES) --name ginger-cloud google/cloud-sdk bash

container:
	docker run -ti $(VOLUMES) --name ginger-container $(GINGER_IMAGE)

r:
	docker stop ginger-container
	docker rm ginger-container


# rebuilds the huge/gweb-multiscreen image
dk-build:
	docker build -t $(GINGER_IMAGE) .
