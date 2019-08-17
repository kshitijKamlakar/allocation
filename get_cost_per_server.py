import InstanceAvail
import ServerType
def get_Data(instance) :
    region_data = list(instance.items())
    detailsData = {}
    perticularSeg = {}
    for region,cpu_type in region_data :
        detailsData = {}
        for server in cpu_type :
            perCost = cpu_type[server]/ServerType.serverType.get(server)
            detailsData[server] = perCost
        perticularSeg[region] = detailsData
    return perticularSeg
'''{'us-east': {'large': 0.12, 'xlarge': 0.115, '2xlarge': 0.1125, '4xlarge': 0.09675, '8xlarge': 0.0875, '10xlarge': 0.088125}, 'us-west': {'large': 0.14, '2xlarge': 0.10325, '4xlarge': 0.
11125, '8xlarge': 0.08125, '10xlarge': 0.0928125}}
'''


def get_Cost_1(instances,hours,cpus) :
    temp_data = get_Data(instances)
    result_List = []

    for region,services in temp_data.items() :
        assigned_cpu = total_cost = 0
        result = {}
        result['region'] = region
        tempList = []
        tempTuple = ()
        while(assigned_cpu < cpus ) :
            if assigned_cpu == cpus :
                break
            key_min = min(services.keys(), key=(lambda k: services[k]))  # 8xlarge
            assigned_cpu = float(assigned_cpu + ServerType.serverType.get(key_min))
            if assigned_cpu > cpus :
                assigned_cpu = assigned_cpu - ServerType.serverType.get(key_min)
                toUp = {key_min : 9999}
                services.update(toUp)
                continue
            total_cost = float(total_cost + InstanceAvail.instanceAvail.get(region).get(key_min))
            if(len(tempList) == 0) :
                tempTuple = (key_min, 0)
                tempList.append(tempTuple)

            for value1,value2 in tempList :
                if value1 == key_min:
                    toCheck = (value1,value2)
                    index = tempList.index(toCheck)
                    value2 = value2 +1
                    tempList[index] = (value1, value2 )
                    break

                else :
                    tempTuple = (key_min, 1)
                    tempList.append(tempTuple)
                    break
        total_cost = total_cost * hours
        result['total_cost'] =  '$'+str(total_cost)
        result['services'] = tempList
        result_List.append(result)

    return result_List



def get_Cost_2(instances,hours,price) :
    temp_data = instances
    result_List = []

    for region,services in temp_data.items() :
        assigned_cpu =  0
        result = {}
        result['region'] = region
        temp_hours = 0
        tempList = []
        tempTuple = ()
        temp_cost = total_cost = 0
        while(temp_cost < price and temp_hours < hours ) :
            temp_hours = temp_hours +1
            if temp_cost == price  :
                break
            key_min = min(services.keys(), key=(lambda k: services[k]))  # 8xlarge
            temp_cost = temp_cost + InstanceAvail.instanceAvail.get(region).get(key_min)
            temp_cost = temp_cost * temp_hours

            if temp_cost > price :
                temp_cost = temp_cost /temp_hours
                temp_cost = temp_cost - InstanceAvail.instanceAvail.get(region).get(key_min)
                toUp = {key_min : 9999}
                services.update(toUp)
                continue
            if(len(tempList) == 0) :
                tempTuple = (key_min, 0)
                tempList.append(tempTuple)

            for value1,value2 in tempList :
                if value1 == key_min:
                    toCheck = (value1,value2)
                    index = tempList.index(toCheck)
                    value2 = value2 +1
                    tempList[index] = (value1, value2 )
                    break

                else :
                    tempTuple = (key_min, 1)
                    tempList.append(tempTuple)
                    break
        print(temp_hours)
        result['total_cost'] =  '$'+str(temp_cost)
        result['services'] = tempList
        result_List.append(result)
    return  result_List


def get_Cost_3(instances,hours,price) :
    return  get_Cost_2(instances,hours,price)
