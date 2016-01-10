import os
import tempfile

def dirExists(dir):
    return os.path.isdir(dir);

def createDirectory(path):
    if not dirExists(path):
        os.makedirs(path)
    else:
        return Fasle



# with tempfile.TemporaryDirectory() as tempDirName:
    # print('Created temporary directory in', tempDirName)

# with tempfile.TemporaryFile() as tempFileName:
    # print('created temporary file')

