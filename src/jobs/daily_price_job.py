from pyspark.sql import SparkSession


def main(destination: str) -> None:
    spark = SparkSession.builder \
        .master("local") \
        .appName("Load Stock Daily Price") \
        .getOrCreate()

    spark.sql(f"DROP TABLE IF EXISTS {destination}")

    spark.sql(f"""
        CREATE TABLE IF NOT EXISTS {destination} (
            date DATE NOT NULL,        
            symbol STRING  NOT NULL,  
            close DOUBLE,
            open DOUBLE,
            high DOUBLE,
            low DOUBLE,
            volume BIGINT
        )
        USING iceberg        
    """)

    df_companies = spark.sql(f"""
        SELECT symbol 
        FROM {CATALOG_NAME}.default.company        
        ORDER BY symbol
    """)

    for row in df_companies.collect():
        symbol = row["symbol"]
        try:
            print(f"Processing data for symbol: {symbol}")

            df = spark.read.parquet(f"/home/iceberg/data/symbols/{symbol}.parquet")

            df.writeTo(f"{destination}").using("iceberg").append()

        except Exception as e:
            print(f"An error occurred while processing symbol={symbol}")
            print(e)

    print(f"Table {destination} created and data written successfully.")
    spark.stop()


if __name__ == "__main__":
    CATALOG_NAME = "stock_market"
    TABLE_NAME = "daily_price"

    main(destination=f"{CATALOG_NAME}.default.{TABLE_NAME}")
