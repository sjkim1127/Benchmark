use std::collections::HashMap;
use std::fs::File;
use std::io::{self, Read};

fn main() -> io::Result<()> {
    // Read entire file to string is usually fastest for moderate sizes
    let mut file = File::open("../../data/input.txt")?;
    let mut contents = String::new();
    file.read_to_string(&mut contents)?;

    let mut counts = HashMap::new();
    for word in contents.split_whitespace() {
        *counts.entry(word).or_insert(0) += 1;
    }

    println!("Unique words: {}", counts.len());
    Ok(())
}
