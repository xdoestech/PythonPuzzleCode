'''
Created on Mar 4, 2022

@author: axyzh
'''
#Problem 2
'''
The Knight's tour problem solved via Warnsdorff's algorithm.
Warnsdorff's algorithm: https://www.geeksforgeeks.org/warnsdorffs-algorithm-
knights-tour-problem/
More info: https://en.wikipedia.org/wiki/Knight%27s_tour
King's Cross Board Configuration: 
*(0,0)  (0,1)  (0,2) *(0,3)
 (1,0)  (1,1)  (1,2)  (1,3)
 (2,0)  (2,1)  (2,2)  (2,3)
*(3,0)  (3,1)  (3,2) *(3,3)
* - the value in these corner squares will remain -1 because they are
not a part of the King's Cross Board
'''
import random
class Cell: 

    def __init__(self, x, y):
        self.x = x; 
        self.y = y;  


class GFG: 
 
    #### CHANGE HERE ####
    # Dimensions of a square chessboard
    N = 4
        
    possible_knight_movements = 8
    # Move pattern on basis of the change of 
    # x coordinates and y coordinates respectively 
    cx = [1, 1, 2, 2, -1, -1, -2, -2]
    cy = [2, -2, 1, -1, 2, -2, 1, -1]
    
    #### CHANGE HERE ####
    # This function should restrict the knight to remain within 
    # the chessboard, adjust accordingly for a non-square chessboard
    def limits(self, x, y): 
        #not in squares (0,0)/(0,3)/(3,0)/(3,3)
        #and ((x+y)>0) and ((x-y) != -3) and ((y-x) != -3)
        return ((x >= 0 and y >= 0) and (x < self.N and y < self.N)and ((x+y)>0) and ((x-y) != -(N-1)) and ((y-x) != -(N-1)) and ((x+y)!= 2*(N-1)))
    
    # Checks whether a square is valid and 
    # empty or not 
    def isempty(self, a, x, y): 
        return (self.limits(x, y)) and (a[y * self.N + x] < 0) 
      
    # Returns the number of empty squares 
    # adjacent to (x, y) in Warnsdorff's graph 
    def get_degree(self, a, x, y): 
        count = 0;
        for i in range(self.possible_knight_movements):
            if (self.isempty(a, (x + self.cx[i]), (y + self.cy[i]))): 
                count += 1 
        return count  
    
    # Picks next square using Warnsdorff's heuristic. 
    # Returns false if it is not possible to pick 
    # next square. 
    def next_move(self, a, cell): 
        min_deg_idx = -1 
        min_deg = (self.N + 1)
        # Try all adjacent nodes of (x, y) 
        # in Warndorff's graph based on the possible moves.
        # Starts from a random adjacent node and finds the one  
        # with minimum degree.
        start = random.randint(0, self.possible_knight_movements - 1);
        for count in range(self.possible_knight_movements):
            i = (start + count) % self.possible_knight_movements 
            nx = cell.x + self.cx[i] 
            ny = cell.y + self.cy[i]
            c = self.get_degree(a, nx, ny)
            if ((self.isempty(a, nx, ny)) and (c) < min_deg): 
                min_deg_idx = i 
                min_deg = c  
        # If we could not find a next cell 
        if (min_deg_idx == -1): 
            return None 
        # Store coordinates of next point 
        nx = cell.x + self.cx[min_deg_idx] 
        ny = cell.y + self.cy[min_deg_idx] 
        # Mark next move 
        a[ny * self.N + nx] = a[(cell.y) * self.N + (cell.x)] + 1 
        # Update next point 
        cell.x = nx 
        cell.y = ny 
        return cell 
    
    # Displays the chessboard with all the 
    # legal knight's moves 
    def print_tour(self, a): 
        for i in range(self.N): 
            for j in range(self.N):
                print("\t", (a[j * self.N + i]), end="")
            
            print('\n')
    
    # Checks its neighbouring squares. 
    # If the knight ends on a square that is one 
    # knight's move from the beginning square, 
    # then tour is closed 
    def neighbour(self, x, y, xx, yy): 
        for i in range(self.possible_knight_movements):
            if (((x + self.cx[i]) == xx) and ((y + self.cy[i]) == yy)): 
                return True 
        return False 
    
    # Generates the legal moves using Warnsdorff's 
    # heuristics. Returns false if not possible
    def find_closed_tour(self, initial_x, initial_y): 
        # Filling up the chessboard matrix with -1's 
        a = [-1] * (self.N * self.N) 
        # Initial position 
        sx = initial_x 
        sy = initial_y 
        # Current points are same as initial points 
        cell = Cell(sx, sy) 
        a[cell.y * self.N + cell.x] = 1  # Mark first move. 
        # Keep picking next points using 
        # Warnsdorff's heuristic
         #### CHANGE HERE ####
        for i in range((N*N) - N-1): #N*N
            ret = self.next_move(a, cell) 
            if (ret == None):
                print("NO MOVES PAST ........................")
                print(i+1)
                self.print_tour(a) #ADDED HERE
                return False 
        # Check if tour is closed (Can end 
        # at starting point) 
        if (not self.neighbour(ret.x, ret.y, sx, sy)): 
            print("UNCLOSED COMPLETE TOUR .....................")
            self.print_tour(a) #ADDED HERE
            return False 
        self.print_tour(a)
        return True 

    
