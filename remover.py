import os, sys

score_file = open("target.txt","r",encoding="utf8") # read 2 list
lines = score_file.read().split() # tolist
uploadFiles = []
score_file.close()
for item in lines:
    fileName = item.split("/")[-1]
    fileNameParent = item.split("/")[-2]
    removeExt = fileName.split(".")[0]
    uploadFiles.append("{0}/{1}".format(fileNameParent,removeExt))

print(uploadFiles)

def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-2]
                extParent = ext.split("\\")[-2]
                extFileName = ext.split("\\")[-1]
                checkNm = "{0}/{1}".format(extParent,extFileName)
                #print(checkNm)
                flag = False
                for checkFileName in uploadFiles:
                    if checkFileName == checkNm:
                        flag = True
                if not flag:
                    print("{0}가 삭제 되었습니다.".format(full_filename))
                    os.remove(full_filename)
    except PermissionError:
        pass


def removeEmptyFolders(path, removeRoot=True):
    'Function to remove empty folders'
    if not os.path.isdir(path):
        return

    # remove empty subfolders
    files = os.listdir(path)
    if len(files):
        for f in files:
            fullpath = os.path.join(path, f)
            if os.path.isdir(fullpath):
                removeEmptyFolders(fullpath)

    # if folder empty, delete it
    files = os.listdir(path)
    if len(files) == 0 and removeRoot:
        #print("Removing empty folder:", path);
        os.rmdir(path)


def usageString():
    'Return usage string to be output in error cases'
    return 'Usage: %s directory [removeRoot]' % sys.argv[0]


fullpath = [풀패스]
search(fullpath)
removeEmptyFolders(fullpath,True)
