prompt = "\nPlease enter the materials of pizza:"
prompt += "\nEnter 'quit' when you are finished."
message = ''
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)