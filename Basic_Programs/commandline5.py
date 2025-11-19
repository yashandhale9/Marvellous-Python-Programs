def Addition(No1,No2):
    Ans=0
    Ans=No1+No2
    return Ans

def main():
    Value1=int(input("Enter first number:"))
    Value2=int(input("Enter second number:"))
    
    result=Addition(Value1,Value2)
    
    print("Additon is :",result)
    
        
if __name__ == "__main__":
    main()