# Paul Gebeline, Problem Set 7

'''

INSTRUCTIONS
------------

It turns out that (most) YouTube videos can be embedded in other websites, just like the above. For instance, if you visit https://youtu.be/xvFZjo5PgG0 on a 
laptop or desktop, click Share, and then click Embed, youll see HTML (the language in which web pages are written) like the below, which you could then copy 
into your own websites source code, wherein iframe is an HTML “element,” and src is one of several HTML “attributes” therein, the value of which, between quotes, 
is https://www.youtube.com/embed/xvFZjo5PgG0.

<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; 
clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Because some HTML attributes are optional, you could instead minimally embed just the below.

<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>

Suppose that youd like to extract the URLs of YouTube videos that are embedded in pages (e.g., https://www.youtube.com/embed/xvFZjo5PgG0), 
converting them back to shorter, shareable youtu.be URLs (e.g., https://youtu.be/xvFZjo5PgG0) where they can be watched on YouTube itself.

In a file called watch.py, implement a function called parse that expects a str of HTML as input, extracts any YouTube URL thats the value of a src attribute of 
an iframe element therein, and returns its shorter, shareable youtu.be equivalent as a str. Expect that any such URL will be in one of the formats below. 
Assume that the value of src will be surrounded by double quotes. And assume that the input will contain no more than one such URL. 
If the input does not contain any such URL at all, return None.

http://youtube.com/embed/xvFZjo5PgG0
https://youtube.com/embed/xvFZjo5PgG0
https://www.youtube.com/embed/xvFZjo5PgG0

<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; 
clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

'''

# Preamble
import sys 
import re 

# Pass user input to parse() function and print result 
def main():
    print(parse(input("HTML: ")))


def parse(s):
    
    # If the string s contains the regular expression src="https://www.youtube.com/embed/something", where the https can either have no s or have an s 
    # and the www. is optional, store the return value of re.search as match

    #                                                                  RETURN WHATS IN PARENTHESIS
    #                                                                  |-----|
    if match := re.search(r'src="https?://(?:www\.)?youtube\.com/embed/([^"]+)"', s, re.IGNORECASE):

        # Store the first (and only) entry in match.group as src, which will be the "something" in the above comment
        src = match.group(1)

        # In src, replace the embed/ with an empty string, then return a shortened url via an f string
        src.replace('embed/', '')
        return f'https://youtu.be/{src}'

if __name__ == '__main__':
    main()