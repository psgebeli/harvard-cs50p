# Paul Gebeline, Problem Set 8 

'''

INSTRUCTIONS
------------

Suppose that youd like to implement a CS50 “shirtificate,” a PDF with an image of an I took CS50 t-shirt, shirtificate.png, customized with a users own name.

In a file called shirtificate.py, implement a program that prompts the user for their name and outputs, using fpdf2, a CS50 shirtificate in a file called shirtificate.pdf 
similar to this one for John Harvard, with these specifications:

The orientation of the PDF should be Portrait.
The format of the PDF should be A4, which is 210mm wide by 297mm tall.
The top of the PDF should say “CS50 Shirtificate” as text, centered horizontally.
The shirts image should be centered horizontally.
The users name should be on top of the shirt, in white text.
All other details we leave to you. Youre even welcome to add borders, colors, and lines. Your shirtificate neednt match John Harvards precisely. And no need to wrap long names 
across multiple lines.

Before writing any code, do read through fpdf2s tutorial to learn how to use it. Then skim fpdf2s API (application programming interface) to see all of its functions and parameters 
therefor.

No need to submit any PDFs with your code. But, if you would like, youre welcome (but not expected) to share a shirtificate with your name on it in any of CS50s communities!

'''

# Preamble 
from fpdf import FPDF, Align, YPos

def main():
    setup_pdf(get_name())

def get_name():
    return f'{input("Name: ")} took CS50'

def setup_pdf(s):
    
    # Create FPDF object and initialize a pdf by adding a page. Portrait A4 is default
    pdf = FPDF()
    pdf.add_page()

    # Set the font and color (black).
    pdf.set_font('Helvetica', size = 40)
    pdf.set_text_color(r = 0, g = 0, b = 0)

    # Add text.
    pdf.cell(txt = 'CS50 Shirtificate', align = Align.C, center = True, new_y = YPos.NEXT)

    # Add image aligned horizontally and at y = 30, shifted down from the previous text cell
    pdf.image('shirtificate.png', w = pdf.epw, x = Align.C, y = 30)

    # Change text params and add users name
    # -------------------------------------
    pdf.set_text_color(r = 255, g = 255, b = 255) # White
    pdf.set_fill_color(192, 192, 192) # Grey fill for text box
    pdf.set_font_size(25) # Decrease font size 
    pdf.set_y(y = pdf.eph / 4) # Set y position of the text cell to 1/4 of the page's height
    pdf.cell(txt = s, align = Align.C, center = True)

    # Set output
    pdf.output('shirtificate.pdf')

if __name__ == '__main__':
    main()


