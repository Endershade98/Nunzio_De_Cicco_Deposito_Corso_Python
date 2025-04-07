class Point:
    """Point is a class representing a geometric Point in the plan
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def move(self, dx, dy):
        """returns the new point position"""
        self.x += dx
        self.y += dy
        return f"<{self.x}, {self.y}>"
    
    def distance_from_origin(self):
        """returns the distance of a point from the origin"""
        return (self.x**2+self.y**2)**0.5
        
