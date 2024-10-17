import yt_dlp
from moviepy.editor import VideoFileClip
import os

def download_video(youtube_url, download_path):
    try:
        # Options for yt-dlp to download the best quality video up to 1080p
        ydl_opts = {
            'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
            'merge_output_format': 'mp4',  # Ensures the output is in MP4 format
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(youtube_url, download=True)
            video_path = ydl.prepare_filename(info_dict)
            print(f"Downloaded video to {video_path}")
            return video_path
    except Exception as e:
        print(f"Error downloading video: {e}")
        return None

def extract_clip(video_path, start_time, end_time, output_folder):
    try:
        # Convert time format mm:ss to seconds
        def time_to_seconds(time_str):
            minutes, seconds = map(int, time_str.split(':'))
            return minutes * 60 + seconds

        start_seconds = time_to_seconds(start_time)
        end_seconds = time_to_seconds(end_time)

        clip = VideoFileClip(video_path).subclip(start_seconds, end_seconds)
        output_path = os.path.join(output_folder, "extracted_clip.mp4")
        clip.write_videofile(output_path, codec='libx264')
        print(f"Clip saved to {output_path}")
        clip.close()
        return output_path
    except Exception as e:
        print(f"Error extracting clip: {e}")
        return None

def main():
    youtube_url = input("Enter YouTube URL: ")
    start_time = input("Enter start time (in format mm:ss): ")
    end_time = input("Enter end time (in format mm:ss): ")
    output_folder = input("Enter output folder path: ")

    # Download video
    video_path = download_video(youtube_url, output_folder)
    if not video_path:
        return

    # Extract clip
    clip_path = extract_clip(video_path, start_time, end_time, output_folder)

    # Clean up original video file
    if clip_path:
        os.remove(video_path)
        print("Original video file deleted to save space.")

if __name__ == "__main__":
    main()
