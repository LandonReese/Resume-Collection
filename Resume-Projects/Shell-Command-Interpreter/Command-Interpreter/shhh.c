#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <fcntl.h>

#define MAX_ARGS 20

void delete_command(char *argv[], int index) {
    while (argv[index] != NULL && argv[index + 1] != NULL) {
        argv[index] = argv[index + 1];
        index++;
    }
    argv[index] = 0;
}

int main() {
    char *path, *argv[MAX_ARGS], buf[80], n, *p;
    int m, status, inword, continu;

    while (1) {
        inword = 0;
        p = buf;
        m = 0;
        continu = 0;

        printf("\nshhh> ");

        while ((n = getchar()) != '\n' || continu) {
            if (n == ' ') {
                if (inword) {
                    inword = 0;
                    *p++ = 0;
                }
            } else if (n == '\n') {
                continu = 0;
            } else if (n == '\\' && !inword) {
                continu = 1;
            } else {
                if (!inword) {
                    inword = 1;
                    argv[m++] = p;
                    *p++ = n;
                } else {
                    *p++ = n;
                }
            }
        }

        *p++ = 0;
        argv[m] = 0;

        // Check for built-in commands
        if (strcmp(argv[0], "exit") == 0) {
            printf("exiting...");
            exit(0);
        }

        // Remove any special characters
        // Check argv for pipes, input & output redirection
        int pipe_counter = 0;
        int command_counter = 0;
        int pipes[MAX_ARGS];
        int commands[MAX_ARGS];
        int output_file_location = -1;
        int input_file_location = -1;
        commands[command_counter++] = 0;

        // m is the total amount of args in argv[]
        for (int i = 1; i < m; ++i) {
            if (strcmp(argv[i], "|") == 0) {
                // Handle pipes '|'
                pipes[pipe_counter++] = i;
                argv[i] = 0;
                commands[command_counter++] = i + 1;
            } else if (strcmp(argv[i], ">") == 0) {
                if (i + 1 < m) {
                    // Handle output redirection '>'
                    output_file_location = i + 1;
                    argv[i] = 0;
                    // If there are additional arguments after ">", break the loop
                    break;
                } else {
                    // Handle error here, as ">" should be followed by the output file name
                    fprintf(stderr, "Error: Missing output file name after '>'\n");
                    exit(1);
                }
            } else if (strcmp(argv[i], "<") == 0) {
                // Handle input redirection '<'
                input_file_location = i + 1;
                argv[i] = 0;
            }
        }

        int left_pipe[2], right_pipe[2];
        for (int command = 0; command < command_counter; ++command) {
            if (command < pipe_counter) {
                // Create a pipe for each command
                pipe(right_pipe);
            }

            pid_t pid = fork();
            // Error handling
            if (pid < 0) {
                perror("Fork failed");
                exit(-1);
            }
            // Child Process
            else if (pid == 0) {
                if (command == 0 && input_file_location >= 0) {
                    // Redirect input if needed for the first command
                    int inputFile = open(argv[input_file_location], O_RDONLY);
                    if (inputFile < 0) {
                        perror("Failed to open input file");
                        exit(-1);
                    }
                    dup2(inputFile, 0);
                    close(inputFile);
                }

                if (command < pipe_counter) {
                    // Handle intermediate pipe commands
                    if (command == 0) {
                        // First Command (write only)
                        close(1);
                        dup2(right_pipe[1], 1);
                    } else {
                        // Middle pipe Command (read & write)
                        close(0);
                        dup2(left_pipe[0], 0);
                        close(left_pipe[0]);
                        close(left_pipe[1]);
                        close(1);
                        dup2(right_pipe[1], 1);
                    }
                    close(right_pipe[0]);
                    close(right_pipe[1]);
                } else {
                    // Last Command (read only)
                    if (pipe_counter > 0) {
                        close(0);
                        dup2(left_pipe[0], 0);
                        close(left_pipe[0]);
                        close(left_pipe[1]);
                    }
                }

                // Handle Output Redirection
                if (command == command_counter - 1 && output_file_location >= 0) {
                    int outputFile = open(argv[output_file_location], O_CREAT | O_WRONLY | O_TRUNC, 0644);
                    if (outputFile < 0) {
                        perror("Failed to open output file");
                        exit(-1);
                    }
                    dup2(outputFile, 1);
                    close(outputFile);
                }

                // Execute the command
                execvp(argv[commands[command]], &argv[commands[command]]);
                perror("Execution failed");
                exit(-1);
            }
            // Parent Process
            else {
                // Close left pipe if not the last command
                if (command > 0) {
                    close(left_pipe[0]);
                    close(left_pipe[1]);
                }
                left_pipe[0] = right_pipe[0];
                left_pipe[1] = right_pipe[1];
                wait(&status);
            }
        }
    }

    return 0;
}


/*****Notes*****
      * path: This variable is not used in the provided code snippet. 
      *         It is declared but not assigned or referenced anywhere in the code.
      * argv[20]: This is an array of character pointers (char*) with a size of 20. 
      *         It is used to store the arguments of a command that will be executed.
      * buf[80]: This is an array of characters with a size of 80. 
      *         It is used as a buffer to store the input command entered by the user.
      * n: This variable of type char is used to temporarily store each character read 
      *         from the input command.
      * p: This variable is a pointer to a character (char*). It is used as a pointer 
      *         to navigate through the buf array while parsing the input command.
      * m: This variable of type int is used to keep track of the number of 
      *         arguments in the argv array.
      * status: This variable of type int is used to store the exit status of a 
      *         child process when it is waited upon using the wait() function.
      * inword: This variable of type int is used as a flag to indicate whether the 
      *         parsing is currently inside a word (argument) or not. It is set to 1 
      *         when a word is being parsed and set to 0 when a word is complete.
      * continu: This variable of type int is used as a flag to indicate whether the 
      *         parsing of the current command continues onto the next line (in case of a 
      *         backslash continuation character \) or not. It is set to 1 when the command 
      *         continues and set to 0 when the command is complete.
    */