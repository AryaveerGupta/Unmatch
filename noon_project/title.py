from  spacy.lang.en import English
import spacy as sp
nlp = sp.load("en_core_web_md")

doc1 = nlp("Generic Dancing cactus twisting music toy premium chargable green color for 2+ years age group kids")
doc2 = nlp("Dancing cactus plush stuffed toy with usb")

print(doc1.similarity(doc2)) 
