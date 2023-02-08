import unittest
from testing_module import AnonymousSurvey


class MyTestCase(unittest.TestCase):
    """Test for the class AnonymousSurvey"""

    def test_store_single_response(self):
        """Test that single response is stored properly."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response("English")
        self.assertIn('English', my_survey.responses)

    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Hindi', 'Marathi']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response, my_survey.responses)


if __name__ == '__main__':
    unittest.main()
