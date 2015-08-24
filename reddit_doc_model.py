import re
import gensim
from gensim.models import Doc2Vec

class RedditModel(object):
    """
    This Class can load the Doc2Vec model, parse a user query,
    and return the most similar subreddits given a query.
    """
    def __init__(self):
        self.model = None

    def load_model(self):
        '''
        Method to load model.
        '''
        self.model = Doc2Vec.load('first_final_model')

    def parse_query(self,query):
            '''
            Parse the user query to positive and negative subreddits.

            input = string
            output = list
            '''
            pos_words = []
            neg_words = []

            # replace '-' with '+-' to split on '+' later
            query = re.sub('-\s*', '+-', query)

            # split on '+'
            terms = query.split('+')
            terms = [x for x in terms if x != '']

            # for every words in between 'plus'
            for term in terms:
                if term[0] == '-':
                    neg_words.append(term[1:]) #everythign past minus
                else:
                    pos_words.append(term)

            return pos_words,neg_words



    def most_sim_subs(self,query):

        # Get Positve and Negative subreddits from query
        pos,neg = self.parse_query(query)
        query_good=True

        # Get top 10 most similar subreddits
        try:
            sim_subs = self.model.docvecs.most_similar(positive=pos,negative=neg,topn=5)
            query_good=True
        except:
            subreddit_names = "Sorry! Looks like one of your Subreddits isn't in the database. Check for spelling and Capitalization!"
            query_good =False

        if query_good:
            # Create empty lists to be fed into HTML table maker
            subreddit_names = ''


            # Assign values for lists
            for name in sim_subs:
                subreddit_names += '/r/'+str(name[0])+' , '

            subreddit_names = subreddit_names[:-3]

            if sim_subs[0][1] < 0.5:
                subreddit_names += "       Warning: Your query resulted in low cosine similarity results!"

            #return self.table_set(subreddit_names,cosine_sim)
        return subreddit_names
