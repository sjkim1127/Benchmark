
let width = 2048
let height = 2048
let maxIter = 255

var count = 0
for y in 0..<height {
    let cy = -1.5 + Float64(y) * 2.0 / Float64(height)
    for x in 0..<width {
        let cx = -2.0 + Float64(x) * 2.5 / Float64(width)
        var zr = 0.0
        var zi = 0.0
        var iter = 0
        while zr * zr + zi * zi <= 4.0 && iter < maxIter {
            let tr = zr * zr - zi * zi + cx
            zi = 2.0 * zr * zi + cy
            zr = tr
            iter += 1
        }
        if iter == maxIter {
            count += 1
        }
    }
}
print("Done")
