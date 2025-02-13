from pathlib import Path

x = Path.cwd() / 'images'
print(x)

path_file = Path(x) / f'epic_{1}.png'
print(path_file)