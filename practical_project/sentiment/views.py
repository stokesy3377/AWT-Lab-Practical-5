from django.shortcuts import render
from .forms import SentimentForm
from textblob import TextBlob

def analyze_sentiment(request):
    result = None
    if request.method == 'POST':
        form = SentimentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            blob = TextBlob(text)
            polarity = blob.sentiment.polarity
            if polarity > 0.1:
                result = "Positive"
            elif polarity < -0.1:
                result = "Negative"
            else:
                result = "Neutral"
    else:
        form = SentimentForm()
    return render(request, 'sentiment/analyze.html', {'form': form, 'result': result})
