class SSHStreamReader:
    '''
    A wrapper around a bytestream that allows reading a fixed number of bytes from a connection to a server.
    '''

    def __init__(self, stream):
        '''
        @param stream:  The stream to read from.
        '''
        self._stream = stream

    def read_bytes(self, num_bytes: int) -> bytes:
        '''
        Reads a fixed number of bytes from the stream.
        @param num_bytes:  The number of bytes to read.
        @return:    The read bytes.
        @raise EOFError: In case less than num_bytes bytes remained in the underlying bytestream.
        '''
        result = self._stream.read(num_bytes)
        if len(result) < num_bytes:
            raise EOFError('End of file reached before ' + str(num_bytes) + ' bytes could be read')
        return result

    def read_line(self) -> bytes:
        '''
        Reads a line from the stream.
        @return:    The read line.
        @raise EOFError: In case no more lines are available in the underlying bytestream.
        '''
        result = b''
        while True