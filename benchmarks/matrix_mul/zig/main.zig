const std = @import("std");
pub fn main() !void {
    const n = 512;
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    const allocator = gpa.allocator();
    defer _ = gpa.deinit();
    const a = try allocator.alloc(f64, n * n);
    const b = try allocator.alloc(f64, n * n);
    const c = try allocator.alloc(f64, n * n);
    defer allocator.free(a);
    defer allocator.free(b);
    defer allocator.free(c);
    @memset(a, 1.0);
    @memset(b, 1.0);
    @memset(c, 0.0);
    var i: usize = 0;
    while (i < n) : (i += 1) {
        var k: usize = 0;
        while (k < n) : (k += 1) {
            const r = a[i * n + k];
            var j: usize = 0;
            while (j < n) : (j += 1) {
                c[i * n + j] += r * b[k * n + j];
            }
        }
    }
    if (c[0] == @as(f64, @floatFromInt(n))) {
        std.debug.print("Done\n", .{});
    } else {
        std.debug.print("Fail\n", .{});
    }
}
