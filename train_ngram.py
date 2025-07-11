import pickle
from collections import defaultdict, Counter

# Load and preprocess data
with open("data.txt", "r", encoding="utf8") as f:
    text = f.read().lower().replace('\n', ' ').split()

# Build trigram dictionary
trigrams = defaultdict(Counter)
for i in range(len(text) - 3):
    key = tuple(text[i:i+3])  # 3-word input
    next_word = text[i+3]     # predicted word
    trigrams[key][next_word] += 1

# Save trigram model
with open("trigram_model.pkl", "wb") as f:
    pickle.dump(trigrams, f)

print("✅ Trigram model trained and saved as trigram_model.pkl")
