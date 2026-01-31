const std = @import("std");
pub fn main() !void {
    const limit = 10_000_000;
    const allocator = std.heap.page_allocator;
    const is_prime = try allocator.alloc(bool, limit + 1);
    defer allocator.free(is_prime);
    @memset(is_prime, true);
    is_prime[0] = false;
    is_prime[1] = false;
    var count: usize = 0;
    var p: usize = 2;
    while (p <= limit) : (p += 1) {
        if (is_prime[p]) {
            count += 1;
            if (p <= 3162) {
                var i = p * p;
                while (i <= limit) : (i += p) {
                    is_prime[i] = false;
                }
            }
        }
    }
    std.debug.print("Count: {d}\n", .{count});
}
