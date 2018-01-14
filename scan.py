# Script:   scan.py
# Desc:     extracts contents from website / txt file
#           looks for emails, phone numbers, MD5 hashes, files, hyperlinks
# Author:   Oliver Thornewill von Essen, 40210534


import urllib
import re

        
def wget(url):
    '''Gets url and displays webpage conten/html'''
    try:
        webpage = urllib.urlopen(url)       #Open url 
        page_contents = webpage.read()      #Define page_contents by reading the webpage
        webpage.close()                     #Close file
        return page_contents
    except Exception as err:
        print 'wget doesn\'t work'
        print err


def txtget(filename):
    '''Opens file and reads each line'''
    # open file read-only, get file contents and close
    try:
        file = open(filename, 'r')          #Open local file as read only
        file_contents = file.read()         #Define file_contents by reading the file
        file.close()                        #Close file
        return file_contents
    except Exception as err:
        print 'txtget doesn\'t work'
        print err


def findemail(url):
    '''Search file or webpage for Email Addresses'''
    emails = []
    try:
        e = wget(url)                              #Gets content from webpage
        match = list(set(re.findall(r'[\w\.-]+@[\w\.-]+', e))) #Finds emails under criteria
    except:
        e = txtget(filename)
        match = list(set(re.findall(r'[\w\.-]+@[\w\.-]+', e)))
    emails = emails + match

    print '[*]', len(emails), 'Email addresses found:'
    for email in emails:
        print '    '+email
        
    return emails



def phone_get(txt):
    '''Finds phone numbers within a webpage'''
    try:
        phone =[]
        p = wget(txt)
        match = list(set(re.findall(r"\+44\(\d\)\d{3}\s?\d{3}\s?\d{4}", p)))
        phone = phone + match
        
        print '[*]', len(match),'Phone Numbers found:'
        for phone in match:
            print '    '+phone
        return phone_get
    except Exception as err: 
        print 'There was an issue finding the phone numbers'
        print err

        
def hash_get(url):
    '''Finds the hashes in html code'''
    pwd =[]
    try:
        p = wget(url)
        match = list(set(re.findall(r"[\d?\w?]{32}", p)))
        pwd = pwd + match
        
        print '[*]', len(match),'Possible MD5 Hashes found:'
        for Hash in match:
            print '    '+Hash
        return hash_get
    except Exception as err:
        print 'There was an issue finding hashes'
        print err


def scrape_files(url):
    """Finds and prints out possible files available in html code"""
    links = []
    try:
        p = wget(url)
        match = list(set(re.findall(r"\"([^\n\"]*(?:\\.[^\n\"]*)*\.(?:bmp|jpg|png|gif|docx))\"", p)))
        links = links + match

        print '[*]', len(match),'Possible files found:'
        for i in match:
            print '    '+i
        return scrape_files
    except Exception as err:
        print err


def hyperlinks_get(url):
    """Finds hyperlinks in the HTML"""
    hyperlinks = []
    try:
        p = wget(url)
        match = list(set(re.findall(r'(?<=<a href=\")([^\"]+)', p)))
        hyperlinks = hyperlinks + match

        print '[*]', len(match),'Hyperlinks found:'
        for hyperlink in match:
            print '    '+hyperlink
        return hyperlinks_get
    except Exception as err:
        print 'There was an issue finding hyperlinks'
        print err

if __name__ == '__main__':
    main()
