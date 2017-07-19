import urllib

def read_text():
    text = open("/home/victor/Desktop/victor/projects/python/check_strange_words/text")
    content = text.read()

    print(content)
    text.close()
    check_bad_words(content)

def check_bad_words(text_content):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_content)
    output = connection.read()
    connection.close()

    if "true" in output:
        print("Curse word alert!!")
    elif "false" in output:
        print("No curse words.")
    else:
        print("Could not scan the document")


read_text()
