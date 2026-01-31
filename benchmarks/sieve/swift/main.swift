
let limit = 10_000_000
var isPrime = [Bool](repeating: true, count: limit + 1)
isPrime[0] = false
isPrime[1] = false

var count = 0
for p in 2...limit {
    if isPrime[p] {
        count += 1
        var i = p * p
        while i <= limit {
            isPrime[i] = false
            i += p
        }
    }
}
print("Count: \(count)")
