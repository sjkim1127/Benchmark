const fs = require('fs');

try {
    const data = fs.readFileSync('../../data/input.txt', 'utf8');
    // Regex split might be slower, simple split by space?
    // The generator uses " ", so split(' ') is fine.
    // However, split(/\s+/) is safer for general whitespace.
    // For benchmark fairness, let's use a split that mirrors others.
    const words = data.trim().split(/\s+/);

    const counts = new Map();
    for (const word of words) {
        if (!word) continue;
        counts.set(word, (counts.get(word) || 0) + 1);
    }

    console.log(`Unique words: ${counts.size}`);
} catch (err) {
    console.error(err);
}
