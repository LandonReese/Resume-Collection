#include <stdio.h>
#include <pthread.h>

#define TIMES 10 // The program will execute this many times

void* print_Letter_A(void* arg) {
    for (int i = 1; i <= TIMES; i++) {
        for (int j = 0; j < 5; j++) {
            printf("%d: AAAAAAAAA\n", i);
        }
    }
    pthread_exit(NULL);
}

void* print_Letter_B(void* arg) {
    for (int i = 1; i <= TIMES; i++) {
        for (int j = 0; j < 5; j++) {
            printf("%d: BBBBBBBBB\n", i);
        }
    }
    pthread_exit(NULL);
}

int main() {
    pthread_t threadA, threadB;

    // Create threads
    pthread_create(&threadA, NULL, print_Letter_A, NULL);
    pthread_create(&threadB, NULL, print_Letter_B, NULL);

    // Wait for threads to finish
    pthread_join(threadA, NULL);
    pthread_join(threadB, NULL);

    return 0;
}

// (a) Do not use any algorithm for mutual exclusion and show the printout, 
// which should be similar to this:

//                              1: AAAAAAAAA
//                              1: AAAAAAAAA
                            
//                              1: BBBBBBBBB
//                              1: BBBBBBBBB
//                              1: BBBBBBBBB

//                              1: AAAAAAAAA
//                              1: AAAAAAAAA
//                              1: AAAAAAAAA

//                              1: BBBBBBBBB
//                              1: BBBBBBBBB

//                              2: AAAAAAAAA
//                              2: AAAAAAAAA

//                              .....................

// In this printout, five lines of A or B have been interrupted. That means
// mutual exclusion is not considered. Your output will be different from this 
// one. But as long as you see one interruption of five lines of A or B, your 
// output is correct. 