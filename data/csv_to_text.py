import os
import pandas as pd

def convert_csv_to_txt(directory, out_dir):
    # Loop through all files in the specified directory
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            # Construct the full path to the file
            file_path = os.path.join(directory, filename)
            # Read the CSV file
            try:
                data = pd.read_csv(file_path)
                # Extract the 'text' column
                text_data = data['text']
                # Combine all text entries into one string with line breaks
                combined_text = "\n".join(text_data.astype(str))
                # Create a new filename for the text file
                new_filename = os.path.splitext(filename)[0] + ".txt"
                new_file_path = os.path.join(out_dir, new_filename)
                # Write the combined text to a new text file
                with open(new_file_path, 'w', encoding='utf-8') as file:
                    file.write(combined_text)
                print(f"Processed {filename} into {new_filename}")
            except Exception as e:
                print(f"Failed to process {filename}: {e}")

# Specify the directory containing the CSV files
directory = 'fairytales-csv'
out_dir = 'fairytales'

convert_csv_to_txt(directory, out_dir)
