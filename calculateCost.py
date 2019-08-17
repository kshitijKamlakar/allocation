from get_cost_per_server import get_Data, get_Cost_1 , get_Cost_2 , get_Cost_3
def get_costs(instances,hours,cpus,price):
        if price == -1 :
            result = get_Cost_1(instances,hours,cpus)
            print(result)
        elif cpus == -1 :
            result = get_Cost_2(instances,hours,price)
            print(result)
        else :
            result  = get_Cost_3(instances,hours,price)
            print(result)

