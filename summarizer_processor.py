import urllib.request 
import pickle


# def summarizeFromContent(content):
#     to_tokenize = content
#     summarizer = pipeline("summarization", model="t5-small")
#     summary = summarizer(to_tokenize, min_length=75, max_length=1000)
#     summaryText = summary[0].get("summary_text") if len(summary)>0  else ''
#     return summaryText.capitalize();


# def summarizeFromURL(url):
#     article_content = fetchDataFromUrl(url)
#     summary = summarizeFromContent(article_content)
#     return summary

def fetchDataFromUrl(url):
    # fetch
    fetched_data = urllib.request.urlopen(url)
    article_read = fetched_data.read()

    # parse
    article_parsed = BeautifulSoup.BeautifulSoup(article_read,'html.parser')
    paragraphs = article_parsed.find_all('p')

    #populate
    article_content = ''
    for p in paragraphs:  
        article_content += p.text
    return article_content

