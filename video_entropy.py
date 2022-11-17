import time
from hashlib import sha256

import cv2
import numpy as np
from accumulation import Accumulator


class RNG:
    def __init__(self, accumulator: Accumulator) -> None:
        self.accumulator = accumulator

    def fill_entropy_pool(self):
        cv2.namedWindow("preview")
        vc = cv2.VideoCapture(0)

        if vc.isOpened():  # try to get the first frame
            rval, frame = vc.read()
        else:
            rval = False

        i = 0
        while True:
            i += 1
            rval, frame = vc.read()

            # frame = cv2.resize(frame, (160, 100), interpolation=cv2.INTER_AREA)

            x_max, y_max, _ = frame.shape

            x = int((time.time() * 1e6) % x_max)
            y = int((time.time() * 1e6) % y_max)
            rval = int(np.sum(frame[x, y, :]))
            self.accumulator.pools[i % 32] += rval.to_bytes(2, "big")

            if i > 50:
                vc.release()
                cv2.destroyWindow("preview")
                break
