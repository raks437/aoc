use std::fs;

fn main(){
  let mut p1 = 0;
  let mut p2 = 0;
  let file = fs::read_to_string("input.txt").expect("Error:: File read error!!");

  for (i, c) in file.chars().enumerate() {
    if c == '(' {
      p1 += 1;
    }
    else if c == ')' {
      p1 -= 1;
    }
    if p2 == 0 && p1 == -1 {
      p2 = i+1;
    }
  }
  
  println!("P1::{}", p1);
  println!("P2::{}", p2);
}