from pytube import YouTube

def Save(link):
	yt=YouTube(link)
	yt=yt.streams.get_highest_resolution()
	
	try:
		yt.download()
		print("Done.....")
	except:
		print("Error")

url=input("Enter Your URL/LINK: ")

Save(url)