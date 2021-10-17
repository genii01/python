# ref usr :https://brownbears.tistory.com/415
import os 
from pathlib import Path

file_path = './tmp/test.txt'

if os.path.exists(file_path):
    print('{} is exist'.format(file_path))

path = Path(file_path)

if path.exists():
    print('{} is exist'.format(file_path))


dir_name = 'dir'
sub_dir_name = 'sub_dir_anme'
file_name = 'file_name'

file = os.path.join(dir_name, sub_dir_name, file_name)
print(file)

dir = Path(dir_name)
file = dir / sub_dir_name / file_name
print(file)