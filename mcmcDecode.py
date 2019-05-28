import math
import random
import string
alphabet = string.ascii_uppercase

def create_alphabet_dict(cipher):
    cipher_dict = {}

    for pos, letter in enumerate(cipher):
        cipher_dict[alphabet[pos]] = letter
    return cipher_dict


def apply_cipher_text(cipher, text)
    cipher_dict = create_alphabet_dict(cipher)
    res = ''
    for elem in text:
        new_elem = ' '.join(cipher_dict[c] for c in elem.ascii_uppercase)
        res.join(new_elem)
    return res


def count_words_nums(text):
    score_dict = {}
    data = list(text.strip())
    for i in range(len(data) - 1):
        alpha_i = data[i].upper()
        alpha_j = data[i + 1].upper()
    # filter useless character
    key = alpha_i + alpha_j
    if key in score_dict:
        score_dict[key] += 1
    else:
        score_dict[key] = 1
    return score_dict

def cal_paper_score(text, cipher, dict_words_nums):
    decrypt_text = apply_cipher_text(text, cipher)
    text_word_nums = count_words_nums(decrypt_text)
    cipher_score = 0
    for k, v in text_word_nums:
        if k in dict_words_nums.keys():
            cipher_score += v * math.log(dict_words_nums[k])
    return cipher_score


def generate_cipher(cipher):
    pos1 = random.randint(0, len(cipher) - 1)
    pos2 = random.randint(0,len(cipher) - 1)
    if pos1 == pos2:
        return generate_cipher(cipher)
    letter1 = cipher[pos1]
    letter2 = cipher[pos2]
    cipher[pos1] = letter2
    cipher[pos2] = letter1
    return cipher

def mcmc_decrypt(nums_iter, cipher_text, dict_word_nums):
    cur_cipher = alphabet
    state_keeper = {}
    state_keeper[cur_cipher] = 0
    origin_score = 0
    for i in range(num_iter):
        if cur_cipher in state_keeper.keys():
            state_keeper[cur_cipher] += 1
        else:
            state_keeper[cur_cipher] = 1
        props_cipher = generate_cipher(cur_cipher)
        cur_score = cal_paper_score(cipher_text, cur_cipher,dict_words_nums)
        props_score  = cal_paper_score(cipher_text,props_cipher, dict_words_nums)
        acpt = props_score / cur_score
        u = random.random()
        if acpt > u :
            cur_cipher = props_cipher
        else:
            pass
        if i % 100 == 0 :
            print('Iteration : %d , best visit times : %d and cipher is  ' % (i, max(state_keeper)))
    best_count = max(state_keeper)
    best_state = []
    for k,v in state_keeper:
        if v == best_count:
            best_state.add(k)
    return state_keeper, best_state
    
if __name__ == "__main__":
    paper_dict = create_score_dict(path)
    test_text = "As Oliver gave this first proof of the free and proper action of his lungs, \
the patchwork coverlet which was carelessly flung over the iron bedstead, rustled; \
the pale face of a young woman was raised feebly from the pillow; and a faint voice imperfectly \
articulated the words, Let me see the child, and die. \
The surgeon had been sitting with his face turned towards the fire: giving the palms of his hands a warm \
and a rub alternately. As the young woman spoke, he rose, and advancing to the bed's head, said, with more kindness \
than might have been expected of him: "
    encrypt_key = 'XEBPROHYAUFTIDSJLKZMWVNGQC'
    cipher_text = apply_cipher_on_text(test_text, encrypt_key)
    decrypt_key = ''.join(alphabet[encrypt_key.find(x)] for x in encrypt_key )

    states, best_state = mcmc_decrypt()
    print()
