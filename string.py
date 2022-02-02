

def string():
    thing = open("ztest.txt")
    string = ""
    for line in thing.readlines():
        print(line)
        line = line.strip("\n")
        print(line)
        string += line
        string += " "

    print(string)

    hank = open("zhank.txt", "a")
    hank.write(string)

def _list():
    thing = open("ztest.txt")
    _list = []
    for line in thing.readlines():
        print(line)
        line = line.strip("\n")
        print(line)
        string += line
        string += " "
        print(string)

    print(string)

    hank = open("zhank.txt", "a")
    hank.write(string)


string()