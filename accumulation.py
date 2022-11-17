import time
from hashlib import sha256

from generation import Gen


class Accumulator:
    def __init__(self, key: str) -> None:
        self.pools = [b""] * 32
        self.cnt = 0
        self.generator = Gen(key=key)

    def get_random(self, n_bytes):
        ready = time.time() * 1e7
        # print(time.time() * 1e7 - ready)
        if len(self.pools[0]) > 64 or time.time() * 1e7 - ready > 10:
            # print("pool filled")
            self.cnt += 1
            s = b""
            for i in range(32):
                if 2 ** i % self.cnt == 0:
                    s += sha256(self.pools[i]).digest()
                    self.pools[i] = b""
            self.generator.reseed(s)
        return self.generator.generate_random(n_bytes=n_bytes)
