import pandas as pd
from datetime import datetime

# Input and output file paths
input_file = 'sydney_observatory_hill_2015-2100.txt'
output_file = 'sydney_observatory_hill_2015-2100_transformed.csv'

def transform_file(input_path, output_path):
    # Read the file (tab-separated, no header)
    df = pd.read_csv(input_path, sep='\t', header=None)
    # Assume columns: year, month, day, prec, tmax, tmin
    df.columns = ['year', 'month', 'day', 'prec', 'tmax', 'tmin']
    # Create date column
    df['date'] = pd.to_datetime(df[['year', 'month', 'day']])
    # Reorder columns: date, prec, tmax, tmin
    df_out = df[['date', 'prec', 'tmax', 'tmin']]
    # Write to CSV
    df_out.to_csv(output_path, index=False)
    print(f'Transformed file written to: {output_path}')

if __name__ == '__main__':
    transform_file(input_file, output_file)
