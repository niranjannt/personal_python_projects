
# import required modules
from googletrans import Translator

translator = Translator()

translate_text=input("What do you want to translate?")
input_language=input("What language do you want to translate from?")
output_language=input("What is the output language?")

translate_text = translator.translate(translate_text, src=input_language, dest=output_language)
print(translate_text)
