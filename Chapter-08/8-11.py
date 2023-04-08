"""
8-11. Archived Messages: Start with your work from Exercise 8-10. 
Call the function send_mes-sages () with a copy of the list of messages. 
After calling the function, print both of your lists to show that 
the original list has retained its messages.
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

send_messages(text_messages.copy(), sended_messages)
show_messages(sended_messages)

print(f'unsend_messages list: {text_messages}')
print(f'sended messages list: {sended_messages}')

