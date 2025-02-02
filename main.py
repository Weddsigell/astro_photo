import os
from pathlib import Path
from pprint import pprint
from environs import Env

def main():
    # Path('./images').mkdir(parents=True, exist_ok=True)
    # with open(f'{path_file}/{img_name}', 'wb') as file:
    #     file.write(response.content)


    photos = []
    ext = ('.png', '.jpg', '.txt')
    for datas in os.walk('./images'):
        for filename in datas[2]:
            file = os.path.join(datas[0], filename)
            if file.endswith(ext):
                photos.append(file)
            else:
                continue
    pprint(photos)
    print(os.path.split(photos[0]))

if __name__ == '__main__':
    env = Env()
    env.read_env()
    main()
