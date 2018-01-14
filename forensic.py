# Script:   forsnsic.py
# Desc:     Performs forensic analysis, such as:
#               - MD5 Hash dictionary crack
#               - Checks downloaded files against dictionary for bad files. 
# Author:   Oliver Thornewill von Essen, 40210534

import re
import hashlib
import scan
import os


def pw_hash_crack(url):
    """Attempts to crack the possible hashes found in HTML code by Dictionary attack
    reporting on how many MD5 Hashes were cracked"""
    try:
        pwd = []
        match = list(set(re.findall(r"[\d?\w?]{32}", scan.wget(url))))
        pwd = pwd + match
        dic = ['joshua','dragon','starwars']
        result = ''

        passwd_found = False

        print '[*] Attempting to crack MD5 hashes in HTML code'
        x = 0
        
        for item in dic:
            passwd = hashlib.md5(item).hexdigest()
            print '   ',passwd
            
            if passwd in pwd:
                print '    Password recovered: %s' % (item)
                print''
                x = x + 1         
        y = len(match) - x

        print '[*] Reporting on hash crack'
        if not x == 1:
            print '   ',x,'MD5 password hashes were successfully cracked.'
        else:
            print '   ',x,'MD5 password hash cracked.'
        if not y == 1:
            print '   ',y,'MD5 password hashes did not get cracked.'
        else:
            print '   ',y,'MD5 password hash did not get cracked.'
    except Exception as err:
        print 'Problem with pw_hash_crack()'
        print err


def get_hash_and_check(url):
    """Hashes downloaded files in C:\\temp\\coursework and checks them against dictionary of bad hashes
    reporting on bad files found"""
    try:
        directory = (r'C:\\temp\\coursework\\')
        bad_files = {'9d377b10ce778c4938b3c7e2c63a229a' : 'contraband_file1.jpg', 
                     '6bbaa34b19edd6c6fa06cccf29b33125' : 'contraband_file2.jpg',
                     'e4e7c3451a35944ca8697f9f2ac037f1' : 'contraband_file3.jpg',
                     '1d6d9c72e3476d336e657b50a77aee05' : 'contraband_file4.gif'}
        hashed_files = {}
        print '[*] Attempting to hash the',len(os.listdir(directory)),' files in the directory:', directory
        x = 0
        with open('C:\\temp\\hashed_files.txt', 'wb') as location:
            for filename in os.listdir(directory):
                fh = open(os.path.join(directory,filename), 'rb')
                file_content = fh.read()
                hashmatch = hashlib.md5(file_content)
                md5hash = hashmatch.hexdigest()
                print '    \''+md5hash+'\'',':', '\''+filename+'\'' 
                hashed_files[md5hash] = md5hash, filename
                print >> location, hashed_files[md5hash]
                x = x + 1
        print '\n '
        print '[*] Preforming forensic analysis on files'
        y = 0
        try:
            for key in hashed_files.keys(): 
                if key in bad_files.keys():
                    print '    !!MALICIOUS FILE FOUND!!'
                    print '     The (hash : name) of malicious file:', hashed_files[key]
                    print '      In our database, this file is known as:',bad_files[key], '\n'
                    y = y + 1
                    
        except Exception as err:
            print err
            raise

        print '[*] Reporting on files'
        print '   ',x,'files in',directory,'were successfully hashed'
        print '   ',y,'files in',directory,'were found to be malicious/ dubious'
    except Exception as err:
        print 'There is a problem with get_hash_and_check()'
        print err


if __name__ == '__main__':
    main()
