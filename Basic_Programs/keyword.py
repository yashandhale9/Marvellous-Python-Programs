def CalculatePercentage(Total,Obtained):
    output=(Obtained/Total)*100
    return output

def main():
    print("Enter total marks:")
    Value1=int(input())
    
    print("Enter obtained marks:")
    Value2=int(input())
    
    result=CalculatePercentage(Obtained=Value2,Total=Value1) #keyword argument
    
    print("Percentage is:",result)
    
if __name__ == "__main__":
    main()