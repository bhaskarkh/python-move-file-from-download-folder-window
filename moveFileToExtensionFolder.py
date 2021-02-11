import os
import pyttsx3

def getExtName(file):
    return file.split(".")[-1]

def isDirOrFileExist(filePath):
    return os.path.exists(filePath)

def makeNewPath(filePath):
    splitWord=filePath.split(".")
    dotExt='.'+splitWord[-1]
    renamedDotExt="_copy"+dotExt
    newWord=filePath.replace(dotExt,renamedDotExt)
    return newWord
    
def voiceMsg(strVal):
    engine = pyttsx3.init()
    engine.setProperty('rate', 110)
    engine.setProperty('volume',1)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(strVal)
    engine.runAndWait()



def moveFile(files,trgFol,pathVar):
    for file in files:
        ext=getExtName(file)
        extDirPath=trgFol + "\\" + ext
       
        filePath=extDirPath+"\\"+file
        src=pathVar+file

        isDirExist1=isDirOrFileExist(extDirPath)
        print(filePath)
        if isDirExist1:
            if isDirOrFileExist(filePath):
                print(file,"file is already There")
                newFilePath=makeNewPath(filePath)
                os.rename(src,newFilePath)
                print(file," copied  Succesfull")     
            else:
                print(file,"file not Present wait moving......")
                os.rename(src,filePath)
                print(file," moved Succesful")
        else:
            print("dir not present wait making for you ......")
            try:
                os.mkdir(extDirPath)
                print("dir created")
                os.rename(src,filePath)
                print(file," moved Succesful")
            except Exception as e:
                print(e)
                
                
source_folder=r'C:\Users\bhask\Downloads'+'\\'
target_folder=r'C:\Users\bhask\Downloads'
for path,dir,files in os.walk(source_folder):
    moveFile(files,target_folder,path)
    break


strVal="Hi Bhaskar All File Moved  Successfully"
voiceMsg(strVal)