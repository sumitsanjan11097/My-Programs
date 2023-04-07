import os

def main():
    n = input("Enter the type of file like .pdf: ")
    data = input("Enter the location of file: ")
    files = os.listdir(data)
    i = 1
    for file in (files):
    
        
        if file.endswith(n):
            os.rename(f"{data}/{file}", f"{data}/{i}{n}")
            i +=1
        else:
            print(file)
            
            
if __name__ == "__main__":
    main()
        
            
    
