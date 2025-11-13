def CalculatePercentage(Obtained,Total=500):
    output=(Obtained/Total)*100
    return output

def main():
   
    
    print("Enter obtained marks:")
    Value2=int(input())
    
    result=CalculatePercentage(Value2) #default argument
    
    print("Percentage is:",result)
    
if __name__ == "__main__":
    main()