from datetime import time
from pytz import timezone

from pandas.tseries.holiday import AbstractHolidayCalendar
from pandas_market_calendars.holidays.us import (
    USNewYearsDay,
    Christmas,
)
from pandas_market_calendars.market_calendar import MarketCalendar


class IBForexExchangeCalendar(MarketCalendar):
    aliases = ['IB_Currency', 'IB_FX', 'IB_Forex', 'IB_Currency']

    # Using IB Forex trading times
    regular_market_times = {
        "market_open": ((None, time(17, 15), -1),),  # offset by -1 day
        "market_close": ((None, time(17, 00)),)
    }

    @property
    def name(self):
        return "IB_FX"

    @property
    def tz(self):
        return timezone("US/Eastern")

    @property
    def regular_holidays(self):
        return AbstractHolidayCalendar(rules=[
            USNewYearsDay,
            Christmas,
        ])
