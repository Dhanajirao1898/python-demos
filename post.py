class Post:
    def __init__(self,message,author):
        self.message=message
        self.author=author

    def get_post_info(self):
        print(f"post: {self.message} written by {self.author}")  

post1=Post("i am boom","dj")      
post1.get_post_info()