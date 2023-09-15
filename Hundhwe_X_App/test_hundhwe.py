import unittest
from unittest.mock import patch, Mock
import hundhwe

class HundhweTestCase(unittest.TestCase):

    @patch('hundhwe.requests.post')
    def test_create_tweet_success(self, mock_post):
        # Mock a successful response
        mock_response = Mock()
        mock_response.status_code = 201
        mock_post.return_value = mock_response
        
        response = hundhwe.create_tweet("test tweet")
        self.assertEqual(response, "Tweet posted successfully!")
    
    @patch('hundhwe.requests.post')
    def test_create_tweet_failure(self, mock_post):
        # Mock a failed response
        mock_response = Mock()
        mock_response.status_code = 400
        mock_response.text = "Error message"
        mock_post.return_value = mock_response
        
        response = hundhwe.create_tweet("test tweet")
        self.assertEqual(response, "Failed to post tweet. Status code: 400, Message: Error message")

    @patch('hundhwe.requests.delete')
    def test_delete_tweet_success(self, mock_delete):
        # Mock a successful response
        mock_response = Mock()
        mock_response.status_code = 204
        mock_delete.return_value = mock_response

        response = hundhwe.delete_tweet("12345")
        self.assertEqual(response, "Tweet with ID 12345 deleted successfully!")

    @patch('hundhwe.requests.delete')
    def test_delete_tweet_failure(self, mock_delete):
    # Mock a failed response
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.text = "Tweet not found"
        mock_delete.return_value = mock_response

        response = hundhwe.delete_tweet("12345")
        self.assertEqual(response, "Failed to delete tweet. Status code: 404, Message: Tweet not found")


    @patch('hundhwe.requests.get')
    def test_fetch_user_details_success(self, mock_get):
        # Mock a successful response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"id": "123", "name": "Test User"}
        mock_get.return_value = mock_response

        user_data = hundhwe.fetch_user_details()
        self.assertEqual(user_data, {"id": "123", "name": "Test User"})

    @patch('hundhwe.requests.get')
    def test_fetch_user_details_failure(self, mock_get):
        # Mock a failed response
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.text = "User not found"
        mock_get.return_value = mock_response

        user_data = hundhwe.fetch_user_details()
        self.assertEqual(user_data, {"error": "Failed to fetch user details. Status code: 404, Message: User not found"})


if __name__ == "__main__":
    unittest.main()
