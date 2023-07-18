def create_youtube_video(title, description):
	youtube = {title: "", description : "", "likes" : 0 , "dislikes" : 51, 'comments': {"o" : "hi"}, "hashtags" : []}
	youtube["hashtags"].append([input("enter hashtags ")])
	youtube["hashtags"].append([input("enter hashtags ")])
	return youtube

def like(youtube):
	if "likes" in youtube:
		youtube["likes"] = youtube["likes"]+1

	return youtube


def dislike(youtube):
	if "dislikes" in youtube:
		youtube["dislikes"] = youtube["dislikes"]+1
	return youtube

def addcomment(youtube, username, comment_text):
	youtube['comments'][username] = comment_text
	return 


def similarity(y1, y2):
	similar = 0
	
	list("hashtags")
	for i in (hashtags(len(num))):
		if y1(num[i]) == y2(num):
			similar + 1
	similar/len(num)
	return similar






y1 = create_youtube_video("the vid","haha") 
y2 = create_youtube_video("my vid","hihi" )
for i in range (495):
	like(y1)
print(y1)
print(similarity(y1, y2))


