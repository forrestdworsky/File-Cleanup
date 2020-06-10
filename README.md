# File Cleanup
Traverse directory (including subdirectories) and delete files older than 30 days.

# Purpose
This script will delete files older than 30 days in a specified folder.
It should be automated using a scheduled task or a cron job to automaticall delete files from a folder.
Automatic file deletion could be used for old logs or old temporary files produced by running services.


## Usage
The script takes a command line argument that specifies the folder to be examined.
The script will then display a list of filenames with their timestamps.
The user will be prompted if you want to delete the files.
The files will only be deleted if they are older than 30 days.

This variable can be modified to change the required age of the files in order for them to be deleted:
thirtydays = timedelta(days=30).total_seconds() #make a var for 30 days
