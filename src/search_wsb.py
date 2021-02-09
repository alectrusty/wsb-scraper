from psaw import PushshiftAPI
import datetime

# instantiate the API
api = PushshiftAPI()

# set start time
start_time=int(datetime.datetime(2021, 1, 1).timestamp())

# get a list of submissions over the given time frame
submissions = api.search_submissions(after=start_time,
                                    subreddit='wallstreetbets',
                                    filter=['url','author', 'title', 'subreddit'])
                            

for submission in submissions:
    #print(submission.created_utc)
    #print(submission.title)
    #print(submission.url)

    words = submission.title.split()
    # filter the list down to items that fit certain criteria -- only grab words with cashtags
    cashtags = list(set(filter(lambda word: word.lower().startswith('$'), words)))

    if len(cashtags) > 0:
        print(cashtags)
        print(submission.title)