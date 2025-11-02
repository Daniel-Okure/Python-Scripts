import subprocess
from pathlib import Path


def ffmpeg_converter():
    video_path = Path.home() / "Videos"
    music_path = Path.home() / "Music"
    videos = video_path.iterdir()
    
    
    for video in videos:
        
        if video.name.endswith((".ts", ".mp4", ".mkv", ".webm")):
            name = video.stem
            output_path = music_path / f"{name}.mp3"
    
            command = ["ffmpeg", "-i", video, "-q:a", "0", "-map", "a", output_path]  # Requires ffmpeg
            subprocess.run(command, check=True)
            print(f"Converted: {video} -> {output_path}")


if __name__ == "__main__":
    ffmpeg_converter()

    




    





















