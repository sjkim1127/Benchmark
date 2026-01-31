const WIDTH: usize = 2048;
const HEIGHT: usize = 2048;
const MAX_ITER: usize = 255;

fn main() {
    let mut buffer = vec![0u8; WIDTH * HEIGHT];

    let min_x = -2.0;
    let max_x = 0.47;
    let min_y = -1.12;
    let max_y = 1.12;

    let scalex = (max_x - min_x) / WIDTH as f64;
    let scaley = (max_y - min_y) / HEIGHT as f64;

    for y in 0..HEIGHT {
        let cy = min_y + y as f64 * scaley;
        for x in 0..WIDTH {
            let cx = min_x + x as f64 * scalex;

            let mut zx = 0.0;
            let mut zy = 0.0;
            let mut zx2 = 0.0;
            let mut zy2 = 0.0;
            let mut iter = 0;

            while iter < MAX_ITER && (zx2 + zy2) < 4.0 {
                zy = 2.0 * zx * zy + cy;
                zx = zx2 - zy2 + cx;
                zx2 = zx * zx;
                zy2 = zy * zy;
                iter += 1;
            }
            buffer[y * WIDTH + x] = iter as u8;
        }
    }

    let sum: usize = buffer.iter().map(|&x| x as usize).sum();
    println!("Done. Sum: {}", sum);
}
