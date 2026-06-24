#xiaopeng Chen| lab 3| intro to python


#ticket 1
username = "instagram"
print(len(username))
#there is 9 characters for my social handle
# yes, len() counts every worda, no symbols include.

#ticket 2
print(username[0])
print(username[-1])
# "i" and "m" will be print
# -1 is the last index because that -1 always grabs the last index

#ticket 3
print("welcome to loop" + " @"+ username+"!")
print(f"welcome to loop @{username}!")
#yes, both line looks identical on the screen
# f"string feels easier, because you don't have to type that much


#ticket 4
#username[0]= "X"  #'str' object does not support item assignment
#its gonna be an error
# I think immutable means that you can't change it once it created

#ticket 5
feed = ["food","plays","random stuff"]
print(len(feed))
print(feed[0])
#there 3 for the counts, and the first caption is food
#I use index 0 to print the first post

#ticket 6
feed.append("funny") 
print(feed)
#This new post would have index 3
#is at index 3 because we start count from 0
print(feed[3])

#ticket 7
feed.pop(0)
feed.sort()
print(feed)
# food post got removed 
# I use .pop() to remove the first post
# Then I use .sort() to make the list in alphabetical order

#ticket 8
profile = {"username":"xiaopeng",
           "followers":1000000,
           "verified":False}
#profile[0] #KeyError: 0
#follower number is 1000000
#profile[0] does nothing and its an error for dic
#dic looks things up with key name, because dic doesn't have index

#ticket 9
profile["followers"]= profile["followers"]+50
profile["bio"]= "oths"
print(profile)
profile.get("age")#print nothing without key
#.get() is safer than profile["age"] because that profile["age"] will break the code and .get() wouldn't

#ticket 10
print(f"@{username} has {profile["followers"]} and {len(feed)} post.Top post:{feed[0]}")
