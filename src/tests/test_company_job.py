from collections import namedtuple

from chispa.dataframe_comparer import *

Company = namedtuple("Company", "symbol")


def test_company(spark):
    source_data = [
        Company("TSLA"),
        Company("MSFT"),
        Company("META")
    ]
    source_df = spark.createDataFrame(source_data)

    actual_df = do_transform(spark, source_df)  # TODO
    expected_data = [
        Company("TSLA"),
        Company("MSFT"),
        Company("META")
    ]
    expected_df = spark.createDataFrame(expected_data)
    assert_df_equality(actual_df, expected_df)
