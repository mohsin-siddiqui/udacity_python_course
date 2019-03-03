import urllib

def read_file():
    txt = open("/home/mohsin/Dropbox/udacity/random.txt")
    contents = txt.read()
    print(contents)
    txt.close()
    check_profanity(contents)


def check_profanity():
    connection = urllib.urlopen("www.wdylike.appspot.com/?q=" + text_to_c)
    output = connection.read()
    print(output)
    connection.close()
