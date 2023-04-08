"""
8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. 
Write a function called send _messages () that prints each text message and moves each message 
to a new list called sent _messages as it's printed. 
After calling the function, print both of your lists to make sure the messages were moved correctly.
"""
def send_messages(unsend_messages, sended_messages):
    while unsend_messages:
        message = unsend_messages.pop()
        print(f"Sending message: {message}")
        sended_messages.append(message)

def show_messages(messages):
    print('\nThe following messages have been sended:')
    for message in messages:
        print(message)

text_messages = [
    'Hi, dont forget my money.',
    'I love Lionel Messi.',
    'I love Python.',
    'Python >>>>>>> C.',
    'Naah, just joking, C > Python.',
]

sended_messages = []

send_messages(text_messages, sended_messages)
show_messages(sended_messages)

print(f'unsend_messages list: {text_messages}')
print(f'sended messages list: {sended_messages}')