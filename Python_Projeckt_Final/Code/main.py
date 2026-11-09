import os
import shutil
from datetime import datetime

def organize_files(target_directory):
    """
    Automatically organizes files into categorized folders based on their extensions
    and logs all actions to a report file.
    """
    if not os.path.exists(target_directory):
        print(f"Directory '{target_directory}' not found.")
        return

    # Define category folders and their extensions
    extensions_map = {
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Code': ['.py', '.js', '.html', '.css', '.cpp', '.cs'],
        'Archives': ['.zip', '.rar', '.tar']
    }

    log_filename = "automation_report.log"
    
    with open(log_filename, "w", encoding="utf-8") as log_file:
        log_file.write(f"--- File Automation Log - {datetime.now()} ---\n\n")
        
        # Scan the directory
        items = os.listdir(target_directory)
        for item in items:
            item_path = os.path.join(target_directory, item)
            
            # Skip directories, process only files
            if os.path.isfile(item_path) and item != log_filename:
                file_ext = os.path.splitext(item)[1].lower()
                moved = False
                
                # Find the matching category
                for folder_name, exts in extensions_map.items():
                    if file_ext in exts:
                        dest_folder = os.path.join(target_directory, folder_name)
                        os.makedirs(dest_folder, exist_ok=True)
                        
                        shutil.move(item_path, os.path.join(dest_folder, item))
                        log_msg = f"Moved: {item} -> {folder_name}/\n"
                        log_file.write(log_msg)
                        print(log_msg.strip())
                        moved = True
                        break
                
                if not moved:
                    # Move to 'Others' if extension doesn't match predefined categories
                    other_folder = os.path.join(target_directory, 'Others')
                    os.makedirs(other_folder, exist_ok=True)
                    shutil.move(item_path, os.path.join(other_folder, item))
                    log_msg = f"Moved to Others: {item}\n"
                    log_file.write(log_msg)
                    print(log_msg.strip())

    print("\nProcess completed successfully!")

if __name__ == "__main__":
    target = input("Enter the path of the directory to organize (or press Enter for current directory): ").strip()
    if not target:
        target = "."
    organize_files(target)