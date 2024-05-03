
class Product:

    def __init__(self,
        id= None,
        imgPath= '',
        name= '',
        description= '',
        stockQuantity= 0,
    ):
        self.id             = id
        self.imgPath        = imgPath
        self.name           = name
        self.description    = description
        self.stockQuantity  = stockQuantity
        ...
    # END def __init__
    ...
# END class Product

class DataManager:

    MEM_DB = [
        Product(1, 'pics/apple.png', 'Apple', 'One Apple a day keep the doctor away!', 10),
        Product(2, 'pics/banana.jpeg', 'Banana', 'Is yellow!', 4000),
        Product(3, 'pics/avocato.jpeg', 'Avocato', 'Very Healthy', 8),
        Product(4, 'pics/orange.jpeg', 'Orange', 'Juicy', 8),

        Product(5, 'pics/pineapple.jpeg', 'Pineapple', 'Sweet', 8),
        Product(6, 'pics/kiwi.jpg', 'Kiwi', 'Is green!', 23),
        Product(7, 'pics/strawberry.jpeg', 'Strawberry', 'Is red', 8),
        Product(8, 'pics/lemon.png', 'Lemon', 'Vitamin C', 8),
        
        Product(9, 'pics/mango.png', 'Mango', 'Is orange inside!', 8),
    ]

    def get(maxItemsPerPage, pageNumber, 
        # TODO - name and stock below 
    ):

        startIdx    = maxItemsPerPage * (pageNumber - 1)
        endIdx      = startIdx + maxItemsPerPage

        data = DataManager.MEM_DB

        # TODO - filter data

        return data[startIdx : endIdx]
        ...
    # END def get               
    ...
# END class DataManager