# Driver Code to run your tour
not_closed = True
count =0
roundNum =1
N =4
# While we don't have a solution, try to find one. 
while(not_closed and count < 420):
    solution = GFG()
    print("ROUND: ", roundNum)
    #starting position defined here
    for i in range(N):
        if(not_closed == False):
            break;
        else:
            for j in range(N):
                guesses = 0
                if(not_closed == False):
                    print("SOLUTION FOUND!!!!!!")
                    break;
                elif((i+j == 2*(N-1)) or (i+j == 0)):
                    continue;
                else:
                    while(guesses < 100):
                        print("attempt # ", count)
                        print("starting position: ", i,j)
                        print("guess # ", guesses)
                        current_tour = solution.find_closed_tour(i,j)
                        count += 1
                        guesses += 1
                        if(current_tour):
                            not_closed = False
                            break;
    roundNum +=1   

# class Cell: 
#     def __init__(self, x, y):
#         self.x = x; 
#         self.y = y;  
# class GFG: 
#
#     #### CHANGE HERE ####
#     # Dimensions of a square chessboard
#     N = 8
#
#     possible_knight_movements = 8
#     # Move pattern on basis of the change of 
#     # x coordinates and y coordinates respectively 
#     cx = [1, 1, 2, 2, -1, -1, -2, -2]
#     cy = [2, -2, 1, -1, 2, -2, 1, -1]
#
#
#     #### CHANGE HERE ####
#     # This function should restrict the knight to remain within 
#     # the chessboard, adjust accordingly for a non-square chessboard
#     def limits(self, x, y): 
#         return ((x >= 0 and y >= 0) and (x < self.N and y < self.N)) 
#
#     # Checks whether a square is valid and 
#     # empty or not 
#     def isempty(self, a, x, y): 
#         return (self.limits(x, y)) and (a[y * self.N + x] < 0) 
#
#
#     # Returns the number of empty squares 
#     # adjacent to (x, y) in Warnsdorff's graph 
#     def get_degree(self, a, x, y): 
#         count = 0;
#         for i in range(self.possible_knight_movements):
#             if (self.isempty(a, (x + self.cx[i]), (y + self.cy[i]))): 
#                 count += 1 
#         return count  
#
#     # Picks next square using Warnsdorff's heuristic. 
#     # Returns false if it is not possible to pick 
#     # next square. 
#     def next_move(self, a, cell): 
#         min_deg_idx = -1 
#         min_deg = (self.N + 1)
#         # Try all adjacent nodes of (x, y) 
#         # in Warndorff's graph based on the possible moves.
#         # Starts from a random adjacent node and finds the one  
#         # with minimum degree.
#         start = random.randint(0,self.possible_knight_movements - 1);
#         for count in range(self.possible_knight_movements):
#             i = (start + count) % self.possible_knight_movements 
#             nx = cell.x + self.cx[i] 
#             ny = cell.y + self.cy[i]
#             c = self.get_degree(a, nx, ny)
#             if ((self.isempty(a, nx, ny)) and (c) < min_deg): 
#                 min_deg_idx = i 
#                 min_deg = c  
#         # If we could not find a next cell 
#         if (min_deg_idx == -1): 
#             return None 
#         # Store coordinates of next point 
#         nx = cell.x + self.cx[min_deg_idx] 
#         ny = cell.y + self.cy[min_deg_idx] 
#         # Mark next move 
#         a[ny * self.N + nx] = a[(cell.y) * self.N + (cell.x)] + 1 
#         # Update next point 
#         cell.x = nx 
#         cell.y = ny 
#         return cell 
#
#     # Displays the chessboard with all the 
#     # legal knight's moves 
#     def print_tour(self, a): 
#         for i in range(self.N): 
#             for j in range(self.N):
#                 print("\t", (a[j * self.N + i]), end="")
#
#             print('\n')
#
#
#     # Checks its neighbouring squares. 
#     # If the knight ends on a square that is one 
#     # knight's move from the beginning square, 
#     # then tour is closed 
#     def neighbour(self, x, y, xx, yy): 
#         for i in range(self.possible_knight_movements):
#             if (((x + self.cx[i]) == xx) and ((y + self.cy[i]) == yy)): 
#                 return True 
#         return False 
#
#
#
#     # Generates the legal moves using Warnsdorff's 
#     # heuristics. Returns false if not possible
#     def find_closed_tour(self, initial_x,initial_y): 
#         # Filling up the chessboard matrix with -1's 
#         a = [-1] * (self.N*self.N) 
#         # Initial position 
#         sx = initial_x 
#         sy = initial_y 
#         # Current points are same as initial points 
#         cell = Cell(sx, sy) 
#         a[cell.y * self.N + cell.x] = 1 # Mark first move. 
#         # Keep picking next points using 
#         # Warnsdorff's heuristic
#          #### CHANGE HERE ####
#         for i in range(64 - 1):
#             ret = self.next_move(a, cell) 
#             if (ret == None): 
#                 return False 
#         # Check if tour is closed (Can end 
#         # at starting point) 
#         if (not self.neighbour(ret.x, ret.y, sx, sy)): 
#             return False 
#         self.print_tour(a)
#         return True 
#
# # Driver Code to run your tour
# not_closed = True
# # While we don't have a solution, try to find one. 
# while(not_closed):
#     solution = GFG()
#     current_tour = solution.find_closed_tour(0,1)
#     if(current_tour):
#         not_closed = False