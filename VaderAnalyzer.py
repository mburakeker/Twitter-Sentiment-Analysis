import pandas as pd
from nltk.tokenize import PunktSentenceTokenizer,sent_tokenize, word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords


def Analyze():
	sid = SentimentIntensityAnalyzer()
	translated_df = pd.read_csv("translated.csv").drop(['Unnamed: 0'],axis=1)
	textonly_df = pd.DataFrame(columns=["Text"])
	for i in translated_df.Metin:
		wordsToAppend = []
		for j in i.split(" "):
			if len(j) > 2 and (not j.startswith(("#","#","@","http","RT"))):
		    		wordsToAppend.append(j.strip())
		i = ""
		for x in wordsToAppend:
			i += x + " "
		textonly_df.loc[clen_df.shape[0]] = i

	stopWords = set(stopwords.words('english'))
	for i in translated_df.Metin.split():
		if (i.lower() not in stopWords):
			print(sid.polarity_scores(i)["pos"])	
