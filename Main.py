from pytube import YouTube

def main():
    url = input("Enter URL to start download!")
    filetype = input("Enter filetype that you want to download.")


    yt = YouTube(url=url).streams.all()
    
    #video = Youtube.streams.filter(progressive=True, file_extension='mp4').first()


if __name__ == '__main__':
    main()