import os

old = '../ladino-diksionaryo-generated/docs/'
new = 'docs/'

def get_html(url):
    return f'''
<!DOCTYPE html>
<meta charset="utf-8">
<title>Redirecting to {url}</title>
<meta http-equiv="refresh" content="0; URL={url}">
<link rel="canonical" href="{url}">
'''


for dirname, dirs, files in os.walk(old):
    #print(dirname)     # relative path (from cwd) to the directory being processed
    #print(dirs)       # list of subdirectories in the currently processed directory
    #print(files)       # list of files in the currently processed directory

    for filename in files:
        path = os.path.join(dirname, filename)
        #print(path)
        url = path.replace(old, '')
        path = path.replace(old, new)
        if url.endswith('.html'):
            url = 'https://kantoniko.com/' + url[:-5]
        #print(path)
        this_dir = os.path.dirname(path)
        os.makedirs(this_dir, exist_ok=True)
        #print(url)
        #print(this_dir)
        #print()
        with open(path, 'w') as fh:
            fh.write(get_html(url))
