from gtts import gTTS 
import wikipedia as wiki

# wiki
query = input("wiki what\n")
result = wiki.page(title=query)
print("Got " + result.title + ", now encoding")

# gtts
tts = gTTS(text=result.summary,lang='en-au')
tts.save(result.title +'.mp3')