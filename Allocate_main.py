from pip._vendor.distlib.compat import raw_input
import InstanceAvail
import calculateCost
if __name__ == '__main__':
    hours = cpus = price = -1
    instances = InstanceAvail.instanceAvail
    print("Please enter a value")
    print("1) Get Cost with minimum (C)CPU and (H)Hours")
    print("2) Get maximum price P will be paid for H Hours")
    print("3) Combination of both");
    input_value = raw_input("Enter : ")
    if(input_value == '1' ):
        hours = int(raw_input("Enter the hours : "))
        cpus = int(raw_input("Enter the CPUS :"))
        calculateCost.get_costs(instances,hours,cpus,price),
    elif input_value == '2' :
        hours = int(raw_input("Enter the hours : "))
        price = float(raw_input("Enter the price :"))
        calculateCost.get_costs(instances,hours,cpus,price),
    elif input_value =='3' :
        hours = int(raw_input("Enter the hours : "))
        cpus = int(raw_input("Enter the CPUS :"))
        price = float(raw_input("Enter the price :"))
        calculateCost.get_costs(instances,hours,cpus,price),
    else :
        print('Incorrect Values')
        exit(0)
