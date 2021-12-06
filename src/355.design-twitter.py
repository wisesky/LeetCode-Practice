#
# @lc app=leetcode id=355 lang=python3
#
# [355] Design Twitter
#
# https://leetcode.com/problems/design-twitter/description/
#
# algorithms
# Medium (33.15%)
# Likes:    1631
# Dislikes: 250
# Total Accepted:    75K
# Total Submissions: 225.1K
# Testcase Example:  '["Twitter","postTweet","getNewsFeed","follow","postTweet","getNewsFeed","unfollow","getNewsFeed"]\n' +
#  '[[],[1,5],[1],[1,2],[2,6],[1],[1,2],[1]]'
#
# Design a simplified version of Twitter where users can post tweets,
# follow/unfollow another user, and is able to see the 10 most recent tweets in
# the user's news feed.
# 
# Implement the Twitter class:
# 
# 
# Twitter() Initializes your twitter object.
# void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId
# by the user userId. Each call to this function will be made with a unique
# tweetId.
# List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs
# in the user's news feed. Each item in the news feed must be posted by users
# who the user followed or by the user themself. Tweets must be ordered from
# most recent to least recent.
# void follow(int followerId, int followeeId) The user with ID followerId
# started following the user with ID followeeId.
# void unfollow(int followerId, int followeeId) The user with ID followerId
# started unfollowing the user with ID followeeId.
# 
# 
# 
# Example 1:
# 
# 
# Input
# ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed",
# "unfollow", "getNewsFeed"]
# [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
# Output
# [null, null, [5], null, null, [6, 5], null, [5]]
# 
# Explanation
# Twitter twitter = new Twitter();
# twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1
# tweet id -> [5]. return [5]
# twitter.follow(1, 2);    // User 1 follows user 2.
# twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2
# tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is
# posted after tweet id 5.
# twitter.unfollow(1, 2);  // User 1 unfollows user 2.
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1
# tweet id -> [5], since user 1 is no longer following user 2.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= userId, followerId, followeeId <= 500
# 0 <= tweetId <= 10^4
# All the tweets have unique IDs.
# At most 3 * 10^4 calls will be made to postTweet, getNewsFeed, follow, and
# unfollow.
# 
# 
#
from typing import List
from heapq import heappop, heappush
# @lc code=start
class Twitter:
    # 46 ms 24% 14.1MB 99%
    """
    题目信息太少，很多边界条件都没说清楚，最新的tweet 的order ，
    最初以为是tweetId的大小，最后发现实际上并不是，仅仅只是post的先后顺序，
    这样就无法使用优先队列来存储post时间，最后只能一个list按照 先后顺序存储所有tweets
    """
    def __init__(self):
        self.followers = {} # follower to followed
        # self.user2tweets = {} # userid to tweets
        self.tweets = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        # if userId in self.user2tweets:
        #   self.user2tweets[userId].append(tweetId)
        # else:
        #   self.user2tweets[userId] = [tweetId]
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.followers.get(userId, []) + [userId]
        users = set(users)
        r = []
        i = len(self.tweets)-1
        c = 0
        while i >= 0 and c < 10:
          user, tweet = self.tweets[i]
          if user in users:
            r.append(tweet)
            c += 1
          i -= 1

        return r

        # pq = []
        # ps = []
        # for i,user in enumerate(users):
        #   tweets = self.user2tweets.get(user, [])
        #   tweet = tweets[-1] if len(tweets)>0 else None
        #   p = -2 if len(tweets)>1 else None
        #   if tweet is not None:
        #     heappush(pq, (-tweet, i))
          
        #   ps.append(p)
        
        # r = []
        # c = 0
        # while c+len(pq)<10 and len(pq) > 0:
        #   tweet, index = heappop(pq)
        #   # refresh pq
        #   if ps[index] is not None:
        #     newTweet = self.user2tweets[users[index]][ps[index]]
        #     ps[index] = ps[index]-1 if abs(ps[index]) < len(self.user2tweets[users[index]]) else None
        #     heappush(pq, (-newTweet, index))
          

        #   r.append(-tweet)
        #   c += 1
        
        # while len(pq) > 0:
        #   tweet, _ = heappop(pq)
        #   r.append(-tweet)

        # return r


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers:
          if followeeId not in self.followers[followerId]:
            self.followers[followerId].append(followeeId)
        else:
          self.followers[followerId] = [followeeId]

    def unfollow(self, followerId: int, followeeId: int) -> None:
        try:
          self.followers[followerId].remove(followeeId)
        except:
          pass


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end

twitter = Twitter()

twitter.postTweet(1, 5)
print(twitter.getNewsFeed(1))
twitter.follow(1, 2)
twitter.postTweet(2, 6)
print(twitter.getNewsFeed(1))
twitter.unfollow(1, 2)
print(twitter.getNewsFeed(1))

# twitter.postTweet(1, 1)
# print(twitter.getNewsFeed(1))
# twitter.follow(2,1)
# print(twitter.getNewsFeed(2))
# twitter.unfollow(2,1)
# print(twitter.getNewsFeed(2))

# twitter.postTweet(1, 4)
# twitter.postTweet(2, 5)
# twitter.unfollow(1, 2)
# print(twitter.getNewsFeed(1))

# twitter.postTweet(2, 5)
# twitter.follow(1, 2)
# twitter.follow(1, 2)
# print(twitter.getNewsFeed(1))
