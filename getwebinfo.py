import sys
import scan
import download
import forensic


def main():
    """Main script which strings all scripts together
    Scanning for multiple things in HTML code
    Attempting downloads
    Perform forensic analysis
    Reporting where necessary"""
    sys.argv.append('http://www.soc.napier.ac.uk/~40001507/CSN08115/cw_webpage/')
    try:
        print '\n\n\n!!!SCANNING CONTENT FROM %sindex.html !!!\n\n\n' %sys.argv[1]
        scan.findemail(sys.argv[1])
        print ''
        scan.phone_get(sys.argv[1])
        print ''
        scan.hash_get(sys.argv[1])
        print ''
        scan.scrape_files(sys.argv[1])
        print ''
        scan.hyperlinks_get(sys.argv[1])
        print '\n\n\n !!! DOWNLOADING PHASE !!! \n\n\n'
        download.save_file(sys.argv[1])
        print '\n\n\n !!! FORENSIC ANALYSIS !!! \n\n\n'
        forensic.pw_hash_crack(sys.argv[1])
        print ''
        forensic.get_hash_and_check(sys.argv[1])
        print ''
    except:
        raise
    
    
if __name__ == '__main__':
    main()
