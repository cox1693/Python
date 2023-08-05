#Here is creating the object
class Car:
    #Controls
    GasPedal = 0
    BrakePedal = 0
    EngineState = False
    RightBlinker =False
    LeftBlinker = False

    #RunningState
    Speed = 0
    RightBlinkerLight =False
    LeftBlinkerLight = False

    def ___init___(self):
        return None

    def TurnKey(self):
        if self.EngineState==True:
            self.EngineState = False
            print("Engine is now stopped")
        if self.EngineState== False:
            self.EngineState=True
            print("Engine is now running")

    def StepGasPedal(self, StepDown):
        if self.EngineState == False :
            self.Speed = 0
            print("Nothing happen Car is not running")
            return None
        
        if StepDown > self.Speed:
            self.Speed = StepDown
        print("The current speed is ",self.Speed)

    def StepBrakePedal(self, StepDown):
        if self.Speed > 100-StepDown:
            self.Speed = 100-StepDown
        print("The current speed is",self.Speed)



       # self.Speed= StepDown
       # print("The car speed is",self.Speed)

    def SignalRight(self):
        if self.EngineState == True:
            self.RightBlinkerLight = True
            self.LeftBlinkerLight = False
            print("The right blinker light is on")
        elif self.EngineState == False:
            self.RightBlinkerLight = False
            self.LeftBlinkerLight = False
            print("Engine is not running so no lights are on")

    def SignalLeft(self):
        if self.EngineState == True:
            self.LeftBlinkerLight = True
            self.RightBlinkerLight= False
            print("Left blinker light is on")
        elif self.EngineState== False:
            self.LeftBlinkerLight= False
            self.RightBlinkerLight=False
            print("Engine is not running so no lights are on")

















#Here is the main  program
Nissan = Car()
#Nissan.TurnKey()
#Nissan.StepGasPedal(50)
Nissan.StepBrakePedal(25)
Nissan.TurnKey()

Nissan.SignalLeft()
Nissan.SignalRight()
#Nissan.StepGasPedal()
Nissan.StepGasPedal(75)
Nissan.StepGasPedal(25)
Nissan.StepBrakePedal(50)






