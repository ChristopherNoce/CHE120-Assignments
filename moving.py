def move_list(a_list, n):
    """
    this function moves the entries in the list by n values and returns the new list
    
    For example:
        
     >>>move_list([1,2,3,4,5], 2)
[4, 5, 1, 2, 3]
>>>move_list([1,2,3,4,5], -2)
[3, 4, 5, 1, 2]
>>>move_list([1,2,3,4,5], 7)
[4, 5, 1, 2, 3]
>>>move_list(['a','b','hello',3,4], 2)
[3, 4, 'a', 'b', 'hello']   
    """
    if type(a_list) != list: #if it's not a list, its invalid
        return None
    elif type(n) != int: #if n isnt an integer, it is invalid. Ex: you can't move an entry 2.5 places over (if n is a float)
        return None

    new_list = a_list[-n:] + a_list[0:-n] #this takes the last n (use negative because it takes the last n) entries of the list and then adds the remaining entries (from 0 to -n) to form a new list    
    return new_list
    

if __name__ == "__main__":
    #tests
    print(move_list([1,2,3,4,5], 2)) 
    print(move_list([1,2,3,4,5], -2))
    print(move_list(["CHE120","CHE100","MATH115","CHE102","MATH116"], 7))
    print(move_list(['hello',5,[1,2,3,4,5],3,"4"], 2))