while True:
    try:
    # def reverse(chars):
        # seqs = chars.split()
        seqs = input().split()
        reverse_seqs = list(reversed(seqs))
        r = ' '.join(reverse_seqs)
        # return r
        print(r)

    except:
        break