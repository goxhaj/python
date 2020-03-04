try:
    with open ('myfile.txt') as file:
        file_data = file.read()
    print(file_data)
except FileNotFoundError as err:
    print('File not found, Error:', str(err))
except PermissionError as err:
    print('Permission denied, Error:', str(err))
except Exception as err:
    print('Some other error occured, Error:', str(err))