use sqlite::num_chocolate; // Replace `rust_avg` with your actual crate name
use std::fs::OpenOptions;
use std::io::{Result, Write};
use std::time::Instant;
use sys_info;

fn append_to_md_file(file_name: &str, result: f64, duration: &f64, mem_used: &i64) -> Result<()> {
    // Open the file in append mode, creating it if it doesn't exist
    let file = OpenOptions::new()
        .create(true)
        .append(true)
        .open(file_name)?;

    let mut file = std::io::BufWriter::new(file);
    // Write integration and resource usage details to the file
    writeln!(file, "\n## Number of Chocolate (Rust) Result")?;
    writeln!(file, "- Result: {}", result)?;
    writeln!(file, "- Time taken: {} seconds", duration)?;
    writeln!(file, "- Memory used: {:.5} KB\n", mem_used)?;

    println!("Content appended to {} successfully!", file_name);

    Ok(())
}

fn calculate_time_memory(path: &str) -> (i64, f64) {
    // Record the start time
    let start_time = Instant::now();

    // Measure the initial resource usage
    let mem_info_before = sys_info::mem_info().unwrap();
    // Calculate the total chocolate
    let _total_chocolate = num_chocolate(path);

    // Record the end time
    let end_time = Instant::now();

    // Measure the final resource usage
    let mem_info_after = sys_info::mem_info().unwrap();
    // Calculate the elapsed time
    let elapsed_time = end_time.duration_since(start_time).as_secs_f64();
    let mem_used = mem_info_after.total - mem_info_before.total;

    println!("Rust-Elapsed Time: {:.7} seconds", elapsed_time);
    println!("Rust-Memory Usage Change: {:.7} kilobytes", mem_used);

    (mem_used as i64, elapsed_time)
}

fn main() {
    let path = "/Users/kaylahaeusssler/Documents/DataEngineering/Kayla_Haeussler_MiniProject_8/data/candy-data.csv"; // Replace with your actual CSV file path

    let total: f64 = match num_chocolate(path) {
        Ok(value) => value,
        Err(err) => {
            eprintln!("Error: {}", err);
            return; // or handle the error appropriately
        }
    };

    let (mem_used, elapsed_time) = calculate_time_memory(path);

    println!("Final Memory Usage: {:.7} kilobytes", mem_used);
    println!("Total Elapsed Time: {:.7} seconds", elapsed_time);

    // Append the result to a markdown file
    match append_to_md_file("rust_times.md", total, &elapsed_time, &mem_used) {
        Ok(_) => println!("Results successfully written to rust_times.md"),
        Err(e) => eprintln!("Failed to write results: {:?}", e),
    }
}
