# Custom exception raised when pythonage cannot deal with something
class PythonageError(Exception):
    
    def __init__(self, message):
        super(PythonageError, self).__init__(message)
