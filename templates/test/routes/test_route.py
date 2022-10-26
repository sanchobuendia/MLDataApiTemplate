import unittest
from unittest.mock import patch, MagicMock

import src.main as main
import src.routes.route as route

@patch("src.routes.route.service")
class TestRoute(unittest.TestCase):
    def setUp(self):
        self.app = main.app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_sum_success(self, mock_service):
        with self.app.test_request_context():
            mock_service.sum.return_value = {"result": 3}

            response = route.sum(1, 2)

            mock_service.sum.assert_called_once()
            self.assertEqual(response.status_code, 200)

    def test_sum_exception(self, mock_service):
        with self.assertRaises(Exception):
            route.sum(1, "r")
