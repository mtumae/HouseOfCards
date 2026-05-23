"""Real-time video -> ASCII (in-memory, vectorized, CLI)

Replaces disk I/O with in-memory processing and uses a per-frame LUT for
fast brightness->character mapping. Includes proper resource handling and
an argparse CLI.
"""

import argparse
import os
import sys
import time
from logging import makeLogRecord

import cv2
import numpy as np

# ASCII palette and zone bounds (lighter -> darker)
GREYSCALE = [
    " ",
    " ",
    ".,-",
    "_ivc=!/|\\~",
    "gjez2]/(YL)t[+T7Vf",
    "mdK4ZGbNDXY5P*Q",
    "W8KMA",
    "#%$",
]
ZONEBOUNDS = [36, 72, 108, 144, 180, 216, 252]


def make_lut(zonebounds=ZONEBOUNDS, greyscale=GREYSCALE):
    """Create a 256-entry LUT mapping brightness (0-255) to a random
    character from the appropriate greyscale zone. A new LUT can be made
    each frame for visual variation, or reused for deterministic output.
    """
    lut = np.empty(256, dtype="U1")
    for v in range(256):
        zone = np.digitize(v, zonebounds)
        chars = greyscale[zone]
        lut[v] = chars[np.random.randint(len(chars))]
    print(lut)
    return lut


def frame_to_ascii(frame, width, height, zonebounds=ZONEBOUNDS, greyscale=GREYSCALE):
    """Convert a BGR OpenCV frame (numpy array) to an ASCII string.

    - Resize and convert to grayscale in-memory
    - Build a random LUT for this frame (fast)
    - Map pixels through LUT using numpy indexing
    - Join rows into a single string ready for printing
    """
    # grayscale and resize
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    small = cv2.resize(gray, (width, height), interpolation=cv2.INTER_LINEAR)

    # invert brightness so 0 -> darkest (optional, matches original behavior)
    inverted = 255 - small

    # make LUT and map
    lut = make_lut(zonebounds, greyscale)
    chars = lut[inverted]

    # join rows into lines
    # chars is an array of shape (height, width) dtype '<U1'
    lines = ["".join(row) for row in chars.tolist()]
    return "\n".join(lines)


def clear_terminal():
    # ANSI clear (fast) - works on most terminals
    sys.stdout.write("\033[H\033[J")
    sys.stdout.flush()


def parse_args():
    p = argparse.ArgumentParser(description="Real-time camera -> ASCII")
    p.add_argument("--width", type=int, default=200, help="ASCII frame width")
    p.add_argument("--height", type=int, default=100, help="ASCII frame height")
    p.add_argument("--camera", type=int, default=0, help="Camera index")
    p.add_argument(
        "--no-preview", action="store_true", help="Don't show OpenCV preview window"
    )
    p.add_argument(
        "--backend-dshow", action="store_true", help="Use CAP_DSHOW on Windows"
    )
    return p.parse_args()


def convert_video():
    args = parse_args()

    # Choose backend if requested (Windows often benefits from DSHOW)
    backend = cv2.CAP_DSHOW if args.backend_dshow else 0
    cap = (
        cv2.VideoCapture(args.camera, backend)
        if args.backend_dshow
        else cv2.VideoCapture(args.camera)
    )

    if not cap.isOpened():
        print("Cannot open camera. Check if camera is closed.")
        return 1

    try:
        # Read loop
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break

            ascii_frame = frame_to_ascii(frame, args.width, args.height)

            # print to terminal
            clear_terminal()
            print(ascii_frame)

            # optional preview window
            if not args.no_preview:
                cv2.imshow("Preview", frame)
                # waitKey required for imshow to work; small delay
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break

            # allow quick exit from terminal as well
            # If user presses Ctrl+C, we'll catch KeyboardInterrupt
    except KeyboardInterrupt:
        pass
    finally:
        cap.release()
        cv2.destroyAllWindows()

    return 0
