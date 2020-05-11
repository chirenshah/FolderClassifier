import os
import shutil
import sys
import argparse
import re
import random

def get_download_folder():
        home = os.path.expanduser("~")
        return os.path.join(home, "Downloads")

def systemArgument():
    # Initialize parser 
    parser = argparse.ArgumentParser() 
    
    # Adding optional argument 
    parser.add_argument("-f", "--Folder", help = "Enter Path of Folder") 
    
    # Read arguments from command line 
    args = parser.parse_args() 
    
    if args.Folder:
        move(args.Folder)
    else:
        move() 
    
def ifexist(element):
    video_formats = ["mp4","mpg","flv","avi","3gp","wmv","mov","qt"]
    for ext in video_formats:
        if(element.endswith("."+ext)):
            print("hi"+element)
            return True
        else:
            return False


def move(folder = get_download_folder()):

    files = os.listdir(folder)

    for file in files:
        split = file.split(".")
        print(len(split))
        if (len(split)>1):
            filename = split[0]
            ext = split[1]
            if(file.endswith(".pdf") or file.endswith(".html")):
                if(not os.path.exists(folder + "\Pdfs")):
                    os.mkdir(folder + "\Pdfs")
                try:
                    shutil.move("{}/{}".format(folder, file),"{}/{}".format(folder,"Pdfs"))
                except:
                    shutil.move("{}/{}".format(folder,file), "{}/{}/{}({}).{}".format(folder, "Pdfs",filename,random.randrange(0,10),ext))

            if(file.endswith(".exe") or file.endswith(".msi")):
                if(not os.path.exists(folder + "\Setups")):
                    os.mkdir(folder + "\Setups")
                try:
                    shutil.move("{}/{}".format(folder, file),"{}/{}".format(folder,"Setups"))
                except:
                   shutil.move("{}/{}".format(folder,file), "{}/{}/{}({}).{}".format(folder, "Setups",filename,random.randrange(0,10),ext))

            if(file.endswith(".torrent")):
                if(not os.path.exists(folder + "\Torrents")):
                    os.mkdir(folder + "\Torrent")
                try:
                    shutil.move("{}/{}".format(folder, file),"{}/{}".format(folder,"Torrents"))
                except:
                    shutil.move("{}/{}".format(folder,file), "{}/{}/{}({}).{}".format(folder, "Torrents",filename,random.randrange(0,10),ext))

            if(file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg")):
                if(not os.path.exists(folder + "\Images")):
                    os.mkdir(folder + "\Images")
                try:
                    shutil.move("{}/{}".format(folder, file),"{}/{}".format(folder,"Images"))
                except:
                    shutil.move("{}/{}".format(folder,file), "{}/{}/{}({}).{}".format(folder, "Images",filename,random.randrange(0,10),ext))

            if(ifexist(file)):
                if(not os.path.exists(folder + "\Video")):
                    os.mkdir(folder + "\Video")
                try:
                    shutil.move("{}/{}".format(folder, file),"{}/{}".format(folder,"Video"))
                except:
                    shutil.move("{}/{}".format(folder,file), "{}/{}/{}({}).{}".format(folder, "Video",filename,random.randrange(0,10),ext))
                       
            if(file.endswith(".zip")):
                if(not os.path.exists(folder + "\Zipfile")):
                    os.mkdir(folder + "\Zipfile")
                try:
                    shutil.move("{}/{}".format(folder, file),"{}/{}".format(folder,"Zipfile"))
                except:
                    shutil.move("{}/{}".format(folder,file), "{}/{}/{}({}).{}".format(folder, "Zipfile",filename,random.randrange(0,10),ext))
                    
            if(file.endswith(".xls") or file.endswith(".txt")):
                if(not os.path.exists(folder + "\Textfiles")):
                    os.mkdir(folder + "\Textfiles")
                try:
                    shutil.move("{}/{}".format(folder, file),"{}/{}".format(folder,"Textfiles"))
                except:
                   shutil.move("{}/{}".format(folder,file), "{}/{}/{}({}).{}".format(folder, "Textfiles",filename,random.randrange(0,10),ext))   
        
if __name__ == "__main__":
    systemArgument()
