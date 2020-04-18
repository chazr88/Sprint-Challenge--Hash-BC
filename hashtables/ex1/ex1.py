#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    #Store them in the Hash Table
    for i in range(length):
        hash_table_insert(ht, weights[i], i)

    for j in range(length):
        answer = limit - weights[j]
        if hash_table_retrieve(ht, answer):
            print(j, hash_table_retrieve(ht, answer))
            if weights[j] > answer:
                print ((j, hash_table_retrieve(ht, answer)))
                return ((j, hash_table_retrieve(ht, answer)))
            else:
                print ((hash_table_retrieve(ht, answer), j))
                return ((hash_table_retrieve(ht, answer), j))
    return None

    # for j in range(length - 1):
    #     if limit - limit == limit:
    #         print("we did it")
        
    #print(hash_table_retrieve(ht, 15))
        # firstIndex += 1
        # for j in weights:
        #     if j + i == limit:
        #         print (weights[i])
    #When we add those numbers we can see if they = the limit
    #Return false until the = the limit
    #Return the 2 indexes if they = the limit


    return None

weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
get_indices_of_item_weights(weights_4, 9, 7)
# weights_2 = [4, 4]
# get_indices_of_item_weights(weights_2, 2, 8)
# ht = HashTable(2)
# hash_table_insert(ht ,0, 12)
# hash_table_insert(ht ,1, 22)
# hash_table_insert(ht ,0, 42)
# print(hash_table_retrieve(ht, 1))


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
