import news_cnn_model
import numpy as np
import os
import pandas as pd
import pickle
import shutil
import tensorflow as tf
import logging

from sklearn import metrics
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize
from os.path import join
from os.path import normpath

learn = tf.contrib.learn

REMOVE_PREVIOUS_MODEL = True

MODEL_OUTPUT_DIR = normpath(join(os.path.dirname(__file__), '../model/'))
DATA_SET_FILE = normpath(join(os.path.dirname(__file__), '../data/labeled_news.csv'))
VARS_FILE = normpath(join(os.path.dirname(__file__), '../model/vars'))
VOCAB_PROCESSOR_SAVE_FILE = normpath(join(os.path.dirname(__file__), '../model/vocab_procesor_save_file'))
MAX_DOCUMENT_LENGTH = 200
N_CLASSES = 8

# Training parms
STEPS = 100

LOGGER_FORMAT = '%(asctime)s - %(message)s'
logging.basicConfig(format=LOGGER_FORMAT)
LOGGER = logging.getLogger('news_class_trainer')
LOGGER.setLevel(logging.DEBUG)

stemmer = PorterStemmer()
stop_words = set(stopwords.words('english'))

def main(unused_argv):
    if REMOVE_PREVIOUS_MODEL:
        # Remove old model
        print("Removing previous model...")
        shutil.rmtree(MODEL_OUTPUT_DIR)
        os.mkdir(MODEL_OUTPUT_DIR)
    
    # Random shuffle
    df.sample(frac=1)

    # Prepare training and testing data
    df = pd.read_csv(DATA_SET_FILE, header=None)
    train_df = df[0:400]
    test_df = df.drop(train_df.index)

    # x - news description, y - class
    x_train = train_df[2]
    y_train = train_df[0]
    x_test = test_df[2]
    y_test = test_df[0]

    # tokenize sentences
    x_train = [word_tokenize(sentence) for sentence in x_train.tolist()]
    x_test = [word_tokenize(sentence) for sentence in x_test.tolist()]

    # Stemming words.
    norm_x_train = []
    norm_x_test = []
    for tokens in x_train:
        stemmed_tokens = [stemmer.stem(w.lower()) for w in tokens if not w in stop_words]
        norm_sentence =  ' '.join(stemmed_tokens)
        norm_x_train.append(norm_sentence)

    for tokens in x_test:
        stemmed_tokens = [stemmer.stem(w.lower()) for w in tokens if not w in stop_words]
        norm_sentence =  ' '.join(stemmed_tokens)
        norm_x_test.append(norm_sentence)

    x_train = norm_x_train
    x_test = norm_x_test    

    # Process vocabulary
    vocab_processor = learn.preprocessing.VocabularyProcessor(MAX_DOCUMENT_LENGTH)
    x_train = np.array(list(vocab_processor.fit_transform(x_train)))
    x_test = np.array(list(vocab_processor.transform(x_test)))

    n_words = len(vocab_processor.vocabulary_)
    print('Total words: %d' % n_words)

    # Saving n_words and vocab_processor:
    with open(VARS_FILE, 'wb') as f:  # needs to be opened in binary mode.
        pickle.dump(n_words, f)

    vocab_processor.save(VOCAB_PROCESSOR_SAVE_FILE)

    # Build model
    classifier = learn.Estimator(
        model_fn=news_cnn_model.generate_cnn_model(N_CLASSES, n_words),
        model_dir=MODEL_OUTPUT_DIR)

    # Train and predict
    classifier.fit(x_train, y_train, steps=STEPS)

    # Evaluate model
    y_predicted = [
        p['class'] for p in classifier.predict(x_test, as_iterable=True)
    ]

    score = metrics.accuracy_score(y_test, y_predicted)
    print('Accuracy: {0:f}'.format(score))

if __name__ == '__main__':
    tf.app.run(main=main)
