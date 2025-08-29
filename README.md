**📂 File Read & Write Challenge & Error Handling Lab
📖 Overview**

This project demonstrates how to:

Read a file and write a modified version to a new file.

Handle errors when asking the user for a filename (e.g., file not found, no permission).

The program is written in Python and includes two main parts:

**File Read & Write Challenge 🖋️** – Reads a file, modifies the text (converts to uppercase), and writes it to a new file.

**Error Handling Lab 🧪** – Prompts the user for a filename and handles errors if the file doesn’t exist or can’t be read.

🚀 How to Run

Could you make sure you have Python 3 installed on your system?

Save the code in a file named file_challenge.py.

Create a sample input.txt file with some text in it.

Run the program in your terminal:

python file_challenge.py

**🖋️ File Read & Write Challenge**

The program reads text from input.txt.

It modifies the content (makes it uppercase).

It saves the modified version to output.txt.

**🧪 Error Handling Lab**

The program asks the user to enter a filename.

If the file exists, it displays the content.

If the file is missing or unreadable, an appropriate error message is displayed.

**✅ Example Output**

Case 1: File exists

Enter the filename you want to read: input.txt

📄 File content:
HELLO WORLD


**Case 2: File missing**

Enter the filename you want to read: missing.txt
❌ Error: The file 'missing.txt' does not exist.
