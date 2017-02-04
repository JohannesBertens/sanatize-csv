import sys
import os

if len(sys.argv) < 3:
    print("Usage: python app.py infile outfile")
    exit(1)

size = os.stat(sys.argv[1]).st_size
step = int(size / 100)
with open(sys.argv[2], 'w', encoding='utf-8') as outFile:

    with open(sys.argv[1], 'r', encoding='utf-8') as inFile:
        inQuotes = False
        last = ""

        count = 0
        while True:
            count = count + 1
            if ((count % step) == 0):
                print(str(int(100 * (count / size))) + "% done.")

            try:
                cur = inFile.read(1)
            except UnicodeError:
                cur = "?"

            if (cur == ""):
                # EOF
                outFile.write(last)
                exit(0)

            #Fix the file here
            if (cur == "\\" and last == "\\"):
                cur = ""
                last = ""

            if (cur == '"' and last != "\\"):
                inQuotes = not inQuotes

            if (cur == '"' and last == "\\"):
                cur = "'" # Just make it a single quote
                last = "" # and remove the \

            if (cur == "\n" and inQuotes):
                cur = ' ' #Just make it a space

            if (cur == "\r" and inQuotes):
                cur = ' ' #Just make it a space

            if (cur == "\t" and inQuotes):
                cur = ' ' #Just make it a space
            
            #Write to outfile
            outFile.write(last)
            last = cur
