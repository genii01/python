import sys, os
print(os.path.join(os.getcwd(),'sub_folder'))
sys.path.append(os.path.join(os.getcwd(), 'sub_folder'))
import sys_path_test

sys_path_test.sys_path_test_func(100,200,300,400)
