



import os
import shutil
import logging





def make_and_clear(dest):
    '''
    Create dest if it does not exist and
    remove any files, but not folders, in dest if exists
    NOTE: All of this printing is not necessary. It is here for some troubleshooting with Condor.
    '''

    # Create destination folder
    if os.path.exists(dest):

        #logging.info("Recursively removing:\t{}".format(dest))
        shutil.rmtree(dest)
        #logging.info("Recursive removal complete")



    if not os.path.exists(dest):
        #logging.info("Creating directory:\t{}".format(dest))
        os.makedirs(dest)

    return True