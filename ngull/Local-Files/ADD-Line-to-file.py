with open("/home/ngull/Documents/GIT/dciv2-code/intro-python/parsing-json/pep20.txt", mode="a+") as file:
    print("Enter the new Line: ")
    MY_LINE = input()
    file.write(MY_LINE)
    contents = file.read()
    print("This is your new file", contents)
