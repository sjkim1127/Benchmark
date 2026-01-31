const N: usize = 512;

fn mat_mul(a: &[f64], b: &[f64], c: &mut [f64]) {
    for i in 0..N {
        for j in 0..N {
            let mut sum = 0.0;
            for k in 0..N {
                sum += a[i * N + k] * b[k * N + j];
            }
            c[i * N + j] = sum;
        }
    }
}

fn main() {
    let a = vec![1.0; N * N];
    let b = vec![1.0; N * N];
    let mut c = vec![0.0; N * N];

    mat_mul(&a, &b, &mut c);
    println!("Done. C[0][0] = {}", c[0]);
}
