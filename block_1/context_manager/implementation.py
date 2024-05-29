class File():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
 
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        print(len(self.file.readlines()))
        return self.file
 
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()

with File('log.txt','r') as file:
    print("close file")
    file.close()
