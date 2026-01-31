
import Foundation

var count = 0
let lock = NSLock()
let total = 100_000
let group = DispatchGroup()

for _ in 0..<total {
    group.enter()
    DispatchQueue.global().async {
        lock.lock()
        count += 1
        lock.unlock()
        group.leave()
    }
}

group.wait()
print("Counter: \(count)")
print("Done")
