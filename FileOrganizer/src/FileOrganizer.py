import shutil
import os

Directories = {
    'Audio-Files': ('.aif', '.cda', '.mid', '.midi', '.mp3', '.mpa', '.ogg', '.wav', '.wma', '.wpl'),
    'Compressed-Files': ('.7zp', '.arj', '.deb', '.pkg', '.rar', '.rpm', '.tar.gz', '.z', '.zip'),
    'Database-Files':  ('.csv', '.dat', '.db', '.dbf', '.log', '.mdb', '.sav', '.sql', '.tar', '.xml'),
    'Email-Files': ('.email', '.eml', '.emlx', '.msg', '.oft', '.ost', '.pst', '.vcf'),
    'Executable-Files': ('.apk', '.py', '.bat', '.bin', '.cgi', '.pl', '.com', '.exe', '.gadget', '.jar', '.msi', '.wsf'),
    'Font-Files': ('.fnt', '.fon', '.otf', '.ttf'),
    'Image-Files': ('.ai', '.bpm', '.ico', '.jpeg', '.jpg', '.png', '.ps', '.psd', '.svg', '.tif', '.tiff', '.heic', '.HEIC', '.JPG', '.PNG'),
    'Internet-Files': ('.asp', '.aspx', '.cer', '.cfm', '.css', '.htm', '.html', '.js', '.jsp', '.part', '.php', '.rss', '.xhtml'),
    'Media-Files': ('.bin', '.dmg', '.iso', '.toast', '.vcd', '.app'),
    'Presentation-Files': ('.key', '.odp', '.pps', '.ppt', '.pptx'),
    'Programming-Files': ('.c', '.class', '.cpp', '.cs', '.h', '.java', '.pl', '.sh', '.swift', '.vb'),
    'Spreadsheet-Files': ('.ods', '.xls', '.xlsm', '.xlsx'),
    'System-Files': ('.bak', '.cab', '.cfg', '.cpl', '.cur', '.dll', '.dmp', '.drv', '.icns', '.ico', '.ini', '.lnk', '.msi', '.sys', '.tmp'),
    'Video-Files': ('.3g2', '.3gp', '.avi', '.flv', '.h264', '.m4v', '.mkv', '.mov', '.mp4', '.mpg', '.mpeg', '.rm', '.swf', '.vob', '.wmv', '.MOV'),
    'Word-Files': ('.doc', '.docx', '.odt', '.pdf', '.lpdf', '.rtf', '.tex', '.txt', '.wpd')
}

if __name__ == '__main__':
    os.chdir('/Users/brandontenorio/Downloads')     # Go to my Downloads folder
    filesMoved = 0

    for file in os.listdir():   # Go through every file in current folder (my Downloads folder)
        for key, value in Directories.items():  # Go through the keys and values in the hashmap
            if file.endswith(Directories[f'{key}']):    # If the file extension of the folder we're currently looking at is in one of the tuples saved in one of the keys in the hashmap
                try:
                    shutil.move('/Users/brandontenorio/Downloads/' + file, '/Users/brandontenorio/Files' + f'/{key}')
                    filesMoved += 1
                    print('Files moved from Downloads to ' + f'{key}' + ':\n- ' + file + '\n')
                except shutil.Error:
                    try:
                        shutil.move('/Users/brandontenorio/Downloads/' + file, '/Users/brandontenorio/Files/Replicated-Files')
                        filesMoved += 1
                        print('Files moved from Downloads to Replicated-Files:' + '\n- ' + file + '\n')
                    except shutil.Error:
                        shutil.move('/Users/brandontenorio/Downloads/' + file, '/Users/brandontenorio/.Trash')
                        print('Files moved from Downloads to Trash: ' + '\n-' + file + '\n')

    if filesMoved == 0:
        print('No files were moved')
