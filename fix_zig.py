
import os

categories = ["sieve", "fibonacci", "binary_tree", "word_count", "matrix_mul", "concurrency", "mandelbrot"]

zig_templates = {
    "sieve": """const std = @import("std");
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
    std.debug.print("Count: {d}\\n", .{count});
}
""",
    "fibonacci": """const std = @import("std");
fn fib(n: u64) u64 {
    if (n <= 1) return n;
    return fib(n - 1) + fib(n - 2);
}
pub fn main() !void {
    std.debug.print("Result: {d}\\n", .{fib(40)});
}
""",
    "binary_tree": """const std = @import("std");
const Node = struct {
    left: ?*Node,
    right: ?*Node,
    fn create(allocator: std.mem.Allocator, depth: i32) !*Node {
        const node = try allocator.create(Node);
        if (depth > 0) {
            node.left = try Node.create(allocator, depth - 1);
            node.right = try Node.create(allocator, depth - 1);
        } else {
            node.left = null;
            node.right = null;
        }
        return node;
    }
    fn destroy(self: *Node, allocator: std.mem.Allocator) void {
        if (self.left) |l| l.destroy(allocator);
        if (self.right) |r| r.destroy(allocator);
        allocator.destroy(self);
    }
};
pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    const allocator = gpa.allocator();
    defer _ = gpa.deinit();
    const root = try Node.create(allocator, 20);
    root.destroy(allocator);
    std.debug.print("Done\\n", .{});
}
""",
    "word_count": """const std = @import("std");
pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    const allocator = gpa.allocator();
    defer _ = gpa.deinit();
    const file = try std.fs.cwd().openFile("../../data/input.txt", .{});
    defer file.close();
    const content = try file.readToEndAlloc(allocator, 100 * 1024 * 1024);
    defer allocator.free(content);
    var counts = std.StringHashMap(u32).init(allocator);
    defer counts.deinit();
    var it = std.mem.tokenizeAny(u8, content, " \\n\\r\\t");
    while (it.next()) |word| {
        const result = try counts.getOrPut(word);
        if (result.found_existing) {
            result.value_ptr.* += 1;
        } else {
            result.value_ptr.* = 1;
        }
    }
    std.debug.print("Done\\n", .{});
}
""",
    "matrix_mul": """const std = @import("std");
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
        std.debug.print("Done\\n", .{});
    } else {
        std.debug.print("Fail\\n", .{});
    }
}
""",
    "concurrency": """const std = @import("std");
pub fn main() !void {
    const total = 1000;
    var count: u32 = 0;
    var mutex = std.Thread.Mutex{};
    const context = struct {
        c: *u32,
        l: *std.Thread.Mutex,
        fn run(ctx: @This()) void {
            ctx.l.lock();
            ctx.c.* += 1;
            ctx.l.unlock();
        }
    }{ .c = &count, .l = &mutex };
    var threads: [total]std.Thread = undefined;
    for (&threads) |*t| {
        t.* = try std.Thread.spawn(.{}, context.run, .{context});
    }
    for (threads) |t| {
        t.join();
    }
    std.debug.print("Counter: {d}\\nDone\\n", .{count});
}
""",
    "mandelbrot": """const std = @import("std");
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
    std.debug.print("Done\\n", .{});
}
"""
}

for cat in categories:
    path = os.path.join("benchmarks", cat, "zig", "main.zig")
    with open(path, "w") as f:
        f.write(zig_templates[cat])
    print(f"Fixed {path}")
