class User:
    name = "Bob"
    email_address = "bob@google.com"
    license_number = 123123123

    def __init__(self, name, email_address, license_number):
        self.name = name
        self.email_address = email_address
        self.license_number = license_number

    def __str__(self):
        return "I am {}, my email is {}, and my license number is {}.".format(self.name, self.email_address, self.license_number)

    def interact(self):
        return "interacted!"

    def post(self, post_title, post_date, post_desc):
        new_post = {"post_title": post_title,
                    "post_date": post_date,
                    "post_desc": post_desc}
        Posts.add_post(new_post)


class Posts:
    posts = []

    def add_post(self, post):
        self.posts.append(post)


rob = User("Rob", "rob@gmail.com", 123321123)
print(rob)
