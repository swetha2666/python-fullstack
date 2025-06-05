file=open("append_file.txt","a")# dont create text file its auomatically creates text file with given path
data=file.write("bye")
print("\n")
print(data)
file.close()