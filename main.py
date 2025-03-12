'''
File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.
Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
'''

def read_n_write(file_name):
    #start here
    try:
        with open(file_name, 'w') as file:
            try:
                file.write(input('Entre what youd like to be written in the file\n'))
                print('File written successfully')
            except:
                print('File could not be written')
    except FileNotFoundError:
        print('file provided does not exists')
    except IOError:
        print('File could not be read')

print(read_n_write(input('enter file name here: ')))