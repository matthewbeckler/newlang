fn sum_multiples_of_3_or_5(below: u32) -> u32 {
    let mut sum: u32 = 0;
//    for i in range(below):
//        if (i % 3 == 0) or (i % 5 == 0):
//            s += i
    for i in 0..below {
        if (i % 3 == 0) || (i % 5 == 0) {
            sum += i;
        }
    }
    sum
}

fn main() {
    let mut b: u32 = 10;
    println!("Sum below {} is {}", b, sum_multiples_of_3_or_5(b));
    b = 1000;
    println!("Sum below {} is {}", b, sum_multiples_of_3_or_5(b));
}
