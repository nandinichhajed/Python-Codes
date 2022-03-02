class RailwayForm:
    formType = "RailwayForm"
    
    def printData(self):
        print(f"name of the applicant is {self.name}")
        print(f"name of the train is {self.train}")
        
Application = RailwayForm()
Application.name = "Nandini"
Application.train = "express"

Application.printData()