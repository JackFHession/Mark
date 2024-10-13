from utils.functions import *
from nl_processing.process_input import *
from gui import *

def local_main():
    UserInput = input("You: ")
    display_face(thinking)
    intent_class = classify(UserInput)
    display_face(smile)
    print(intent_class)

if __name__ == "__main__":
    local_main()