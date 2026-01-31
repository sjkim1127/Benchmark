
let n = 512
var a = [Double](repeating: 1.0, count: n * n)
var b = [Double](repeating: 1.0, count: n * n)
var c = [Double](repeating: 0.0, count: n * n)

for i in 0..<n {
    for k in 0..<n {
        let r = a[i * n + k]
        for j in 0..<n {
            c[i * n + j] += r * b[k * n + j]
        }
    }
}

if c[0] == Double(n) {
    print("Done")
} else {
    print("Fail")
}
