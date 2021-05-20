import pandas as pds
import numpy as np

def generate_df(loc, session, chamber):

    '''
        loc -> the type of data being located.
        session -> the session of Congress, i.e. 115
        chamber -> either Senate or House
    '''

    sessions = np.arange(1, 117)

    try:
        if int(session) in sessions:

            session = str(session)
            while len(session) != 3:
                session = "0" + session

            if chamber.title() == 'House':
                url = 'https://voteview.com/static/data/out/{}/H{}_{}.csv'.format(loc, session, loc)

            elif chamber.title() == 'Senate':
                url = 'https://voteview.com/static/data/out/{}/S{}_{}.csv'.format(loc, session, loc)

            else:
                print('The chamber must either be House or Senate!')
                return None

            df = pds.read_csv(url)

            return df

        else:
            print('The session must be between 1 and 116!')
            return None
    except:
        print('The session must be convertable to an integer!')
        return None

def get_ideology_df(session, chamber):

    '''
        session -> the session of Congress, i.e. 115
        chamber -> either Senate or House
    '''

    return generate_df('members', session, chamber)

def get_bills_df(session, chamber):

    '''
        session -> the session of Congress, i.e. 115
        chamber -> either Senate or House
    '''

    return generate_df('rollcalls', session, chamber)
