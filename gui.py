from guizero import *
from handleRequest import *

def check_input():
    if user_input.value in list_items:
      reply.value = "Item is in list!"
      successful_reply.value = "Retrieving item..."
      # add function to retrive item by moving motors
    else:
      reply.value = "Item is not in list, please try again"
      successful_reply.value = ""

def open_new_item_window():
  window.show()

def close_new_item_window():
  window.hide()

app = App(title="Smart Retriever")

window = Window(app, title="Insert New Item")
window.hide()


#list_items = ["item1", "item2", "item3", "item4", "item5", "item6", "item7", "item8"]

title = Text(app, text="Smart Retriever", size=20)

intro = Text(app, text="Please type item to retrieve")

list_box = ListBox(app, items=inventory)

user_input = TextBox(app)

submit_button = PushButton(app, text="Submit", command=check_input)

reply = Text(app)

successful_reply = Text(app)


new_item_button = PushButton(app, text="Insert New Item", command=open_new_item_window)

close_new_item_window_btn = PushButton(window, text="Close", command=close_new_item_window)




app.display()