from PIL import Image
from docx2pdf import convert

file_type_input = input('Is the file type an .png/.jpg or .doc?\nEnter ".png" or ".jpg" or ".doc":\n')

if file_type_input == '.png':
    image_1 = Image.open(input('Enter the source path:\n'))
    im_1 = image_1.convert('RGB')
    im_1.save(input('Enter the destination path:\n'))

elif file_type_input == '.jpg':
    image_1 = Image.open(input('Enter the source path:\n'))
    im_1 = image_1.convert('RGB')
    im_1.save(input('Enter the destination path:\n'))

elif file_type_input == '.doc':
    source_path = input('Enter the source path:\n')
    convert(f'{source_path}')
    #destination_path = input('Enter the new file name:\n')
    #convert(f'{source_path}',f'{destination_path}')
    #dest_full_path = input('Enter the destination path:\n')
    #convert(f'{dest_full_path}')

else:
    print('File type was not entered...Exiting the program.')

print('Script executed successfully. Please verify the results:\n')