"""reference book python crash course : passage 147 9-4"""
class Restruant():
    """ a restruant"""

    def __init__(self, name, cusine_type):
        """constructor"""
        self.name = name
        self.cusine_type = cusine_type
        self.number_served = 0

    def describe_restruant(self):
        """describe restruant"""
        print("resruant name:" + self.name)
        print("cusine_type:" + self.cusine_type)

    def open_restruant(self):
        """open restruant"""
        print("open restruant")

    def print_restruant_num(self):
        #print served people number
        print("There are " + str(self.number_served) + " people")

    def set_number_served(self, num_people):
        #set served people
        if num_people >= 0:
            self.number_served = num_people
        else:
            print("you can't set a negative number")


    def increment_number_served(self, increase_num):
        #increase served people
        if increase_num >= 0:
            self.number_served += increase_num
        else:
            print("you can't add a negative number")


#main function

job_restruant = Restruant('job', 'huoGuo')
job_restruant.describe_restruant()
job_restruant.open_restruant()
job_restruant.print_restruant_num()

job_restruant.set_number_served(20)
job_restruant.print_restruant_num()

job_restruant.increment_number_served(50)
job_restruant.print_restruant_num()

