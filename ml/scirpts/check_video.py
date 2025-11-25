import cv2
from pathlib import Path

def main():
    video_path = Path("data/raw/example_match.mp4")
    if not video_path.exists():
        raise FileNotFoundError(f"Video not found at {video_path}")

    cap = cv2.VideoCapture(str(video_path))

    if not cap.isOpened():
        raise RuntimeError("Could not open video")

    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration_sec = frame_count / fps if fps else 0

    print(f"Video: {video_path}")
    print(f"FPS: {fps}")
    print(f"Frames: {frame_count}")
    print(f"Duration: {duration_sec/60:.2f} minutes")

    cap.release()

if __name__ == "__main__":
    main()

