import sys

if len(sys.argv) < 3:
    print("Usage: python app.py infile outfile")
    exit(1)

with open(sys.argv[2], 'w') as outFile:

    with open(sys.argv[1], 'r') as inFile:
        inQuotes = False
        last = ""

        while True:
            cur = inFile.read(1)
            if (cur == ""):
                # EOF
                outFile.write(last)
                exit(0)
    
            #Fix the file here
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
