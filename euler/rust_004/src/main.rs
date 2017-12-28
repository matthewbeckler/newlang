/*
 * Project Euler 004
 * Largest palindrome product
 *
 * A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
 *
 * Find the largest palindrome made from the product of two 3-digit numbers.
 */

fn prime_factors(x: u64) -> Vec<u64> {
    let mut pfs: Vec<u64> = vec![];
    let mut number = x;
    let mut candidate = 2;

    while number > 1 {
        while number % candidate == 0 {
            pfs.push(candidate);
            number /= candidate;
        }
        candidate += 1
    }

    return pfs;
}

fn is_palindrome(x: u64) -> bool {

}

fn main() {
    let mut best = 0;

    println!("best is {}", best);
}
