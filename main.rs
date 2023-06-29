use std::io;

fn main () {
    println!("Who is there?");
    println!("Typ in your Name ...");
    let mut name = String::new();
    io::stdin()
        .read_line(&mut name)
        .expect("Failed to read line");

    println!("Hello, {} !", name);
}