import math
from hashlib import sha256

from Crypto.Cipher import AES


class Gen:
    def __init__(self, key: str):
        self.k = sha256(key).digest()
        self.cnt: int = 0

    def reseed(self, seed) -> None:
        result = sha256(self.k + seed)
        self.k = result.digest()
        self.cnt += 1

    def generate_blocks(self, num_blocks: int) -> bytes:
        res = b""
        for block in range(num_blocks):
            # print(f"key: {self.k}")
            res += AES.new(key=self.k).encrypt(self.cnt.to_bytes(16, "big"))
            # print(res[-num_blocks:])
            self.cnt += 1
        return res

    def generate_random(self, n_bytes) -> bytes:
        n = math.ceil(n_bytes / 16)
        res = self.generate_blocks(n)[-n_bytes:]
        self.k = self.generate_blocks(2)
        return res.hex()
