# Shell Command Interpreter
This project provides a Shell Command Interpreter along with additional programs for processing and sorting student data. Here's how to use the components of this project:

## Shell Command Interpreter (shhh.c)

### How to Run
Open the project directory.
Compile the shhh.c program using a C compiler (e.g., GCC) with the command:
'gcc shhh.c -o shhh'

1. Run the compiled shell interpreter with:

./shhh

You can now enter and execute various commands within the provided shell script.
Basic Usage
The shell interpreter allows you to execute commands, both system commands and built-in commands.
A built-in command included in the shell is "exit," which allows you to exit the shell.
You can pipe commands using the "|" symbol, redirect input from a file using "<," and redirect output to a file using ">".
Example
Running a command like ./pre < input.txt | ./sort > output.txt with the provided input text:

Kyle 3.5
Jeremy 2.1
Applesauce 4.0
Cat 0.0
Jerome 4.9

Will produce the following output in output.txt (students alphabetized with a GPA of 3.0 or greater):

Applesauce
Jerome
Kyle

Shell Programming (shhh.c)
This section summarizes the key features and accomplishments related to the development of the Shell Command Interpreter:

* Developed a shell program capable of accepting and executing user commands.
* Implemented functionalities for parsing and tokenizing user input.
* Supported built-in commands, including the "exit" command for exiting the shell.
* Enabled command execution and management using fork() and wait().
* Implemented handling of pipes, input redirection ("<"), and output redirection (">").
* Included robust error handling for file operations and child process creation.
* Gained experience in process management, input/output redirection, and command execution.