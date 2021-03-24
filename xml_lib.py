
import time
import threading
import traceback
import sys
import inspect
import os
from tkinter import messagebox
import re
from pprint import pprint

from bs4 import BeautifulSoup




class Error_Tools:

      @staticmethod
      def error_type(e):

         #curframe = inspect.currentframe()
         #calframe = inspect.getouterframes(curframe, 2)
         template = 'An exception of type "{0}" occurred in function "{1}". Arguments:\n{2!r}'
         message = template.format(type(e).__name__, sys._getframe().f_back.f_code.co_name,e.args)
         return message

      @staticmethod
      def trace_msg():
         return traceback.format_exc()

      @staticmethod
      def all_msg(e):
          if e:
              return Error_Tools.error_type(e)+traceback.format_exc()
          else:
              return ''

      @staticmethod
      def error_exit(title,e=None,msg='',parent=None):
          messagebox.showerror(title, msg+Error_Tools.all_msg(e),parent=parent)
          os._exit(0)

      @staticmethod
      def warning_box(title,e=None,msg='',parent=None):
          messagebox.showwarning(title, msg+Error_Tools.all_msg(e),parent=parent)

      @staticmethod
      def ask_box(title, msg='',parent=None):
          return messagebox.askokcancel(title,msg,parent=parent)

      @staticmethod
      def show_box(title, msg='',parent=None):
           messagebox.showinfo(title, msg,parent=parent)



if __name__ =='__main__':
    html_doc  =  ''' 
                <html> <head> <title>睡鼠的故事</ title> </ head> 
                <body> 
                <p class ='title'> <b>睡鼠的故事</ b> </ p>

                <p class ='story'>從前，有三個妹妹。其名稱為
                <a href="http://example.com/elsie" class="sister" id="link1"> Elsie </a>，
                <a href =' http://example.com/lacie ' class ='sister' id =' link2'> Lacie </a>和
                <a href="http://example.com/tillie" class="sister" id="link3"> Tillie </a>；
                他們住在井底。</ p>

                <p class ='story'> ... </ p> 
                '''
    print(123)
    soup = BeautifulSoup(html_doc, 'lxml')
    pprint(soup.select('[class~=sister]'))

    xml_doc = '''
    <?xml version="1.0"?>
   <catalog>
   <book id="bk101">
      <author>Gambardella, Matthew</author>
      <title>XML Developer's Guide</title>
      <genre>Computer</genre>
      <price>44.95</price>
      <publish_date>2000-10-01</publish_date>
      <description>An in-depth look at creating applications 
      with XML.</description>
   </book>
   <book id="bk102">
      <author>Ralls, Kim</author>
      <title>Midnight Rain</title>
      <genre>Fantasy</genre>
      <price>5.95</price>
      <publish_date>2000-12-16</publish_date>
      <description>A former architect battles corporate zombies, 
      an evil sorceress, and her own childhood to become queen 
      of the world.</description>
   </book>
   <book id="bk103">
      <author>Corets, Eva</author>
      <title>Maeve Ascendant</title>
      <genre>Fantasy</genre>
      <price>5.95</price>
      <publish_date>2000-11-17</publish_date>
      <description>After the collapse of a nanotechnology 
      society in England, the young survivors lay the 
      foundation for a new society.</description>
   </book>
   <book id="bk104">
      <author>Corets, Eva</author>
      <title>Oberon's Legacy</title>
      <genre>Fantasy</genre>
      <price>5.95</price>
      <publish_date>2001-03-10</publish_date>
      <description>In post-apocalypse England, the mysterious 
      agent known only as Oberon helps to create a new life 
      for the inhabitants of London. Sequel to Maeve 
      Ascendant.</description>
   </book>
   <book id="bk105">
      <author>Corets, Eva</author>
      <title>The Sundered Grail</title>
      <genre>Fantasy</genre>
      <price>5.95</price>
      <publish_date>2001-09-10</publish_date>
      <description>The two daughters of Maeve, half-sisters, 
      battle one another for control of England. Sequel to 
      Oberon's Legacy.</description>
   </book>
   <book id="bk106">
      <author>Randall, Cynthia</author>
      <title>Lover Birds</title>
      <genre>Romance</genre>
      <price>4.95</price>
      <publish_date>2000-09-02</publish_date>
      <description>When Carla meets Paul at an ornithology 
      conference, tempers fly as feathers get ruffled.</description>
   </book>
   <book id="bk107">
      <author>Thurman, Paula</author>
      <title>Splish Splash</title>
      <genre>Romance</genre>
      <price>4.95</price>
      <publish_date>2000-11-02</publish_date>
      <description>A deep sea diver finds true love twenty 
      thousand leagues beneath the sea.</description>
   </book>
   <book id="bk108">
      <author>Knorr, Stefan</author>
      <title>Creepy Crawlies</title>
      <genre>Horror</genre>
      <price>4.95</price>
      <publish_date>2000-12-06</publish_date>
      <description>An anthology of horror stories about roaches,
      centipedes, scorpions  and other insects.</description>
   </book>
   <book id="bk109">
      <author>Kress, Peter</author>
      <title>Paradox Lost</title>
      <genre>Science Fiction</genre>
      <price>6.95</price>
      <publish_date>2000-11-02</publish_date>
      <description>After an inadvertant trip through a Heisenberg
      Uncertainty Device, James Salway discovers the problems 
      of being quantum.</description>
   </book>
   <book id="bk110">
      <author>O'Brien, Tim</author>
      <title>Microsoft .NET: The Programming Bible</title>
      <genre>Computer</genre>
      <price>36.95</price>
      <publish_date>2000-12-09</publish_date>
      <description>Microsoft's .NET initiative is explored in 
      detail in this deep programmer's reference.</description>
   </book>
   <book id="bk111">
      <author>O'Brien, Tim</author>
      <title>MSXML3: A Comprehensive Guide</title>
      <genre>Computer</genre>
      <price>36.95</price>
      <publish_date>2000-12-01</publish_date>
      <description>The Microsoft MSXML3 parser is covered in 
      detail, with attention to XML DOM interfaces, XSLT processing, 
      SAX and more.</description>
   </book>
   <book id="bk112">
      <author>Galos, Mike</author>
      <title>Visual Studio 7: A Comprehensive Guide</title>
      <genre>Computer</genre>
      <price>49.95</price>
      <publish_date>2001-04-16</publish_date>
      <description>Microsoft Visual Studio 7 is explored in depth,
      looking at how Visual Basic, Visual C++, C#, and ASP+ are 
      integrated into a comprehensive development 
      environment.</description>
   </book>
    </catalog>
    '''
    print('xml test')
    soup = BeautifulSoup(xml_doc, 'lxml')
    #先找book這個標籤再找genre的標籤和取值
    pprint(soup.select('book > genre'))
    #取text值
    print(soup.select('book > genre')[0].text)
    #取attr值
    pprint(soup.select('book ')[0]['id'])
    #選擇書這個標籤帶有特定id屬性
    print('test3',soup.select("book[id] > genre"))
    #選擇書這個標籤帶有特定id屬性名為bk112
    print(soup.select("book[id='bk112'] > genre")[0].text)
   


