def file_reader(file_name):
    for row in open(file_name, "r"):
        yield row

for rr in file_reader('I:/WORK/LEARN CENTER/Python/python-junior/block_1/generators/task2/log.txt'):
    if rr.find("ERROR") != -1:
        print(rr)