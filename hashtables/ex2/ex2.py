#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def __str__(self):
        return self.source


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """

    for i in range(length):
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)

    for j in range(length):
        current_loc = hash_table_retrieve(hashtable, tickets[j].source)
        last_loc = hash_table_retrieve(hashtable, tickets[j-1].destination)
        print(hash_table_retrieve(hashtable, tickets[j].source))
        print(hash_table_retrieve(hashtable, tickets[j-1].destination))
        # if tickets[j].source == None:
        #     route.insert(0, tickets[j].destination)
        if hash_table_retrieve(hashtable, current_loc) and current_loc == tickets.destination:
            print("worked")
            route[j] = (current_loc)
            
    while "NONE" in route: route.remove("NONE")

    print(route)
    return route
    
ticket_1 = Ticket("PIT", "ORD")
ticket_2 = Ticket("XNA", "SAP")
ticket_3 = Ticket("SFO", "BHM")
ticket_4 = Ticket("FLG", "XNA")
ticket_5 = Ticket("NONE", "LAX")
ticket_6 = Ticket("LAX", "SFO")
ticket_7 = Ticket("SAP", "SLC")
ticket_8 = Ticket("ORD", "NONE")
ticket_9 = Ticket("SLC", "PIT")
ticket_10 = Ticket("BHM", "FLG")

tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
            ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]


reconstruct_trip(tickets, 10)
