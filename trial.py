class HealthWorker:
    def __init__(self, clinical_officer, doctor, nurse):
        self.clinical_officer = clinical_officer
        self.doctor = doctor
        self. nurse =  nurse
    def display(self):
        print("Clinical Officer:", self.clinical_officer) 
        print("Doctor:", self.doctor) 
        print("Nurse:", self.nurse) 
#Creating an instance of the Healthworker class    
health_worker = HealthWorker("Terry","Mary","John")  
#displaying the arguments
health_worker.display()   

#Create a class of health workers. Capture self, nurse, doctor, clinical officer. Then, display the arguments
        