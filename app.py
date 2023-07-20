import streamlit as st
import spacy_streamlit as spt
import spacy
import nltk
nlp=spacy.load('en_core_web_sm')
def main():
	st.write('### Name Entity Recongnization App')
	menu=['Home','NER']
	choice=st.sidebar.selectbox('menu',menu)
	if choice =="Home":
		st.subheader('Word Tokenization')
		raw_text=st.text_area('Text to Tokenize','Enter Text Here')
		docs=nlp(raw_text)
		if st.button('Tokenize'):
			spt.visualize_tokens(docs)
	
	elif choice=='NER':
		st.subheader('Name Entity Recongnization')
		raw_text=st.text_area('Text to Tokenize','Enter Text Here')
		docs=nlp(raw_text)
		spt.visualize_ner(docs)

	else:
		pass




if __name__=='__main__':
	main()







