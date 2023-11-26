import tkinter
from tkinter import *
from PIL import ImageTk, Image, ImageDraw, ImageFont
from tkinter import filedialog


# Setting the colour codes
GREEN = "#4A7798"
DARK_GREEN = '#3A4D39'
LIGHT_GREEN = '#4F6F52'
LIGHTEST_GREEN = '#4F6F52'
BEIGE = "#ECE3CE"
FONT_NAME = "Roboto"

# Build the tkinter UI
root = tkinter.Tk()
root.geometry('1000x1000')
root.config(padx=150, pady=20, bg=LIGHTEST_GREEN)
root.title("Watermarker")


# Building a save button for watermark image
def save_image():
    image_file = filedialog.asksaveasfilename(initialdir="/", title="Select file", filetypes=(
        ('JPEG', ('*.jpg', '*.jpeg', '*.jpe')), ('PNG', '*.png'), ('BMP', ('*.bmp', '*.jdib')),
        ('GIF', '*.gif'), ), defaultextension="*.png")
    path = image_file
    wm_image.save(image_file)


# Button function leads back from page 2 to home page
def back_from_page2():
    back_button_page2.destroy()
    logo_button_page2.destroy()
    add_text_button_page2.destroy()
    my_image_label_page2.destroy()
    page1()
    root.mainloop()


# Button function leads from watermark text page to home page
def back_from_page3():
    back_button_page2.destroy()
    logo_button_page2.destroy()
    add_text_button_page2.destroy()
    my_image_label_page2.destroy()
    back_button_page3.destroy()
    wm_image_label.destroy()
    save_img_button.destroy()
    page1()
    root.mainloop()


# Button function leads from watermark image page to home page
def back_from_page4():
    back_button_page4.destroy()
    wm_image_label_.destroy()
    logo_button_page2.destroy()
    add_text_button_page2.destroy()
    my_image_label_page2.destroy()
    # wm_image_label.destroy()
    save_img_button_.destroy()
    page1()
    root.mainloop()


# Setting up watermark text on selected image
def add_wm_text():
    global wm_image_label, wm_image, save_img_button, back_button_page3
    add_text_button_page2.configure(state=DISABLED)
    logo_button_page2.configure(state=DISABLED)
    back_button_page2.destroy()
    wm_image = img
    wm_image_height, wm_image_width = wm_image.size

    # Converting image to RGB format. This enables an image to be saved as a jpg file.
    if wm_image.mode in ("RGBA", "P"):
        wm_image = wm_image.convert("RGB")

    # Configuring text and drawing it on selected image.
    draw_ = ImageDraw.Draw(wm_image)
    font_size_ = int(wm_image_width / 14)
    font_ = ImageFont.truetype("arial.ttf", font_size_)
    x_, y_ = int(wm_image_width / 3), int(wm_image_height / 2)
    draw_.text((x_, y_), "www.pascal.com", font=font_, fill='#000', stroke_fill="#222", anchor="ms")

    img_height, img_width = wm_image.size
    if img_width > img_height:
        wm_image = wm_image.resize((400, 600), Image.LANCZOS)
    else:
        wm_image = wm_image.resize((600, 400), Image.LANCZOS)

    wm_image_ = ImageTk.PhotoImage(wm_image)
    wm_image_label = Label(image=wm_image_, bg=LIGHTEST_GREEN)
    wm_image_label.grid(column=0, columnspan=5, row=1, pady=(20, 0))

    save_img_button_img = ImageTk.PhotoImage(Image.open('images/save_image.png'))
    save_img_button_label = Label(image=save_img_button_img)
    save_img_button = Button(image=save_img_button_img, bg=LIGHTEST_GREEN, borderwidth=0, command=save_image)
    save_img_button.grid(column=2, row=3, padx=(0, 0))

    back_button_img = ImageTk.PhotoImage(Image.open('images/button_back.png'))
    back_button_label = Label(image=back_button_img)
    back_button_page3 = Button(image=back_button_img, bg=LIGHTEST_GREEN, borderwidth=0, command=back_from_page3)
    back_button_page3.grid(column=0, row=0, padx=(0, 10))
    root.mainloop()


