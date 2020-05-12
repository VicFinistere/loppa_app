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

        if self.name:
            print("New experience for {category}: {name} !".format(category=self.category, name=self.name))
        else:
            print("New {category} experience !".format(category=self.category))