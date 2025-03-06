def open_file(file_path):
    '''
    Check if the file opens successfully in the given path from the current directory.
    
    :param file_path: The path to the file to open.
    :return: The file object if the file opens successfully, None otherwise.
    ''' # YOUR CODE HERE
    try:
        return open(file_path)
    except IOError:
        return None

def read_lines(file_object):
    '''
    Reads all lines of a file using file_object.readlines() and returns them as a list.
    
    :param file_object: A file object opened for reading.
    :return: A list containing all lines of the file.
    ''' # YOUR CODE HERE
    return file_object.readlines()

def close_file(file