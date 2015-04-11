import os, sys

#Sean Zhang

def fileSort():

    #path name of the directory of the files that you have duplicates of, but you want to keep       
    start = "Photo A Day"

    #path name of the directory where the duplicate files are intermixed with other misc. files
    destination = "December 30th 2014 to January 8th 2015"

    path = "/Users/Sean/Documents/iPhone Backup Photos/" + start
    path2 = "/Users/Sean/Documents/iPhone Backup Photos/" + destination
    # Check current working directory.
    retval = os.getcwd()
    print "Current working directory %s" % retval
    
    # change current working directory to first path file
    os.chdir( path )
    # Check current working directory.
    retval = os.getcwd()
    print "Directory changed successfully %s" % retval
    
    #assign 'start' directory to origin
    origin = os.listdir(os.getcwd())
    
    # change current working directory to second path file
    os.chdir(path2)
    retval = os.getcwd()
    print "Directory changed successfully %s" % retval
    
    #assign 'destination' directory to dates
    dates = os.listdir(os.getcwd())

    #traverse through each file 
    for date in dates:
        for images in origin:
            #if there's a duplicate
            if(date == images):
                #create the corresponding path with the correct file names
                toRemove = "/Users/Sean/Documents/iPhone Backup Photos/" + destination  + "/" + date
                print('we removed', date)
                os.remove(toRemove)
