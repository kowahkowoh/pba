#import
print('4')
import nltk
import random
import string
import time
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import telegram

from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater,CommandHandler, MessageHandler, Filters,ConversationHandler)



#tokenisasi
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]


#normalisasi
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


#sapaan
def greeting(sentence):
    triggersapa = ["hello", "hi", "greetings", "sup", "what's up","hey", "hai"]
    GREETING_RESPONSES = ["Hi", "Hey", "*senyum* Iya ada apa?", "Hello", "Ada apa bre?"]
    for word in sentence.split():
        if word.lower() in triggersapa:
            return random.choice(GREETING_RESPONSES)


#respons
def response(inputan):
    respon=''
    
    #prosesing masih belum bagusp
    sent_tokens.append(inputan)
    
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize)
    
    tfidf = TfidfVec.fit_transform(sent_tokens)
    
    vals = cosine_similarity(tfidf[-1], tfidf)
    
    idx=vals.argsort()[0][-2]
    
    flat = vals.flatten()
    
    flat.sort()
    
    req_tfidf = flat[-2]
    
    #time.sleep(50)

    if(req_tfidf<0.2):
        respon=respon+"Maaf saya tidak mengenali kalimat anda"
        print('a')
        return respon
    else:
        respon = respon+sent_tokens[idx]
        print('b')
        return respon


update_id = None


def main():
    """Run the bot."""
    global update_id
    # Telegram Bot Authorization Token
    bot = telegram.Bot("1269345611:AAHjqM7rkHOZ5KUZiRLMxdYlwwh9pb4w2NI")

    
    
    try:
        update_id = bot.get_updates()[0].update_id
    except:
        update_id = None
    
    print('1')

    
    while True:
        try:
            echo(bot)
        except:
            time.sleep(1)


def echo(bot):
    global update_id
    # Request updates after the last update_id
    for update in bot.get_updates(offset=update_id, timeout=10):
        update_id = update.update_id + 1
        

        if update.message:  
            # Reply to the message
            print(update.message.text)
            
            inputan = update.message.text.lower()
            if True:
            	if inputan == 'thanks' or inputan == 'thank you' or inputan == 'terima kasih':
            		update.message.reply_text('sama sama')
            	elif inputan == 'help':
            		update.message.reply_text("Nama saya Covidbot. Saya akan mencoba menjawab pertanyaan kamu seputar COVID-19. ")
            		
            	elif inputan == 'dimana pia tinggal?':
            		update.message.reply_text("Kayangan kata dia")
            	
            	elif inputan == 'disana minum apa?':
            		update.message.reply_text("air suci")
            	
            	
            	elif inputan == 'emang disana ada gereja?':
            		update.message.reply_text("eh ... masa kubilang air zam-zam")
            		
            	else:
            		if greeting(inputan)!=None:
            			update.message.reply_text(greeting(inputan))
            		else:
            			update.message.reply_text(response(inputan))
            			sent_tokens.remove(inputan)
            
        

if __name__ == "__main__":
	
	print('3')
	#open corpus
	f=open('covid19corpus.txt','r')
	raw=f.read()
	#print(raw)

	#normalisasi ke bentuk huruf kecil
	raw=raw.lower()

	#nltk.download('punkt') # first-time use only
	#nltk.download('wordnet') # first-time use only

	#tokenisasi per kalimat
	sent_tokens = nltk.sent_tokenize(raw)
	

	#tokenisasi per kata
	word_tokens = nltk.word_tokenize(raw)

	#pelemmatisasi
	lemmer = nltk.stem.WordNetLemmatizer()
	

	remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
	print('2')
	
	
	main()
