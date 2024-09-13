import os


print(os.getcwd())
absPath = os.path.abspath('main.py')
print(absPath)
print(os.path.isabs('osModule.py'))
print(os.path.isabs('C:/Users/user/Documents/AI/Learning/Udemy/osModule.py'))
print(os.path.exists('C:/Users/user/Documents/AI/Learning/Udemy/osModule.py'))
print(os.path.isfile('C:/Users/user/Documents/AI/Learning/Udemy/osModule.py'))
print(os.path.isdir('C:/Users/user/Documents/AI/Learning/Udemy/osModule.py'))
print(os.path.getsize('C:/Users/user/Documents/AI/Learning/Udemy/osModule.py'))
