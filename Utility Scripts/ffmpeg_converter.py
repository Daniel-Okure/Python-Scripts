import subprocess
from pathlib import Path


def video_converter(dest, video):
    music_path = Path.home() / "Music"
        
    video_name = video.stem
    output_path = music_path / f"{video_name}{dest}"
    
    command = ["ffmpeg", "-i", str(video), "-q:a", "0", "-map", "a", str(output_path)]  # Requires ffmpeg
    subprocess.run(command, check=True)
    print(f"Converted: {video} -> {output_path}")


if __name__ == "__main__":
    video_path = Path(input("Enter absolute path of specific video: ").strip())
    dest_format = input('Enter desired format (e.g., ".wav"): ').strip()

    video_converter(dest_format, video_path)

    




    





















