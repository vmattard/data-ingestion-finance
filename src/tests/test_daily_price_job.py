from collections import namedtuple
from datetime import date

from chispa.dataframe_comparer import *

DailyPrice = namedtuple("DailyPrice", "date symbol open high close low volume")


def test_daily_price(spark):
    source_data = [
        DailyPrice(date(2024, 12, 1), "TSLA", 10.1, 11.1, 9.1, 8.1, 10000),
        DailyPrice(date(2024, 12, 2), "TSLA", 10.1, 11.1, 9.1, 8.1, 10000),
        DailyPrice(date(2024, 12, 3), "TSLA", 10.1, 11.1, 9.1, 8.1, 10000)
    ]
    source_df = spark.createDataFrame(source_data)

    actual_df = do_transform(spark, source_df)  # TODO
    expected_data = [
        DailyPrice(date(2024, 12, 1), "TSLA", 10.1, 11.1, 9.1, 8.1, 10000),
        DailyPrice(date(2024, 12, 2), "TSLA", 10.1, 11.1, 9.1, 8.1, 10000),
        DailyPrice(date(2024, 12, 3), "TSLA", 10.1, 11.1, 9.1, 8.1, 10000)
    ]
    expected_df = spark.createDataFrame(expected_data)
    assert_df_equality(actual_df, expected_df)
