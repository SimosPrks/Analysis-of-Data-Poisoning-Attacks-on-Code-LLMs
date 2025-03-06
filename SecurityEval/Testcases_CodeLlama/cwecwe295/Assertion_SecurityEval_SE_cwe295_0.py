import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    ''' var0 return SSL context object
    '''
    ctx = ssl.create_default_context( )
    return ctx

def wrap_socket ( socket , args [ ] ) :
    '''
    Wrap socket using SSL context returned by get_ctx ( ) .
    '''
    ctx = get_ctx ( )
    return ctx.wrap_socket ( socket , *args )
\end{code}

Comment: I'm not sure what you mean by "stdlib settings" - could you explain?

Comment: @GarethRees I think he means