import unittest
from EmotionDetection import emotion_detector


class TestEmotionDetection(unittest.TestCase):

    def test_emotion_detection(self):
        self.assertEqual(
            emotion_detector("I am glad this happened")["dominant_emotion"],
            "joy"
        )

if __name__ == "__main__":
    unittest.main()