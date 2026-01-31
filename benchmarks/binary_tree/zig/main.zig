const std = @import("std");
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
    std.debug.print("Done\n", .{});
}
