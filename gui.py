from guizero import App, PushButton, Text, Box
from handleRequest import *

app = App(title="Smart Retriever")

# title= Text(app, text="Smart Retriever", grid=[0,0,3,0])

#Retrieve
retrievelabel = Text(app, text="Press button to retrieve:")
retrivebox = Box(app, layout="grid")
retrieve1button = PushButton(retrivebox, command=retrieve1, text="1", grid=[1,1])
retrieve2button = PushButton(retrivebox, command=retrieve2, text="2", grid=[2,1])
retrieve3button = PushButton(retrivebox, command=retrieve3, text="3", grid=[3,1])
retrieve4button = PushButton(retrivebox, command=retrieve4, text="4", grid=[1,2])
retrieve5button = PushButton(retrivebox, command=retrieve5, text="5", grid=[2,2])
retrieve6button = PushButton(retrivebox, command=retrieve6, text="6", grid=[3,2])
retrieve7button = PushButton(retrivebox, command=retrieve7, text="7", grid=[1,3])
retrieve8button = PushButton(retrivebox, command=retrieve8, text="8", grid=[2,3])

#Return
retrievelabel = Text(app, text="Press button to return:")
returnbox = Box(app, layout="grid")
return1button = PushButton(returnbox, command=return1, text="1", grid=[1,1])
return2button = PushButton(returnbox, command=return2, text="2", grid=[2,1])
return3button = PushButton(returnbox, command=return3, text="3", grid=[3,1])
return4button = PushButton(returnbox, command=return4, text="4", grid=[1,2])
return5button = PushButton(returnbox, command=return5, text="5", grid=[2,2])
return6button = PushButton(returnbox, command=return6, text="6", grid=[3,2])
return7button = PushButton(returnbox, command=return7, text="7", grid=[1,3])
return8button = PushButton(returnbox, command=return8, text="8", grid=[2,3])

app.display()