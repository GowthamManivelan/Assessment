#Author: Gowtham Manivelan
#Problem Statement : Processing sales report of the individual products
#Date: 05/18/2018
import csv
import sys
import operator
ProductList = []
SalesList = []
ProductReportList = []
final_list = []
#Class to store all the product list from csv
class Product:
   def __init__(self, id, name,price,Quantity):
      self.id = id
      self.name = name
      self.price=price
      self.Quantity = Quantity

with open(sys.argv[1], 'rb') as f:
    productMaster = csv.reader(f)
    for row in productMaster:
        product = Product(row[0],row[1],row[2],row[3])
        ProductList.append(product) #ProductList now has all the inputs from csv
#Class to store all the sales list from csv
class Sales:
     def __init__(self, SaleId, ProductId,TeamId,Quantity):
      self.SaleId = SaleId
      self.ProductId = ProductId
      self.TeamId= TeamId
      self.Quantity = Quantity

with open(sys.argv[2], 'rb') as f:
    sales = csv.reader(f)

    for row in sales:
        sales = Sales(row[0],row[1],row[2], row[3])
        SalesList.append(sales)
#Class to generate product report
class ProductReport:
      def __init__(self, ProductId,ProductName,GrossRevenue,TotalUnits):
       self.ProductId = ProductId
       self.ProductName = ProductName
       self.GrossRevenue= GrossRevenue
       self.TotalUnits = TotalUnits

#Perform mathematical calculations for each product.
for product in ProductList:
    for sales in SalesList:
        if product.id==sales.ProductId :
            product.totalUnits =int(sales.Quantity) *  int( product.Quantity) 
            product.GrossRevenue = float(product.price) *  float(product.totalUnits)
            report = ProductReport(product.id,product.name,product.GrossRevenue,product.totalUnits)
            ProductReportList.append(report)
            
#Now we have individual sales list for each product, product will have multiple instances as follows
#1 Minor Widget 625.0 2500
#1 Minor Widget 62.5 250
#2 Critical Widget 250.0 50
#3 Complete System (Basic) 500.0 1
#3 Complete System (Basic) 1000.0 2

#To generate consolidated sales report for each product.
consolidated = []
for i in range(len(ProductReportList)):
    isAvailable = False
    availableindex=0
    for j in range(len(consolidated)):
        if(ProductReportList[i].ProductId==consolidated[j].ProductId):
            isAvailable=True
            availableindex=j
    if isAvailable:
        consolidated[availableindex].GrossRevenue= consolidated[availableindex].GrossRevenue+ProductReportList[i].GrossRevenue
        consolidated[availableindex].TotalUnits= consolidated[availableindex].TotalUnits+ProductReportList[i].TotalUnits
    else:
        consolidated.append(ProductReportList[i])


consolidated.sort(key=lambda x: x.GrossRevenue, reverse=True) #Sorting in descending order based on the Gross revenue

#Writing to the output file 
with open(sys.argv[3], 'w') as the_file:
    the_file.write('ProductName,GrossRevenue,TotalUnits\n')
    for consolidatedReport in consolidated:
        the_file.write(consolidatedReport.ProductName+','+str(consolidatedReport.GrossRevenue)+','+str(consolidatedReport.TotalUnits))
        the_file.write('\n')

the_file.close
#Sample output
#ProductName,GrossRevenue,TotalUnits
#Complete System (Basic),1500.0,3
#Minor Widget,687.5,2750
#Critical Widget,250.0,50




       

    

   

    

   
          



 

    
   
               


               

    



