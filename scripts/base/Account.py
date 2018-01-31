# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *


class Account(KBEngine.Proxy):
	def __init__(self):
		KBEngine.Proxy.__init__(self)
		DEBUG_MSG("account createCellEntity")
		#if  KBEngine.globalData.has_key["space"]:
		#	self.createCellEntity(KBEngine.globalData["space"].cell)
		#else:
		#	KBEngine.globalData["space"]=self.createInNewSpace()
	def onTimer(self, id, userArg):
		"""
		KBEngine method.
		使用addTimer后， 当时间到达则该接口被调用
		@param id		: addTimer 的返回值ID
		@param userArg	: addTimer 最后一个参数所给入的数据
		"""
		DEBUG_MSG(id, userArg)
		
	def onEntitiesEnabled(self):
		"""
		KBEngine method.
		该entity被正式激活为可使用， 此时entity已经建立了client对应实体， 可以在此创建它的
		cell部分。
		"""
		self.cellData["position"]=(0,0,0)
		self.cellData["WarFieldId"]=KBEngine.globalData["one"].id#加入warField的id用于cell类别的呼叫方法
		DEBUG_MSG("global one.cell is{0}".format(KBEngine.globalData["one"].cell))
		self.createCellEntity(KBEngine.globalData["one"].cell)
		INFO_MSG("account[%i] entities enable. mailbox:%s" % (self.id, self.client))
			
	def onLogOnAttempt(self, ip, port, password):
		"""
		KBEngine method.
		客户端登陆失败时会回调到这里
		"""
		INFO_MSG(ip, port, password)
		return KBEngine.LOG_ON_ACCEPT
		
	def onClientDeath(self):
		"""
		KBEngine method.
		客户端对应实体已经销毁
		"""
		DEBUG_MSG("Account[%i].onClientDeath:" % self.id)
		self.destroyCellEntity()
	def onLoseCell(self):
		self.destroy()
	def onGetCell(self):
		self.client.cellReady()
	def createSpace(self):
		self.space = pymunk.Space()