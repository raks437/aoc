use std::io::BufReader;
use std::io::BufRead;
use std::fs::File;

struct Rectangle {
  w: i32,
  h: i32,
  l: i32,
}

impl Rectangle {
  fn diameter(&self) -> i32 {
    self.l * self.w * self.h
  }

  fn surface_area(&self) -> i32 {
    2 * (self.l * self.w + self.w * self.h + self.h * self.l)
  }

  fn smallest_side_diameter(&self) -> i32 {
    if self.l >= self.h && self.l >= self.w {
      self.h + self.h + self.w + self.w
    }
    else if self.h >= self.l && self.h >= self.w {
      self.l + self.l + self.w + self.w
    }
    else {
      self.l + self.l + self.h + self.h
    }
  }

  fn smallest_side_area(&self) -> i32 {
    if self.l >= self.h && self.l >= self.w {
      self.h * self.w
    }
    else if self.h >= self.l && self.h >= self.w {
      self.l * self.w
    }
    else {
      self.l * self.h
    }
  }
}

fn main(){
  let mut p1 = 0;
  let mut p2 = 0;
  
  let file = File::open("input.txt").unwrap();
  let reader = BufReader::new(&file);
  for (_num, line) in reader.lines().enumerate() {
    let l = line.unwrap();
    let r: Vec<i32> = l.split('x').map(|s| s.parse().unwrap()).collect();
    let rect = Rectangle {w: r[0], h: r[1], l: r[2]};
    p1 += rect.surface_area() + rect.smallest_side_area();
    p2 += rect.diameter() + rect.smallest_side_diameter();
  }

  println!("P1::{}", p1);
  println!("P2::{}", p2);
}