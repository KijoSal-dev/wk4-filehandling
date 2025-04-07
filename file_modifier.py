def modify_and_write_file(input_filename, output_filename):
    """
    Reads a file, modifies its contents (uppercases each line), and writes
    the modified content to a new file. Handles potential file-related errors.

    Args:
        input_filename (str): The name of the file to read from.
        output_filename (str): The name of the file to write to.
    """

    try:
        with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
            for line in infile:
                modified_line = line.upper()  # Modify each line (uppercase in this case)
                outfile.write(modified_line)

        print(f"Successfully processed '{input_filename}' and wrote modified content to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")
    except PermissionError:
        print(f"Error: Permission denied to read '{input_filename}' or write to '{output_filename}'.")
    except Exception as e:  # Catch any other potential errors
        print(f"An unexpected error occurred: {e}")


def main():
    """
    Prompts the user for input and output filenames and calls the file processing function.
    Includes error handling for invalid filename input.
    """
    while True:
        input_filename = input("Enter the name of the input file: ")
        if not input_filename:
            print("Input filename cannot be empty.")
            continue  # Go back to the beginning of the loop

        output_filename = input("Enter the name of the output file: ")
        if not output_filename:
            print("Output filename cannot be empty.")
            continue
        break # Break out of the loop if both filenames are valid

    modify_and_write_file(input_filename, output_filename)


if __name__ == "__main__":
    main()