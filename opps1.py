from OOPS import User
from post import Post
user_one=User("atish.com","atish",26,"tcs")   
user_one.get_user_info()

user_one.change_job_title("devops engineer")
user_one.get_user_info()

user_two=User("samu.com","samu",26,"cogni")
user_two.get_user_info()

post1=Post("i am boom","dj")      
post1.get_post_info()
            