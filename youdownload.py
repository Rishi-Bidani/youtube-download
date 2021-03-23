from pytube import YouTube, Playlist
from tablemaker import TableMaker
from colorama import Fore


class YouDownPlay:
    def __init__(self, link):
        self.link = link
        self.ytpObject = ""

    def createytpObject(self):
        self.ytpObject = Playlist(self.link)

    def downloadFullPlayAudio(self, location):
        for i in self.ytpObject.videos:
            print(f"Downloading {i.title}")
            i.streams.get_audio_only().download(f"{location}")

    def downloadFullPlayvideo(self, location):
        for i in self.ytpObject.videos:
            print(f"downloading {i.title}")
            i.streams.filter(progressive=True).last().download(f"{location}")


class YouDownVideo:
    def __init__(self, link):
        self.link = link
        self.options = []
        self.ytObject = ""

    def createytObject(self):
        self.ytObject = YouTube(self.link)

    def listAudioOptions(self):
        for i in self.ytObject.streams.filter(only_audio=True):
            self.options.append(i)
        print(*self.options, sep="\n", end="\n")

    def listVideoOptions(self):
        for i in self.ytObject.streams.filter(progressive=True):
            self.options.append(i)
        print(*self.options, sep="\n", end="\n")

    def downloadAudioItag(self, itag):
        self.ytObject.streams.get_by_itag(itag=itag).download()

    def downloadVideoItag(self, itag):
        self.ytObject.streams.get_by_itag(itag=itag).download()


print("Choose desired option: ")
optionsTable = TableMaker(2, [20, 5], "cyan")
heading = ["Available Options", "Value"]
optionsTable.heading(heading)
row1 = ["Only audio from video", "av"]
row2 = ["Entire video", "v"]
row3 = ["Audio from playlist", "ap"]
row4 = ["Entire Playlist", "p"]
optionsTable.items(row1)
optionsTable.items(row2)
optionsTable.items(row3)
optionsTable.items(row4)

chosevp = input("Your choice: ")
if chosevp == "v" or chosevp == "av":
    vidLink = input("Enter your video link: \n")
    yd = YouDownVideo(vidLink)
    yd.createytObject()

    if chosevp == "av":
        yd.listAudioOptions()
        inpItag = input("enter itag: ")
        yd.downloadAudioItag(inpItag)

    elif chosevp == "v":
        yd.listVideoOptions()
        inpItag = input("enter itag: ")
        yd.downloadAudioItag(inpItag)
else:
    print("CAUTION ENTER PUBLIC PLAYLIST LINK!!!!")
    playLink = input("Enter your playlist link: \n")
    ydp = YouDownPlay(playLink)
    ydp.createytpObject()
    if chosevp == "ap":
        print("Enter download location \n")
        location = input("Press enter for current directory: \n")
        ydp.downloadFullPlayAudio(location)

    elif chosevp == "p":
        print("Enter download location \n")
        location = input("Press Enter for current directory: \n")
        ydp.downloadFullPlayvideo(location)
    else:
        print("ERROR")