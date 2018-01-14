# Script:   download.py
# Desc:     Finds files to download from html code,
#           Attempts to download found files and gives report
# Author:   Oliver Thornewill von Essen, 40210534
# 

import sys
import os
import scan
import re



def scrape_files(url):
    """Finds and prints out possible files available in html code"""
    try: 
        links = []
        match = list(set(re.findall(r"\"([^\n\"]*(?:\\.[^\n\"]*)*\.(?:php|bmp|jpg|png|gif|docx))\"", scan.wget(url))))
        links = links + match
        return links
    except Exception as err:
        print err


def save_file(url):
    """saves files to C:\\temp\\coursework
    reporting on file downloads"""    
    try:
        location = os.path.abspath('C:\\temp\\coursework')   
        if not os.path.exists(location):      #checks if the destination directory exists, if not then it will make it. If it does, then it moves on
            os.mkdir(location)
        print '[*] Attempting to download found files to:',location
        y = 0
        z = 0
        for file_name in scrape_files(url):
            try:
                with open('C:\\temp\\coursework'+'\\'+file_name, 'wb') as location:
                    location.write(scan.wget(url+file_name))
                print '    Success downloading file: ', file_name
                z = z+1
                    
            except IOError:
                print '   ', IOError, file_name
                y = y+1

        print ''
        print '[*] Report on download'
        if not z == 1:
            print '   ',z,'Files were downloaded successfully.'
        else:
            print '   ',z,'File was successfully downloaded.'
        if not y == 1:
            print '   ',y,'Files failed to download.'
        else:
            print '   ',y,'File failed to download.'
    except Exception as err:
        print 'There is an issue with save_file()'
        print err
    

def analyse(url):
    """DOC STRING HERE"""
    try:
        url = 'http://www.soc.napier.ac.uk/~40001507/CSN08115/cw_webpage/'
        txt = url
        sys.argv.append('http://www.soc.napier.ac.uk/~40001507/CSN08115/cw_webpage/')
        scan.wget(sys.argv[1])
        print ''
        save_file(sys.argv[1])
        print ''       
    except Exception as err:
        print 'There is a problem with analyse()'
        print err
    

if __name__ == '__main__':
    main()
