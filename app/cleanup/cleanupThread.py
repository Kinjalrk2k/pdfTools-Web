import threading
import time
from ..pdfTools import merger
import os
import shutil


class cleanupThread(threading.Thread):
    def __init__(self, root, threadID, time_limit):
        threading.Thread.__init__(self)
        self.root = root
        self.threadID = threadID
        self.start_time = time.time()
        self.time_limit = time_limit
        print(self.time_limit)

    def run(self):
        print("cleanupThread WAITING for threadID: {} started...!".format(self.threadID))
        time.sleep(self.time_limit)
        print("cleanupThread CLEANUP for threadID: {} started...!".format(self.threadID))
        self.cleanup(self.root, self.threadID)
        print("cleanupThread for threadID: {} ended...!".format(self.threadID))

    @staticmethod
    def cleanup(root, id):
        new_open_file_list = []
        for openfile in merger.openfile_list:
            if openfile['id'] == id:
                openfile['file'].close()
            else:
                new_open_file_list.append(openfile)
        merger.openfile_list = new_open_file_list

        folder = os.path.join(root, id)

        if os.path.exists(folder):
            for filename in os.listdir(folder):
                filepath = os.path.join(folder, filename)
                try:
                    shutil.rmtree(filepath)
                except OSError:
                    os.remove(filepath)
        shutil.rmtree(folder, ignore_errors=True)
