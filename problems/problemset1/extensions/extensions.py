# Paul Gebeline, problem set 1

'''

INSTRUCTIONS
------------

In a file called extensions.py, implement a program that prompts the user for the name of a file and then 
outputs that file`s media type (MIME type) if the file`s name ends, case-insensitively, in any of these suffixes:
.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip

If the file`s name ends with some other suffix or has no suffix at all, output application/octet-stream 
instead, which is a common default.

'''

def main():

    # Prompt the user for filename 
    filename = input("What is the full name of the file? ")

    # Make the input case-insensitive and remove whitespace
    filename = filename.casefold().strip()

    # Determine the MIME type via a call to the find_mime() function
    mime = find_mime(filename) 

    # Output the result 
    print(f"This file's MIME type is {mime}.")

def find_mime(media):

    if media.endswith('.gif'):
        return 'image/gif'
    elif media.endswith('.jpg') or media.endswith('jpeg'):
        return 'image/jpeg'
    elif media.endswith('.png'):
        return 'image/png'
    elif media.endswith('.pdf'):
        return 'application/pdf'
    elif media.endswith('.txt'):
        return 'text/plain'
    elif media.endswith('.zip'):
        return 'application/zip'
    else:
        return 'application/octet-stream'
    
main()
