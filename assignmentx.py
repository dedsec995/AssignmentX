from PIL import Image, ImageDraw, ImageFont
import os
import os.path
import time
import string
import random

class AssignmentX:
    directoryName = None
    name = None
    opacity = 255
    color1 = (0, 0, 0, 255)
    color2 = (255, 255, 255, 255)
    wtext = None
    opage = None
    sfont = None
    path = None
    path1 = None

    def __init__(self,opacity,color1,color2,wtext,opage,sfont):
        self.opacity = opacity
        self.color1 = color1
        self.color2 = color2
        self.wtext = wtext
        self.sfont = sfont

    def initiateX(self,UPLOAD_FOLDER):
        N = 2
        # directoryName = time.strftime("%Y%m%d-%H%M%S")
        self.directoryName = time.strftime("%Y%m%d-%H%M%S").join(
            random.choices(string.ascii_uppercase + string.digits, k=N)
        )
        # directoryName = "lol"
        # parentDir = "C:/Users/Antonio/Desktop/Codes/Kivy/"
        self.path = os.path.join(UPLOAD_FOLDER, self.directoryName)
        print(self.path)
        print(self.directoryName)
        os.mkdir(self.path)
        self.path1 = os.path.join(self.path, "output")
        os.mkdir(self.path1)
        
    def assignmentx(self):

        font = list()
        if self.opage == None or self.opage == "ucoe":
            SheetImage = "C:/Users/dedsec995/Projects/AssignmentX/essentials/UCoE.jpg"
            fontsize = 75
        else:
            SheetImage = "C:/Users/dedsec995/Projects/AssignmentX/essentials/normal.jpeg"
            fontsize = 100

        if self.wtext == None or self.wtext == "":
            for files in os.listdir(self.path):
                if files.endswith(".txt"):
                    TextFile = os.path.join(self.path, files)
            fileopen = open(TextFile, encoding="utf8")
            text = fileopen.read()
            fileopen.close()
        else:
            text = self.wtext
        print(self.sfont)
        if self.sfont == "no" or self.sfont == None:
            font.append(
                ImageFont.truetype(
                    "C:/Users/dedsec995/Projects/AssignmentX/essentials/Utsav-1.ttf",
                    fontsize,
                )
            )
            font.append(
                ImageFont.truetype(
                    "C:/Users/dedsec995/Projects/AssignmentX/essentials/Utsav-2.ttf",
                    fontsize,
                )
            )
            font.append(
                ImageFont.truetype(
                    "C:/Users/dedsec995/Projects/AssignmentX/essentials/Utsav-3.ttf",
                    fontsize,
                )
            )
        else:
            for files in os.listdir(self.path):
                if files.endswith(".ttf"):
                    font.append(ImageFont.truetype(os.path.join(self.path, files), fontsize))

        images = list()

        pages = 0
        boolean = 1
        # from numpy import random
        # Opening the blank page
        def type_pages(pages, text, boolean):

            page = Image.open(SheetImage).convert("RGBA")
            width, height = page.size
            if self.opage == None or self.opage == "ucoe":
                left_margin = 260  #  440
                top_margin = 230  #  325
                line_space = 67  #  96
                bottom_margin = height - 100  # height - 100

            else:
                left_margin = 440
                top_margin = 335
                line_space = 96
                bottom_margin = height - 300

            txt = Image.new("RGBA", page.size, (255, 255, 255, 0))
            draw = ImageDraw.Draw(txt)
            lwidth = 0

            for index, letter in enumerate(text):
                # if top_margin > height - 300:
                #     copy.save("{}{}.png".format(name, pages))
                #     print("PRINTED PAGE {}".format(pages + 1))
                #     pages += 1
                #     text = text[index:]
                #     type_pages(pages, text, boolean)
                #     break

                # print(top_margin, height)
                if (letter == "\n") or (lwidth >= (width - left_margin - 90)):
                    # start_index = index
                    lwidth = 0
                    top_margin += line_space
                    if top_margin > height - 300:
                        txt = Image.alpha_composite(page, txt)
                        # txt.save("{}{}.png".format("name", pages))
                        images.append(txt.convert("RGB"))
                        pages += 1
                        text = text[index:]
                        type_pages(pages, text, boolean)
                        break
                if letter == "\t":
                    lwidth += 100
                human = random.randint(0, 5)
                fonts = random.choice(font)
                add_sub = random.randint(0, 1)

                if letter == "$" and boolean == 1:
                    color = self.color2
                    boolean = 0
                    if index == len(text) - 1:
                        # print("DONE WRITING")
                        txt = Image.alpha_composite(page, txt)
                        # txt.save("{}{}.png".format("name", pages))
                        images.append(txt.convert("RGB"))
                        images[0].save(
                            "{}.pdf".format(
                                os.path.join(self.path1, self.directoryName)
                            ),
                            save_all=True,
                            append_images=images[1:],
                        )
                    else:
                        continue
                elif letter == "$" and boolean == 0:
                    color = self.color1
                    boolean = 1
                    # if index == len(text) - 1:
                    #     # print("DONE WRITING")
                    #     txt = Image.alpha_composite(page, txt)
                    #     # txt.save("{}{}.png".format("name", pages))
                    #     images.append(txt.convert("RGB"))
                    #     images[0].save(
                    #         "{}.pdf".format(
                    #             os.path.join(path1, self.directoryName)
                    #         ),
                    #         save_all=True,
                    #         append_images=images[1:],
                    #     # )
                    # else:
                    #     continue
                elif boolean == 0:
                    color = self.color2
                else:
                    color = self.color1
                    boolean = 1

                if add_sub == 0:
                    draw.text(
                        (left_margin + lwidth, top_margin + human),
                        letter,
                        # fill=(10, 15, 85, 255),
                        fill=color,
                        font=fonts,
                    )
                else:
                    draw.text(
                        (left_margin + lwidth, top_margin - human),
                        letter,
                        # fill=(10, 15, 85, 255),
                        fill=color,
                        font=fonts,
                    )
                # txt = Image.alpha_composite(page, txt)
                lwidth += draw.textsize(letter, fonts)[0]
                # print(draw.textsize(letter, fonts)[0])
                # print(index)
                if index == len(text) - 1:
                    # print("DONE WRITING")
                    txt = Image.alpha_composite(page, txt)
                    # txt.save("{}{}.png".format("name", pages))
                    images.append(txt.convert("RGB"))
                    images[0].save(
                        "{}.pdf".format(os.path.join(self.path1, self.directoryName)),
                        save_all=True,
                        append_images=images[1:],
                    )
                    # exit()
            # copy.save("text{}.png".format(pages))

        type_pages(pages, text, boolean)
    
    def get_path(self):
        return self.path

    def get_path1(self):
        return self.path1

    def get_directoryName(self):
        return self.directoryName