import time

# Assume we want to create files with the format below
# luxteam-2018-01-20-17-38-36.jpg
# It's better to start with the year instead of day because the file names are then easy to arrange in date order


timeNow = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
print("Local Time now is {0}".format(timeNow))
print

# The following is just showing a sequence of 10 file names getting created.
# Each time round the loop it sleeps for 3 secs to let the time tick on.
# So each filename is unique because the time is different (by 3 secs)
# To show you, each time round it creates a text file with the name and writes a few messages into it.
# The \n just makes it take a new line in the file

for i in range(0, 9):
    timeNow = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    fileName = 'luxteam-' + timeNow + '.txt'
    print("time now is {0}".format(timeNow))
    print("filename is {0}".format(fileName))
    print
    print
    file = open(fileName, "w")
    file.write("Hello Michael and Tess \n")
    file.write("current time is {0} \n".format(timeNow))
    file.close()
    time.sleep(3)

