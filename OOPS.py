class User:
    def __init__(self,mail,user_name,age,job):
        self.mail=mail
        self.name=user_name
        self.age=age
        self.job=job

    def change_password(self,new_password):
        self.password=new_password

    def change_job_title(self,new_job_title):
        self.job=new_job_title

    def get_user_info(self):
        print(f"user {self.name} currently working in {self.job} you will contact him {self.mail}\n")    

         




