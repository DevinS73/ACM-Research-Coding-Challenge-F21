
from afinn import Afinn
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from time import sleep
"""
Solutions 1 and 2 found from an article on sentiment analysis here: https://nealcaren.org/lessons/wordlists/
More info on the tools themselves can be found here
Afinn: https://github.com/fnielsen/afinn
vader: https://github.com/cjhutto/vaderSentiment
"""
def solution1():
  afinn = Afinn(language='en')
  file=open("input.txt","r")
  fileText=file.read()
  wordCount=len(fileText.strip().split())
  print("Afinn score: "+str(afinn.score(fileText)))
  print("Average sentiment: "+str(afinn.score(fileText)/wordCount))
  print("\nAfinn is a word list developed by Finn Årup Nielsen,")
  print("it contains 2500 words, each assigned a value between -5 and 5.")
  print("Sentiment analysis using this provides a simple sum, which")
  print("can be good for straightforward shorter texts or reviews, but can")
  print("be less relaible for longer texts or those with compound statements, negatives, or modifiers")
  print("\nThis rating of the text shows it to have a somewhat positive sentiment,")
  print("which makes sense, as the first paragraph has a more negative sentiment of an ")
  print("argument, while the second seems more positive.")
  print("Also given is the average sentiment, but this may be flawed as many of the")
  print("words and names may not have been included in the list.")

def solution2():
  analyzer = SentimentIntensityAnalyzer()
  file=open("input.txt","r")
  fileText=file.read()
  print(analyzer.polarity_scores(fileText))
  print("\n VADER (Valence Aware Dictionary and sEntiment Reasoner) was developed by")
  print("C.J. Hutto and Eric Gilbert at the Georgia Institute of Technology, primarily")
  print("for sentiment analysis in social media texts.")
  print("The first three values are the proportions of the text that are negative, neutral")
  print("or positive. Compound indicates a normalized and weighted score for the overall text sentiment.")
  print("This method takes into account a few more rules, such as punctuation emphasis,")
  print("degree modifiers, and contractions.")
  print("\nWhile this model identified most of the words used as neutral, the compound")
  print("score was overwhelmingly positive (.9978 out of a maximum of 1).")
  print("This second paragraph is positive, and while the first could be construed as positive")
  print("as the argument is more playful, it's difficult to say if this or the use of")
  print("exclamation points, typically more positive in social media posts, is the reason for this score.")
def additionalSolutions():
  print("Other solutions for this problem could use supervised machine learning")
  print("with similar texts, such as longer length texts or those from a similar genre.")
  print("More complicated models could consider the sincerity of parts of a text, ")
  print("break up sentiment by characters and/or narrator, or take into consideration")
  print("the time period/author of a piece to consider how sentiment of words could ")
  print("change depending on the context.")

def main():
  print("Welcome to sentiment analyzer!")
  choice=""
  while(choice!="4"):
    if choice!="":
      sleep(10)
      print("\n"*10)
    print("1. Afinn solution")
    print("2. VADER solution")
    print("3. Ideas for other solutions")
    print("4. Quit")
    choice=input(">> ")
    if choice=="1":
      solution1()
    if choice=="2":
      solution2()
    if choice=="3":
      additionalSolutions()
  print("Thank you for using sentiment analyzer!")
if __name__=="__main__":
  main()