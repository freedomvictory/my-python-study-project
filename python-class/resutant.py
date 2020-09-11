"""reference book python crash course : passage 142 9-1"""
class Restruant():
    """ a restruant"""

    def __init__(self, name, cusine_type):
        """constructor"""
        self.name = name
        self.cusine_type = cusine_type

    def describe_restruant(self):
        """describe restruant"""
        print("resruant name:" + self.name)
        print("cusine_type:" + self.cusine_type)

    def open_restruant(self):
        """open restruant"""
        print("open restruant")

"""main function """
job_restruant = Restruant('job', 'huoGuo')
mike_restruant = Restruant('mike', 'luCai')

job_restruant.describe_restruant()
job_restruant.open_restruant()

mike_restruant.describe_restruant()
mike_restruant.open_restruant()

