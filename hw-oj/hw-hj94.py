from collections import OrderedDict
while True:
    try:
        numPerson, names, numVoters, votes = int(input()), input().split(),\
                         int(input()), input().split()
        
        name2Votes = OrderedDict()
        for name in names:
            name2Votes[name] = 0

        inValid = 0
        for vote in votes:
            if vote in names:
                name2Votes[vote] = name2Votes.get(vote, 0) + 1
            else:
                inValid += 1

        for n, vs in name2Votes.items():
            print(' : '.join([n, str(vs)]))
        print(' : '.join(['Invalid', str(inValid)]))

    except:
        break