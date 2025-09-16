import os, subprocess


def ffmpeg_converter():
    video_path = os.path.join(os.path.expanduser("~"), "Videos")
    music_path = os.path.join(os.path.expanduser("~"), "Music")
    videos = os.listdir(video_path)
    
    
    for video in videos:
        file_path = os.path.join(video_path, video)
        
        if file_path.endswith((".ts", ".mp4", ".mkv", ".webm")):
            name, _ = os.path.splitext(video)
            output_path = os.path.join(music_path, f"{name}.mp3")
    
            command = ["ffmpeg", "-i", file_path, "-q:a", "0", "-map", "a", output_path]  # Requires ffmpeg
            subprocess.run(command, check=True)
            print(f"Converted: {file_path} -> {output_path}")


if __name__ == "__main__":
    ffmpeg_converter()

    




    





















