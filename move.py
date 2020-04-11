import os
import shutil
import sys
import argparse

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
    

def move(folder = get_download_folder()):

    files = os.listdir(folder)

    for file in files:
        if(file.endswith(".pdf")):
            if(not os.path.exists(folder + "\Pdfs")):
                os.mkdir(folder + "\Pdfs")
            shutil.move("{}/{}".format(folder, file),"{}/{}".format(folder,"Pdfs"))
        if(file.endswith(".exe")):
            if(not os.path.exists(folder + "\Setups")):
                os.mkdir(folder + "\Setups")
            shutil.move("{}/{}".format(folder, file),"{}/{}".format(folder,"Setups"))
        if(file.endswith(".torrent")):
            if(not os.path.exists(folder + "\Torrents")):
                os.mkdir(folder + "\Torrent")
            shutil.move("{}/{}".format(folder, file),"{}/{}".format(folder,"Torrent"))
        if(file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg")):
            if(not os.path.exists(folder + "\Images")):
                os.mkdir(folder + "\Images")
            shutil.move("{}/{}".format(folder, file),"{}/{}".format(folder,"Images"))
        
if __name__ == "__main__":
    systemArgument()