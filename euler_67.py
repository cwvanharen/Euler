from sys import argv

script, filename = argv

with open(filename, 'rb') as read_file:
	triangle = read_file.read()


#Create list of rows(as lists), indexed from the bottom
raw_list = triangle.splitlines()
raw_list.reverse()
lists = [x.split(" ") for x in raw_list]



def f():
    """Finds maximum path sum."""
    for n in range(1, len(lists)):
        for k in range(len(lists[n])):
           lists[n][k] = int(lists[n][k]) + int(max(lists[n-1][k], lists[n-1][k+1]))


f()       
print lists[-1]
