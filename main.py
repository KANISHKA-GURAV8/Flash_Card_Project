from tkinter import *


BACKGROUND_COLOR = "#B1DDC6"
#----random words generator---------#
import pandas
import random
random_word = {}
word_list={}

try:
  data=pandas.read_csv('data/words_to_learn.csv')

except FileNotFoundError:
     original_data=pandas.read_csv('data/french_words.csv')
     word_list=original_data.to_dict(orient='records')
else:
     word_list = data.to_dict(orient="records")  # converts dataframe to dictionary



def random_w():
     global random_word
     global flip_timer
     window.after_cancel(flip_timer)
     random_word=random.choice(word_list)
     french_word = random_word["French"]
     # main_word=canvas.create_text(400, 150, text=french_word, fill='black', font=('Ariel', 40, 'italic'))
     canvas.itemconfig(main_text,text='French',fill='black')
     canvas.itemconfig(sub_text, text=french_word,fill='black')
     canvas.itemconfig(canvas_image, image=old_card_f)
     flip_timer=window.after(3000, func=flipcard)


def is_known():
     word_list.remove(random_word)
     data=pandas.DataFrame(word_list)
     data.to_csv('data/words_to_learn.csv',index=False)
     random_w()




#----flip card---#
def flipcard():
     canvas.itemconfig(main_text,text='English',fill='white')
     canvas.itemconfig(sub_text,text=random_word['English'],fill='white')
     # to change image
     canvas.itemconfig(canvas_image, image=new_card_f)


# ------UI Setup----------#
window=Tk()
window.title('flashy')
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer=window.after(3000,func=flipcard)

canvas=Canvas(width=800, height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
old_card_f=PhotoImage(file='images/card_front.png')
new_card_f=PhotoImage(file='images/card_back.png')
canvas_image=canvas.create_image(400,263,image=old_card_f)
main_text=canvas.create_text(400,150,text='',fill='black',font=('Ariel',40,'italic'))
sub_text=canvas.create_text(400,263,text='',fill='black',font=('Ariel',40,'bold'))

canvas.grid(row=0,column=0,columnspan=2)


right=PhotoImage(file='images/right.png')
right_button = Button(image=right, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0,command=is_known)
right_button.grid(row=1,column=1)

wrong=PhotoImage(file='images/wrong.png')
wrong_b=Button(image=wrong,highlightthickness=0,bg=BACKGROUND_COLOR,borderwidth=0,command=random_w)
wrong_b.grid(row=1,column=0)

random_w()

window.mainloop()
# path/to/image_file.png