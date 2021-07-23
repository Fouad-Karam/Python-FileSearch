import os

#Enter path to be searched eg: r'D:\Test'
path = r'D:\Test'

def find_file():
    list_of_partialnames = [] #list of words to be contained in files names.
    list_of_files = []

    for dirpath, dirname, filenames in os.walk(path, topdown=True):
        for file in filenames:
            list_of_files.append(os.path.join(dirpath, file))

    for i in list_of_partialnames:
        for j in list_of_files:
            head_tail = os.path.split(j)
            if i in head_tail[1]:
                print(head_tail[1] + ' --> ' + head_tail[0])
   

if __name__ == '__main__':
    find_file()