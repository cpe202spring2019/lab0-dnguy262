def weight_on_planets():
   # write your code here
    weight = int(input("What do you weigh on earth? "))
    mars_weight = weight * 0.38
    jupiter_weight = weight * 2.34
    string = "\nOn Mars you would weigh {} pounds.\nOn Jupiter you would weigh {} pounds."
    print(string.format(mars_weight, jupiter_weight))
    
   
   
if __name__ == '__main__':
   weight_on_planets()
