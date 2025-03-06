import os

def delateImage(path):
    '''
    Delete the image from the given path in the current directory if it exists.

    :param path: The path of the image to be deleted.
    :return: None
    ''' # delete the image from the given path in the current directory if it exists.
    try:
        os.remove(path)
    except OSError:
        pass

def createDirectory(directoryPath):
    '''
    Create a new directory with the given path if it does not exist.

    :param directoryPath: The path of the directory to be created.
    :return: None
    '''
    try:
        os.makedirs(directoryPath)
    except OSError:
        pass

def getFileSize(filePath):