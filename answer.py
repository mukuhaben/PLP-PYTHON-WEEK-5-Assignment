def read_and_write_modified_file():
    # Ask the user for the filename
    filename = input("Enter the filename to read from: ")

    try:
        # Try to open and read the file
        with open(filename, 'r') as file:
            lines = file.readlines()

        # Modify the content - here we reverse each line
        modified_lines = [line[::-1] for line in lines]

        # Prepare new filename
        new_filename = "modified_" + filename

        # Write the modified content to a new file
        with open(new_filename, 'w') as new_file:
            new_file.writelines(modified_lines)

        print(f"Modified file saved as: {new_filename}")

    except FileNotFoundError:
        print("🚫 Error: File not found. Please check the filename and try again.")
    except PermissionError:
        print("🚫 Error: Permission denied. You don't have access to this file.")
    except Exception as e:
        print(f"🚫 Unexpected error: {e}")

# Run the program
read_and_write_modified_file()
