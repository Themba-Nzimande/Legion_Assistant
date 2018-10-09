import webbrowser
import wolframalpha
import wikipedia
import time
import os
from gtts import gTTS
import speech_recognition as sr
import pyperclip
#import tweepy as tp


def talkToMe(audio):
    print(audio)
    tts = gTTS(text=audio, lang='en')
    tts.save('audio.mp3')
    #os.system('mpg123 audio.mp3')
    browser_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(browser_path))
    webbrowser.get('chrome').open("audio.mp3")


cl = wolframalpha.Client('HE5HVG-RY4HA53WK4')
#att = cl.query('Test/Attempt')                                                                      #selecting ivona voice
r = sr.Recognizer()  # starting the speech_recognition recognizer
r.pause_threshold = 0.7  # it works with 1.2 as well
r.energy_threshold = 400
#to handle keyboard events
talkToMe('Hello"...')


print("For a list of commands, please say: 'keyword list'...")


#List of Available Commands

keywd = 'keyword list'
google = 'search for'
tweet = 'write a tweet'
slide_into_DM = 'Slide into'
acad = 'academic search'
sc = 'deep search'
wkp = 'wiki page for'
rdds = 'read this text'
sav = 'save this text'
bkmk = 'bookmark this page'
vid = 'video for'
wtis = 'what is'
wtar = 'what are'
whis = 'who is'
whws = 'who was'
when = 'when'
where = 'where'
how = 'how'
paint = 'open paint'
lsp = 'silence please'
lsc = 'resume listening'
stoplst = 'stop listening'



