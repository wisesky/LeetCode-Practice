import re
import string
import jieba
import gensim
import os
from sklearn.feature_extraction.text import CountVectorizer , TfidfVectorizer
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import metrics
def get_stopwords():
    stopwords_list = []
    with open('./stopwords.utf8') as f:
        for line in f:
            stopwords_list.append(line.strip())
    return stopwords_list
# 中文分词
def tokenize_text(text):
    tokens = jieba.cut(text)
    tokens = [token.strip() for token in tokens]
    return tokens
def remove_stopwords(text):
    stopwords = get_stopwords()
    tokens_text = tokenize_text(text)
    removed_text = [token for token in tokenize_text if token not in stopwords]
    return ' '.join(removed_stopwords)
def remove_special_characters(text):
    tokens = tokenize_text(text)
    # a = Is Chicago 
    # b = Not Chicago
    # >>> print('{} {}'.format(a,b))
    #Is Chicago Not Chicago?
    pattern = re.compile('[{}]'.format(re.escape(string.punctuation)))
    filtered_tokens = filter(
        None, [re.sub(pattern=pattern, repl="", string=token) for token in tokens])
    filtered_text = ' '.join(filtered_tokens)
    return filtered_text
def normalize_corpus(corpus):
    normalize_corpus = []
    for text in corpus:
        text = remove_special_characters(text)
        text = remove_stopwords(text)
        normalize_corpus.append(text)
    return normalize_corpus
def remove_empty_docs(corpus, labels):
    filtered_corpus = []
    filtered_labels = []
    for doc, label in zip(corpus, labels):
        if doc.strip():
            filtered_corpus.append(doc)
            filtered_labels.append(label)
    return filtered_corpus, filtered_labels
def get_data():
    '''
    获取数据
    :return: 文本数据，对应的labels
    '''
    with open("../input/spam identification/data/ham_data.txt", encoding="utf8") as ham_f, open("../input/spam identification/data/spam_data.txt", encoding="utf8") as spam_f:
        ham_data = ham_f.readlines()
        spam_data = spam_f.readlines()

        ham_label = np.ones(len(ham_data)).tolist()
        spam_label = np.zeros(len(spam_data)).tolist()
        corpus = ham_data + spam_data
        labels = ham_label + spam_label
    return corpus, labels
def get_metrics(true_labels, predicted_labels):
    print('准确率:', np.round(
        metrics.accuracy_score(true_labels,
                               predicted_labels),
        2))
    print('精度:', np.round(
        metrics.precision_score(true_labels,
                                predicted_labels,
                                average='weighted'),
        2))
    print('召回率:', np.round(
        metrics.recall_score(true_labels,
                             predicted_labels,
                             average='weighted'),
        2))
    print('F1得分:', np.round(
        metrics.f1_score(true_labels,
                         predicted_labels,
                         average='weighted'),
        2))
def train_prediction_evaluation(classifier, train, train_labels, test, test_labels):
    classifier.fit(train, train_labels)
    pred = classifier.transform(test)
    get_metrics(test_labels, pred)
    return pred
def main():
    corpus , lables = get_data()
    corpus, labels = remove_empty_docs(corpus, labels)
    print("总的数据量:", len(labels))
    print('样本之一:', corpus[10])
    print('样本的label:', labels[10])
    label_name_map = ["垃圾邮件", "正常邮件"]
    print('实际类型:', label_name_map[int(labels[10])],
          label_name_map[int(labels[5900])])

    train_corpus, test_corpus, train_labels, test_labels = train_test_split(corpus, labels, test_size = 0.2)
    norm_train_corpus = normalize_corpus(train_corpus)
    norm_test_corpus = normalize_corpus(test_corpus)
    # bow
    bow = CountVectorizer(min_df=1, ngram_range=(1,1)):
    bow_train = bow.fit_transform(norm_train_corpus)
    bow_test = bow.transform(norm_test_corpus)
    #tfidf
    tfidf = TfidfVectorizer(
        min_df=1, norm='l2', smooth_idf=True, use_idf=True, ngram_range=(1,1))
    tfidf_train = tfidf.fit_transform(norm_train_corpus)
    tfidf_test = tfidf.transform(norm_test_corpus)

    from sklearn.naive_bayes import MultinomialNB
    from sklearn.linear_model import SGDClassifier
    from sklearn.linear_model import LogisticRegression
    mnb = MultinomialNB()
    svm = SGDClassifier(loss='hinge', n_iter=100)
    lr = LogisticRegression()

    mnb_bow = train_prediction_evaluation(mnb, bow_train, train_labels, bow_test, test_labels )
    svm_bow = train_prediction_evaluation(svm, bow_train, train_labels, bow_test, test_labels)
    lr_bow = train_prediction_evaluation(lr, bow_train, train_labels, bow_test, test_labels)
    mnb_tfidf = train_prediction_evaluation(mnb, tfidf_train, train_labels, tfidf_test, test_labels)
    svm_tfidf = train_prediction_evaluation(svm, tfidf_train, train_labels, tfidf_test, test_labels)
    lr_tfidf = train_prediction_evaluation(lr, tfidf_train, train_labels, tfidf_test, test_labels)

    # word2vec
    tokenized_train = [jieba.lcut(text) for text in train_corpus]
    tokenized_test = [jieba.lcut(text) for text in test_corpus]
    model = gensim.models.word2vec(tokenized_train, size = 500, window=100, min_count=30, sample=1e-3)
    
    


    
