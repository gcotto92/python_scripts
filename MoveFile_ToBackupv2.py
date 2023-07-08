import shutil 
import os 

source_path = input('Enter source path:\n')
destination = input('Enter the destination path:\n')


extension = input('Enter extension for files (.jpg, .jpeg, .png, .mp4, .txt, .pdf) to move:\n')


if extension == '.jpg':
    os.chdir(source_path)
    print(f'Current path is {source_path}.\n')
    mv_jpg = f'mv *{extension} {destination}'
    os.system(mv_jpg)
    print(f'File type of {extension} has been moved to {destination}.\nVerify results\n')

elif extension == '.jpeg':
    os.chdir(source_path)
    print(f'Current path is {source_path}.\n')
    mv_jpeg = f'mv *{extension} {destination}'
    os.system(mv_jpeg)
    print(f'File type of {extension} has been moved to {destination}.\nVerify results\n')

elif extension == '.png':
    os.chdir(source_path)
    print(f'Current path is {source_path}.\n')
    mv_png = f'mv *{extension} {destination}'
    os.system(mv_png)
    print(f'File type of {extension} has been moved to {destination}.\nVerify results\n')

elif extension == '.mp4':
    os.chdir(source_path)
    print(f'Current path is {source_path}.\n')
    mv_mp4 = f'mv *{extension} {destination}'
    os.system(mv_mp4)
    print(f'File type of {extension} has been moved to {destination}.\nVerify results\n')

elif extension == '.txt':
    os.chdir(source_path)
    print(f'Current path is {source_path}.\n')
    mv_txt = f'mv *{extension} {destination}'
    os.system(mv_txt)
    print(f'File type of {extension} has been moved to {destination}.\nVerify results\n')

elif extension == '.pdf':
    os.chdir(source_path)
    print(f'Current path is {source_path}.\n')
    mv_pdf = f'mv *{extension} {destination}'
    os.system(mv_pdf)
    print(f'File type of {extension} has been moved to {destination}.\nVerify results\n')

else:
    print(f'Selection of {extension} type is not correct.\n')
    exit()