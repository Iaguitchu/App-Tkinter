from tkinter import *
from tkinter.font import Font
from dataManagement import *

class MyStockManager:
    def __init__(self):

        #CONFIGURAÇÕES
        TK_WINDOW_WIDTH = 700
        TK_WINDOW_HEIGHT = 600

        FRAME_SEARCH_WIDTH = TK_WINDOW_WIDTH
        FRAME_PRODUCTS_WIDTH = TK_WINDOW_WIDTH
        FRAME_ADD_DEL_WIDTH = TK_WINDOW_WIDTH

        FRAME_SEARCH_HEIGHT = int(TK_WINDOW_HEIGHT * 5 / 100)
        FRAME_PRODUCTS_HEIGHT = int(TK_WINDOW_HEIGHT * 90 / 100)
        FRAME_ADD_DEL_HEIGHT = int(TK_WINDOW_HEIGHT * 5 / 100)

        #VARIAVEIS GLOBAIS
        self._defineGlobalVars()
        


        self.window = Tk()
        self._defineGlobalFonts()
        root = self.window

        root.title('My Products Stock Manager')
        root.geometry(f'{TK_WINDOW_WIDTH}x{TK_WINDOW_HEIGHT}+300+100')
        root.resizable(width= False, height=False)

        frameSearch = Frame(master = root, width=FRAME_SEARCH_WIDTH, height= FRAME_SEARCH_HEIGHT, )
        frameProducts = Frame(master = root, width=FRAME_PRODUCTS_WIDTH, height= FRAME_PRODUCTS_HEIGHT, )
        frameAddDelete = Frame(master = root, width=FRAME_ADD_DEL_WIDTH, height= FRAME_ADD_DEL_HEIGHT, )
        
        frameSearch.pack()
        frameProducts.pack()
        frameAddDelete.pack()

        self._BuildFrameSearchContent(frameSearch)
        self._BuildFrameProductsContent(frameProducts)
        self._BuildFrameAddDeleteContent(frameAddDelete)

        root.mainloop()
        ...
    def _defineGlobalFonts(self):
        from tkinter.font import families

        self.f_TimesBold = Font(family='Times', size=12, weight= 'bold')
        self.f_Times = Font(family='Times', size=12)
        self.f_BookAntiq = Font(family='Book Antiqua', size=12)
          


    def _defineGlobalVars(self):
        self.g_SPINBOX_SEARCH_VAL = 300
        self.g_SPINBOX_SEARCH_MIN = 3
        self.g_SPINBOX_SEARCH_MAX = 5000

        self.g_MAX_ITEMS_PER_PAGE = 4
        self.g_PRODUCTS_COL_FRAMES = []
        self.g_currentPage = 1


    def _BuildFrameSearchContent(self, parent: Frame):
            
            lblName = Label(master= parent, text='Product Name:',# font= 'Times 23 bold',
                             font = self.f_TimesBold)

            entryName = Entry(master= parent, justify='center', bd=2, font= self.f_BookAntiq)
            
            lblStock = Label(master= parent, text='Stock Bellow:', font= self.f_TimesBold)

            var = IntVar(value=self.g_SPINBOX_SEARCH_VAL)
            spinboxStock = Spinbox(master= parent,bd= 2, from_= self.g_SPINBOX_SEARCH_MIN, to= self.g_SPINBOX_SEARCH_MAX,
                                   justify='right', width=9, state= 'readonly', increment= 3, textvariable= var, font= self.f_BookAntiq)

            btnSearch = Button(master= parent, text= 'Search', command= lambda  x = entryName, y=var:  self._action_search(x,y), 
                               font= self.f_Times)

            btnClear = Button(master= parent, text= 'Clear', command= lambda  x = entryName, y=var:  self._action_clear(x,y), font= self.f_Times)

            lblName.pack(side= LEFT, padx= (0,10))
            entryName.pack(side= LEFT, padx= (0,10))

            lblStock.pack(side= LEFT, padx= (10,10))
            spinboxStock.pack(side= LEFT, )
            
            btnSearch.pack(side= LEFT,padx= (20,20))
            btnClear.pack(side= LEFT, )

            ...

    def _BuildFrameProductsContent(self, parent: Frame):

        parentWidth     = parent.winfo_reqwidth()
        parentHeight    = parent.winfo_reqheight()

        frameProdsListWidth = parentWidth
        framePagesNavWidth  = parentWidth

        frameProdsListHeight    = int(parentHeight * 95 / 100)
        framePagesNavHeight     = int(parentHeight *  5 / 100)

        frameProdsList = Frame(master= parent,
            width= frameProdsListWidth, height= frameProdsListHeight,
            # bg= 'red'
        )
        framePagesNav = Frame(master= parent,
            width= framePagesNavWidth, height= framePagesNavHeight,
            # bg= 'purple'
        )

        frameProdsList.pack()
        framePagesNav.pack()

        self._BuildFrameProdsListContent(frameProdsList)
        self._BuildFramePagesNavContent(framePagesNav)


        self._load_productsList()
        self._load_pagesNav()   
    
    def _BuildFrameProdsListContent(self, parent: Frame):

        parentWidth = parent.winfo_reqwidth()
        parentHeight= parent.winfo_reqheight()

        pHeight = parentHeight - self.g_MAX_ITEMS_PER_PAGE - 1
        frameProdRowHeight = int(pHeight / self.g_MAX_ITEMS_PER_PAGE)

        def addFrameSeparator():
            Frame(master= parent, width=parentWidth, height=1, bg='grey').pack()
            

        colors = ['orange','purple','green','red']
        addFrameSeparator()
        for i in range(self.g_MAX_ITEMS_PER_PAGE):
            frameProdRow = Frame(master=parent, width=parentWidth, height= frameProdRowHeight, #bg= colors[i]
                                  highlightbackground='grey', )
            frameProdRow.pack()
            addFrameSeparator()
            self._BuildFrameProdsListRowContent(frameProdRow)
        

        

    def _BuildFrameProdsListRowContent(self, parent: Frame):
        parentsWidth = parent.winfo_reqwidth() #largura requerida
        parentHeight = parent.winfo_reqheight() #altura requerida

        framesColumnsWidthList = [
             parentsWidth * 20/100,
             parentsWidth * 60/100,
             parentsWidth * 10/100,
             parentsWidth * 10/100
        ]

        self.g_PRODUCTS_COL_FRAMES.append([])
        for colWidth in framesColumnsWidthList:
             frameColumn = Frame(master = parent, width= colWidth, height= parentHeight,) # highlightbackground='black', highlightthickness=1,  => usado para fazer linha
             
             frameColumn.pack(side = LEFT)
            
             self.g_PRODUCTS_COL_FRAMES[-1].append(frameColumn)


        ...
        
    def _BuildFramePagesNavContent(self, parent: Frame):
        btnPrevPag = Button(master=parent, text= '<<', command= self._action_movePrevPage)
        btnPrevPag.pack(side= LEFT)

        lblCurrentPageOfN = Label(master = parent, text= '1 of 2')
        lblCurrentPageOfN.pack(side= LEFT)

        btnNextPage = Button(master= parent, text= '>>', command= self._action_moveNextPage)
        btnNextPage.pack(side= LEFT)
    
  
            
    def _BuildFrameAddDeleteContent(self, parent: Frame):
        
        btnAddProduct = Button(master=parent, text= 'Add Product', command=self._action_addProduct)
        
        btnDeleteProdutcs = Button(master=parent, text= 'Delete Product', command=self._action_deleteProducts, state= DISABLED)
        btnAddProduct.pack(side= LEFT)
        btnDeleteProdutcs.pack(side= RIGHT)


    def _load_productsList(self):
        products = DataManager.get(
             self.g_MAX_ITEMS_PER_PAGE,
             self.g_currentPage,
             #TODO - nomes do estoque
        )
        
        for idx, product in enumerate(products):
            rowColsFrames = self.g_PRODUCTS_COL_FRAMES[idx]

            self._load_productRow(rowColsFrames, product)
            
        #print(rowColsFrames)
        #print(product)
    def _load_productRow(self, rowColsFrame, product: Product):
         

        self._load_image(rowColsFrame[0], product)
        self._load_nameDesc(rowColsFrame[1], product)
        self._load_stockQuantity(rowColsFrame[2], product)
        self._load_deleteCheckButton(rowColsFrame[3], product)   
        
        

    def _load_image(self, parent: Frame, product: Product):    
        ...

    def _load_nameDesc(self, parent: Frame, product: Product):
        
        parentWidth = parent.winfo_reqwidth()
        parentHeight = parent.winfo_reqheight()

        frameNameHeight = int(parentHeight * 10/100)
        frameDescHeight = int(parentHeight * 90/100)

        frameName = Frame(master = parent, width= parentWidth, height = frameNameHeight,)
        frameDesc = Frame(master = parent, width= parentWidth, height=frameDescHeight)
        frameName.pack()
        frameDesc.pack()
        
        lblName = Label(master= frameName, text= product.name, font= self.f_TimesBold)
        lblDesc = Label(master= frameDesc, text= product.description, font= self.f_BookAntiq)

        print(product.name)

        lblName.pack()
        lblDesc.pack()

    def _load_stockQuantity(self, parent:Frame, product: Product):
        ...

    def _load_deleteCheckButton(self, parent:Frame, product: Product):
        ...

    def _load_pagesNav(self):
         ...

    #-----------------ACTIONS---------------------------------
        
    def _action_movePrevPage(self):
         ...
         
    def _action_moveNextPage(self):
         ...

    def _action_search(self, name: Entry, stock:IntVar):
          print(f'action search {name.get()} - {stock.get()}')
    
    def _action_clear(self, name: Entry, stock:IntVar):
          print(f'action clear {name.get()} - {stock.get()}')

    def _action_addProduct(self):
         print('action addProduct')
         ...

    def _action_deleteProducts(self):
          print('action Delete Products')

        
MyStockManager()
        