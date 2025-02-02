from collections import deque


class GraphBuilder:
    
    numberOfVertices = 0#decalring numberOfVertices
    adjacencyMatrix = [[0 for x in range (20)] for y in range(20)] #initialising matrix
    
    
    
    defaultDestinations = {
       
        0:'SleetCity',
        1:'EmberFall',
        2:'CinderSpire',
        3:'DustHaven',
        4:'MirageNexus',
        5:'ScorchField',
        6:'BlazePort',
        7:'SolarisReach',
        8:'AetherOasis',
        9:'CrimsonGrit',
        10:'FrostHaven'
        
        
    }
    
    
    def __init__(self, vertices: int):
        self.numberOfVertices = vertices
        
        for i in range(0, self.numberOfVertices):
            for j in range(0, self.numberOfVertices):
                self.adjacencyMatrix[i][j] = 0
    
    def addDefaultEdges(self, matrix: list, vertices: int, node: int, neighbour: int):
        
        n = self.numberOfVertices
        matrix = self.adjacencyMatrix
        x = node
        y = neighbour
        
        if(x>=n) or (y>=n):
            print(" ")
        
        if (x==y):
            print("Cannot connect node to the same node.")
            
        else:
            matrix[x][y] = 1 #adding edge between nodes
            matrix[y][x] = 1 #adding bidirectional feature
            
        return
    
    def BuildDefaultGraph(self):#building default graph with all default locations
        
        matrix = self.adjacencyMatrix
        vertices = self.numberOfVertices
        
        SleetCity = 0
        EmberFall = 1
        CinderSpire = 2
        DustHaven = 3
        MirageNexus = 4
        ScorchField = 5
        BlazePort = 6
        SolarisReach = 7
        AetherOasis = 8
        CrimsonGrit = 9
        FrostHaven = 10
        
        #Setup for Sleet City
        self.addDefaultEdges(matrix, vertices, SleetCity, EmberFall)
        self.addDefaultEdges(matrix, vertices, SleetCity, CinderSpire)
        
        #Setup for Ember Fall
        self.addDefaultEdges(matrix, vertices, EmberFall,DustHaven)
        self.addDefaultEdges(matrix, vertices, EmberFall, MirageNexus)
        
        #Setup for Cinder Spire
        self.addDefaultEdges(matrix, vertices, CinderSpire, MirageNexus)
        self.addDefaultEdges(matrix, vertices, CinderSpire, ScorchField)
        self.addDefaultEdges(matrix, vertices, CinderSpire, BlazePort)
        
        #Setup for Dust Haven
        self.addDefaultEdges(matrix, vertices, DustHaven, SolarisReach)
        self.addDefaultEdges(matrix, vertices, DustHaven, AetherOasis)
        self.addDefaultEdges(matrix, vertices, DustHaven, MirageNexus)
        
        #Setup for Mirage Nexus
        self.addDefaultEdges(matrix, vertices,MirageNexus, AetherOasis)
        
        #Setup for Scorch Field
        self.addDefaultEdges(matrix, vertices, ScorchField, FrostHaven)
        
        #Setup for Aether Oasis
        self.addDefaultEdges(matrix, vertices, AetherOasis, CrimsonGrit)
        self.addDefaultEdges(matrix, vertices, AetherOasis, SolarisReach)
        
        #Setup for Crimson Grit
        self.addDefaultEdges(matrix,vertices, CrimsonGrit, FrostHaven)
        
        #Setup for Frost Haven
        self.addDefaultEdges(matrix, vertices, FrostHaven, BlazePort)
        
        return matrix
        
    def displayMatrix(self, matrix: list):
        #function to display the adjacency matrix without commas and brackets
        print("\n\n Adjacency Matrix:", end ="")
        print("")
        for i in range(0, self.numberOfVertices):#looping in x axis
            print()
            for j in range(0, self.numberOfVertices): #looping in y axis
                print("", matrix[i][j], end= "")#reading value of matrix[a][b] index
                
    def addNewVertex(self, name: str):
        newLocation = name
        self.numberOfVertices = self.numberOfVertices + 1
        self.defaultDestinations.update({self.numberOfVertices:newLocation}) # adding new Location to dictionary
        for i in range(0, self.numberOfVertices):
            self.adjacencyMatrix[i][self.numberOfVertices-1] = 0
            self.adjacencyMatrix[self.numberOfVertices-1][i] = 0
    
    def addNewEdge(self, newNode: int, neighbour: int): # adding new route/edge between 2 different locations
        if(newNode>= self.numberOfVertices) or (neighbour>= self.numberOfVertices):#checking if new node is valid or not
            print("invalid")#message for an invalid input
        if (newNode == neighbour):#check if node are not identical
            print("Same Node")
        else:#updating adjacency matrix
            self.adjacencyMatrix[newNode-1][neighbour] = 1#edge denoted by 1
            self.adjacencyMatrix[neighbour][newNode-1] = 1#bidirectionality feature
            
    def removeVertex(self, node: int):#this function removes a node in the graph
        if(node>self.numberOfVertices):#check if node not more than the number of current vertices
            print("Vertex not found")
        else:
            while(node<self.numberOfVertices):#valid condition 
                
                for i in range(0,self.numberOfVertices):#loop around matrix to shift y axis when deleting a column
                    self.adjacencyMatrix[i][node] = self.adjacencyMatrix[i][node + 1]
                
                for i in range (0, self.numberOfVertices):#loop around matrix to shift x axis
                    self.adjacencyMatrix[node][i] = self.adjacencyMatrix[node + 1][i]#setting next row 
                node = node + 1#break loop
                
            self.numberOfVertices = self.numberOfVertices - 1
        self.defaultDestinations.pop(node) #deleting destination from dictionary
            
    def removeEdge(self, node: int, neighbour: int):
        #removing edge between 2 different nodes
        self.adjacencyMatrix[node][neighbour]= 0
        self.adjacencyMatrix[neighbour][node]= 0
        
        
    def BreadthFirstSearch (self, source: int, destination: int):
        
        visited = [False]*self.numberOfVertices#initiating list
        q = [source]#declaring first element which is the source into a lsit
        visited[source] = True#first node visited since it is the source of the traversal
        path = []#path list to store the element that are dequed
        
        while q:#loopping around q which is the list of all vertices that are visited in order
            vis = q[0]#declaring first index as visited
            print(vis, end = ' ')#prints the visited vertice
            q.pop(0)#deletes the visited vertice
            
            
            for i in range(self.numberOfVertices):#looping around all vertices
                if (self.adjacencyMatrix[vis][i])==1 and (not visited[i]):#if it is connected to an edge to another node and its not visited
                    q.append(i)# add this element into the queue
                    path.append(i)#adds this element into the path
                    visited[i] = True#declaring this vertice as visited
                if destination in path:#checks if destination is in the path
                    
                    break
                    
        print("This is the queue: ")
        print(q)
        print(visited)
        print("Path: ", path)
        route = []
        for i in path:
            tempdes = self.defaultDestinations.get(i)
            route.append(tempdes)
            
        
        print("BFS optimisation: ",)
        arrow = '--->'
        
        for i in route:
            print(i, arrow, end = " ")
        print("END")
        return
        


    
