#include <iostream>
#include <thread>
#include <vector>
#include <atomic>

const int N_THREADS = 1000;
std::atomic<int> counter(0);

void thread_func() {
    counter++;
}

int main() {
    std::vector<std::thread> threads;
    threads.reserve(N_THREADS);

    for (int i = 0; i < N_THREADS; ++i) {
        threads.emplace_back(thread_func);
    }

    for (auto& t : threads) {
        t.join();
    }

    std::cout << "Done. Counter: " << counter << std::endl;
    return 0;
}
