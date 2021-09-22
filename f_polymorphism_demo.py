# This program demonstrates polymorphism.

import f_animals as animals

def show_mammal_info(creature):
    if isinstance(creature,animals.Mammal):
        creature.show_species()
        creature.make_sound()
        #checking to see if object belongs to mammal class
    else:
        print("that is not a mammal.")

def main():
    # Create a Mammal object, a Dog object, and
    # a Cat object.
    mammal = animals.Mammal('regular animal')
    dog = animals.Dog()
    cat = animals.Cat()


    # Display information about each one.
    print('Here are some animals and')
    print('the sounds they make.')
    print('--------------------------')

    '''
    mammal.show_species()
    mammal.make_sound()

    print()

    dog.show_species()
    dog.make_sound()

    print()

    cat.show_species()
    cat.make_sound()
'''
# Call the main function.


    show_mammal_info(mammal)
    print()

    show_mammal_info(dog)
    print()

    show_mammal_info(cat)
    print()

    mouse = 'I am a mouse'
    show_mammal_info(mouse)
    #it is a string object so it is not a part of the mammal group. Make sure it is an instance of that class
    #there is not a show_species in string object 

main()