class playerControl(object):
    def __init__(self):
        self.X = -100
        self.Y = -300
        self.Exists = False
        self.projectiles = 0
    
    def spawn(self,x,y):
        if not self.Exists:
            self.X = x
            self.Y = y
            self.Exists = True
    
    def move(self,w,a,s,d,walls):
        if self.Exists:
            if w:
                move = True
                for wall in walls:
                    if self.Y == wall[1] + 96 and self.X in range(wall[0] - 31,wall[0] + 95):
                        move = False
                        break
                if move:
                    self.Y -= 2
            elif a:
                move = True
                for wall in walls:
                    if self.X == wall[0] + 96 and self.Y in range(wall[1] - 31,wall[1] + 95):
                        move = False
                        break
                if move:
                    self.X -= 2
            elif s:
                move = True
                for wall in walls:
                    if self.Y == wall[1] - 32 and self.X in range(wall[0] - 31,wall[0] + 95):
                        move = False
                        break
                if move:
                    self.Y += 2
            elif d:
                move = True
                for wall in walls:
                    if self.X == wall[0] - 32 and self.Y in range(wall[1] - 31,wall[1] + 95):
                        move = False
                        break
                if move:
                    self.X += 2
    
    def collide(self,target):
        if self.Exists:
            if ((self.X - target.X)**2 + (self.Y - target.Y)**2)**.5 <= 32:
                if target.exists:
                    self.Exists = False
                    target.exists = False
                    self.X = -100
                    self.Y = -300
                    target.X = -100
                    target.Y = -100
