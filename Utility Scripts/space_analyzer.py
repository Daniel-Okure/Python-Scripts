import platform
from pathlib import Path

script = Path(__file__)

if platform.system() == "Windows":
    root = rf"{script.drive}\\"
    
elif platform.system() in  ("Darwin", "Linux"):
    root = Path("/")

threshold = 5 * 1024 ** 3 # Check for files greater than or equal to 5GB

def space_analyzer(folder, target_size):
    large_files = {}
    large_dirs = []
    
    # Walk through directory paths, names, and files
    for dirpath, dirnames, filenames in Path(folder).walk():
        for filename in filenames:
            try:
                file_path = dirpath / filename
                size = file_path.stat().st_size
                if size >= target_size:
                    large_dirs.append(dirpath)
                    large_files[filename] = f"{size / 1024 ** 3:.2f} GB"
            except(PermissionError, FileNotFoundError):
                continue
                
    
    if large_files:
        for dir in large_dirs:
            print("You might want to look into these:", dir)
        print("\n\nThese are the files that are eating up your space!", large_files)

if __name__ == "__main__":
    space_analyzer(root, threshold)