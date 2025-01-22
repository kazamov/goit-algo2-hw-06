import requests
import matplotlib.pyplot as plt
from map_reduce import map_reduce

def get_text(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        return None
    
def get_top_words(result, top=10):
    sorted_result = sorted(result.items(), key=lambda x: x[1], reverse=True)
    return sorted_result[:top]
    
def visualize_top_words(word_counts):
    words = [item[0] for item in word_counts]
    counts = [item[1] for item in word_counts]
    plt.figure(figsize=(10, 6))
    plt.barh(words, counts, color='blue')
    plt.gca().invert_yaxis()
    plt.xlabel("Frequency")
    plt.ylabel("Words")
    plt.title("Top Words")
    plt.tight_layout()
    plt.show(block=True)

if __name__ == "__main__":
    url = "https://gutenberg.net.au/ebooks01/0100021.txt"
    text = get_text(url)
    if text:
        result = map_reduce(text)
        top_words = get_top_words(result)
        visualize_top_words(top_words)
    else:
        print("Помилка: Не вдалося отримати вхідний текст.")