class book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.is_borrowed=False


    def borrow(self):
       self.is_borrowed=True
       print(f"confirmation:{self.title} has been sucsessfully been borrowed")


    def returnbook(self):
        self.is_borrowed=False
        print(f"confirmation:{self.title} has been sucseesfully been returned")


    def checkavailibility(self):
        if self.is_borrowed==True:
            print(self.title,"is not available")
        else:
            print(self.title,"is available")








book1=book("harry potter","J.K rowling")
book2=book("wimpy kid","jeff kinney")
book3=book("captain underpants","david williams")


print("-----------LIBRARY SYSTEM---------------")
book1.checkavailibility()
book1.borrow()
book1.checkavailibility()
book1.returnbook()
book1.checkavailibility()

book2.checkavailibility()
book2.borrow()
book2.checkavailibility()
book2.returnbook()
book2.checkavailibility()



book3.checkavailibility()
book3.borrow()
book3.checkavailibility()
book3.returnbook()
book3.checkavailibility()
