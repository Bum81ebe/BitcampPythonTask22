##
import emoji

#question = str(input("Tell me an emoji text "))

question = input("Input: ")
print(emoji.emojize("Output:" + question, language='alias'))