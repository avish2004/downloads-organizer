import os
import shutil

downloads_folder = os.path.expanduser('~/Downloads')

folders = {
    'PDFs': ['.pdf'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Screenshots': ['.png', '.jpg', '.jpeg'],  # Assuming screenshots are in these formats
    'Documents': ['.doc', '.docx', '.txt', '.xlsx', '.pptx', '.csv'],
    'Music': ['.mp3', '.wav', '.flac'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
    'Archives': ['.zip', '.tar', '.gz', '.rar', '.7z'],
    'Scripts': ['.py', '.sh', '.bat', '.js'],
    'C++': ['.c', '.h', '.cpp'],
    'Others': []
}

def create_folders():
    for folder in folders:
        folder_path = os.path.join(downloads_folder, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

def move_files():
    for item in os.listdir(downloads_folder):
        item_path = os.path.join(downloads_folder, item)
        if os.path.isfile(item_path):
            moved = False
            for folder, extensions in folders.items():
                if any(item.lower().endswith(ext) for ext in extensions):
                    dest_folder = os.path.join(downloads_folder, folder)
                    shutil.move(item_path, os.path.join(dest_folder, item))
                    moved = True
                    break
            if not moved:
                # If file type doesn't match any predefined folders, move to 'Others'
                dest_folder = os.path.join(downloads_folder, 'Others')
                shutil.move(item_path, os.path.join(dest_folder, item))

if __name__ == "__main__":
    create_folders()
    move_files()
