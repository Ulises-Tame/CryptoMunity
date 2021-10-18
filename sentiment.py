from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

key = "6ee8a38b9dfa405a848603f871fcacda"
endpoint = "https://analyticsjdrt.cognitiveservices.azure.com/"
def get_authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, 
            credential=ta_credential)
    return text_analytics_client

client = get_authenticate_client()

def sentiment_analysis(client, frase):
    documents = [frase]
    response = client.analyze_sentiment(documents=documents)[0]
    sentiment = response.sentiment
    #print(sentiment)
    overall = ("Overall scores: positive={0:.2f}; neutral={1:.2f}; negative={2:.2f} \n".format(
        response.confidence_scores.positive,
        response.confidence_scores.neutral,
        response.confidence_scores.negative,
    ))
    return sentiment
    #print(overall)
    #for idx, sentence in enumerate(response.sentences):
     #   print("Sentence: {}".format(sentence.text))
      #  print("Sentence {} sentiment: {}".format(idx+1, sentence.sentiment))
      #  print("Sentence score:\nPositive={0:.2f}\nNeutral={1:.2f}\nNegative={2:.2f}\n".format(
        #    sentence.confidence_scores.positive,
         #   sentence.confidence_scores.neutral,
          #  sentence.confidence_scores.negative,
        #))
          
#sentiment_analysis(client)