# REDDIT 2 VEC

Welcome to the Reddit 2 Vec project Repository on GitHub! Reddit 2 Vec is a project that uses the Doc2Vec (Paragraph to Vector) algorithm to convert SubReddits into vectors, based on the corpus of comments in that particular SubReddit.

#### Try it out at www.reddit2vec.com

## Motivation

Traditional recommendation techniques such as collaborative filtering, while having the potential to be highly personalized, have their own drawbacks. This includes issues like cold start problems for users who haven't used the website. This is has the potential for being a large problem for Reddit, because the vast majority of their users do not log in.

## Solution - Doc2Vec

I used the Doc2Vec algorithm developed at Google to convert the comments of a SubReddit into a vector representation of that SubReddit. Doc2Vec is built on top of Word2Vec.

Word2vec is a neural network with 1 hidden layer that has continuous bag of words (CBOW) or skip-grams implementation. Reddit2Vec uses the version that uses skip-grams and hierarchical softmax for optimization. 

As a simple overview, Word2Vec tries to train the neural network to paramatize a model that can predict the surrounding words for every word in the corpus. The predictions are then used to backpropogate and optimize the parameters to make words with similar contexts be closer together, while being further away from words that have different contexts. This means that the model is trying to predict the conditional probability of a word given words that would be around it. For instance:
"I went swimming at the ??? today and got sunburned" will return a higher probability of returning the words "beach" or "pool". This means that the model can begin to learn the context of words in a sentence.

The input-hidden layer weighting matrix, which is also the vector representation of words, is then used to gain insight into the meaning/similarity of words. 

## Reddit 2 Vec

Reddit 2 Vec used the recent data dump of comments and is trained on all the comments posted during May 2015 (about 54 Million comments). I ran the comments (stored as JSON objects) through ujson on a large AWS EC2 instance. The model then used the gensim library to implement Doc2Vec and currently uses Flask to serve up the application. The model ran for a total of about 72 hours to run through all the comments (Fun Fact: It actually degraded the instance).

Thanks for visiting!
