import urllib2

def tecaj():
# file to be written to
    file = "downloaded_file.xml"

    url = "http://www.pbz.hr/Downloads/HNBteclist.xml"
    response = urllib2.urlopen(url)

#open the file for writing
    fh = open(file, "w")
    fh.write(response.read())
    fh.close()

