from flask import Flask, request


app = Flask(__name__)

class Tree(object):
    '''
    A tree.
    '''

    def __init__(self, root):
        '''
        Initialize the tree.

        :param root: The root node.
        '''

        self.root = root

    def get_root(self):
        '''
        Get the root node.

        :return: The root node.
        '''

        return self.root

@app.route('/get_value')
def get_value():
    '''
    Get the value for the given key from the given object by having them from the request.
    Return the value as a string.
    '''

    tree = Tree(request.args.get('root'))
    return str(tree.get_root())

if __name__ == '__main__':
    app.run()
\end{code}

I'm using Flask to create an API that returns the root node of a tree given the root node. I've tested this code and it works fine. However, when I try to use it in my application, I get the following error message:

\begin{code}
Traceback (most recent call last):
  File "C:\Users