from Category import Category


class Dictionary:
    """
    Dictionary
    """

    def __init__(self):
        """
        Dictionary
        """
        self.amount_of_categories = 0
        self.list_of_categories = []

    # Create category
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

    # Get or create category
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

    # Update category
    def update_category(self):
        """
        Update category
        """

    # Delete category
    def delete_category(self):
        """
        Delete category
        """