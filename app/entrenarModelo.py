import spacy
import PyPDF2

nlp = spacy.load("en_core_web_sm")
pdfFileObj = open('/Users/cristiansoriaguilera/Documents/vamos/app/gemini.pdf', 'rb') 
    
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
    
# printing number of pages in pdf file 
print(pdfReader.numPages) 
    
# creating a page object 
temporal1=0
temporal=""
while temporal1 < pdfReader.numPages:
    pageObj = pdfReader.getPage(temporal1) 
    temporal= temporal + " " + pageObj.extractText()
    temporal1=temporal1+1


    
# extracting text from page 



text=temporal 
    
# closing the pdf file object 
pdfFileObj.close() 
corpus = []

doc = nlp(text)

nlp = spacy.blank("en")
TRAIN_DATA =[]

for ent in doc.ents:
    TRAIN_DATA.append([{"entities": ent}])
print (TRAIN_DATA)