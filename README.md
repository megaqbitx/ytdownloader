# YouTube Clip Extractor

This repository contains a Python script that allows users to download videos from YouTube and extract specific clips from them. The tool uses `yt-dlp` for downloading and `moviepy` for video editing.

## Features

- Download YouTube videos in high quality (up to 1080p).
- Extract clips from downloaded videos using specified start and end times.
- Save extracted clips in MP4 format.

## Requirements

Before using the script, ensure you have the following installed:

- Python 3.6 or higher
- `yt-dlp` (YouTube downloader)
- `moviepy` (Video editing library)
- `ffmpeg` (Required by `moviepy` for video processing)

You can install the necessary Python packages using pip:

```bash
pip install yt-dlp moviepy

```

## Example
```
Enter YouTube URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Enter start time (in format mm:ss): 00:30
Enter end time (in format mm:ss): 01:00
Enter output folder path: /path/to/output

```
