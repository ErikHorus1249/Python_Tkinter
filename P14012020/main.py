import tkinter as tk
import time 
from functools import partial
from googletrans import Translator

def getText(input1):
    raw = input1.get()
    root1 = tk.Toplevel()
    root1.title("result")
    notify = tk.Label(root1)
    if raw != "":
        notify.config(text=raw, bg='green', fg="white")
    else:
        notify.config(text="text is empty !", bg="red")
    notify.pack()

def translate(label,input2):
    raw = input2.get()
    print(raw)
    translator = Translator()
    result = translator.translate(raw,src='en',dest='vi')
    raw =  result.text
    label.config(root, text=raw, bg="yellow",font="helvetica 14", wraplength=400)
    lable.pack()

def show_result(input3):
    root2 = tk.Toplevel()
    root2.title("ket qua")
    final_result = tk.Label(root2,text=input3, bg="yellow").pack()



# to set window for app use method Tk()
root = tk.Tk()
# to set title for windown use method has name is title 
root.title("Google translate")
root.geometry("500x500")
phara = tk.StringVar()
input_label = tk.Label(root,text="type your pharagraph !").pack()
text_input = tk.Entry(root, textvariable=phara, justify="center",width="100",cursor="hand2").pack()
result_label = tk.Label(root)
getText = partial(getText,phara)
translate = partial(translate,result_label,phara)
# show_result = partial(show_result,translate(phara))
submit  = tk.Button(root, text="submit",command=getText)
trans = tk.Button(root,text="translate", command=translate)
trans.pack()
print(phara)


root.mainloop()





