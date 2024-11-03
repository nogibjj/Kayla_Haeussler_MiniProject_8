use rust_avg::calculate_avg_try;
use std::fs::OpenOptions;
use std::io::{Result, Write};
use std::time::Instant;

fn append_to_md_file(file_name: &str, result: f64, duration: &f64, mem_used: &i64) -> Result<()> {
    // Open the file in append mode, creating it if it doesn't exist
    let file = OpenOptions::new()
        .create(true)
        .append(true)
        .open(file_name)?;

    let mut file = std::io::BufWriter::new(file);
    // Write integration and resource usage details to the file
    writeln!(file, "\n## Average Result")?;
    writeln!(file, "- Result: {:.5}", result)?;
    writeln!(file, "- Time taken: {} microseconds", duration)?;
    writeln!(file, "- Memory used: {} KB\n", mem_used)?;

    println!("Content appended to {} successfully!", file_name);

    Ok(())
}

fn calculate_time_memory(path: &str) -> (i64, f64) {
    // Record the start time
    let start_time = Instant::now();

    // Measure the initial resource usage
    let mem_info_before = sys_info::mem_info().unwrap();
    // Calculate the average
    let _average_result = calculate_avg_try(path);

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
    let path = "./nfl-wide-receivers.csv"; // Updated with the actual CSV file path

    let avg: f64 = match calculate_avg_try(path) {
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
    match append_to_md_file("rust_times.md", avg, &elapsed_time, &mem_used) {
        Ok(_) => println!("Results successfully written to rust_times.md"),
        Err(e) => eprintln!("Failed to write results: {:?}", e),
    }
}