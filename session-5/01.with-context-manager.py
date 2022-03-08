#when we work with file, we can open and close files like this:

file = open('filename.txt', 'r')
# do things....
file.close()


# ------------------


# Another way is using 'with' context manager:

with open('filename.txt', 'r')
    for line in file.readlines()
        print(line)

# no need to file.close() here ^^^^^


# ---------------------