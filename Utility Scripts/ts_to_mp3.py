import os, subprocess

video_path = os.path.join(os.path.expanduser("~"), "Videos")
videos = os.listdir(video_path)
ts_path = ""
mp3_path = os.path.join(os.path.expanduser("~"), "Music", "file.mp3")

for video in videos:
    file_path = os.path.join(video_path, video)
    if file_path.endswith(".ts"):
        ts_path = file_path
        
def ts_to_mp3(input_path, output_path):
    
    command = ["ffmpeg", "-i", input_path, "-q:a", "0", "-map", "a", output_path] #Requires ffmpeg
    
    subprocess.run(command)
    print(f"Converted: {output_path}")
    
ts_to_mp3(ts_path, mp3_path)
    
    

    




    





















