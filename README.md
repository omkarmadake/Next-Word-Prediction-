# 🧠 N-gram Next Word Prediction

A simple Python-based next word prediction system using **N-gram modeling** (bigram/trigram). This project uses a small corpus to predict the most likely next word based on the previous 2 words.

---

## 📁 Files

- `train.py`: Reads `data.txt` and builds an N-gram model (saved as `ngram_model.json`).
- `test.py`: Loads the N-gram model and takes user input to predict the next word.
- `data.txt`: The training corpus used to build the model.
- `ngram_model.json`: JSON representation of the N-gram frequencies.

---

## 🛠 How it works

1. **Training (`train.py`)**
   - Reads `data.txt`
   - Builds a trigram model: For every 2-word sequence, stores frequency of the next word
   - Saves the model to `ngram_model.json`

2. **Prediction (`test.py`)**
   - Takes 2-word user input
   - Predicts the next word using the highest probability from trained model

---

## 🚀 Steps to Run

1. Prepare your `data.txt` file (e.g., copy the sample lines).
2. Train the model:

   ```bash
   python train.py

3. Test the model:

   ```bash
   python test.py
   
