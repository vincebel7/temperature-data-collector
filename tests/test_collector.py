import datetime
from collector.collector import build_message

class MockResponse:
    def __init__(self, temperature, humidity):
        self.temperature = temperature
        self.humidity = humidity


def test_build_message():
    response = MockResponse(25.5, 60.2)
    msg = build_message(response)
    assert msg["temperature"] == "25.5"
    assert msg["humidity"] == "60.2"
    # Check ISO time format
    datetime.datetime.fromisoformat(msg["time"])