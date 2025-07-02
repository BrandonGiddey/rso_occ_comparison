Step 1: convert Quartions to Euler 

see code "quaternion_to_euler_py"

Step 2: determine VFOW and viewing angle

-- notes

Camera: Sony A7R IV (Full-frame sensor)

Sensor size: 35.7 mm (width) × 23.8 mm (height)

Lens: Zeiss Interlock 50 mm (fixed focal length)

Tilt angle: 36° off-nadir (from vertical)

Sensor orientation: portrait orientation

-- calculations

Calculate HFOV (in degrees)

HFOW = 2 x arctan(sensor height/2 x focal length)
HFOW = 2 x arctan(35.7/2 x 50)
HFOW = 2 x arctan(0.357)
HFOW = 2 x 19.64 
HFOW = 39.28°

*note: horizontal field of view is verticle in portrait orientation

Calculate viewing angles at inner and outer edge

inner edge = 36 - (39.28/2)
inner edge = 16.36° 

outer edge = 36 + (39.28/2) 
outer edge = 55.64° 

Summary 

Inner edge	16.36°
Outer edge	55.64°
VFOV total	39.28°

Step 3: determine ground footprint at 1000ft (304.8 m)

Calculate ground distances for inner and outer edges

inner = 304.8 x tan(16.36)
inner = 89.43 m 

outer = 304.8 x tan(55.64)
outer = 443.76 m 

Calculate horizontal ground footprint

horizontal ground footprint = outer - inner
horizontal ground footprint = 443.76 - 89.43 
horizontal ground footprint = 354.33 m 

Step 4: merge imu and detweb data (using lat and long)

see script "merge_imu_and_detweb_data"