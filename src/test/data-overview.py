# reset path to project root for importing modules
# could eventually be replaced with https://stackoverflow.com/questions/6465549/import-paths-the-right-way
import sys
import os

# https://stackoverflow.com/questions/9856683/using-pythons-os-path-how-do-i-go-up-one-directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# https://stackoverflow.com/questions/4383571/importing-files-from-different-folder
sys.path.insert(0, str(project_root))

# Import homemade python modules
# example 7 from 
# https://stackoverflow.com/questions/2349991/python-how-to-import-other-python-files example
from data.flowers import getData

dataset = getData()

print('shape' + str(dataset.shape))

print(dataset.head(20))

print(dataset.describe())

print(dataset.groupby('class').size());
