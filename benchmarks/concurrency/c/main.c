#include <stdio.h>
#include <pthread.h>
#include <stdatomic.h>

#define N_THREADS 1000

atomic_int counter = 0;

void* thread_func(void* arg) {
    atomic_fetch_add(&counter, 1);
    return NULL;
}

int main() {
    pthread_t threads[N_THREADS];

    for (int i = 0; i < N_THREADS; i++) {
        if (pthread_create(&threads[i], NULL, thread_func, NULL) != 0) {
            perror("pthread_create");
            return 1;
        }
    }

    for (int i = 0; i < N_THREADS; i++) {
        pthread_join(threads[i], NULL);
    }

    printf("Done. Counter: %d\n", counter);
    return 0;
}
