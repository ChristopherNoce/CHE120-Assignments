#Christopher Noce | 21143999


def mad_libs_generator(adjective, noun, verb, place, get_input=False):
    """
    This function is a recreation of Mad Libs. There is a story template and the user can input words to fill in the blanks.
    Examples: 
        
        Welcome to Mad Libs!

        Here's your story:

        It was a dark night and the studious student remebered they had a midterm in an hour that they didn't study for. To prepare, the student went to library to study.
        Welcome to Mad Libs!

        Here's your story:

        Enter an adjective: magical
        Enter a noun: dog
        Enter a verb: run
        Enter a place: park
        It was a dark night and the magical dog remebered they had a midterm in an hour that they didn't study for. To prepare, the dog went to park to run.
    
        """#docstring
    print("Welcome to Mad Libs!")
    
    print("\nHere's your story:\n")
    
    if get_input == True: #if get_input is True, I want it to get the user to input an adjective, noun, verb, & place
        adjective = input("Enter an adjective: ") #receives user input
        noun = input("Enter a noun: ")
        verb = input("Enter a verb: ")
        place = input("Enter a place: ")
    story = print(f"It was a dark night and the {adjective} {noun} remebered they had a midterm in an hour that they didn't study for. To prepare, the {noun} went to {place} to {verb}.") #formatted strings make it easier to embed variables

if __name__=='__main__':
    mad_libs_generator('studious', 'student', 'study', 'library')
    mad_libs_generator('studious', 'student', 'study', 'library', get_input = True)
