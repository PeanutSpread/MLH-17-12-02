class playerControl(object):
    def __init__(self,x,y):
        self.X = x
        self.Y = y
        self.Exists = True
    
    def move(self,w,a,s,d):
        if w:
            self.Y -= 2
        elif a:
            self.X -= 2
        elif s:
            self.Y += 2
        elif d:
            self.X += 2
    
    def collide(self,target):
        if ((self.X - target.X)**2 + (self.Y - target.Y)**2)**.5 <= 32:
            if target.Exists:
                self.Exists = False
