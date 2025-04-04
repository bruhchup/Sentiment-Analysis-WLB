import matplotlib.pyplot as plt
from wordcloud import WordCloud

def generate_pie_chart(df):
    """Generate a pie chart showing sentiment distribution (for text analysis)."""
    counts = df['sentiment'].value_counts()
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90)
    ax.set_title("Sentiment Distribution")
    return fig

def generate_sentiment_pie_chart(df):
    """Generate a pie chart showing sentiment distribution based on numeric ratings."""
    sentiment_counts = df['rating_sentiment'].value_counts()
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=90)
    ax.set_title("Sentiment Distribution")
    return fig

def generate_scatter_plot(df):
    """Generate a scatter plot of polarity values (for text analysis) with axes switched."""
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.scatter(df['polarity'], range(len(df)), color='blue')
    ax.set_title("Polarity Scatter Plot")
    ax.set_xlabel("Polarity")
    ax.set_ylabel("Data Inputs")
    return fig

def generate_sentiment_scatter_plot(df):
    """Generate a scatter plot for numeric ratings
       x-axis: rating (1-5), y-axis: Inputs, colored by sentiment.
    """
    colors = {"Negative": "red", "Neutral": "gray", "Positive": "green"}
    df_filtered = df[df['numeric'].between(1, 5)]
    fig, ax = plt.subplots(figsize=(6, 4))
    x_values = df_filtered['numeric']
    y_values = df_filtered.index
    ax.scatter(x_values, y_values, c=df_filtered['rating_sentiment'].map(colors), s=20)
    ax.set_title("Scores Scatter Plot")
    ax.set_xlabel("Score")
    ax.set_ylabel("Data Inputs")
    ax.set_xticks([1, 2, 3, 4, 5])
    return fig

def generate_wordcloud(text, title):
    """Generate a word cloud figure from the provided text."""
    if not text.strip():
        text = "No data available."
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    ax.set_title(title)
    return fig
