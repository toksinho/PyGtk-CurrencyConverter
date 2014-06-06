
import pygtk
import pango #pango for font in line 169
pygtk.require('2.0')
import gtk
from xmlParse import Xml
value1=0
value2=0
entryValue=1.0

class Window:
    
    def combo_selected1(self,widget):
        string=widget.get_active_text()
        active=widget.get_active()
        global value1
        value1=active
    
        
    def combo_selected2(self,widget):
        string=widget.get_active_text()
        active=widget.get_active()
        global value2
        value2=active
        print value2

    # This callback clicking on button converts values    
    def callback(self, widget,entry2):
 
        converted=0
        print x.date
        global value1
        global entryValue
        if value1==0:
            if value2==0:
                entry2.set_text(str(entryValue))
            elif value2==1:
                converted=entryValue / x.EurHr()
                entry2.set_text(str(converted))
            elif value2==2:
                converted=entryValue / x.UsaHr()
                entry2.set_text(str(converted))
            elif value2==3:
                converted=entryValue / x.SuiHr()
                entry2.set_text(str(converted))

        if value1==1:
            if value2==0:
                converted=entryValue * x.EurHr()
                entry2.set_text(str(converted))
            elif value2==1:
                entry2.set_text(str(entryValue))
                
            elif value2==2:
                converted=entryValue * x.EurUsa()
                entry2.set_text(str(converted))
            elif value2==3:
                converted=entryValue * x.EurSui()
                entry2.set_text(str(converted))       
            
        if value1==2:
            if value2==0:
                converted=entryValue * x.UsaHr()
                entry2.set_text(str(converted))
                
            elif value2==1:
                converted=entryValue / x.EurUsa()
                entry2.set_text(str(converted))
                
            elif value2==2:
                entry2.set_text(str(entryValue))
                
            elif value2==3:
                converted=entryValue * x.UsaSui()
                entry2.set_text(str(converted))              
                
        if value1==3:
            if value2==0:
                converted=entryValue * x.SuiHr()
                entry2.set_text(str(converted))
                
            elif value2==1:
                converted=entryValue / x.EurSui()
                entry2.set_text(str(converted))
                
            elif value2==2:
                converted=entryValue / x.UsaSui()
                entry2.set_text(str(converted))  
                
            elif value2==3:
                entry2.set_text(str(entryValue))   

        
        
    def combo_entry(self,widget,entry):
        active=widget.get_active()
        if active!=4:
            entVal=str(entryValue)
            entry.set_text(entVal)

    def entry_data(self,widget,event):
        global entryValue
        entryValue=float(widget.get_text())
        print entryValue
        

    
    # This callback quits the program
    def delete_event(self, widget, event, data=None):
        gtk.main_quit()
        return False

    def response(self,widget,data=None):
        message = gtk.AboutDialog()
        message.set_name("Currency Converter")
        message.set_version("1.0")
        message.set_copyright("(c) Ivica Tokic")
        message.run()
        message.destroy()


        
    def __init__(self):
        # Create a new window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        
        # Set the window title
        self.window.set_title("CurrencyConverter")

        # Set a handler for delete_event that immediately
        # exits GTK.
        self.window.connect("delete_event", self.delete_event)
       

        slist = ["HR Kuna","Euro","US Dollar","Swiss Franc"]
        # Create a 2x2 table
        table = gtk.Table(5, 3, True)

        # Put the table in the main window
        self.window.add(table)

        # Create first button
        button1 = gtk.Button("Convert")


        #choose a currency from 2 combo box
        combo1 = gtk.combo_box_new_text()
        combo1.append_text(slist[0])
        combo1.append_text(slist[1])
        combo1.append_text(slist[2])
        combo1.append_text(slist[3])
        #combo1.set_active(0)
        combo1.connect("changed",self.combo_selected1)
        
        combo2 = gtk.combo_box_new_text()
        combo2.append_text(slist[0])
        combo2.append_text(slist[1])
        combo2.append_text(slist[2])
        combo2.append_text(slist[3])
        #combo2.set_active(0)
        combo2.connect("changed",self.combo_selected2)
        

        label1 = gtk.Label("Currency I Have")
        label2 = gtk.Label("Currency I Want")
        label3 = gtk.Label("Amount")
        label4 = gtk.Label("Converted")
        datelabel = gtk.Label(x.date)
        datelabel.modify_font(pango.FontDescription("sans 16"))

        menu_bar = gtk.MenuBar()
        file_menu = gtk.Menu()
        help_menu = gtk.Menu()

        help_item = gtk.MenuItem("Help")
        about_item = gtk.MenuItem("About")
        quit_item = gtk.MenuItem("Quit")
        file_menu.append(quit_item)
        help_menu.append(about_item)    
        file_item = gtk.MenuItem("File")
        help_item = gtk.MenuItem("Help")
        
        file_item.set_submenu(file_menu)
        menu_bar.append(file_item)
        help_item.set_submenu(help_menu)
        menu_bar.append(help_item)
        
        entry1 = gtk.Entry(max=10)
        entry2 = gtk.Entry(max=10)
        combo1.connect("changed",self.combo_entry,entry1)
        button1.connect("clicked", self.callback,entry2)
        table.attach(button1, 1, 2, 3, 4,gtk.FILL|gtk.SHRINK,gtk.FILL|gtk.SHRINK,10,5)
        
        table.attach(combo1, 0, 1, 2, 3,gtk.FILL|gtk.SHRINK,gtk.FILL|gtk.SHRINK,10,5)
        table.attach(combo2, 2, 3, 2, 3,gtk.FILL|gtk.SHRINK,gtk.FILL|gtk.SHRINK,10,5)
        
        table.attach(label1,0, 1, 1, 2,gtk.FILL|gtk.SHRINK,gtk.FILL|gtk.SHRINK,10,5)
        table.attach(label2,2, 3, 1, 2,gtk.FILL|gtk.SHRINK,gtk.FILL|gtk.SHRINK,10,5)                          
        table.attach(label3,0, 1, 3, 4,gtk.FILL|gtk.SHRINK,gtk.FILL|gtk.SHRINK,10,5)
        table.attach(label4,2, 3, 3, 4,gtk.FILL|gtk.SHRINK,gtk.FILL|gtk.SHRINK,10,5)
        table.attach(datelabel,1, 2, 1, 2,gtk.FILL|gtk.SHRINK,gtk.FILL|gtk.SHRINK,10,5)
        
        table.attach(entry1,0, 1, 4, 5,gtk.FILL|gtk.SHRINK,gtk.FILL|gtk.SHRINK,10,5)
        table.attach(entry2,2, 3, 4,5,gtk.FILL|gtk.SHRINK,gtk.FILL|gtk.SHRINK,10,5)
        
        table.attach(menu_bar,0, 3, 0, 1,gtk.FILL|gtk.SHRINK,gtk.FILL|gtk.SHRINK,0,0)
        table.set_row_spacings(15)
        table.set_col_spacings(10)

        quit_item.connect("activate",gtk.main_quit)
        about_item.connect("activate",self.response,None)

        entry1.connect("key-release-event",self.entry_data)
        button1.show()
        combo1.show()
        combo2.show()
        
        quit_item.show()
        help_item.show()
 
        file_item.show()
        about_item.show()
        menu_bar.show()
        
        label1.show()
        label2.show()
        label3.show()
        label4.show()
        datelabel.show()
        
        entry1.show()
        entry2.show()
        
        table.show()
        self.window.show()

def main():
    gtk.main()

    return 0       

if __name__ == "__main__":
    x=Xml()
    Window()
    main()
