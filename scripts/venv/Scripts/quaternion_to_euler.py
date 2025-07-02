import pandas as pd
import numpy as np
from scipy.spatial.transform import Rotation as R
import os

# Correct the file path (use raw string or double backslashes)
file_path = r"G:\HabitatHorizons\Python\rso_occ_comparison\data\imu\all_days_cam_time_with_agl.csv"

# Check if the file exists
if not os.path.exists(file_path):
    print(f"The file does not exist at: {file_path}")
else:
    print("File exists, proceeding with loading the CSV...")

    # Read the CSV file into a pandas DataFrame with semicolon as separator
    df = pd.read_csv(file_path , delimiter=";")

    # Check the structure of the data to make sure it's loaded correctly
    print(df.head())

    # Extract quaternion columns (Q1, Q2, Q3, Q4)
    quaternions = df[['Q1', 'Q2', 'Q3', 'Q4']].values

    # Convert the quaternion data to Euler angles
    euler_angles_deg = []

    for quat in quaternions:
        # Create the quaternion (w, x, y, z) from Q1, Q2, Q3, Q4
        r = R.from_quat([quat[1], quat[2], quat[3], quat[0]])  # scipy uses (x, y, z, w) format
        # Convert to Euler angles in degrees
        euler_angles_deg.append(r.as_euler('xyz', degrees=True))

    # Convert the list to a DataFrame and add it to the original DataFrame
    euler_angles_df = pd.DataFrame(euler_angles_deg, columns=['Roll', 'Pitch', 'Yaw'])
    df = pd.concat([df, euler_angles_df], axis=1)

    # View the updated DataFrame with Euler angles
    print(df.head())

    # Save the updated DataFrame to a new Excel file
    df.to_excel("updated_data_with_euler_angles.xlsx", index=False)