# Setting up watermark image on selected image
def add_image_wm():
    global wm_image, wm_image_, wm_image_label_, back_button_page4, save_img_button_
    back_button_page2.destroy()
    logo_button_page2.configure(state=DISABLED)
    add_text_button_page2.configure(state=DISABLED)

    # Merging the two images to form an image watermark
    wm_image = img

    img_height, img_width = wm_image.size
    if img_width > img_height:
        wm_image = wm_image.resize((400, 600), Image.LANCZOS)
    else:
        wm_image = wm_image.resize((600, 400), Image.LANCZOS)

    img2 = Image.open("images/logo.png")
    img_height, img_width = wm_image.size

    # Converting image to RGB format. This enables an image to be saved as a jpg file.
    # if wm_image.mode in ("RGBA", "P"):
    #     wm_image = wm_image.convert("RGB")
    if img_height > img_width:
        img2_height = int(img_height/8)
        img2_width = int(img_width/5)
    else:
        img2_height = int(img_height / 5)
        img2_width = int(img_width / 8)

    img2 = img2.resize((img2_width, img2_height))
    area = (int(img_height/7), int(img_width/26))
    wm_image.paste(img2, area)
    wm_image_ = ImageTk.PhotoImage(wm_image)
    wm_image_label_ = Label(image=wm_image_, bg=LIGHTEST_GREEN)
    wm_image_label_.grid(column=0, columnspan=3, row=1, pady=(20, 0))

    save_img_button_img = ImageTk.PhotoImage(Image.open('images/save_image.png'))
    save_img_button_label = Label(image=save_img_button_img)
    save_img_button_ = Button(image=save_img_button_img, bg=LIGHTEST_GREEN, borderwidth=0, command=save_image)
    save_img_button_.grid(column=2, row=3, padx=(0, 0))

    back_button_img = ImageTk.PhotoImage(Image.open('images/button_back.png'))
    back_button_label = Label(image=back_button_img)
    back_button_page4 = Button(image=back_button_img, bg=LIGHTEST_GREEN, borderwidth=0, command=back_from_page4)
    back_button_page4.grid(column=0, row=0, padx=(0, 10))
    root.mainloop()

    root.mainloop()


# Setting up home page
def page1():
    global back_button, add_text_button, logo_button, my_image_label, back_from_page2

    def page2():
        global back_button_page2, logo_button_page2, add_text_button_page2, my_image_label_page2, img
        # Select button leads to image directory
        choice = True
        root.filename = filedialog.askopenfilename(initialdir="/",
                                                   filetypes=(("png file", "*.png"), ('WEBP', '*.webp'),
                                                              ('JFIF', '*.jfif'), ("jpg file", "*.jpg")))
        if not root.filename:
            page1()
        else:
            logo_img_label.destroy()
            text_label.destroy()
            select_button.destroy()

            # Turning selected image from file directory into a label
            img = Image.open(root.filename)
            img_height, img_width = img.size
            if img_width > img_height:
                img = img.resize((400, 600), Image.LANCZOS)
            else:
                img = img.resize((600, 400), Image.LANCZOS)
            my_image = ImageTk.PhotoImage(img)
            my_image_label_page2 = Label(image=my_image, bg=LIGHTEST_GREEN)
            my_image_label_page2.grid(column=0, columnspan=3, row=1, pady=(20, 0))

            back_button_img = ImageTk.PhotoImage(Image.open('images/button_back.png'))
            back_button_label = Label(image=back_button_img)
            back_button_page2 = Button(image=back_button_img, bg=LIGHTEST_GREEN, borderwidth=0, command=back_from_page2)
            back_button_page2.grid(column=0, row=0, padx=(0, 10))

            # Add text watermark button
            add_text_button_img = ImageTk.PhotoImage(Image.open('images/button_add-text.png'))
            add_text_button_label = Label(image=add_text_button_img)
            add_text_button_page2 = Button(image=add_text_button_img, bg=LIGHTEST_GREEN,
                                           borderwidth=0, command=add_wm_text)
            add_text_button_page2.grid(column=1, row=0, padx=(0, 0))

            # Add logo or image watermark button
            logo_button_img = ImageTk.PhotoImage(Image.open('images/button_add-logo.png'))
            logo_button_label = Label(image=logo_button_img)
            logo_button_page2 = Button(image=logo_button_img, bg=LIGHTEST_GREEN, borderwidth=0, command=add_image_wm)
            logo_button_page2.grid(column=2, row=0, padx=(0, 0))
            root.mainloop()

    logo_img = ImageTk.PhotoImage(file='images/VectorLogo.png')
    logo_img_label = Label(root, image=logo_img, bg=LIGHTEST_GREEN)
    logo_img_label.grid(column=1, row=0, pady=(0, 40), padx=(200, 0))

    # Home page text label
    text_label = Label(text="Add Watermark", fg=BEIGE, bg=LIGHTEST_GREEN, font=(FONT_NAME, 20))
    text_label.grid(column=1, row=1, pady=(150, 40), padx=(200, 0))

    # Home page select button
    button_img = PhotoImage(file='images/select_image.png')
    button_img_label = Label(image=button_img)
    select_button = Button(root, image=button_img, bg=LIGHTEST_GREEN, padx=20, borderwidth=0, command=page2)
    select_button.grid(column=1, row=2, pady=(10, 5), padx=(200, 0))

    root.mainloop()


page1()





















