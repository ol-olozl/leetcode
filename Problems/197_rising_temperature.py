import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather.sort_values(by="recordDate", inplace=True)
    weather["prevTemperature"] = weather["temperature"].shift(1)
    weather["prevDate"] = weather["recordDate"].shift(1)
    weather = weather[
        (weather["prevTemperature"] < weather["temperature"]) & ((weather["recordDate"] - weather["prevDate"]).dt.days == 1)
    ]
    return weather[["id"]]
