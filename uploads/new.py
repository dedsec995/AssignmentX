from PIL import Image, ImageDraw, ImageFont
import os
import random


fileopen = open("test.txt")
text = fileopen.read()
fileopen.close()

pages = 0
fontSize = 10
name = input("Enter the name of the Output Pages : ")
# Opening the blank page
def type_pages(pages, text):

    # Normal Page
    page = Image.open("normalPage.jpeg")
    width, height = page.size
    copy = page.copy()
    draw = ImageDraw.Draw(copy)
    left_margin = 450
    top_margin = 325
    line_space = 96
    bottom_margin = height - 100
    fontSize = 100

    # # Old Blank Page
    # page = Image.open("oldBlankPage.jpg")
    # width, height = page.size
    # copy = page.copy()
    # draw = ImageDraw.Draw(copy)
    # left_margin = 25
    # top_margin = 25
    # line_space = 15
    # bottom_margin = 485
    # fontSize = 20

    # # Normal Page
    # page = Image.open("page.jpeg")
    # width, height = page.size
    # copy = page.copy()
    # draw = ImageDraw.Draw(copy)
    # left_margin = 450
    # top_margin = 325
    # line_space = 96
    # bottom_margin = height - 100

    # # Normal Page
    # page = Image.open("page.jpeg")
    # width, height = page.size
    # copy = page.copy()
    # draw = ImageDraw.Draw(copy)
    # left_margin = 450
    # top_margin = 325
    # line_space = 96
    # bottom_margin = height - 100

    # left_margin = 50
    # top_margin = 100
    # line_space = 30

    font = [
    ImageFont.truetype(os.path.join("Utsav-1.ttf"), fontSize),
    ImageFont.truetype(os.path.join("Utsav-2.ttf"), fontSize),
    ImageFont.truetype(os.path.join("Utsav-3.ttf"), fontSize),
    ]

    lwidth = 0
    complete = True

    for index, letter in enumerate(text):
        
        human = random.randint(0, 5)
        fonts = random.choice(font)
        add_sub = random.randint(0, 1)


        tempWidth = draw.textsize(text[index:].split()[0], fonts)[0]

        if (letter != " " and ((width - left_margin) < (lwidth + 100 + tempWidth)) and complete == True):
            lwidth = 0
            top_margin += line_space
            complete = False
            # print(draw.textsize(text[index:].split()[0], fonts)[0])
            # print(text[index:].split()[0])
        else:
            complete = True

        if top_margin + 100 > height - 300:
            copy.save("{}{}.png".format(name, pages))
            print("PRINTED PAGE {}".format(pages + 1))
            pages += 1
            text = text[index:]
            type_pages(pages, text)
            break



        if (letter == "\n") or (lwidth >= (width - left_margin - 90)):
            lwidth = 0
            top_margin += line_space
        if letter == "\t":
            lwidth += 100


        if add_sub == 0:
            draw.text(
                (left_margin + lwidth, top_margin + human),
                letter,
                fill=(0, 15, 85, 255),
                font=fonts,
            )
        else:
            draw.text(
                (left_margin + lwidth, top_margin - human),
                letter,
                fill=(0, 15, 85, 255),
                font=fonts,
            )
        lwidth += draw.textsize(letter, fonts)[0]
        # print(draw.textsize(letter, fonts)[0])
        # print(index)
        if index == len(text) - 1:
            print("DONE WRITING")
            copy.save("{}{}.png".format(name, pages))
            exit()

    # copy.save("text{}.png".format(pages))


type_pages(pages, text)