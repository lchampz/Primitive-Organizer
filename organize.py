import os

audio = ['.mp3', '.ogg', '.wav', '.aac', '.aiff', '.pmc', '.flac']
video = ['.mp4', '.mov', '.avi']
img = ['.png', '.jpeg', '.jpg', '.gif']
doc = ['.txt', '.log', '.pdf', '.csv', '.xlsx', '.docx']

def getExtension(file):
    index = file.rfind('.')
    return file[index:]

def organize(dir):
    if dir == '':
        dir = os.path.abspath('.')
        
    audioDir = os.path.join(dir, "audios")
    imgDir = os.path.join(dir, "images")
    videoDir = os.path.join(dir, "videos")
    docDir = os.path.join(dir, "docs")
    othersDir = os.path.join(dir, "others")
    
    if not os.path.isdir(audioDir):
        os.mkdir(audioDir)
    
    if not os.path.isdir(imgDir):
        os.mkdir(imgDir)
    
    if not os.path.isdir(videoDir):
        os.mkdir(videoDir)
        
    if not os.path.isdir(docDir):
        os.mkdir(docDir)
           
    if not os.path.isdir(othersDir):
        os.mkdir(othersDir)
    
    nameFiles = os.listdir(dir)
    newDir = ""
    for file in nameFiles:
        if os.path.isfile(os.path.join(dir, file)):
            ext = str.lower(getExtension(file))
            
            if ext in img:
                newDir = imgDir
            elif ext in audio:
                newDir = audioDir
            elif ext in video:
                newDir = videoDir
            elif ext in doc:
                newDir = docDir
            else:
                newDir = othersDir

            old = os.path.join(dir, file)
            new = os.path.join(newDir, file)
            os.rename(old, new)
            print("Moved", file, "->", new)

if __name__ == '__main__':
    name = input("Enter directiory name: ")
    organize(name)
