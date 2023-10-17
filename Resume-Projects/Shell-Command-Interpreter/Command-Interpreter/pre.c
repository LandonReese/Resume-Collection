#include <stdio.h>
#include <string.h>

struct Student
{
    char name[50];
    double gpa;
};

struct Student students[50]; //Can store up to 50 students
int AmountOfStudents = 0; //Starts at 0, increments each time a student is added

int main() {
    while (scanf("%s %lf", students[AmountOfStudents].name, &students[AmountOfStudents].gpa) != EOF) {
        AmountOfStudents++;
    }
    
    for(int i = 0; i < AmountOfStudents; i++){
        if(students[i].gpa >= 3.0){
            printf("%s\n", students[i].name); //print each student name, then new line
        }
    }
    
    
    
    return 0;
}

