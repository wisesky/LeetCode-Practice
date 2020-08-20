import re
def reverse(line):
    words = re.split('[^a-zA-Z]+', line)
    reverse_words = words[ : :-1]
    cor_reverse_words = [x  if len(x)<20 else x[ :20] for x in reverse_words]
    output = ' '.join(cor_reverse_words)
    return output.stirp()

while True:
    try:
        line = input()
        output = reverse(line)
        print(output)
    except:
        break