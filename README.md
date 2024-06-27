# Downloads Organizer

This Python script organizes files in your Downloads folder into subfolders based on their file type. It helps keep your Downloads folder neat and manageable by automatically sorting files into relevant categories.

### How It Works

1. **Define Folders and Extensions**:
   - The script defines a set of folders (e.g., PDFs, Images, Screenshots, Documents, Music, Videos, Archives, Scripts, C++, Others) and the file extensions associated with each folder.

2. **Create Folders**:
   - The `create_folders` function checks if the predefined folders exist in the Downloads directory. If they don't exist, the function creates them.

3. **Move Files**:
   - The `move_files` function iterates through each file in the Downloads folder. It checks the file extension and moves the file to the corresponding folder.
   - If a file's extension doesn't match any predefined folder, the file is moved to the "Others" folder.

### Installation

1. Clone the repository:
   git clone https://github.com/your-username/downloads-organizer.git
  

2. Navigate to the project directory:
   cd downloads-organizer
   

BOTTOM LINE: This will create the necessary folders in your Downloads directory and move files into the appropriate subfolders based on their file type.
