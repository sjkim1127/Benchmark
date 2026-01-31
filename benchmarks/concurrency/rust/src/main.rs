use std::sync::atomic::{AtomicUsize, Ordering};
use std::sync::Arc;

const N_TASKS: usize = 100_000;

#[tokio::main]
async fn main() {
    let counter = Arc::new(AtomicUsize::new(0));
    let mut handles = Vec::with_capacity(N_TASKS);

    for _ in 0..N_TASKS {
        let c = counter.clone();
        handles.push(tokio::spawn(async move {
            c.fetch_add(1, Ordering::Relaxed);
        }));
    }

    for h in handles {
        let _ = h.await;
    }

    println!("Done. Counter: {}", counter.load(Ordering::SeqCst));
}
