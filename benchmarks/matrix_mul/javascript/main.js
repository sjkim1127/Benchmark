const N = 512;

function matMul(a, b, c) {
    for (let i = 0; i < N; i++) {
        for (let j = 0; j < N; j++) {
            let sum = 0.0;
            for (let k = 0; k < N; k++) {
                sum += a[i * N + k] * b[k * N + j];
            }
            c[i * N + j] = sum;
        }
    }
}

const a = new Float64Array(N * N).fill(1.0);
const b = new Float64Array(N * N).fill(1.0);
const c = new Float64Array(N * N);

matMul(a, b, c);

console.log(`Done. C[0][0] = ${c[0]}`);
