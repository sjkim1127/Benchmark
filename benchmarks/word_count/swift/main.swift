
import Foundation

let path = "../../data/input.txt"
if let content = try? String(contentsOfFile: path) {
    let words = content.components(separatedBy: .whitespacesAndNewlines)
    var counts = [String: Int]()
    for word in words {
        if !word.isEmpty {
            counts[word, default: 0] += 1
        }
    }
    print("Done")
} else {
    print("File error")
}
