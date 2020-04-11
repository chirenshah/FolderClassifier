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
        if(file.endswith(".pdf")):
            if(not os.path.exists(folder + "\Pdfs")):
                os.mkdir(folder + "\Pdfs")
            try:
                shutil.move("{}/{}".format(folder, file),"{}/{}".format(folder,"Pdfs"))
            except:
                shutil.move("{}/{}({})".format(folder, file,random.randrange(0,10)),"{}/{}".format(folder,"Pdfs"))

        if(file.endswith(".exe")):
            if(not os.path.exists(folder + "\Setups")):
                os.mkdir(folder + "\Setups")
            try:
                shutil.move("{}/{}".format(folder, file),"{}/{}".format(folder,"Setups"))
            except:
                shutil.move("{}/{}({})".format(folder, file,random.randrange(0,10)),"{}/{}".format(folder,"Setups"))

        if(file.endswith(".torrent")):
            if(not os.path.exists(folder + "\Torrents")):
                os.mkdir(folder + "\Torrent")
            try:
                shutil.move("{}/{}".format(folder, file),"{}/{}".format(folder,"Torrents"))
            except:
                shutil.move("{}/{}({})".format(folder, file,random.randrange(0,10)),"{}/{}".format(folder,"Torrents"))

        if(file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg")):
            if(not os.path.exists(folder + "\Images")):
                os.mkdir(folder + "\Images")
            try:
                shutil.move("{}/{}".format(folder, file),"{}/{}".format(folder,"Images"))
            except:
                shutil.move("{}/{}({})".format(folder, file,random.randrange(0,10)),"{}/{}".format(folder,"Images"))

        if(ifexist(file)):
            if(not os.path.exists(folder + "\Video")):
                os.mkdir(folder + "\Video")
            try:
                shutil.move("{}/{}".format(folder, file),"{}/{}".format(folder,"Video"))
            except:
                shutil.move("{}/{}({})".format(folder, file,random.randrange(0,10)),"{}/{}".format(folder,"Video"))   
        
if __name__ == "__main__":
    systemArgument()