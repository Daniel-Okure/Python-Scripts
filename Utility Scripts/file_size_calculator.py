import os

def get_folder_size(path):
    total = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            filepath = os.path.join(dirpath, file)
            try:
                total += os.path.getsize(filepath)
            except(FileNotFoundError, PermissionError):
                pass
    return total
            

base = os.path.expanduser("~")
folder_list = ["Desktop", "Downloads", "Documents", "Videos", "Pictures", "Music"]
sizes = {}
grand_total = 0

for folder in folder_list:
    folder_path = os.path.join(base, folder)
    size = get_folder_size(folder_path)
    sizes[folder] = size
    grand_total += size

for folder, size in sizes.items():
    print(f"{folder}: {size / (1024 ** 3):.2f} GB")
    
print(f"\nTotal size: {grand_total / (1024 ** 3):.2f} GB")