import os

# --- 1. SET YOUR FOLDER PATH HERE ---
# IMPORTANT: Use forward slashes (/) even on Windows.
# Example: 'C:/Users/YourName/Desktop/MyPhotos'
# Example: '/home/YourName/Documents/MyFiles'
folder_path = 'C:/Users/YourUser/Desktop/MyFolder'

# --- 2. SET YOUR PREFERENCES ---
# The starting number for the count
start_number = 1
# A temporary suffix to avoid file conflicts. You shouldn't need to change this.
temp_suffix = '.tmp_rename'

# -----------------------------------------------------------------
# PHASE 1: Rename all files to a temporary name.
# This prevents conflicts, e.g., renaming 'a.jpg' to '1.jpg'
# when '1.jpg' already exists.
# -----------------------------------------------------------------
print(f"--- PHASE 1: Renaming files to temporary names in '{folder_path}' ---")
try:
    file_list = os.listdir(folder_path)

    for filename in file_list:
        old_file_path = os.path.join(folder_path, filename)

        # Check if it's a file and not already a temp file
        if os.path.isfile(old_file_path) and not filename.endswith(temp_suffix):
            # Create the new temporary name
            temp_name = f"{filename}{temp_suffix}"
            new_file_path = os.path.join(folder_path, temp_name)

            # Rename
            os.rename(old_file_path, new_file_path)
            print(f"Renamed: {filename}  ->  {temp_name}")

except FileNotFoundError:
    print(f"ERROR: Folder not found. Please check the 'folder_path': {folder_path}")
    exit()
except Exception as e:
    print(f"An error occurred during Phase 1: {e}")
    exit()

# -----------------------------------------------------------------
# PHASE 2: Rename all temporary files to their final number.
# -----------------------------------------------------------------
print("\n--- PHASE 2: Renaming temporary files to final numbers ---")
try:
    # Get a new list of all the temporary files we just created
    temp_file_list = [f for f in os.listdir(folder_path) if f.endswith(temp_suffix)]

    # Sort the list alphabetically to ensure a consistent order
    temp_file_list.sort()

    # Initialize our counter
    count = start_number

    for temp_filename in temp_file_list:
        old_temp_path = os.path.join(folder_path, temp_filename)

        # Get the original filename back (by removing the suffix)
        original_filename = temp_filename.replace(temp_suffix, '')

        # Get the original file extension
        _root, extension = os.path.splitext(original_filename)

        # Create the new final filename
        final_name = f"{count}{extension}"
        final_file_path = os.path.join(folder_path, final_name)

        # Rename
        os.rename(old_temp_path, final_file_path)
        print(f"Renamed: {temp_filename}  ->  {final_name}")

        # Increment the counter for the next file
        count += 1

    print(f"\n✅ Renaming complete! {count - start_number} files were renamed.")

except Exception as e:
    print(f"An error occurred during Phase 2: {e}")
    print(
        "Your files might be left with the '.tmp_rename' suffix. You may need to run the script again or rename them manually.")