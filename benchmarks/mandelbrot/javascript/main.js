const WIDTH = 2048;
const HEIGHT = 2048;
const MAX_ITER = 255;

function main() {
    const buffer = new Uint8Array(WIDTH * HEIGHT);

    const min_x = -2.0;
    const max_x = 0.47;
    const min_y = -1.12;
    const max_y = 1.12;

    const scalex = (max_x - min_x) / WIDTH;
    const scaley = (max_y - min_y) / HEIGHT;

    for (let y = 0; y < HEIGHT; y++) {
        const cy = min_y + y * scaley;
        for (let x = 0; x < WIDTH; x++) {
            const cx = min_x + x * scalex;

            let zx = 0.0;
            let zy = 0.0;
            let zx2 = 0.0;
            let zy2 = 0.0;

            let iter = 0;
            while (iter < MAX_ITER && (zx2 + zy2) < 4.0) {
                zy = 2.0 * zx * zy + cy;
                zx = zx2 - zy2 + cx;
                zx2 = zx * zx;
                zy2 = zy * zy;
                iter++;
            }
            buffer[y * WIDTH + x] = iter;
        }
    }

    let sum = 0;
    for (let i = 0; i < buffer.length; i++) {
        sum += buffer[i];
    }
    console.log(`Done. Sum: ${sum}`);
}

main();
