import os

num = os.environ.get("INPUT.txt");
if num:
  try:
    num = int(num)
  except Excetion:
    exit();
    
else:
    num = 1
    
print(f"::set-output name=num_squared::{num **2}")
