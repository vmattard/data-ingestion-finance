.PHONY: up down restart submit-job create-env update-env activate-env

# Docker
up:
	@docker compose up -d

down:
	@docker compose down

restart: down up

# Spark
submit-job:
	@docker exec -it spark-iceberg /bin/bash -c "cd /opt/spark/jobs && /opt/spark/bin/spark-submit $(job)"

# Conda
create-env:
	@conda env create -f environment.yaml

update-env:
	@conda env update -f environment.yaml

activate-env:
	@conda activate data-ingestion-finance
