reviews = ["Good coffee", "very GOOD tea", "good food and good coffee", "Tea is very hot"]
def count_words(text):
    counts={}
    words=text.lower().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts
all_text=" ".join(reviews)
counts=count_words(all_text)
for word, count in counts.items():
    if count>=2:
        print(f"{word} : {count}")
best=None
best_count=0
for word, count in counts.items():
    if count>best_count:
        best=word
        best_count=count
print(f"Most common: {best} ({best_count})")
