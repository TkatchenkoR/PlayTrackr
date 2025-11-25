# PlayTrackr ⚽📊  
_Automated football player touch detection from match video_

PlayTrackr is an AI-powered system that automatically analyses full-game football footage and extracts **every moment a selected player touches the ball**.  
Paste a YouTube link (or upload a video), identify yourself once, and get a curated list of touch timestamps and clips — without manually scrubbing through a 90-minute match.

---

## 🚀 Features (MVP Scope)

- Upload or link a full match video (YouTube or file upload)
- Automatic detection of:
  - All players
  - The ball
- Player tracking using advanced multi-object tracking
- Select yourself once in the video (click-to-identify)
- Automatic detection of your touches based on ball–player proximity and motion patterns
- Output:
  - List of timestamps
  - Optional clipped highlights
  - JSON or CSV export

---

## 🧠 How It Works (High-Level)

1. **Ingest Video**  
   The system downloads or accepts the uploaded file and normalises it using `ffmpeg`.

2. **Frame Processing**  
   Video is sampled (e.g., 10–15 FPS) for efficient analysis.

3. **Object Detection**  
   YOLOv8 identifies:
   - Player bounding boxes  
   - Ball bounding boxes  

4. **Multi-Object Tracking**  
   Trackers such as **ByteTrack** or **DeepSORT** produce stable player IDs over time.

5. **Player Identification**  
   The user clicks on themselves once.  
   The system infers which track corresponds to the target player.

6. **Touch Event Detection**  
   Ball proximity + velocity change + track association generate timestamped “touch events”.

7. **Output Generation**  
   Results are returned as:
   - Touch timestamps  
   - Optional highlight clips  
   - JSON/CSV event objects  

---
