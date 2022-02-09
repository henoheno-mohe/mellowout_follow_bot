import sys
sys.path.append('../')
#import config
import tweepy
import time


CK="EysUOIqkVI5kKFEN17Twpb1pn"
CS="ZZCWDnibFgYZMApqIIhwJCnfYIJc5zS9Q4bnkb3Fiyekwb4biX"
AT="1394284521059586051-vEaXKGsdBBii0HLgnANsYXFgA3rB0c"
AS="JGD5T8cGWe9vNs0GiNs75g7IbUbFrbe4WUvqRhtYXUXmy"
BT="AAAAAAAAAAAAAAAAAAAAAC47WAEAAAAAvDr%2BNmWSYD1aDQBTTBlwezMGMAQ%3D3meZEihmnksSVkQgJeYmVELL4v3J2pY1PuWxr0nVAFre0eRE8Q"

# API KEY
#CK = config.CK
#CS = config.CS
#AT = config.AT
#AS = config.AS
#BT = config.BT

#tweepyの設定
client = tweepy.Client(BT, CK, CS, AT, AS)


# USER_NAME = "1394284521059586051"

#２）あるキーワードで検索したユーザを指定の件数フォローする

# 検索キーワード
keyword = "#相互フォロー  -is:retweet"

# フォロー数
follow_cnt = 0

# 現在のフォローリストを作成
follow_list = client.get_users_following(id="1475721163594952706",max_results=100)
follow_lists = []

for follow in follow_list[0]:
    follow_lists.append(follow.id)

block_list = client.get_blocked(max_results=100)
block_lists = []

print(block_list.data)

if block_list.data != None:
    for block in block_list[0]:
        block_lists.append(block.id)

print(block_lists)

follow_block_list = follow_lists + block_lists

s_count = 50
results = client.search_recent_tweets(query=keyword, max_results=s_count, user_fields = "name", expansions=["author_id","referenced_tweets.id"],)

for result in results.data: 
    print(result.author_id)
    # print(result.referenced_tweets)


for result in results.data: 
    client.like(tweet_id=result.id)
    if result.author_id not in follow_block_list:
        client.follow_user(result.author_id)
        print(result.author_id)
        time.sleep(61)
        

