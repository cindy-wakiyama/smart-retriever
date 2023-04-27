from guizero import App, PushButton, Text, Box
from handleRequest import *

app = App(title="Smart Retriever", bg = "#fbe8a6")

title= Text(app, text="Smart Retriever", color="#303c6c")
 #font="Courier", size=20)
title.tk.config(font=("Courier", 20, "bold"))
#303c6c

#Retrieve
retrievelabel = Text(app, text="Press button to retrieve:", font="Courier")
retrievebox = Box(app, layout="grid")
#, bg = "#f4976c"
# retrievebox.bg = "#f4976c"
# retrievebox.text_color = "white"
retrieve1button = PushButton(retrievebox, command=retrieve1, text="1", grid=[1,1])
retrieve1button.bg = "#f4976c"
retrieve2button = PushButton(retrievebox, command=retrieve2, text="2", grid=[2,1])
retrieve2button.bg = "#f4976c"
retrieve3button = PushButton(retrievebox, command=retrieve3, text="3", grid=[3,1])
retrieve3button.bg = "#f4976c"
retrieve4button = PushButton(retrievebox, command=retrieve4, text="4", grid=[1,2])
retrieve4button.bg = "#f4976c"
retrieve5button = PushButton(retrievebox, command=retrieve5, text="5", grid=[2,2])
retrieve5button.bg = "#f4976c"
retrieve6button = PushButton(retrievebox, command=retrieve6, text="6", grid=[3,2])
retrieve6button.bg = "#f4976c"
retrieve7button = PushButton(retrievebox, command=retrieve7, text="7", grid=[1,3])
retrieve7button.bg = "#f4976c"
retrieve8button = PushButton(retrievebox, command=retrieve8, text="8", grid=[2,3])
retrieve8button.bg = "#f4976c"

#Return
retrievelabel = Text(app, text="Press button to return:", font="Courier")
returnbox = Box(app, layout="grid")
return1button = PushButton(returnbox, command=return1, text="1", grid=[1,1])
return1button.bg = "#f4976c"
return2button = PushButton(returnbox, command=return2, text="2", grid=[2,1])
return2button.bg = "#f4976c"
return3button = PushButton(returnbox, command=return3, text="3", grid=[3,1])
return3button.bg = "#f4976c"
return4button = PushButton(returnbox, command=return4, text="4", grid=[1,2])
return4button.bg = "#f4976c"
return5button = PushButton(returnbox, command=return5, text="5", grid=[2,2])
return5button.bg = "#f4976c"
return6button = PushButton(returnbox, command=return6, text="6", grid=[3,2])
return6button.bg = "#f4976c"
return7button = PushButton(returnbox, command=return7, text="7", grid=[1,3])
return7button.bg = "#f4976c"
return8button = PushButton(returnbox, command=return8, text="8", grid=[2,3])
return8button.bg = "#f4976c"

app.display()