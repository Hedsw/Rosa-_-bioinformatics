def helper(data):
    count = 0
    for i in range(len(data) - 1):
        # Couting the near values in lists
        if int(data[i]) != int(data[i+1]) - 1: # pick up only interger values 
            count += 1 
        else:
            continue
    print(count)
        
if __name__ == "__main__":
    with open('data.txt', 'r') as file:
        # Read a line of data from a txt file.
        data_ = file.readline().strip().split()
        for i in range(len(data_)):
            # Get Data from datasets
            data = [0] + data_ + [len(data_) + 1]
            
    helper(data)