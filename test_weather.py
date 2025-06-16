import unittest
from unittest.mock import patch
from weather import get_weather

class TestWeather(unittest.TestCase):
    
    @patch("weather.requests.get")
    def test_get_weather_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "main": {"temp": 25},
            "weather": [{"description": "clear sky"}]
        }
        result = get_weather("London")
        self.assertEqual(result["temperature"], 25)
        self.assertEqual(result["description"], "clear sky")

    @patch("weather.requests.get")
    def test_get_weather_not_found(self, mock_get):
        mock_get.return_value.status_code = 404
        result = get_weather("InvalidCity")
        self.assertIsNone(result)

    @patch("weather.requests.get")
    def test_get_weather_city_name(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "main": {"temp": 20},
            "weather": [{"description": "rainy"}]
        }
        result = get_weather("Paris")
        self.assertEqual(result["city"], "Paris")

    @patch("weather.requests.get")
    def test_get_weather_data_type(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "main": {"temp": 15},
            "weather": [{"description": "mist"}]
        }
        result = get_weather("Toronto")
        self.assertIsInstance(result, dict)

if __name__ == '__main__':
    unittest.main()
