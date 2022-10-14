from tkinter import *
import wikipedia

root=Tk()

title_bar = Frame(root, bg="darkgreen", relief="raised", bd=1)
title_bar.pack(expand=1, fill=X)


def get_me():
    entry_value = entry.get()
    answer.delete(1.0, END)
    try:
        answer_value = wikipedia.summary(entry_value)
        answer.insert(INSERT, answer_value)
    except:
        answer.insert(INSERT, "please check you Query or internet connection Mr. razzaque!")

root = Tk()

root.title('Wikiepedia Searcher by quev')
root.geometry('350x200')
topframe = Frame(root)
entry = Entry(topframe)
entry.pack()
button = Button(topframe, text="Search Already!", command=get_me)
button.pack()
topframe.pack(side = TOP)

l = Label(root, text="Thank Queveryyy for this amazing tool!")
l.pack()



bottomframe = Frame(root)
scroll = Scrollbar(bottomframe)
scroll.pack(side=RIGHT, fill=Y)
answer =  Text(bottomframe, width=30, height=10, yscrollcommand = scroll.set, wrap=WORD)
scroll.config(command=answer.yview)
answer.pack()
bottomframe.pack()


root.mainloop()
