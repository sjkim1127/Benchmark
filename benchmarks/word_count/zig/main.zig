const std = @import("std");
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
    var it = std.mem.tokenizeAny(u8, content, " \n\r\t");
    while (it.next()) |word| {
        const result = try counts.getOrPut(word);
        if (result.found_existing) {
            result.value_ptr.* += 1;
        } else {
            result.value_ptr.* = 1;
        }
    }
    std.debug.print("Done\n", .{});
}
