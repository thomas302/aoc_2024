use std::collections::HashMap;
use std::env;
use std::fs;


fn main() {
    let args: Vec<String> = env::args().collect();

    let f_name = args[1].clone();
    let input = get_input(f_name);
    
    let positions = get_antenna_positions(input.clone());
    let bounds = get_bounds(input.clone());

    println!("{:?}", bounds);

    let an = get_antinode_positions(positions, bounds);

    let cnt = an.iter().count();

    println!("Count is {}!", cnt);
}


fn get_input(f_name:String) -> String{
    let input = fs::read_to_string(f_name).expect("Failed to red file");
    return input
}

fn get_antinode_positions(antenas:Vec<Position>, bounds:(i32,i32)) -> Vec<Position>{
    let mut antinodes:Vec<Position> = Vec::new();
    for p1 in &antenas{
        for p2 in &antenas{
            if p2.value != p1.value {continue}
            if p2.pos == p1.pos{ continue;}

            let dist = p1.get_dist(p2);
            
            let res1 = Position{
                value:String::from("#"),
                pos:p1.sub(&dist)
            };

            let res2 = Position{
                value:String::from("#"),
                pos:p2.add(&dist)
            };

            if (res1.is_in_bounds(bounds)) {
                if antinodes.iter().filter(|x| x.pos == res1.pos).count() < 1{
                    antinodes.push(res1);
                }
            }
            if (res2.is_in_bounds(bounds)) {
                if antinodes.iter().filter(|x| x.pos == res2.pos).count() < 1{
                    antinodes.push(res2);
                }
            }
        }
    }
    return antinodes
}

fn get_bounds(input:String)->(i32,i32){
    let lines = input.split("\n");
    let rows: i32 = lines.clone().count().try_into().unwrap();

    // Handle the first line more safely
    let first_line = lines.clone().next().unwrap(); // Or provide a default empty string
    let cols: i32 = first_line.trim().len().try_into().unwrap();
    return (rows, cols);
}

fn get_antenna_positions(input:String) ->Vec<Position>{
    let lines = input.split("\n");

    //let mut map:HashMap<String, Vec<Position>> = HashMap::new();
    let mut positions:Vec<Position> = Vec::new();

    let mut row:i32 = 0;
    let mut col:i32 = 0;
    for l in lines{
        col = 0;
        let s = String::from(l);
        for c in s.trim().chars(){
            if c != '.'{
                let p = Position{
                    value: c.to_string(), 
                    pos: (row,col)
                };

                positions.push(p);
            }
            col+=1
        }
        row += 1;
    }
    return positions;
}


struct Position{
    value: String,
    pos: (i32, i32)
}


impl Position{
    fn get_dist(&self, other:&Position)->Position{
        let p = other.sub(self);
        return Position{
            value:String::from("Dist"),
            pos: (p.0, p.1)
        };

    }

    fn add(&self, other:&Position)->(i32, i32) {
        return (self.pos.0 + other.pos.0, self.pos.1 + other.pos.1)
    }

    fn sub(&self, other:&Position)->(i32, i32) {
        return (self.pos.0 - other.pos.0, self.pos.1 - other.pos.1)
    }

    fn is_in_bounds(&self, bounds:(i32,i32)) -> bool{
        let cond = self.pos.0 >=0 && self.pos.0 < bounds.0 && self.pos.1 >= 0 && self.pos.1 < bounds.1;
        //if !cond{println!("Failed")}
        return cond;
    }
}