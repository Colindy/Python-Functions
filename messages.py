"""Making a function to handle lists"""

 

def show_messages(messages):

                #print the message out from a list

                for message in messages:

                                print(message)

                print("\n")

 

 

def send_messages(messages):

    #This function simulates the sending of the message

    while messages:

        sent = messages.pop()

        print(f'Sending "{sent}"')

        messagestx.append(sent)

    print("\n")

 

"""Here we have our two lists"""

messages = ['Hi there', 'New message', 'Go Colts!']

messagestx = []

 

"""

Here we call the functions.  We use '[:]' to represent making a copy of ths list in the send_messages() function.

This is normally done if an archive needs to be kept of the original list

"""

show_messages(messages)

send_messages(messages[:])

 

# Now going to print both lists to make sure they moved correctly and the [:] archived the original list correctly

print(messages)

print(messagestx)


"""
Interesting bit, I did this one at work and had to email myself the raw code.
This extra space between each line makes it a bit more readable but I don't expect them to all be this way.
"""