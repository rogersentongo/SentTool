from textblob import TextBlob, Word
from textblob.wordnet import VERB
from newsapi import NewsApiClient
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from collections import OrderedDict


newsapi = NewsApiClient(api_key='Insert your key here')

top10 = pd.read_csv('Top10.csv', index_col=0)
bottom10 = pd.read_csv('Bottom10.csv', index_col=0)

#datetime variables
datetime_now = datetime.now()
threedays_ago = datetime_now - timedelta(30)
end_date = datetime_now.strftime('%Y-%m-%d')
begin_date = threedays_ago.strftime('%Y-%m-%d')

top10_list =top10['Ticker'].tolist()
bottom10_list = bottom10['Ticker'].tolist()

top10_dict = OrderedDict((el,0) for el in top10_list)
bottom10_dict = OrderedDict((el,0) for el in bottom10_list)

top10_dict1 = OrderedDict((el,0) for el in top10_list)
bottom10_dict1 = OrderedDict((el,0) for el in bottom10_list)


for item, b in top10_dict.items():
        print("""Part 1""")
        print(item)
        print()
        print()
        all_articles = newsapi.get_everything(q=item,
                                              sources= 'google-news, associated-press, financial-post, financial-times, the-verge, yahoo, Reuters, cnbc, the-economist, bloomberg',
                                              domains='reuters.com, yahoonews.com, bloomberg.com, stocknewstimes.com, investorplace.com',
                                              from_parameter=begin_date,
                                              to=end_date,
                                              language='en',
                                              sort_by='relevancy')

        #Picks out the second key of the dictionary
        #The articles key points to a list of articles
        all_articles = all_articles['articles']
        if not all_articles:
            print("This stock has no news")
            top10_dict[item] = 'Neutral'
            continue


        description = []

        print("""Part 2""")
        for a in all_articles:
            #Loads dictionary into variable
            b = a['description']
            description.append(b)

        print(description)
        print()
        print()

        print("""Part 3""")
        dp = pd.DataFrame(description, columns = ['Text'])
        print(dp['Text'])
        print()

        #dp = dp[(dp['Text'].str.contains(item))]

        print("""Part 4""")
        sentlist = dp['Text'].tolist()
        sentlist = filter(None, sentlist)
        # print(sentlist)
        # print()
        # print(sentopt)
        # print()
        # print()

        # print("""Part 5""")
        # for text in sentlist:
        #
        #     #Creates a textblob object of the sentence
        #     blob = TextBlob(text)
        #     print(type(blob.sentences))
        #     print()
        #     print()

        polarity = []

        print("""Part 6""")
        for text in sentlist:
            #Creates a textblob object of the sentence
            blob = TextBlob(text)

            for sentence in blob.sentences:
                print(sentence)
                print()
                b = sentence.sentiment.polarity
                print(b)
                polarity.append(b)

        try:
            average_polarity1 = sum(polarity)/len(polarity)
        except ZeroDivisionError:
            average_polarity1 = 0.0
        print('The sentiment for '+item+' is '+str(average_polarity1))

        if -1.0 == average_polarity1:
            average_polarity = 'Very Negative'
        elif -1.0 < average_polarity1 <0.0:
            average_polarity = 'Negative'
        elif average_polarity1 == 0.0:
            average_polarity = 'Neutral'
        elif 0.0 < average_polarity1 <1.0:
            average_polarity = 'Positive'
        elif average_polarity1 ==1.0:
            average_polarity = 'Very Positive'

        top10_dict[item] = average_polarity
        top10_dict1[item] = average_polarity1

for item, b in bottom10_dict.items():
        if item == 'MO':
            bottom10_dict[item] = 'Neutral'
            continue
        all_articles = newsapi.get_everything(q=item,
                                              sources= 'google-news, associated-press, financial-post, financial-times, the-verge, yahoo, Reuters, cnbc, the-economist, bloomberg',
                                              domains='reuters.com, yahoonews.com, bloomberg.com, stocknewstimes.com, investorplace.com',
                                              from_parameter=begin_date,
                                              to=end_date,
                                              language='en',
                                              sort_by='relevancy')

        #Picks out the second key of the dictionary
        #The articles key points to a list of articles
        all_articles = all_articles['articles']
        if not all_articles:
            print("This stock has no news")
            bottom10_dict[item] = 'Neutral'
            continue


        description = []

        for a in all_articles:
            #Loads dictionary into variable
            b = a['description']
            description.append(b)

        print(description)

        dp = pd.DataFrame(description, columns = ['Text'])
#         print(dp['Text'])

        #dp = dp[(dp['Text'].str.contains(item))]

        sentlist = dp['Text'].tolist()
        sentlist = filter(None, sentlist)
        # print(sentlist)
        # print()
        # print(sentopt)

        for text in sentlist:

            #Creates a textblob object of the sentence
            blob = TextBlob(text)
#             print(type(blob.sentences))
#             print()
#             print()

        polarity = []


        for text in sentlist:
            #Creates a textblob object of the sentence
            try:
                blob = TextBlob(text)
            except:
                continue

            for sentence in blob.sentences:
#                 print(sentence)
#                 print()
                b = sentence.sentiment.polarity
                print(b)
                polarity.append(b)

        try:
            average_polarity1 = sum(polarity)/len(polarity)
        except ZeroDivisionError:
            average_polarity1 = 0.0
        print('The sentiment for '+item+' is '+str(average_polarity1))

        if -1.0 == average_polarity1:
            average_polarity = 'Extremely Negative'
        elif -1.0 < average_polarity1 <= -0.5:
            average_polarity = 'Very Negative'
        elif -0.5 < average_polarity1 <0:
            average_polarity = 'Negative'
        elif average_polarity1 == 0.0:
            average_polarity = 'Neutral'
        elif 0.0 < average_polarity1 <=0.5:
            average_polarity = 'Positive'
        elif 0.5 < average_polarity1 <1.0:
            average_polarity = 'Very Positive'
        elif average_polarity1 ==1.0:
            average_polarity = 'Extremely Positive'

        print()
        bottom10_dict[item] = average_polarity
        bottom10_dict1[item] = average_polarity1

sent1 = list(top10_dict.values())
sent1 = pd.DataFrame(sent1)
print(sent1)

sent2 = list(bottom10_dict.values())
sent2 = pd.DataFrame(sent2)
print(sent2)

sent3 = list(top10_dict1.values())
sent3 = pd.DataFrame(sent3)
print(sent1)

sent4 = list(bottom10_dict1.values())
sent4 = pd.DataFrame(sent3)
print(sent2)

top10_stocks = top10.join(sent1)
bottom10_stocks = bottom10.join(sent2)


top10_stocks= top10_stocks.rename(columns={0:'Sentiment'})
bottom10_stocks=bottom10_stocks.rename(columns={0:'Sentiment'})

top10_stocks = top10_stocks.join(sent3)
bottom10_stocks = bottom10_stocks.join(sent4)

top10_stocks= top10_stocks.rename(columns={0:'Polarity'})
bottom10_stocks=bottom10_stocks.rename(columns={0:'Polarity'})

top10_stocks = top10_stocks.round({'Polarity': 3})
bottom10_stocks = bottom10_stocks.round({'Polarity': 3})

# colname = Top10.columns[1]
# top10_stocks = top10_stocks.round({colname: 2})
# bottom10_stocks = bottom10_stocks.round({colname: 2})

top10_stocks.to_csv('finaltop10.csv')
bottom10_stocks.to_csv('finalbottom10.csv')
