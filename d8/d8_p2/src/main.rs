use std::env;
use std::fs;
use std::collections::HashSet;
use std::collections::HashMap;

fn main() {
    let args: Vec<String> = env::args().collect();
    let input = get_input(&args[1]);

    let bounds = get_bounds(&input);
    let antennas = get_antenna_positions(&input);
    
    let an = get_antinodes(antennas, bounds);

    println!("Antinodes No. {}", an.iter().count());
}

fn get_antinodes(antennas:HashMap<char, HashSet<(i32, i32)>>, bounds:(i32,i32)) -> HashSet<(i32, i32)>{
    let mut out: HashSet<(i32, i32)> = HashSet::new();
    for (_c, set) in antennas{
        let v:Vec<(i32, i32)> = set.iter().cloned().collect();
        for i in 0 .. v.len(){
            for j in (i+1)..v.len(){
                let p1 = v[i];
                let p2= v[j];
                let gcd_dist = get_gcd_dist(&p1, &p2);
                out.insert(p1);
                let mut p = p1;
                loop {
                    let test_p = add(&p, &gcd_dist);
                    if check_bounds(&test_p, &bounds){
                        out.insert(test_p);
                    }
                    else {
                        break;
                    }
                    p = test_p
                }

                let mut p = p1;
                loop {
                    let test_p = sub(&p, &gcd_dist);
                    if check_bounds(&test_p, &bounds){
                        out.insert(test_p);
                    }
                    else {
                        break;
                    }
                    p = test_p
                }
            }
        }
    }
    return out;
}

fn check_bounds(p:&(i32,i32), bounds:&(i32,i32))->bool{
    let (x, y) = *p;
    let (x_max, y_max) = *bounds;
    return x >= 0 && x < x_max && y >= 0 && y < y_max;
}

fn sub(p1:&(i32,i32), p2:&(i32,i32)) -> (i32,i32){
    return(p1.0 - p2.0, p1.1-p2.1);
}

fn add(p1:&(i32,i32), p2:&(i32,i32)) -> (i32,i32){
    return(p1.0 + p2.0, p1.1+p2.1);
}

fn get_gcd_dist(p1:&(i32,i32), p2:&(i32,i32)) -> (i32,i32){
    let dist = getDist(&p1, &p2);
    let gcd = get_gcd(dist.0, dist.1);
    return (dist.0/gcd, dist.1/gcd);
}

fn get_gcd(a:i32, b:i32)->i32{
    if(a == 0){
        return b;
    }
    return get_gcd(b%a, a);
}

fn getDist(p1:&(i32,i32), p2:&(i32,i32))->(i32,i32){
    return (p2.0 - p1.0, p2.1-p1.1);
}


fn get_input(f_name:&String) -> String{
    let input = fs::read_to_string(f_name).expect("Failed to red file");
    return input
}

fn get_bounds(input:&String)->(i32,i32){
    let lines = input.split("\n");
    let rows: i32 = lines.clone().count().try_into().unwrap();

    // Handle the first line more safely
    let first_line = lines.clone().next().unwrap(); // Or provide a default empty string
    let cols: i32 = first_line.trim().len().try_into().unwrap();
    return (rows, cols);
}


fn get_antenna_positions(input:&String) ->HashMap<char, HashSet<(i32, i32)>>{
    let lines = input.split("\n");

    let mut positions:HashMap<char, HashSet<(i32, i32)>> = HashMap::new();

    let mut row:i32 = 0;
    let mut col:i32 = 0;
    for l in lines{
        col = 0;
        let s = String::from(l);
        for c in s.trim().chars(){
            if c != '.'{
                positions.
                    entry(c).
                    or_insert_with(HashSet::new).
                    insert((row, col));
            }
            col+=1
        }
        row += 1;
    }
    return positions;
}