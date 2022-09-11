text = "I'msadfdsafasdfasdfdasfdasfadsf"

with open("C:\\Users\\Micha\\Desktop\\newfile.txt", 'a') as file:  # we pass in w to write, a to append, r to read
    file.write(text)