def remove_bg2(x):
    import requests
    import os
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    target1 = os.path.join(ROOT_DIR, 'static/')

    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={'image_file': open(x, 'rb')},
        data={'size': 'auto'},
        headers={'X-Api-Key': '3uVE6ierroU6VSH5hGNMUazf'},
    )
    if response.status_code == requests.codes.ok:
        with open(target1+'no-bg_2.png', 'wb') as out:
            out.write(response.content)
    else:
        print("Error:", response.status_code, response.text)
        print('CHANGE API KEY')
    s=""
    s='static/no-bg_2.png'

    print('Patch bg removed')

    return s
