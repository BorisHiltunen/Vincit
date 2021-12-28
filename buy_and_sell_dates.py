"""
buy_and_sell_dates.py:
Contains function that returns the best days to buy and sell bitcoin.
"""

import incorrect_input_json_formatter
import sum_difference_iterator
from timestamp_engine import TimeForm
from buy_and_sell_dates_json_formatter import TradingFormatter
import __init__

timeform = TimeForm()
trading_formatter = TradingFormatter()


def get_best_days_trading_days():
    """Function for getting the best days to buy and sell bitcoin."""

    both = (
        ('buy', 1637971200.0, 1000000000.0, 24),
        ('sell', 1637971200.0, 0.0),
        0.0
        )

    if __init__.incorrect_input:
        text = "Incorrect input"

        return incorrect_input_json_formatter.incorrect_input_to_json_form(
            tuple((
                text,
                __init__.data
            ))
        )

    for difference in sum_difference_iterator.get_sum_differences():
        if difference[2] > both[2]:
            both = difference

    if __init__.one_day:
        text = ("Don't buy unless you want to sell on the same day")

        return trading_formatter.trading_on_the_same_day_to_json_form(
            tuple((
                text,
                __init__.data[0][3],
                __init__.data[0][3][:10],
                __init__.data[0][3][11:],
                str(timeform.get_date_from_timestamp(both[0][1]))[:10],
                str(timeform.get_date_from_timestamp(both[1][1]))[:10],
                str(timeform.get_date_from_timestamp(both[0][1]))[11:],
                str(timeform.get_date_from_timestamp(both[1][1]))[11:],
                int(both[0][2]),
                int(both[1][2]),
                both[2]
            ))
        )

    if both[2] <= 0:
        text = "Don't buy"

        return trading_formatter.buy_and_sell_dates_to_json_form(
            tuple((
                text,
                __init__.data[0][3],
                __init__.data[0][3][:10],
                __init__.data[0][3][11:],
                str(timeform.get_date_from_timestamp(both[0][1]))[:10],
                str(timeform.get_date_from_timestamp(both[1][1]))[:10],
                str(timeform.get_date_from_timestamp(both[0][1]))[11:],
                str(timeform.get_date_from_timestamp(both[1][1]))[11:],
                int(both[0][2]),
                int(both[1][2]),
                both[2]
            ))
        )
    else:
        text = (f"Buy date: "
                f"{timeform.get_date_from_timestamp(both[0][1])[:10]}, "
                f"Sell date: "
                f"{timeform.get_date_from_timestamp(both[1][1])[:10]}")

        return trading_formatter.buy_and_sell_dates_to_json_form(
            tuple((
                text,
                __init__.data[0][3],
                __init__.data[0][3][:10],
                __init__.data[0][3][11:],
                str(timeform.get_date_from_timestamp(both[0][1]))[:10],
                str(timeform.get_date_from_timestamp(both[1][1]))[:10],
                str(timeform.get_date_from_timestamp(both[0][1]))[11:],
                str(timeform.get_date_from_timestamp(both[1][1]))[11:],
                int(both[0][2]),
                int(both[1][2]),
                both[2]
            ))
        )
