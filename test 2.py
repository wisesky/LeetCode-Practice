import sys

url = 'Origin'
fileurl = '.'
def main(argv):
    print('start...')
    
    for i ,j in enumerate(argv):
        #print(i, j)
        if i == 1:
            url = j
        #elif i == 2:
         #   fileurl = j
    print('url', url)
    print('fileurl', fileurl)
  #  for i,j in enumerate(argv):
   #     print(i, j)


if __name__ == '__main__':
    main(sys.argv)
