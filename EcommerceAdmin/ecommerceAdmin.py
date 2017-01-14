import random

class Product:

    brands = ['Samsung', 'Lenovo', 'Apple']
    
    
    def __init__(self, model, price, prCamera, color, brandId):
        self.model = model
        self.price = price
        self.prCamera = prCamera
        self.color = color
        
        self.id = random.randint(1, 100)
        self.brand = Product.brands[brandId]

    @property
    def briefDescription(self):
        return 'ID: {5}\n\
Brand: {4}\n\
Model: {0}\n\
Price: {1}$\n\
Color: {2}\n\
Primary camera: {3} px\n'.format(self.model, self.price, self.color, self.prCamera, self.brand, self.id )

    @briefDescription.setter
    def briefDescription(self, adjust):
        self.model, self.price, self.prCamera, self.color,  self.brand = adjust

    @briefDescription.deleter
    def briefDescription(self):
        del self.model
        del self.price
        del self.prCamera
        del self.color
        del self.brand
        del self.id

def createProduct():
    productModel = input('Type product model: ')
    productPrice = input('Type product price: ')
    productPrCamera = input('Type product camera pixel: ')
    productColor = input('Type product color: ')
    productBrand = int(input('Select product brand. Type number of brand(0 - Samsung, 1 - Lenovo, 2 - Apple): '))
    new_obj = Product(productModel, productPrice, productPrCamera, productColor, productBrand)
    productStorage[new_obj.id] = new_obj

def createEditProduct(prodId):
    productModel = input('Type product model: ')
    productPrice = input('Type product price: ')
    productPrCamera = input('Type product camera pixel: ')
    productColor = input('Type product color: ')
    productBrand = int(input('Select product brand. Type number of brand(0 - Samsung, 1 - Lenovo, 2 - Apple): '))
    edit_obj = productStorage[prodId]
    edit_obj.briefDescription = productModel, productPrice, productPrCamera, productColor, Product.brands[productBrand]
    productStorage[prodId] = edit_obj

if __name__ == '__main__':
    productStorage = dict()
    continueProgram = False

    while not continueProgram:
        print('{:_^100}'.format(''))
        print('{:^100}'.format('Main manu'))
        print()
        print('{:^100}'.format('Please choose program mod by specifying mod\'s number'))
        print()
        try:
            modSelection = int(input('{:^100}'.format('1- Show_all_product  2-Add_new_product  3-Edit_product  4-Delete_product  5-Exit')))
            print('{:_^100}'.format(''))

            if modSelection == 1:
                if productStorage:
                    print()
                    print('{:^100}'.format('All Products:'))
                    for id in productStorage:
                        print(productStorage[id].briefDescription)
                else:
                    print()
                    print('{:^100}'.format('Product storage is empty...'))

            elif modSelection == 2:
                createProduct() 
                print()
                print('{:^100}'.format('Success!! New product added to product storage.'))

            elif modSelection == 3:
                print()
                productIdToEdit = int(input('Specify id of product you want to edit: '))
                createEditProduct(productIdToEdit)
                print()
                print('{:^100}'.format('Success!! Product has been just edited.'))

            elif modSelection == 4:
                print()
                productIdToDelete = int(input('Specify id of product you want to delete: '))
                del productStorage[productIdToDelete]
                print()
                print('{:^100}'.format('Success!! Product has been successfully deleted.'))

            elif modSelection == 5:
                continueProgram = True

            else:
                print('{:^100}'.format('Non-existent mod. Try again.'))

        except:
            print('{:_^100}'.format(''))
            print('{:^100}'.format('Incorrect input. Please be attentive. Try again.'))
            
        