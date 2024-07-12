import bloomdata.helper_functions as hf

# 1st Pair of lists 
adjectives = ['blue', 'large', 'grainy', 
              'substantial', 'potent', 'thermonuclear']

nouns = ['food', 'house', 'bycicle', 'toupee', 'phone']

# 2nd Pair of Lists 

list1 = [1, 2, 3]
list2 = [4, 5, 6]

def test_random_phrase():
    assert type(hf.random_phrase(adjectives, nouns)) == str
    assert type(hf.random_phrase(list1, list2)) == str
    assert hf.random_phrase(['Ricardo'], ['Ruiz']) == 'Ricardo Ruiz'
    assert hf.random_phrase([1], [2]) == '1 2'

