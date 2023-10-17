# Thread Synchronization with Mutual Exclusion

This project explores the concept of thread synchronization with and without mutual exclusion mechanisms in a multi-threaded environment. In this project, we have two parts:

## Part (a) - Without Mutual Exclusion

In this part, two threads, named threadA and threadB, run concurrently without any mutual exclusion mechanism. This results in interleaved output, where lines of "AAAAAAAAA" and "BBBBBBBBB" can be interrupted, as shown in the provided example. This part demonstrates the lack of synchronization between the threads.

## Part (b) - With Mutual Exclusion

In this part, mutual exclusion is introduced using a mutex (pthread_mutex_t) to ensure that only one thread can access the shared resource (printing to the console) at a time. With mutual exclusion, you should not see lines of "AAAAAAAAA" and "BBBBBBBBB" being interrupted, as the mutex ensures that one thread completes its printing before the other can access the shared resource. The sleep(1) function is used to extend the execution time of threads, helping to clearly demonstrate the synchronized behavior.

This project provides a practical demonstration of the importance of mutual exclusion in multi-threaded programming and how it ensures thread synchronization.

## How to Use

1. Compile and run the provided code for both Part (a) and Part (b).
2. Observe the output to compare the behavior of threads in each part.

## Key Takeaways

- Part (a) showcases the challenges of managing multiple threads without proper synchronization, leading to interleaved execution.

- Part (b) demonstrates the effectiveness of mutual exclusion in preventing thread interference and ensuring synchronized execution.

This project offers insights into the principles of thread synchronization and the role of mutual exclusion in multi-threaded applications.
