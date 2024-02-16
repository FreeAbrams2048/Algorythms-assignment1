import sys
import time

ShopList = open('product_data.txt', 'r')
data = ShopList.read()

class ListItems:
    def __init__(self,id,name,price,type):
        self.id=id
        self.name=name
        self.price=price
        self.type=type
    def __str__(self):
        return f"product: {self.id} {self.name}{self.price}{self.type}"
    def __repr__(self):
        return f"product: {self.id} {self.name}{self.price}{self.type}"
    
DataList=data.split("\n")
Items=[]

for i in range(len(DataList)):
    tempList=DataList[i].split(",")
    if(len(tempList)==4):
        tempProd = ListItems(int(tempList[0]),tempList[1],float(tempList[2]),tempList[3])
        Items.append(tempProd)

for item in Items:
    print (item)

def BubbleSort(itemList):
    n=len(itemList)
    for i in range(n-1):
        swapped = False
        for j in range(0,n-i-1):
            if itemList[j].price < itemList[j+1].price:
                swapped=True
                itemList[j], itemList[j+1] = itemList[j+1], itemList[j]
        if not swapped:
            return
        
def Search(itemList, searchFor):
    i = 0
    for product in Items:
        i+=1
        if isinstance(searchFor, float) and product.price == searchFor:
            return product
        elif isinstance(searchFor, int) or isinstance(searchFor, str):
            if str(product.id) == str(searchFor) or product.name == searchFor or product.type == searchFor:
                return product
            
def RemoveItem(itemList, searchFor):
    for product in Items:
        if isinstance(searchFor, float) and product.price == searchFor:
            Items.pop(i)
        elif isinstance(searchFor, int) or isinstance(searchFor, str):
            if str(product.id) == str(searchFor) or product.name == searchFor or product.type == searchFor:
                Items.pop(i)
            
def ModifyProduct(itemList, productToUpdateID, modifyName, modifyPrice, modifyType):
    for product in itemList:
        if product.id == productToUpdateID:
            product.name=modifyName
            product.price=modifyPrice
            product.type=modifyType

def AddProduct(itemList, id, name, price, type):
    tempProd=ListItems(int(id), name, float(price), type)
    Items.append(tempProd)

def analyzeSortPerformance(data, description, time_complexity):
    #print(f"\n{description} - Starting array: {data}")
    start = time.time()
    BubbleSort(data.copy())
    end = time.time()
    space_complexity = sys.getsizeof(data) + sys.getsizeof(start) + sys.getsizeof(end) + 64
    print(f"{description} - Time taken: {end - start:.6f} seconds, Space used: {space_complexity} bytes")
    print(f"Time Complexity: {time_complexity}\n")

AddProduct(Items, 654387, 'Apple, ', 2.98, ' Produce')

for item in Items:
    print (item)

ModifyProduct(Items, 654387, 'Banana', 8.91, 'Produce')
for item in Items:
    print (item)

RemoveItem(Items, 654387)

for item in Items:
    print (item)

result = Search(Items, 36.39)
print(result)

print("\n")

analyzeSortPerformance(Items, "Average", "O(n^2)")
print("\n")
analyzeSortPerformance(Items, "Best case", "O(n)")
print("\n")

reverseList = Items[::-1]

analyzeSortPerformance(Items, "Worst Case", "O(n^2)")