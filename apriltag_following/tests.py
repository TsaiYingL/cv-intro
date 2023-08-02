import unittest
import main
import move
from video import Video
from move import process_frame
import cv2
from dt_apriltags import Detector


class Tests(unittest.TestCase):
    def test1(self):
        """
        Scenario: right width, right height
        center: (960,540)
        """
        video = Video()  # <- Test on this
        frame = video.frame()
        height, width, depth = frame.shape
        self.assertEqual(height, 1080)
        self.assertNotEqual(width, 1080)
        self.assertEqual(width, 1920)
        self.assertNotEqual(height, 1920)
        pass

    def test2(self):
        """
        Scenario: test frame: give picture with tags, compare to positions and # of tags
        """

        frame = cv2.imread(
            "test.jpg"
        )  # <- Open picture with tags in it and then run process_frame

        self.assertEqual()

    def test3(self):
        """
        Scenario: test April tag detector
        """

        # I'm going to take this - Amanda
        at_detector = Detector(
            families="tag36h11",
            nthreads=1,
            quad_decimate=1.0,
            quad_sigma=0.0,
            refine_edges=1,
            decode_sharpening=0.25,
            debug=0,
        )
        frame = cv2.imread("test.jpg")
        (x, y) = process_frame(frame, at_detector)
        # Only 2 AprilTags in the photo
        self.assertEqual(len(x), 2)
        self.assertEqual(len(y), 2)
        # We return percentage so it should be approximately equal?

    def test4(self):
        """
        scenario: test pids? output test %s, use fake tags
        """
        x_list = [1000, 900]
        y_list = [550, 500]
        self.assertEqual(
            main.find_pid(x_list, y_list),
        )


if __name__ == "__main__":
    unittest.main()
