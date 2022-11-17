from accumulation import Accumulator
from video_entropy import RNG

accumulator = Accumulator("this is my key".encode())
rng = RNG(accumulator=accumulator)


while True:
    # print(f"pool 0: {accumulator.pools[0]}")
    rng.fill_entropy_pool()
    # print(f"pool0: {accumulator.pools[0]}")
    print(accumulator.get_random(1))
