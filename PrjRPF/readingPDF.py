#include thu vien
import pyttsx3
import PyPDF2

#open & reading file
book = open("E:/PYProject/PrjRPF/readpdf.pdf","rb")
pdfReader = PyPDF2.PdfReader(book)
page = len(pdfReader.pages)

print(page)

#khoi tao tai nguyen cho thu vien pyttsx3 
bot = pyttsx3.init()

#make voice and change to women voice
voices= bot.getProperty('voices')
bot.setProperty('voice', voices[1].id)

#chon va trich xuat van ban
page = pdfReader.pages[0]
text = page.extract_text()

#Doc van ban
bot.say(text)

#reading file convert text to speech
bot.runAndWait()
