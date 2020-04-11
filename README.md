# FolderSort
The Download folder is often filled with torrent files , images , setup files etc. rendered
Navigation through it difficult.
This program was made to ease that navigation by sorting files in relevant folders using file extensions
Below are the instructions to Schedule the sorting of Folder using Task Scheduler to execute this script on booting   

**Setup**
1. Clone the Directory into a Local Folder
2. Set up a Basic task in Task Scheduler (Windows)
   More information on the Process [Here](https://www.esri.com/arcgis-blog/products/product/analytics/scheduling-a-python-script-or-model-to-run-at-a-prescribed-time/)   
3. Set the Trigger and/or Period for Execution
4. In the Action tab Browse to the **move.py** file in the clone Repository

**Optional**

By Default the Program will find and sort Download Files to change the folder location

Add this command to `Add arguments` section
> -f  YOUR_FOLDER_PATH

