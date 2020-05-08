#!/usr/bin/env python3
# This script is made to be an interactive way to share experiences 

import sys


#Knowledge represents a list of experiences
class Knowledge:

    def __init__(self, name='knowledge', **kwargs):
        """
        Knowledge initialization
        """

        # Initialize experiences list
        self.list_of_experiences = []

        # Initialize experiences counter
        self.length_of_experiences_list = 0
        
        # Knowledge name
        self.knowledge_name=name
        
        # Dictionnary 
        dictionnary = Dictionnary()


    #Create experience
    def add_experience(self, experience_name, experience_category):
        """
        Create a new experience
        param: experience_name : The experience's name
        param: experience_category : The experience's category
        return: void
        """
        
        # CREATE | New experience 
        print("The new experience {experience_name} will be registered !".format(experience_name=experience_name))
        
        # Experience number
        # Incrementation of the list experiences lenght
        self.length_of_experiences_list += 1
        
        # Get or create category
        self.dictionnary.get_or_create_category(experience_category)

        # Create experience
        experience = Experience(self.length_of_experiences_list, experience_name, category)
        
        # Add experience in list 
        self.list_of_experiences.append(experience)
        
        # Experience has been created !
        print("OK : Experience {experience_name} added !".format(experience_name=experience_name))
    

    # Consult experiences
    def list_experiences(self):
        """
        Consult knowledge's experiences
        """
        
        # Amount of experiences
        print("There is {amount_of_experiences} experiences in {knowledge}.".format(
            amount_of_experiences=self.length_of_experiences_list,
            knowledge=self.knowledge_name))
        
        # List experiences
        for experience in self.list_of_experiences:
            print("Exeperience {name} {category}".format(name=experience.name, category=experience.category))
    
    #Read
    def read_experience():
        """
        Consult a registered experience
        """

    #Update
    def update_experience():
        """
        Update a registered experience
        """

    #Delete
    def delete_experience():
        """
        Remove an experience
        """

class Experience:
    """
    Experience
    """

    def __init__(self, experience_id, name='', category='default_category', **kwargs): 
        """
        Experience 
        - id
        - name
        - category
        """

        self.id = experience_id
        self.name = name
        self.category = category
        
        if self.name :
            print("New experience for {category}: {name} !".format(category=self.category, name=self.name))
        else: 
            print("New {category} experience !".format(category=self.category))

class Dictionnary:
    """
    Dictionnary
    """
    
    def __init__(self):
        """
        Dictionnary
        """
        self.amount_of_categories = 0
        self.list_of_categories = []
        
    #Create category
    def create_category(self, category_name):
        """
        Create category
        """
        
        # Increment list of categories
        self.amount_of_categories += 1

        # Index of category
        category_index = self.amount_of_categories
       
        # Create category
        category = Category(category_index, category_name)

        # Add category in dictionnary
        self.list_of_categories.append(category)


    #Get or create category
    def get_or_create_category(self, category_name):
        """
        Get or create category
        param: category_name: The name of category to be get or create
        return: void
        """
        if category_name in self.list_of_categories:
            print("Category {name} already exists".format(name=category_name))
        else:
            print("Category {name} must be created".format(name=category_name))
            self.create_category(category_name)

    #Update category
    def update_category():
        """
        Update category
        """

    #Delete category
    def delete_category():
        """
        Delete category
        """

class Category:
    """
    Category
    """

    def __init__(self, category_index, category_name):
        """
        Category 
        - index
        - name
        """
        self.index=category_index
        self.name=category_name


# Show title 
def show_title():
    """
    Show title
    """

    print("""   
    __    __  __          ___     
    | |   (_) | |        / _ \             
    | |    _| | | __ _  / /_\ \_ __  _ __  
    | |   | | | |/ _` | |  _  | '_ \| '_ \ 
    | |___| | | | (_| | | | | | |_) | |_) |
    \_____/_|_|_|\__,_| \_| |_/ .__/| .__/ 
                  ______      | |   | |    
                 |______|     |_|   |_|    """)


# Show options
def show_options():
    """
    Show options
    """
    
    # Intro
    print("Knowledge is made of experiences which are stored in dictionnary.")
    
    #-----------------------------
    # Categories
    # TODO : Add a counter for categories
    print("There are {amount_of_categories} categories ".format(amount_of_categories=0))
    # READ
    print("                     - Show all categories")

    # ADD
    print("                     - Add a category")
    
    # UPDATE
    print("                     - Update a category")
    
    # DELETE
    print("                     - Remove a category")
    #-----------------------------

    #----------------------------
    # Experiences
    
    # TODO : Add a counter for experiences
    print("There are {amount_of_experiences} experiences ".format(amount_of_experiences=0))
    
    # READ
    # READ ALL
    print("                     - Show all experiences")
    
    # READ ONE
    print("                     - Find an experience")
    
    # ADD
    print("                     - Add an experience")
    
    # UPDATE
    print("                     - Update an experience")
    
    # DELETE
    print("                     - Remove an experience")
    #----------------------------

# Show help
def show_help():
    """
    Show help
    """
    
    # App name
    app_name=sys.argv[0]

    print("This console app will handle your knowlege's request ")
    print("\n")
    print("Basic Usage: ./{}".format(app_name))
    print("Help: ./{} -h ".format(app_name))
    print("\n")
    print("Contributors : ")
    print("                 - Zoé Belleton")
    print("\n")
    print("Contributions are welcomed !")


# App launcher
def run():
    """
    Run the knowledge app
    """
   
    # knowledge.add_experience('experience_for_test')
    # knowledge.list_experiences() 
    
    # Show title
    show_title()

    # Show options 
    show_options()

    #Create
    knowledge = Knowledge('test_knowledge')
    
    #Read

    #Update

    #Delete

if __name__ == '__main__':
    
    # Help
    if sys.argv[1:] and 'h' in sys.argv[1:][0]:
        show_help()
    
    # Launcher
    else:
        # Launch the app
        run()
