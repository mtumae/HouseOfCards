import sys
import time

import numpy as np

from photo.photo import convert_photo
from video.video import convert_video

if __name__ == "__main__":
    # Seed numpy RNG for reproducible behavior across runs if desired
    np.random.seed(int(time.time() % 2**32))

    # print("Starting photo conversion...")
    # start_time = time.time()
    # try:
    #     convert_photo()
    # except Exception as e:
    #     print(f"Error: {e}")
    #     sys.exit(1)
    # end_time = time.time()
    # print(f"\nConvert photo took: {end_time - start_time}(s)")

    start_time = time.time()
    print("Starting video conversion...")
    try:
        convert_video()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
    end_time = time.time()
    print(f"\nConvert video took: {end_time - start_time}(s)")