while True:  # The main loop

    with sr.Microphone() as source:

        try:

            # instantiating the Microphone, (timeout = None) can be an option
            audio = r.listen(source, timeout=None)
            message = str(r.recognize_google(audio))
            print('You said: ' + message)

            if google in message:  # what happens when google keyword is recognized

                words = message.split()
                del words[0:2]
                st = ' '.join(words)
                print('Google Results for: '+str(st.replace))
                url = 'http://google.com/search?q='+st
                #Broswer default
                browser_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
                webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(browser_path))
                webbrowser.get('chrome').open(url)
                talkToMe('Google Results for: '+str(st))

            elif tweet in message:
                #Had to create new instance of voice to text conversion because I couldnt piggy off the main one, its basically a sub command #what happens when tweet keyword is recognized
                TweetR = sr.Recognizer()
                talkToMe('What would you like to tweet')
                with sr.Microphone() as source:
                    #I'll put this in a function later
                    # Twitter API creds
                    # instantiating the Microphone, (timeout = None) can be an option
                    tweet_status = TweetR.listen(source, timeout=None)
                    actual_tweet = str(TweetR.recognize_google(tweet_status))
                    print(actual_tweet)
                    talkToMe(actual_tweet)
                    consumer_key = 'ca8rUBOtfMWzWij5A639Qsuhi'
                    consumer_secret = 'P3eo3oKdjzEAd0sOfxRzDZ7o40zbtna9U0PYPUEmv96Pbim5A7'
                    access_token = '957203182475759616-W0prNVQjitTr7WOTEtP7STrYJXwBKae'
                    access_secret = 'euGBXajTSEiVTuxnNxvFZRwoDLEg1bawjSa3bD8pyxqMI'

                    #Login in dat ish
                    # auth = tp.OAuthHandler(consumer_key, consumer_secret)
                    # auth.set_access_token(access_token, access_secret)
                    # api = tp.API(auth)
                    # words = message.split()
                    # del words[0:2]
                    # st = ' '.join(words)
                    #print('Academic Results for: '+str(st))
                    #url='https://scholar.google.ro/scholar?q='+st
                    #webbrowser.get('chrome').open(url)
                    #api.update_status(actual_tweet)

            elif acad in message:  # what happens when acad keyword is recognized

                words = message.split()
                del words[0:2]
                st = ' '.join(words)
                print('Academic Results for: '+str(st))
                url = 'https://scholar.google.ro/scholar?q='+st
                browser_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
                webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(browser_path))
                webbrowser.get('chrome').open(url)
                talkToMe('Academic Results for: '+str(st))

            elif wkp in message:  # what happens when wkp keyword is recognized

                try:

                    words = message.split()
                    del words[0:3]
                    st = ' '.join(words)
                    wkpres = wikipedia.summary(st, sentences=2)

                    try:

                        print('\n' + str(wkpres) + '\n')
                        talkToMe(wkpres)

                    except UnicodeEncodeError:
                        talkToMe(wkpres)

                except wikipedia.exceptions.DisambiguationError as e:
                    print(e.options)
                    talkToMe(
                        "Too many results for this keyword. Please be more specific and try again")
                    continue

                except wikipedia.exceptions.PageError as e:
                    print('The page does not exist')
                    talkToMe('The page does not exist')
                    continue

            elif sc in message:  # what happens when sc keyword is recognized

                try:
                    words = message.split()
                    del words[0:1]
                    st = ' '.join(words)
                    scq = cl.query(st)
                    sca = next(scq.results).text
                    print('The answer is: '+str(sca))
                    #url='http://www.wolframalpha.com/input/?i='+st
                    #webbrowser.get('chrome').open(url)
                    talkToMe('The answer is: '+str(sca))

                except StopIteration:
                    print('Your question is ambiguous. Please try again!')
                    talkToMe('Your question is ambiguous. Please try again!')

                else:
                    print('No query provided')

            elif paint in message:  # what happens when paint keyword is recognized
                os.system('mspaint')

            elif rdds in message:  # what happens when rdds keyword is recognized
                print("Reading your text")
                talkToMe(pyperclip.paste())

            elif sav in message:  # what happens when sav keyword is recognized
                with open('path to your text file', 'a') as f:
                    f.write(pyperclip.paste())
                print("Saving your text to file")
                talkToMe("Saving your text to file")

            elif bkmk in message:  # what happens when bkmk keyword is recognized
                # shell.SendKeys("^d")
                talkToMe("Page bookmarked")

            elif keywd in message:  # what happens when keywd keyword is recognized

                print('')
                print('Say ' + google + ' to return a Google search')
                print('Say ' + acad + ' to return a Google Scholar search')
                print('Say ' + sc + ' to return a Wolfram Alpha query')
                print('Say ' + wkp + ' to return a Wikipedia page')
                # print('Say ' + book + ' to return an Amazon book search')
                print(
                    'Say ' + rdds + ' to read the text you have highlighted and Ctrl+C (copied to clipboard)')
                print(
                    'Say ' + sav + ' to save the text you have highlighted and Ctrl+C-ed (copied to clipboard) to a file')
                print(
                    'Say ' + bkmk + ' to bookmark the page your are currently reading in your browser')
                print('Say ' + vid + ' to return video results for your query')
                print(
                    'For more general questions, ask them naturally and I will do my best to find a good answer')
                print('Say ' + stoplst + ' to shut down')
                print('')

            elif vid in message:  # what happens when vid keyword is recognized

                words = message.split()
                del words[0:2]
                st = ' '.join(words)
                print('Video Results for: '+str(st))
                url = 'https://www.youtube.com/results?search_query='+st
                browser_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
                webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(browser_path))
                webbrowser.get('chrome').open(url)
                talkToMe('Video Results for: '+str(st))

            elif wtis in message:  # what happens when wtis keyword is recognized

                try:

                    scq = cl.query(message)
                    sca = next(scq.results).text
                    print('The answer is: '+str(sca))
                    #url='http://www.wolframalpha.com/input/?i='+st
                    #webbrowser.get('chrome').open(url)
                    talkToMe('The answer is: '+str(sca))

                except UnicodeEncodeError:

                    talkToMe('The answer is: '+str(sca))

                except StopIteration:

                    words = message.split()
                    del words[0:2]
                    st = ' '.join(words)
                    print('Google Results for: '+str(st))
                    url = 'http://google.com/search?q='+st
                    browser_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
                    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(browser_path))
                    webbrowser.get('chrome').open(url)
                    talkToMe('Google Results for: '+str(st))

            elif wtar in message:  # what happens when wtar keyword is recognized

                try:

                    scq = cl.query(message)
                    sca = next(scq.results).text
                    print('The answer is: '+str(sca))
                    #url='http://www.wolframalpha.com/input/?i='+st
                    #webbrowser.get('chrome').open(url)
                    talkToMe('The answer is: '+str(sca))

                except UnicodeEncodeError:

                    talkToMe('The answer is: '+str(sca))

                except StopIteration:

                    words = message.split()
                    del words[0:2]
                    st = ' '.join(words)
                    print('Google Results for: '+str(st))
                    url = 'http://google.com/search?q='+st
                    browser_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
                    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(browser_path))
                    webbrowser.get('chrome').open(url)
                    talkToMe('Google Results for: '+str(st))

            elif whis in message:  # what happens when whis keyword is recognized

                try:

                    scq = cl.query(message)
                    sca = next(scq.results).text
                    print('\nThe answer is: '+str(sca)+'\n')
                    talkToMe('The answer is: '+str(sca))

                except StopIteration:

                    try:

                        words = message.split()
                        del words[0:2]
                        st = ' '.join(words)
                        wkpres = wikipedia.summary(st, sentences=2)
                        print('\n' + str(wkpres) + '\n')
                        talkToMe(wkpres)

                    
                    except:

                        words = message.split()
                        del words[0:2]
                        st = ' '.join(words)
                        print('Google Results (last exception) for: '+str(st))
                        url = 'http://google.com/search?q='+st
                        browser_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
                        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(browser_path))
                        webbrowser.get('chrome').open(url)
                        talkToMe('Google Results for: '+str(st))

            elif whws in message:  # what happens when whws keyword is recognized

                try:

                    scq = cl.query(message)
                    sca = next(scq.results).text
                    print('\nThe answer is: '+str(sca)+'\n')
                    talkToMe('The answer is: '+str(sca))

                except StopIteration:

                    try:

                        words = message.split()
                        del words[0:2]
                        st = ' '.join(words)
                        wkpres = wikipedia.summary(st, sentences=2)
                        print('\n' + str(wkpres) + '\n')
                        talkToMe(wkpres)

                    except UnicodeEncodeError:

                        talkToMe(wkpres)

                    except:

                        words = message.split()
                        del words[0:2]
                        st = ' '.join(words)
                        print('Google Results for: '+str(st))
                        url = 'http://google.com/search?q='+st
                        browser_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
                        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(browser_path))
                        webbrowser.get('chrome').open(url)
                        talkToMe('Google Results for: '+str(st))

            elif when in message:  # what happens when 'when' keyword is recognized

                try:

                    scq = cl.query(message)
                    sca = next(scq.results).text
                    print('\nThe answer is: '+str(sca)+'\n')
                    talkToMe('The answer is: '+str(sca))

                except UnicodeEncodeError:

                    talkToMe('The answer is: '+str(sca))

                except:

                    print('Google Results for: '+str(message))
                    url = 'http://google.com/search?q='+str(message)
                    browser_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
                    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(browser_path))
                    webbrowser.get('chrome').open(url)
                    talkToMe('Google Results for: '+str(message))

            elif where in message:  # what happens when 'where' keyword is recognized

                try:

                    scq = cl.query(message)
                    sca = next(scq.results).text
                    print('\nThe answer is: '+str(sca)+'\n')
                    talkToMe('The answer is: '+str(sca))

                except UnicodeEncodeError:

                    talkToMe('The answer is: '+str(sca))

                except:

                    print('Google Results for: '+str(message))
                    url = 'http://google.com/search?q='+str(message)
                    browser_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
                    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(browser_path))
                    webbrowser.get('chrome').open(url)
                    talkToMe('Google Results for: '+str(message))

            elif how in message:  # what happens when 'how' keyword is recognized

                try:

                    scq = cl.query(message)
                    sca = next(scq.results).text
                    print('\nThe answer is: '+str(sca)+'\n')
                    talkToMe('The answer is: '+str(sca))

                except UnicodeEncodeError:

                    talkToMe('The answer is: '+str(sca))

                except:

                    print('Google Results for: '+str(message))
                    url = 'http://google.com/search?q='+str(message)
                    browser_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
                    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(browser_path))
                    webbrowser.get('chrome').open(url)
                    talkToMe('Google Results for: '+str(message))

            elif stoplst in message:  # what happens when stoplst keyword is recognized
                talkToMe("I am shutting down")
                print("Shutting down...")
                break

            elif lsp in message:

                talkToMe('Listening is paused')
                print('Listening is paused')
                r2 = sr.Recognizer()
                r2.pause_threshold = 0.7
                r2.energy_threshold = 400

                while True:

                    with sr.Microphone() as source2:

                        try:

                            audio2 = r2.listen(source2, timeout=None)
                            message2 = str(r.recognize_google(audio2))

                            if lsc in message2:
                                talkToMe('I am listening')
                                break

                            else:
                                continue

                        except sr.UnknownValueError:
                            print(
                                "Listening is paused. Say resume listening when you're ready...")

                        except sr.RequestError:
                            talkToMe("I'm sorry, I couldn't reach google")
                            print("I'm sorry, I couldn't reach google")

            else:
                pass

        except sr.UnknownValueError:
            print("For a list of commands, say: 'keyword list'...")

        except sr.RequestError:
            talkToMe("I'm sorry, I couldn't reach google")
            print("I'm sorry, I couldn't reach google")

    time.sleep(0.3)
