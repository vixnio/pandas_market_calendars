from datetime import time
from pytz import timezone

from pandas.tseries.holiday import AbstractHolidayCalendar
from pandas_market_calendars.holidays.us import (
    USNewYearsDay,
    Christmas,
)
from pandas_market_calendars.market_calendar import MarketCalendar


class DukascopyForexExchangeCalendar(MarketCalendar):
    aliases = ['Dukascopy_Currency', 'Dukascopy_FX', 'Dukascopy_Forex', 'Dukascopy_Currency']

    # Using Dukascopy Forex trading times
    regular_market_times = {
        "market_open": ((None, time(17, 00), -1),),  # offset by -1 day
        "market_close": ((None, time(17, 00)),)
    }

    @property
    def name(self):
        return "Dukascopy_FX"

    @property
    def tz(self):
        return timezone("US/Eastern")

    @property
    def regular_holidays(self):
        return AbstractHolidayCalendar(rules=[
            USNewYearsDay,
            Christmas,
        ])
