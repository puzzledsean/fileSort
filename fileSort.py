import os, sys

def fileSort():        
    origin = "DailyPhoto"
    destination = "December 30th 2014 to January 8th 2015"
    path = "/Users/Sean/Documents/iPhone Backup Photos/" + origin
    path2 = "/Users/Sean/Documents/iPhone Backup Photos/" + destination
    # Check current working directory.
    retval = os.getcwd()
    print "Current working directory %s" % retval
    
    # Now change the directory
    os.chdir( path )
    
    # Check current working directory.
    retval = os.getcwd()
    
    print "Directory changed successfully %s" % retval
    
    origin = os.listdir(os.getcwd())
    
    os.chdir(path2)
    retval = os.getcwd()
    print "Directory changed successfully %s" % retval
    
    dates = os.listdir(os.getcwd())
    for date in dates:
        for images in origin:
            if(date == images):
                test = "/Users/Sean/Documents/iPhone Backup Photos/" + destination  + "/" + date
                print('we removed', date)
                os.remove(test)
