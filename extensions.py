file=input('File:').lower().strip()
if '.jpg' in file or '.jpeg' in file:
    print('image/jpeg')
elif '.gif' in file:
    print('image/gif')
elif '.png' in file:
    print('image/png')
elif '.pdf' in file:
    print('application/pdf')
elif '.txt' in file:
    print('text/plain')
elif '.zip' in file:
    print('application/zip')
else:
    print('application/octet-stream ')

