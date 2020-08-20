from itertools import permutations

def intersection(dic, candidate):
    perm = permutations(candidate)
    list_perm = [''.join(x) for x in perm]
    # set_perm = set(list_perm)
    # list_perm.remove(candidate)

    r = []
    for i in dic:
        if i in list_perm and i != candidate:
            r.append(i)

    return r

while True:
    try:
        # line = '473 bb daccb caddd bddc c baa adb ad abbcb cdaa abab a abcc ddcbd cadcc cdacd aaa a b acccd bbb dacc cc acbdd bcbb ba bacaa adda acd aaad d ab acac bc dabab abcd aacba aba daa bb ad cddab a bbaa aacad cdac acbcc cada bacd adcad cdadc bcbcc aa b acd cbaac ddcd ccb dac a dac adbcb bcda dda a ab ca dd d abd a dbb ccabd bdddd abd adc aaa baccb ccdcd a da c cadc dcdbd d aa bb a cac c ad adb ca cdcc cadd dddca d cba cb caab caa dd cd bca abc cdaa cdb bad dad bda d ddbc dab baaa adaac b a dbccd bd b bdad cdacd baa ac ddcad d bb acc aa cd cbdbb bbbcb a cc aacc c aadc dbcd a bca dd abbb ccdcd ccd ab d a a dadcd dbd bcaa c cda b ddab caaaa cdcdb b acbc ccaa dabca dcd b ba dbcc da bdbcc ab abaca bb cddc caca da dadba accdd bdac dbcd bcbbd ab bd ccb ddaa aa b b d bddd cabac aaba ab ccdb db abbd ada bdadb c abba dd cdb bca cccda badba abaa ac aabad db ccbad bddd ada dba acba b bc dd bbbbd cc cbdd cd abcaa bb ddaca acadb bbbb bddcc bdada aaa bcbda c aaa aadd cdddc adb cdbab c cbca bb aacab acdb bbdab b acbda cbdcd bda bacdc db d adcbd bccc c aaa cdd bdcd bac a aaab ddbb cd ccdbb addcc cdc c ca baadc addba dbdbd dba bbdda bcb c cdad aacac dcada cb aaad a cccab caca aad bbb dd b babbb cba bdaca db bacd bc bcbda cdda bcccd bdcda bdbcd adb cbcb a c bacba abbb adab adab b b d bca badbc baa cdb b abc aabb b d c cdab cacda d cdcda adcdc bcc bbccd b adb caba cbaaa aadb dcc add bcac bacbd bb a b c cabaa c caad c aa bcc ccab ddc dadca cdcba aaba dabbd dcb a bddb bb a c c cbc ccd dd a cabbb b caadb cb dca cbb ddaa bcadc dab a bbda cd bc ccad bbd ab c acddd cdd dbbbb daaab abbb cabc add ca caa bbbb dcab daaaa baca dcd ccacb ba bddaa acac dbcc bcc cbbcc b abba daa dbab bcca ba aa d dcdc d dcaa cbcda bd b ccbcb baa dcacd d c cbda baba d abb c cbdc da dbbb cd aabc dadc b a ddb c ddd ccdc ccd cba dbaac dcccd ddbac dbbdd bad bcdd cb dac dccd d a acdd d c cb b bcbb c a aca bcba d d bbdbc d c dabad ccca dc adb ddb dcdd dba ad ddaba c ac ddac bbbd cd a dacbb 1'.\
            # split()
        # line = '4 abcd acbd acde adeb abcd 1'.split()
        # line = '854 c dd ddb cadda c dbadd adcdc a cccd aab b cbad abc ddd daadb bcdd ccbb cd bbaa cbbac c ac ccca b aaad ca cacc abbb a a cabdc babd d ccada abb d cbc bbdc ca b cbbac db bbd bccd bdaad a aadca a dad c dacb d cdaba bddbc bbbdc bb dba cb acacb cb cb ddacd ac dabca bdd d baa bc bbdcc d da a d cccd bba b db aba ddaab ac cdc c abccd c aac ccad d dadcb bdd bbaa bd abb db acb dac ddba bd a dc dc dacca bccac dabad abb dcbda a bab aada ad dacbb accdd accdd cdd a daa b a dbd cddbd cbdac cbdd d ba b a dcca db acc abdb d caacc d cccb dacab d badd dab c ccaad dcdbc acdd cdda db dc aacba a abdc aca dcdd ccaaa bb dbd aacca dcabb dbcb caaad ddaa ada d badcd cabcb ccda ccbab bddac cbc cdbc adda dc ba dbbd a c aabb bddd cdbc b ac caac a bac b cd a dac d cbaac cabb bbc c ab a aa da ba abb dc cac abcbd addcd dc c c bbc cbcc bcd ddadd bdd ccd dcadb bcbcc cddad adb bddcb ddda bd a cdcdb ddbcc caaa ab a d acba acadc baab daacb c acd bca bcd dcbd a a bc ccda aacca a cdd bca bdaa bcbdc dcc bcaa aaad c cdad abb d dac dcbb bacdc db b cb b bdbac dbc cb bd aba bacb db acccc cdb accd aaba cbb bbcdc d dba cad acbb d aaaaa aa cb abad a bbdc bd baa ac ddd aa adca cb ca dbba dcaab d a caac dd a cbbc ad aacca cba bcbdb c c bb dbdaa b ad dc d adbd cdbbd dbdb abd dab addab c dddd cdbb ca da da ac dd c aadcd cbd bdaab d db bca cadcc adac a adcd cdbad bab cadda bbcbc acbb bacab ab bda a ccad a ccaaa a bcca dc acdaa ac dc bdabb dbad cacd dbbcb aada bc ac bdbb aaac d acaca dbdda aa bbbbb bba cdac dcada cca bd ddcbc ad caacb aabda acaca cab bc bdad acbdc ccd aa bad a c cda a bd ccb ba bbbaa cbad cb d dc bb bdac bda a aad dca dab ccad cbca c ac a abbcd bbbc b bbdc db cdb babbd adb ca da c cabda ccb cdcd daa aa abcd cab d ca abba ab bcbdb dc aa dcdaa bcb aacd caca cccdc aab dcbd cdb cbbb abc cdc dacbb bbbcb c ba ddcc c badca bbaa dcb cbc aacb aabcd acb caa adda bcad accbb dcc ccab cdd a aadbd aadd b cad bbca bacd dd dad b c dbbcd dcabb d cbcbd ac aa adaab dad dbd acdb b da caad babaa bdbd cccbd cdabb dbac a dbba cc cabc a d dcdba dcabd d d aaa cbcab abdda daca dc d cccbd cad abb baadd dba baadc bbc bbbcc ccacd c acb ac babd cbdcd dadcc aacdb aacad abac ddd d acbd b dcaa bbadd dcda b cc b cdbdb bcc dbd adbd bbaba c aa c a dbcbc b dacc a a cad daaa dcb aa ccca dbada dd bbcba cbcc bb b bd dbac cdbcd dbcda cc a abbb adb abd cdd cadd cab abcc cb bbcc b dc dda d dda cddcb cb c ca bad dcd daddd c b ada acaab d bdabd c bd aaba caada ddc dbb dc add ca caabc bdda a accb bdcc adaa aada dba dcba ddc ab aad dcdbb bbaa dcbca bbda acbab bca aaaab bd cdbcb db cd aa bac dc b bbca a a cdabc cbbd b bdac b caca ddb ddcbc aacd db bdcc cb cc abc c a c c cb baacc c badd ccd cbcaa bb aa ddaa cdd aaabc b cbdbc b cddc b acbdd caac abbd d ccd cb bc bcc bd cbda b dcdcb ccbca baabd cd d b accd bc daddb d cdbaa bcb dcd bccd c ab baddb b dddca baaa cab ddbdb ac bad bbabb aa acda b cbc b a b ad dad dbcda d d acadc cdcad ddc bcbac a aac a dc badd cd daaa dd ad acbd cdd c cb dabb cd bda aa ccdbc dcaca c bd cddd abacb dc dccd ab baad bc dccc daba adcbb cccd cd b adccb aabc bccbb ccdd a dbbcd ac bc aabd bb aab abbc caa bca ccccb bbc d bcd bacbc acdc aab dabcc b dd dca cacc bdcca ad d cbcda ab bad cd cbbbb acadb ca d ddb accaa c ccccb acb d d a cac dc bd b dcc d adc b bd abc dbdb baada ddbb bda cab ddb cdb cbcc db d dca cc ba b dbbd abadc bdac cbaa cbadb acb aadb acba cddcd bbab bd cdc cbcdc dbc d cb bca add a abdd b bbd d bcdad cc ca dbc cba aaad dc ad bcbcb cd a acba 3'.\
            # split()
        line = input().split()
        n = int(line[0])
        dic = line[1:1+n]
        candidate = line[-2]
        n_ca = int(line[-1])

        list_res = intersection(dic, candidate)
        print(len(list_res))
        if len(list_res) >= n_ca:
            # print(len(set_res))
            output = sorted(list_res)[n_ca-1]
            print(output)

    except:
        break