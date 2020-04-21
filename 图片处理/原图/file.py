import os



for root, dirs, files in os.walk('原图'):
    for file in files:
        if file.split('.')[-1] in ['png', 'jpg', 'jpeg', 'svg']:
            print(file)
    
