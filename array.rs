// https://www.codewars.com/kata/523f5d21c841566fde000009/train/rust




fn array_diff<T: PartialEq>(a: Vec<T>, b: Vec<T>) -> Vec<T> {
    let mut result = Vec::new();
    for x in a {
        if !b.contains(&x) {
            result.push(x);
        }
    }
    result
}
  
fn main() {
    let a = vec![1, 2, 2, 2, 3];
    let b = vec![2];
    let diff = array_diff(a, b);
    println!("{:?}", diff); // prints "[1, 3]"
}
