def read_and_modify_file():
    filename = input("Please enter the filename: ")

    try:
        # Attempt to open and read the file
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Successfully read file: {filename}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return
    except PermissionError:
        print(f"Error: You do not have permission to read '{filename}'.")
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return

    # Modify the content (for example, convert to uppercase)
    modified_content = content.upper()

    # Create a new filename for the modified file
    new_filename = f"modified_{filename}"

    try:
        # Attempt to write the modified content to a new file
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)
            print(f"Successfully wrote modified content to: {new_filename}")
    except PermissionError:
        print(f"Error: You do not have permission to write to '{new_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred while writing: {e}")

if __name__ == "__main__":
    read_and_modify_file()