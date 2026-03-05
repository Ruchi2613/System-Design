from abc import ABC, abstractmethod

class ItemState(ABC):
    @abstractmethod
    def checkout(self, item):
        pass

    @abstractmethod
    def return_item(self, item):
        pass

    @abstractmethod
    def place_hold(self, item):
        pass


    '''Abstract class ItemState defines common actions like checkout, return, and hold. Different state classes like AvailableState, CheckedOutState, 
    and OnHoldState implement these behaviors differently using the State Design Pattern'''


class AvailableState(ItemState):
    def checkout(self, item):
        print(f'checking out {item.title}')
        item.state = CheckedOutState()

    def return_item(self, item):
        print(f'{item.title} is already available')

    def place_hold(self, item):
        print(f'placing hold on {item.title}')


class CheckedOutState(ItemState):
    def checkout(self, item):
        print(f'{item.title} is already checked out')

    def return_item(self, item):
        print(f'returning {item.title}')
        item.state = AvailableState()

    def place_hold(self, item):
        print(f'placing hold on {item.title}')


class OnHoldState(ItemState):
    def checkout(self, item):
        print(f'{item.title} is on hold and cannot be checked out')

    def return_item(self, item):
        print(f'{item.title} is on hold and cannot be returned')

    def place_hold(self, item):
        print(f'{item.title} is already on hold')
