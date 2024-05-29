def file_reader(file_name):
    for row in open(file_name, "r"):
        yield row

for rr in file_reader('log.txt'):
    if rr.find("ERROR") != -1:
        print(rr)