def mainTest():#testing main functionalities of the system
    example = GraphBuilder(11);
    matrix = example.BuildDefaultGraph()
    example.displayMatrix(matrix)
    example.addNewVertex()
    example.addNewEdge(12,3)
    example.removeEdge(0,1)
    example.removeEdge(2,0)
    currentState = example.adjacencyMatrix
    example.displayMatrix(currentState)
    print(" ")
    print('removing vertex')
    example.removeVertex(0)
    example.removeVertex(5)
    example.removeVertex(3)
    currentState = example.adjacencyMatrix
    example.displayMatrix(currentState)
    
    
def BFS():#call this method to try use the BFS system
    example = GraphBuilder(11);
    matrix = example.BuildDefaultGraph()
    currentState = example.adjacencyMatrix
    example.displayMatrix(matrix)
    example.displayMatrix(currentState)
    example.BreadthFirstSearch(0,5)


def combineMatrixManipulationBFS():#try this method to combine all matrix operations and the BFS system
    example = GraphBuilder(11);
    matrix = example.adjacencyMatrix
    example.displayMatrix(matrix)
    example.addNewVertex("TropicalParadise")
    example.addNewEdge(12,6)
    example.displayMatrix(matrix)
    example.BreadthFirstSearch(0,5)
    

def BFS2():#running BFS again
    example = GraphBuilder(11);
    matrix = example.BuildDefaultGraph()
    currentState = example.adjacencyMatrix
    example.addNewVertex("TropicalParadise")
    example.addNewEdge(12,1)
    example.addNewEdge(12,2)
    example.addNewEdge(12,4)
    example.addNewEdge(12,8)
    example.displayMatrix(matrix)
    example.displayMatrix(currentState)
    example.BreadthFirstSearch(0,6)


def UserInterface():#function to try the user interface
    #console user interface
    print("------- Delivery Route Optimisation System -------")
    print("----------------- Main Menu -----------------")
    print(" ")
    print("Select an option below..........")
    print(" ")
    print("")
    print(" 1 - Add a New Location")
    print(" 2 - Add a New Route")
    print(" 3 - Find Shortest Route between Two Locations")
    print(" 4 - Display Adjacency Matrix")
    print("")
    print("------------------------------------------------------------------")
    #build default graph
    example = GraphBuilder(10)
    matrix = example.BuildDefaultGraph()
    possible = [1,2,3,4]
    #process choice
    
        
    choice = int(input("Enter your choice: "))
    possible = [1,2,3,4]
    
    if choice in possible:
            
        if choice == 1:
            name = input("Add name of new location: ")
            example.addNewVertex(name)
            print("Done.", name, " has been added.")
            print("Here is the Locations Database of the System: ", example.defaultDestinations)
            
        if choice == 2:
            print("These are the available destinations...... ")
            print("Enter a number that holds the key to your chosen destination")
            print(example.defaultDestinations)
            locationFirst = int(input("Enter First Location: "))
            locatitonSecond =int(input("Enter Second Location: "))
            example.addNewEdge(locationFirst, locatitonSecond)
            print("Done. ")
            example.displayMatrix(matrix)
        if choice == 3:
            print("------ Finding Shortest Path --------")
            source = int(input("Enter source: "))
            destination = int(input("Enter destination: "))
            example.BreadthFirstSearch(source, destination)
        if choice == 4:
           example.displayMatrix(matrix) 
    else:
        print("not valid")
    
     
            
    
    
        
    
    
    
UserInterface()
