def load_tasks():
    with open("todos.txt","r") as f:
        return f.readlines()

def save_tasks(to_dos):
    with open("todos.txt","w") as f:
        f.writelines(to_dos)
  
      
if __name__=="__main__":
    print("This is executed from root script")
