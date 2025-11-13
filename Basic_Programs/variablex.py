def Display(*A):
    print("Inside Display",A)
    print(type(A))
   
    
def main():
    Display(11,21,51,101)
    Display(11,21,51,101,151)
    Display(11,21,51)
    Display(11)
    Display()
    
if __name__ == "__main__":
    main()