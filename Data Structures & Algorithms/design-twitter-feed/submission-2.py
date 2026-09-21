from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.edges = defaultdict(set)#edges between users that follow each other
        self.tweets = [] #min heap of tweets based on the tweet ID
        self.tweet_owners = {}
        self.time = 0



    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_owners[tweetId] = userId
        heapq.heappush(self.tweets, (-self.time, tweetId))
        self.time += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        relevant = [userId]
        newsFeed = []
        temp_tweets= list(self.tweets) 


        relevant.extend(self.edges[userId])

        
        while (len(newsFeed) < 10) and temp_tweets:
            time, curr_tweet = heapq.heappop(temp_tweets)
            if self.tweet_owners[curr_tweet] in relevant:
                newsFeed.append(curr_tweet)
        
        return newsFeed


        



    def follow(self, followerId: int, followeeId: int) -> None:
        self.edges[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.edges[followerId].discard(followeeId)
        
