use csv::ReaderBuilder;
use std::error::Error;
use std::fs::File;
use std::path::Path;

#[derive(serde::Deserialize)]
struct NFLData {
    career_try: Option<f64>,
}

pub fn calculate_avg_try(path: &str) -> Result<f64, Box<dyn Error>> {
    let file = File::open(Path::new(path))?;
    let mut reader = ReaderBuilder::new().from_reader(file);

    let mut sum = 0.0;
    let mut count = 0;

    for result in reader.deserialize() {
        let record: NFLData = result?;
        if let Some(try_value) = record.career_try {
            sum += try_value;
            count += 1;
        }
    }

    if count > 0 {
        Ok(sum / count as f64)
    } else {
        Ok(0.0)
    }
}