# Cooper Lappenbusch for Deliverr
class inventoryAllocator:
    def __init__(self, warehouses):
        self.warehouseList = warehouses

    def testOrderedItems(self, orderedItems):
        print("Warehouse List " + str(self.warehouseList))
        print("Items input " + str(orderedItems))
        outputArr = []
        currentDict = {}
        fulfilled = {}
        for warehouse in self.warehouseList:
            for item in list(orderedItems):
                if item in warehouse["inventory"]:
                    if item not in currentDict:
                        currentDict[item] = 0
                    if item in orderedItems and item not in fulfilled:
                        if orderedItems[item] > warehouse["inventory"][item]:
                            orderedItems[item] -= warehouse["inventory"][item]
                            currentDict[item] += warehouse["inventory"][item]
                        else:
                            orderedItems[item] -= warehouse["inventory"][item]
                            currentDict[item] += warehouse["inventory"][item]
                            del orderedItems[item]
                            fulfilled[item] = 1
            if currentDict != {}:
                outputArr.insert(0, {warehouse["name"]: currentDict})
            currentDict = {}
        if orderedItems != {}:
            print("ORDER COULD NOT BE FULFILLED")
            print("Test Output []")
            return []
        print("Test Output " + str(outputArr))
        return outputArr


def main():
    print("Program created by Cooper Lappenbusch for Deliverr")
    print("--------------------------------------------------")
    print("Test 1 PASSED")
    inventory = inventoryAllocator([{"name": "owd", "inventory": {"apple": 5, "orange": 10}}, {
                                   "name": "dm:", "inventory": {"banana": 5, "orange": 10}}])
    inventory.testOrderedItems({"apple": 5, "banana": 5, "orange": 5})
    print("--------------------------------------------------")

    print("Test 2 PASSED")
    inventory = inventoryAllocator([{"name": "owd", "inventory": {"apple": 5, "orange": 10}}, {
                                   "name": "dm:", "inventory": {"orange": 10}}])
    inventory.testOrderedItems({"apple": 5, "banana": 5, "orange": 5})
    print("--------------------------------------------------")

    print("Test 3 PASSED")
    inventory = inventoryAllocator(
        [{"name": "owd", "inventory": {"apple": 1}}])
    inventory.testOrderedItems({"apple": 1})
    print("--------------------------------------------------")
    print("Test 4 PASSED")
    inventory = inventoryAllocator(
        [{"name": "owd", "inventory": {"apple": 0}}])
    inventory.testOrderedItems({"apple": 1})
    print("--------------------------------------------------")
    print("Test 5 PASSED")
    inventory = inventoryAllocator([{"name": "owd", "inventory": {"apple": 5}}, {
                                   "name": "dm", "inventory": {"apple": 5}}])
    inventory.testOrderedItems({"apple": 10})


main()
