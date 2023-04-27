from guizero import App, PushButton
from handleRequest import *

app = App(title="Smart Retriever", layout="grid")

# retrieve = PushButton(app, text="Retrieve Item", command=)

retrieve1button = PushButton(app, command=retrieve1, text="1", grid=[1,1])
retrieve2button = PushButton(app, command=retrieve2, text="2", grid=[2,1])
retrieve3button = PushButton(app, command=retrieve3, text="3", grid=[3,1])
retrieve4button = PushButton(app, command=retrieve4, text="4", grid=[1,2])
retrieve5button = PushButton(app, command=retrieve5, text="5", grid=[2,2])
retrieve6button = PushButton(app, command=retrieve6, text="6", grid=[3,2])
retrieve7button = PushButton(app, command=retrieve7, text="7", grid=[1,3])
retrieve8button = PushButton(app, command=retrieve8, text="8", grid=[2,3])


return1button = PushButton(app, command=return1, text="1", grid=[1,5])
return2button = PushButton(app, command=return2, text="2", grid=[2,5])
return3button = PushButton(app, command=return3, text="3", grid=[3,5])
return4button = PushButton(app, command=return4, text="4", grid=[1,6])
return5button = PushButton(app, command=return5, text="5", grid=[2,6])
return6button = PushButton(app, command=return6, text="6", grid=[3,6])
return7button = PushButton(app, command=return7, text="7", grid=[1,7])
return8button = PushButton(app, command=return8, text="8", grid=[2,7])

app.display()