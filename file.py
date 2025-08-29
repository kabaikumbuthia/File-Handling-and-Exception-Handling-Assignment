# File Read & Write Challenge 

def modify_file(input_file, output_file):
    try:
        # Open the input file for reading
        with open(input_file, 'r') as f_in:
            content = f_in.read()

        # Modify the content (example: make everything uppercase)
        modified_content = content.upper()

        # Write the modified content to the output file
        with open(output_file, 'w') as f_out:
            f_out.write(modified_content)

        print(f" File '{input_file}' has been read and written to '{output_file}' successfully.")

    except FileNotFoundError:
        print(f" Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f" An error occurred: {e}")


# Example usage
modify_file("input.txt", "output.txt")


# Error Handling Lab 🧪

filename = input("Enter the filename you want to read: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
        print("\n📄 File content:\n")
        print(content)

except FileNotFoundError:
    print(f"❌ Error: The file '{filename}' does not exist.")
except PermissionError:
    print(f"🚫 Error: You don’t have permission to read '{filename}'.")
except Exception as e:
    print(f"⚠️ An unexpected error occurred: {e}")

