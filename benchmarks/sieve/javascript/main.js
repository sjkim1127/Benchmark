const LIMIT = 10000000;

function runSieve() {
    // Uint8Array is typed and efficient
    const isPrime = new Uint8Array(LIMIT + 1);
    
    // Initialize to 1 (true)
    isPrime.fill(1);
    
    isPrime[0] = 0;
    isPrime[1] = 0;

    const sqrtLimit = Math.floor(Math.sqrt(LIMIT));
    for (let p = 2; p <= sqrtLimit; p++) {
        if (isPrime[p] === 1) {
            for (let i = p * p; i <= LIMIT; i += p) {
                isPrime[i] = 0;
            }
        }
    }

    let count = 0;
    for (let p = 2; p <= LIMIT; p++) {
        if (isPrime[p] === 1) {
            count++;
        }
    }

    return count;
}

const count = runSieve();
console.log(`Count: ${count}`);
