/**
The main steps for checking if a string is a palindrome are:

1. Convert the string to lowercase.
2. Remove all non-alphanumeric characters.
3. Check if the cleaned-up string reads the same forwards as backwards.
*/

fn is_palindrome(s: &str) -> bool {
    let s = s.to_ascii_lowercase(); // Step 1 complete

    let cleaned: String = s.chars().filter(|c| c.is_alphanumeric()).collect(); // Step 2 complete

    cleaned == cleaned.chars().rev().collect::<String>()

}

fn main() {
    println!("{}", is_palindrome("radar")); // true
    println!("{}", is_palindrome("Level")); // true
    println!("{}", is_palindrome("A man, a plan, a canal, Panama!")); // true
    println!("{}", is_palindrome("hello")); // false
}

