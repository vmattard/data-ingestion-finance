# Data Ingestion - Finance

- Apache Spark
- Apache Iceberg
- MinIO

# [Hadoop Installation on Windows](https://gist.github.com/vorpal56/5e2b67b6be3a827b85ac82a63a5b3b2e)

# [Spark Job Config](https://github.com/databricks/docker-spark-iceberg/blob/main/spark/spark-defaults.conf)

# Paths Mapping

| Local Path  | Container Path          | Purpose                                             |
|-------------|-------------------------|-----------------------------------------------------|
| ./warehouse | /home/iceberg/warehouse | Stores Iceberg metadata and data for persistence.   |
| ./notebooks | /home/iceberg/notebooks | Stores Jupyter notebooks for editing and execution. |
| ./data      | /home/iceberg/data      | Stores raw input data files for Spark jobs.         |
| ./src/jobs  | /opt/spark/jobs         | Stores Spark job scripts for execution.             |

# Usage

```
make create-env
make activate-env
make restart
make submit-job job=company_job.py
make submit-job job=daily_price_job.py
```