from AI import AI
from damage import Damage
list={}
#no0 狐族双剑士
list[0]=[0,1,2,3]
#no1 流浪炎术士
list[1]=[4,5,6,7]
list[2]=[8]
ranges={}
ranges[0]=AI.NEAR_RANGE(2)
ranges[1]=AI.FAR_RANGE(2)
ranges[2]=AI.NEAR_RANGE(2)
propertys={}
propertys[0]=[30,Damage.LIGHT_ARMOR(),100]
propertys[1]=[10,Damage.CLOTH_ARMOR(),80]
propertys[2]=[50,Damage.HEAVY_ARMOR(),120]