#!/usr/bin/python3
'''
    this module contains the function number_of_subscribers
'''
import requests
from sys import argv


def number_of_subscribers(subreddit):
    '''
        returns the number of subscribers for a given subreddit
    '''
url = requests.get('https://www.reddit.com/r/{}/about.json'
                       .format(subreddit), headers=user).json()

i = 0
for entry in subreddit:
    i = i +1
   return i

usersub = open ('usersubscribtions.csv','w')
users=[]
userlist = open("user_ids_noduplicates1.txt","r")
text1 = userlist.readlines()

for l in text1:
        users.append(l.strip().split()[0])
x = 0
while (x<len(users)):

 try:
    GetUserUrl(users[x])
    time.sleep(0.4)
    x = x+1
 except:
    usersub.writelines([str(users[x]),'\n'])
    x = x+1
    pass

usersub.close()
