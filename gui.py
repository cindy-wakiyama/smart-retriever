from guizero import App, PushButton, Waffle
import handleRequest

app = App(title="Smart Retriever")

# retrieve = PushButton(app, text="Retrieve Item", command=)

waffle = Waffle(app)

waffle2 = Waffle(app)

app.display()