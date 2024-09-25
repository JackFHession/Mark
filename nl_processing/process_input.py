from sheilai import *

# start sheila instances

Sheila = sheil_ai("./nl_processing/data.pth")

Sheila.set_intents("./nl_processing/intents.json")
Sheila.set_data("./nl_processing/data.pth")

def classify(UserInput):
    intent_class = Sheila.classify(UserInput)
    return intent_class

# do the key-word detector

def detect_keywords(UserInput):
    #if word(s) in UserInput, etc:
    return UserInput
    #else:
    intent_class = classify(UserInput)
    return intent_class

#

# Remember future jack. Keyword detection to always be done BEFORE classification.