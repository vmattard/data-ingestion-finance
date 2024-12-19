from pyspark.sql import SparkSession


def main(destination: str) -> None:
    spark = SparkSession.builder \
        .master("local") \
        .appName("Load S&P500 companies") \
        .getOrCreate()

    spark.sql(f"DROP TABLE IF EXISTS {destination}")

    spark.sql(f"""
    CREATE TABLE IF NOT EXISTS {destination} (
        symbol STRING
    )
    USING iceberg
    """)

    df = spark.read.csv(f"/home/iceberg/data/snp500.csv", header=True)
    print(df.head(5))

    if "Symbol" not in df.columns:
        raise ValueError("The DataFrame does not contain a 'Symbol' column.")

    df.writeTo(f"{destination}").using("iceberg").append()

    print(f"Table {destination} created and data written successfully.")

    spark.stop()


if __name__ == "__main__":
    CATALOG_NAME = "stock_market"
    TABLE_NAME = "company"

    main(destination=f"{CATALOG_NAME}.default.{TABLE_NAME}")
