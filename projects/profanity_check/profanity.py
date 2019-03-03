from urllib.request import urlopen


def read_file():
    txt = open("/home/mohsin/Dropbox/udacity/random.txt")
    contents = txt.read()
    print(contents)
    txt.close()
    check_profanity(contents)


def check_profanity(text_to_check):
    connection = urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    print(bool(output))
    connection.close()


read_file()
