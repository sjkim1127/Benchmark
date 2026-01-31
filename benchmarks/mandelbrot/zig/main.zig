const std = @import("std");
pub fn main() !void {
    const width = 2048;
    const height = 2048;
    const max_iter = 255;
    var y: usize = 0;
    while (y < height) : (y += 1) {
        const cy: f64 = -1.5 + @as(f64, @floatFromInt(y)) * 2.0 / @as(f64, @floatFromInt(height));
        var x: usize = 0;
        while (x < width) : (x += 1) {
            const cx: f64 = -2.0 + @as(f64, @floatFromInt(x)) * 2.5 / @as(f64, @floatFromInt(width));
            var zr: f64 = 0.0;
            var zi: f64 = 0.0;
            var iter: usize = 0;
            while (zr * zr + zi * zi <= 4.0 and iter < max_iter) : (iter += 1) {
                const tr = zr * zr - zi * zi + cx;
                zi = 2.0 * zr * zi + cy;
                zr = tr;
            }
        }
    }
    std.debug.print("Done\n", .{});
}
