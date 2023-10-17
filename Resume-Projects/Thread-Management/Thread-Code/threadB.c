#include <stdio.h>
#include <pthread.h>
#include <unistd.h>

#define TIMES 10 // The program will execute this many times

void *print_Letter_A(void *arg);
void *print_Letter_B(void *arg);

pthread_t threadA, threadB;
pthread_mutex_t mutex;

int main()
{
    pthread_mutex_init(&mutex, NULL);

    // Create threads
    pthread_create(&threadA, NULL, print_Letter_A, NULL);
    pthread_create(&threadB, NULL, print_Letter_B, NULL);

    // Wait for threads to finish
    pthread_join(threadA, NULL);
    pthread_join(threadB, NULL);

    pthread_mutex_destroy(&mutex);

    pthread_exit(0);
}

void *print_Letter_A(void *arg)
{
    int i;
    for (i = 0; i < TIMES; i++)
    {
        pthread_mutex_lock(&mutex);
        for (int j = 0; j < 5; j++)
            printf("%d: AAAAAAAAA\n", j + 1);
        pthread_mutex_unlock(&mutex);
        sleep(1);
    }
    return NULL;
}

void *print_Letter_B(void *arg)
{
    for (int i = 0; i < TIMES; i++)
    {
        pthread_mutex_lock(&mutex);
        for (int j = 0; j < 5; j++)
            printf("%d: BBBBBBBBB\n", j + 1);
        pthread_mutex_unlock(&mutex);
        sleep(1);
    }
    return NULL;
}

// (b) Write the program again considering the mutual exclusion. Run the 
// program several times to show that no five lines of A or B are interrupted.

// To make longer execution of threads, use some sleep(n) functions in 
// the program. Experiment with n to choose the best one to show the 
// results.


//                             1: AAAAAAAAA
//                             1: AAAAAAAAA
//                             1: AAAAAAAAA
//                             1: AAAAAAAAA
//                             1: AAAAAAAAA

//                             1: BBBBBBBBB
//                             1: BBBBBBBBB
//                             1: BBBBBBBBB
//                             1: BBBBBBBBB
//                             1: BBBBBBBBB

//                             2: AAAAAAAAA
//                             .....................
