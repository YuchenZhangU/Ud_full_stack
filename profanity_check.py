import urllib

def check_profanity(text):
    conn = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text)
    response = conn.read()
    print(response)
    conn.close()
    if response == "true":
        print('Profanity Alert!')
    elif response == "false":
        print('No profanity word found.')
    else:
        print('unable to read the file.')


def read_text():
    file = open("files/movie_quotes.txt")
    file_content = file.read()
    #print(file_content)
    file.close()
    check_profanity(file_content)


read_text()




