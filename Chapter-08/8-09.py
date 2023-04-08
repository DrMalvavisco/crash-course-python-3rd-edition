"""
8-9. Messages: Make a list containing a series of short text messages. 
Pass the list to a function called show_messages (), which prints each text message.
"""

def show_messages(messages):
    for message in messages:
        print(message)

text_messages = [
    'Hi, dont forget my money.',
    'I love Lionel Messi.',
    'I love Python.',
    'Python >>>>>>> C.',
    'Naah, just joking, C > Python.',
]
show_messages(text_messages)

