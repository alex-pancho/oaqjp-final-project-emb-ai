import unittest
from EmotionDetection import emotion_detector


class TestEmotionDetection(unittest.TestCase):

    @staticmethod    
    def call_dominant(text):
        return emotion_detector(text)["dominant_emotion"]


    def test_emotion_detection(self):
        self.assertEqual(
            self.call_dominant("I am glad this happened"),
            "joy"
        )

if __name__ == "__main__":
    unittest.main()