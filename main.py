from subprocess import Popen, PIPE
import requests
from urllib.parse import quote
import webbrowser

def search_error(file_loc, n = 5):
    proc = Popen(['python.exe', file_loc], stdout= PIPE, stderr= PIPE)
    stdout, stderr = proc.communicate()
    dec_stderr = stderr.decode('utf-8')

    if stderr == b'':
        print('No Errors Found')
    else:
        main_err = dec_stderr.splitlines()[-1]
        print(f'Error: {main_err}')
        url_main_err = quote(main_err)
        URL = f'https://api.stackexchange.com/2.2/search/advanced?order=desc&sort=relevance&accepted=True&tagged=Python&title={url_main_err}&site=stackoverflow'
        r = requests.get(url=URL)
        data = r.json()
        links_data = []
        if len(data['items']) < n:
            for i in range(len(data['items'])):
                temp = data['items'][i]['link']
                links_data.append(temp)
        else:
            for i in range(n):
                temp = data['items'][i]['link']
                links_data.append(temp)
        for i in links_data:
            webbrowser.open(i, new=1, autoraise=True)

search_error('trial.py')