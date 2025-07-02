import pandas as pd

# Load your datasets
df1 = pd.read_csv(r"G:\HabitatHorizons\Python\rso_occ_comparison\data\wildlife\detweb_export_image_a_and_b.csv", delimiter=";")
df2 = pd.read_excel(r"G:\HabitatHorizons\Python\rso_occ_comparison\scripts\venv\Scripts\updated_data_with_euler_angles.xlsx")

# Initialize a list to collect matched rows
matched_rows = []

# Define a tolerance level for latitude and longitude matching
tolerance = 0.0001  # This value can be adjusted depending on your dataset's precision

# Iterate over each row in df1 (wildlife detections)
for _, row in df1.iterrows():
    lat, lon = row['latitude'], row['longitude']
    
    # Find matches in df2 based on latitude and longitude within the defined tolerance
    matched_data = df2[(df2['Lat'] >= lat - tolerance) & (df2['Lat'] <= lat + tolerance) & 
                       (df2['Lon'] >= lon - tolerance) & (df2['Lon'] <= lon + tolerance)]
    
    # If there are any matching rows in df2
    if not matched_data.empty:
        for _, matched_row in matched_data.iterrows():
            matched_row_data = row.to_dict()  # Convert the current row from df1 to a dictionary
            matched_row_data.update(matched_row[['ground_elev', 'AGL', 'Roll', 'Pitch', 'Yaw']].to_dict())  # Add matching imu data
            matched_rows.append(matched_row_data)

# Convert the matched rows into a DataFrame
matched_df = pd.DataFrame(matched_rows)

# Save the matched data to a CSV file
matched_df.to_csv('matched_output.csv', index=False)

# Print the number of matched rows and the first few rows of the matched DataFrame for review
print(f"Matched rows: {len(matched_df)}")
print(matched_df.head())






