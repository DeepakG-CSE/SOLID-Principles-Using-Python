'''
The Interface Segregation Principle states that “No client should be forced to depend on methods it does not use”.

The Interface Segregation Principle was introduced by Robert C Martin while he was consulting for Xerox.

The Interface Segregation Principle suggests creating smaller interfaces known as “role interfaces” instead of a large interface consisting of multiple methods.
By segregating the role-based methods into smaller role interfaces, the clients would depend only on the methods that are relevant to it.


'''


from abc import ABCMeta, abstractmethod

class CallingDevice():
  @abstractmethod
  def make_calls():
    pass

class MessagingDevice():
  @abstractmethod
  def send_sms():
    pass

class InternetbrowsingDevice():
  @abstractmethod
  def browse_internet():
    pass

class SmartPhone(CallingDevice, MessagingDevice, InternetbrowsingDevice):
  def make_calls():
    #implementation
    pass

  def send_sms():
    #implementation
    pass

  def browse_internet():
    #implementation
    pass

class LandlinePhone(CallingDevice):
  def make_calls():
    #implementation
    pass
