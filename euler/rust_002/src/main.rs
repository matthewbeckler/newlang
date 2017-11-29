fn main() {
    let mut sum: u32 = 0;
    let mut im1: u32 = 1;
    let mut im2: u32 = 0;

    loop {
        let temp: u32 = im1 + im2;
        println!("term is {}", temp);

        if temp > 4000000 {
            println!("exceeds four million, we are done");
            break;
        }

        im2 = im1;
        im1 = temp;

        
        if temp % 2 == 0 {
            sum += temp;
        }
    }

    println!("Sum is {}", sum);
}
