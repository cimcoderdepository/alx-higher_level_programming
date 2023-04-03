#!/usr/bin/python3
"""Isaac Asimov devised and introduced the so-called "Three Laws of Robotics" in 1942. The appeared in his story "Runaround". His three laws have been picked up by many science fiction writers. As we have started manufacturing robots in Python, it's high time to make sure that they obey Asimovs three laws. As they are the same for every instance, i.e. robot, we will create a class attribute Three_Laws. This attribute is a tuple with the three laws."""

class Robot:
    Three_Laws = (
    """A robot may not injure a human being or, through inaction, allow a human being to come to harm.""",
    """A robot must obey the orders given to it by human beings, except where such orders would conflict with the First Law.,""",
    """A robot must protect its own existence as long as such protection does not conflict with the First or Second Law."""
    )
    def __init__(self, name, build_year):
        self.name = name
        self.build_year = build_year
    # other methods as usual

    """As we mentioned before, we can access a class attribute via instance or via the class name. You can see in the following that we don't need an instance:"""
