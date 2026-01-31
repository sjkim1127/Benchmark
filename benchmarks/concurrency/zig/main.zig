const std = @import("std");

const Context = struct {
    c: *u32,
    l: *std.Thread.Mutex,
};

fn run(ctx: Context) void {
    ctx.l.lock();
    ctx.c.* += 1;
    ctx.l.unlock();
}

pub fn main() !void {
    const total = 1000;
    var count: u32 = 0;
    var mutex = std.Thread.Mutex{};
    
    const context = Context{ .c = &count, .l = &mutex };

    var threads: [total]std.Thread = undefined;
    for (&threads) |*t| {
        t.* = try std.Thread.spawn(.{}, run, .{context});
    }

    for (threads) |t| {
        t.join();
    }

    std.debug.print("Counter: {d}\nDone\n", .{count});
}
