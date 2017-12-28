/*
 * Project Euler 003
 * Largest prime factor
 *
 * The prime factors of 13195 are 5, 7, 13 and 29.
 *
 * What is the largest prime factor of the number 600851475143 ?
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

fn main() {
    let pfs = prime_factors(600851475143);
    for pf in &pfs {
        println!("{}", pf);
    }
}
