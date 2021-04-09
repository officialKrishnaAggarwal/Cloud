import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    def uploadFile(self, fileFrom, fileTo):
        dbx = dropbox.Dropbox(self.access_token)
        with open(fileFrom, "rb") as f:
            dbx.files_upload(f.read(), fileTo)

def main():
    access_token = input("PLEASE ENTER THE ACCESS TOKEN OF YOUR DROPBOX")
    transferData = TransferData(access_token)
    fileFrom = input("Enter The File Path To Transfer:")
    fileTo = input("Enter The Dropbox Path")
    transferData.uploadFile(fileFrom, fileTo)
    print("File Uploaded Successfully")
    
main()    
