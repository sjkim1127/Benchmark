const std = @import("std");
fn fib(n: u64) u64 {
    if (n <= 1) return n;
    return fib(n - 1) + fib(n - 2);
}
pub fn main() !void {
    std.debug.print("Result: {d}\n", .{fib(40)});
}
