# 🧠 Trigram-Based Next Word Prediction

This project builds a simple next-word prediction system using *trigrams*, a specific type of *n-gram* where predictions are made based on the previous three words. The model is built using only Python standard libraries, making it lightweight and easy to run.

---

## 📘 What is an N-Gram?

An *n-gram* is a sequence of `n` consecutive words in a text.

- *Unigram (1-gram)* → `["the", "cat", "sat"]`
- *Bigram (2-gram)* → `[("the", "cat"), ("cat", "sat")]`
- *Trigram (3-gram)* → `[("the", "cat", "sat")]`

In this project, we use **trigrams** to predict the next word after a 3-word input.

---

## 📁 Project Structure

| File                | Description                                               |
|---------------------|-----------------------------------------------------------|
| `data.txt`          | Input text data for training the model                    |
| `train.py`          | Script that builds and saves the trigram frequency model  |
| `trigram_model.pkl` | Auto-generated model file created after training          |
| `test.py`           | Script that loads the model and predicts the next word    |

---

## ⚙️ How the Model Works

### 1. `train.py` – Training Phase

- Loads and reads text from `data.txt`
- Cleans and tokenizes the text into words
- Builds a frequency dictionary of trigrams and their next-word mappings
- Saves the trained model as `trigram_model.pkl`

### 2. `test.py` – Prediction Phase

- Loads the saved model from `trigram_model.pkl`
- Prompts the user to enter a 3-word phrase
- If the phrase exists in the training data, predicts the most likely next word

---

## 🚀 Steps to Run the Project

1. Prepare your `data.txt` file (e.g., copy the sample lines).
2. Train the model:

   ```bash
   python train.py
3. Test the model:
   ```bash
   python train.py

