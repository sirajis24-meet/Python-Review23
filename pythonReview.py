def create_youtube_video(title, description):
	youtube = {title: "", description : "", "likes" : 0 , "dislikes" : 0, 'comments': {}}
	return youtube

def like(youtube):
	if likes in youtube:
		youtube["likes"] = youtube["likes"]+1

	return youtube


def dislike(youtube):
	if dislikes in youtube:
		youtube["dislikes"] = youtube["dislikes"]+1
	return youtube

def addcomment(youtube, username, comment_text):
	youtube['comments'][username] = comment_text
	return youtube

title1 = input("enter title ")
desc1 =input("enter desc ")
username1 = input("enter username ")
comment1=input("enter comment ")
y = create_youtube_video(title1, desc1 )
like(y)
