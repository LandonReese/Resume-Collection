// b). The second program "sort.c" reads in a list of student names from the keyboard and displays them in 
// alphabetical order on the screen. Assume the sequence is read until an EOF is encountered. 

// If the inputs are:

// Susan
// David
// Jessica
// Ctrl-D (press the keys to terminate the inputs.)

// The outputs should be:

// David
// Jessica
// Susan

#include <stdio.h>
#include <string.h>



// Data types
struct Student
{
    char name[50];
    double gpa;
};

struct Student students[50]; //Can store up to 50 students
int AmountOfStudents = 0; //Starts at 0, increments each time a student is added
// Protos
void bubbleSort(struct Student array[], int size);

int main() {
    
    
    while (scanf("%s %lf", students[AmountOfStudents].name, &students[AmountOfStudents].gpa) != EOF) {
        AmountOfStudents++;
    }
    
    // Sort
    bubbleSort(students, AmountOfStudents);

    // Print
    for(int i = 0; i < AmountOfStudents; i++){
        printf("%s\n", students[i].name);
    }
    
    
    
    return 0;
}

void bubbleSort(struct Student array[], int size){
    // i "steps" through the array, j handles letter comparison
    for(int i = 0; i < size - 1; i++){
        for(int j = 0; j < (size - i) - 1; j++){
            // need to use string compare instead of array[j].name > array[j + 1].name
            if (strcmp(array[j].name, array[j + 1].name) > 0) { 
                struct Student temp = array[j];
                array[j] = array[j + 1];
                array[j + 1] = temp;
            }
        }
    }
}

