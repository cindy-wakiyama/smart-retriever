from guizero import App, PushButton, Waffle
from handleRequest import *

app = App(title="Smart Retriever")

# retrieve = PushButton(app, text="Retrieve Item", command=)

retrieve1button = PushButton(app, command=retrieve1, text="1")
retrieve2button = PushButton(app, command=retrieve2, text="2")
retrieve3button = PushButton(app, command=retrieve3, text="3")
retrieve4button = PushButton(app, command=retrieve4, text="4")
retrieve5button = PushButton(app, command=retrieve5, text="5")
retrieve6button = PushButton(app, command=retrieve6, text="6")
retrieve7button = PushButton(app, command=retrieve7, text="7")
retrieve8button = PushButton(app, command=retrieve8, text="8")


return1button = PushButton(app, command=return1, text="1")
return2button = PushButton(app, command=return2, text="2")
return3button = PushButton(app, command=return3, text="3")
return4button = PushButton(app, command=return4, text="4")
return5button = PushButton(app, command=return5, text="5")
return6button = PushButton(app, command=return6, text="6")
return7button = PushButton(app, command=return7, text="7")
return8button = PushButton(app, command=return8, text="8")


# waffle = Waffle(app)

# waffle2 = Waffle(app)

app.display()