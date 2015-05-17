# -*- coding: utf-8 -*-
'''
Created on 22 Dec, 2014

@author: wangyi
'''

__all__ = ['Event']

# basic event descriptor module
class Event(object):
    def __init__(self, doc=None):
        self.__doc__ = doc
        
    def __get__(self, obj, objtype):#__get__(self, caller, callerType):
        if  obj == None:#caller == None:
            return self
        else:
            return EventHandler(self, obj)#EventHandler(self, caller)
        
    def __set__(self, caller, value):
        self.val = value

# basic event handler module
class EventHandler(object):
    
    def __init__(self, event, caller):
        self.event  = event
        self.caller = caller
        
    def _gethanderList(self):
        try:
            eventhandler = self.caller.__eventhandler__
        except AttributeError:
            eventhandler = self.caller.__eventhandler__ = {}
        return \
            eventhandler.setdefault(  self.event , []  )
    
    # register a new handler to the corresponding event        
    def register(self, handler):
        
        self._gethanderList().append( handler )
        
        return self
    
    __add__ = register
    # depatch an old handler from the corresponding event     
    def depatchr(self, handler):
        
        self._gethanderList().remove( handler )
        
        return self
   
    __sub__ = depatchr
    
         
    def fire(self, *args, **keywords):
        
        for handler in self._gethanderList():
            # grammer
            return handler(self.caller, *args, **keywords)
    # for seamlessly calling event trigger
    __call__ = fire 