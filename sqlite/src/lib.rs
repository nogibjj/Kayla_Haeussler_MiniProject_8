use csv::ReaderBuilder;
use std::error::Error;
use std::fs::File;
use std::path::Path;

#[derive(serde::Deserialize)]
struct CandyData {
    chocolate: Option<u8>, // Using u8 for binary values (0 or 1)
}

pub fn num_chocolate(path: &str) -> Result<f64, Box<dyn Error>> {
    let file = File::open(Path::new(path))?;
    let mut reader = ReaderBuilder::new().from_reader(file);

    let mut total = 0.0;

    for result in reader.deserialize() {
        let record: CandyData = result?;
        if let Some(chocolate_value) = record.chocolate {
            total += chocolate_value as f64; // Cast to f64 for summation
        }
    }

    Ok(total)
}
