# NEED TO DO:
# Set Report output to new windows
# Build Output button

from  tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import sqlite3
import pandas as pd

root = Tk()
root.title('Shift Reports')
root.iconbitmap('Images/axe.ico')
root.geometry('700x250')
root.resizable(width=False, height=False)

# DB Name = ShiftReport.db
# Table Names = Open_Shifts 
#                Site_Master


# Import CSV funtion

def import_csv():
    global filename
    
    filename = filedialog.askopenfilename(initialdir='C:', title='Select A File', filetypes=(('csv files', '.csv'),))
    
    # Check if entry box is empty and place file path
    
    if len(file_path.get()) == 0:
        file_path.config(state='normal')
        file_path.insert(0, filename)
        file_path.config(state='disabled')
    else:
        file_path.config(state='normal')
        file_path.delete(0, END)
        file_path.insert(0, filename)
    
    shifts = filename
    conn = sqlite3.connect('ShiftReport.db')
    
    shift_csv = pd.read_csv(shifts, skiprows=2)
    shift_csv.columns = ['Date', 'Site_Name', 'Shift_Type', 'Start', 'End', 'Hours', 'Comments']
    shift_csv.to_sql('Open_Shifts', conn, if_exists='replace')
    
    # Test to make sure imported correctly
    
    # x = conn.cursor()
    
    # # ********INNER JOIN TO SELECT BY COUNTY********** COPY INTO LOWER FUNCTIONS AS NEEDED**********
    
    # x.execute('''SELECT Site_Master.Site_Fixed, 
                # Open_Shifts.Date, 
                # Open_Shifts.Shift_Type, 
                # Open_Shifts.Start, 
                # Open_Shifts.End, 
                # Site_Master.Region 
                # FROM Open_Shifts 
                # INNER JOIN Site_Master 
                # ON Open_Shifts.Site_Name = Site_Master.Site_Name 
                # WHERE (((Site_Master.Region)="Nassau"))'
    # )''')
    
    # records = x.fetchall()
    
    # # Loop results to display 1 record per line

    # print_records = ''
    # for record in records:
        # print_records += str(record) + '\n'
    
    # print(print_records)
    
    conn.commit()
    conn.close()
    
    return filename
    
# Report Generation
def report():
    global report_type
    report_type = region.get()
    
    def nassau():
        conn = sqlite3.connect('ShiftReport.db')
        x = conn.cursor()
        
        # Delete old table
        x.execute('DROP TABLE IF EXISTS Nassau')
        # Create new table
        x.execute('CREATE TABLE Nassau AS SELECT Site_Master.Site_Fixed, Open_Shifts.Date, Open_Shifts.Shift_Type, Open_Shifts.Start, Open_Shifts.End, Site_Master.Region FROM Open_Shifts INNER JOIN Site_Master ON Open_Shifts.Site_Name = Site_Master.Site_Name WHERE Site_Master.Region="Nassau" AND (Open_Shifts.Shift_Type like "%RT%" OR Open_Shifts.Shift_Type like "%MA%" OR Open_Shifts.Shift_Type like "%EMS%")')
        # Read table
        nassau_table = pd.read_sql_query('SELECT * FROM Nassau', conn)
        # Output table
        # Create new window to display report
        report = Tk()
        report.title(report_type)
        report.iconbitmap('Images/axe.ico')
        pd.set_option('display.max_rows', None)
        output = Label(report, text=nassau_table)
        output.pack()
    
        conn.commit()
        conn.close()
        
    def suffolk():
        conn = sqlite3.connect('ShiftReport.db')
        x = conn.cursor()
        
        # Delete old table
        x.execute('DROP TABLE IF EXISTS Suffolk')
        # Create new table
        x.execute('CREATE TABLE Suffolk AS SELECT Site_Master.Site_Fixed, Open_Shifts.Date, Open_Shifts.Shift_Type, Open_Shifts.Start, Open_Shifts.End, Site_Master.Region FROM Open_Shifts INNER JOIN Site_Master ON Open_Shifts.Site_Name = Site_Master.Site_Name WHERE Site_Master.Region="Suffolk" AND (Open_Shifts.Shift_Type like "%RT%" OR Open_Shifts.Shift_Type like "%MA%" OR Open_Shifts.Shift_Type like "%EMS%")')
        # Read table
        suffolk_table = pd.read_sql_query('SELECT * FROM Suffolk', conn)
        # Output table
        report = Tk()
        report.title(report_type)
        report.iconbitmap('Images/axe.ico')
        pd.set_option('display.max_rows', None)
        output = Label(report, text=suffolk_table)
        output.pack()
    
        conn.commit()
        conn.close()
        
    def nyc():
        conn = sqlite3.connect('ShiftReport.db')
        x = conn.cursor()
        
        # Delete old table
        x.execute('DROP TABLE IF EXISTS NYC')
        # Create new table
        x.execute('CREATE TABLE NYC AS SELECT Site_Master.Site_Fixed, Open_Shifts.Date, Open_Shifts.Shift_Type, Open_Shifts.Start, Open_Shifts.End, Site_Master.Region FROM Open_Shifts INNER JOIN Site_Master ON Open_Shifts.Site_Name = Site_Master.Site_Name WHERE Site_Master.Region="NYC" AND (Open_Shifts.Shift_Type like "%RT%" OR Open_Shifts.Shift_Type like "%MA%" OR Open_Shifts.Shift_Type like "%EMS%")')
        # Read table
        nyc_table = pd.read_sql_query('SELECT * FROM NYC', conn)
        # Output table
        report = Tk()
        report.title(report_type)
        report.iconbitmap('Images/axe.ico')
        pd.set_option('display.max_rows', None)
        output = Label(report, text=nyc_table)
        output.pack()
    
        conn.commit()
        conn.close()
        
    def westchester():
        conn = sqlite3.connect('ShiftReport.db')
        x = conn.cursor()
        
        # Delete old table
        x.execute('DROP TABLE IF EXISTS Westchester')
        # Create new table
        x.execute('CREATE TABLE Westchester AS SELECT Site_Master.Site_Fixed, Open_Shifts.Date, Open_Shifts.Shift_Type, Open_Shifts.Start, Open_Shifts.End, Site_Master.Region FROM Open_Shifts INNER JOIN Site_Master ON Open_Shifts.Site_Name = Site_Master.Site_Name WHERE Site_Master.Region="Westchester" AND (Open_Shifts.Shift_Type like "%RT%" OR Open_Shifts.Shift_Type like "%MA%" OR Open_Shifts.Shift_Type like "%EMS%")')
        # Read table
        westchester_table = pd.read_sql_query('SELECT * FROM Westchester', conn)
        # Output table
        report = Tk()
        report.title(report_type)
        report.iconbitmap('Images/axe.ico')
        pd.set_option('display.max_rows', None)
        output = Label(report, text=westchester_table)
        output.pack()
    
        conn.commit()
        conn.close()
        
    def all():
        nassau()
        suffolk()
        nyc()
        westchester()
    
    if report_type == 'Nassau':
        nassau()
    elif report_type == 'Suffolk':
        suffolk()
    elif report_type == 'NYC':
        nyc()
    elif report_type == 'Westchester':
        westchester()
    elif report_type == 'All Regions':
        all()
  
# Export CSV funtion
    
def export_csv():
    global report_type
    report_type = region.get()
    
    def nassau_exp():
        export_path = filedialog.asksaveasfilename(defaultextension='.csv')
        conn = sqlite3.connect('ShiftReport.db')
        x = conn.cursor()
        
        nassau_table = pd.read_sql_query('SELECT * FROM Nassau', conn)
        export_csv = nassau_table.to_csv(export_path, index=None, header=True)
        
        conn.commit()
        conn.close()
        
    def suffolk_exp():
        export_path = filedialog.asksaveasfilename(defaultextension='.csv')
        conn = sqlite3.connect('ShiftReport.db')
        x = conn.cursor()
        
        suffolk_table = pd.read_sql_query('SELECT * FROM Suffolk', conn)
        export_csv = suffolk_table.to_csv(export_path, index=None, header=True)
        
        conn.commit()
        conn.close()
    
    def nyc_exp():
        export_path = filedialog.asksaveasfilename(defaultextension='.csv')
        conn = sqlite3.connect('ShiftReport.db')
        x = conn.cursor()
        
        nyc_table = pd.read_sql_query('SELECT * FROM NYC', conn)
        export_csv = nyc_table.to_csv(export_path, index=None, header=True)
        
        conn.commit()
        conn.close()
    
    def westchester_exp():
        export_path = filedialog.asksaveasfilename(defaultextension='.csv')
        conn = sqlite3.connect('ShiftReport.db')
        x = conn.cursor()
        
        westchester_table = pd.read_sql_query('SELECT * FROM Westchester', conn)
        export_csv = westchester_table.to_csv(export_path, index=None, header=True)
        
        conn.commit()
        conn.close()
    
    def all_exp():
        messagebox.showerror('ERROR', 'Please select only one region for export.')
    
    if report_type == 'Nassau':
        nassau_exp()
    elif report_type == 'Suffolk':
        suffolk_exp()
    elif report_type == 'NYC':
        nyc_exp()
    elif report_type == 'Westchester':
        westchester_exp()
    elif report_type == 'All Regions':
        all_exp()

# Dummy Image for button resizing by pixels

pixel = tk.PhotoImage(width=1, height=20)

# Create inner frame

master = Frame(root, bd=10, padx=50, pady=50, bg='white')
master.pack(fill=BOTH, expand=1)



# Create Buttons, Entry Box, and DropDown

filename = ''


import_button = Button(master, text='Import CSV', image=pixel, compound='center', width=100, command=import_csv)
import_button.grid(row=0, column=0, padx=20, pady=(0,8))

file_path = Entry(master, state='disabled', width=75, text=filename)
file_path.grid(row=0, column=1, pady=15, columnspan=3)

report_button = Button(master, text='Run Report', image=pixel, compound='center', width=100, command=report)
report_button.grid(row=1, column=1, padx=20, pady=(0,8))

export_button = Button(master, text='Export CSV', image=pixel, compound='center', width=100, command=export_csv)
export_button.grid(row=3, column=1, padx=20, pady=(0,8))

    # Drop Down

region = StringVar()
region_select = ['Nassau', 'Suffolk', 'NYC', 'Westchester', 'All Regions']
region.set('Nassau')

region_menu = OptionMenu(master, region, *region_select)
region_menu.config(width=11)
region_menu.grid(row=1, column=0)

# Dummy Labels for spacing

dummy1 = Label(master, text='', bg='white')
dummy1.grid(row=1, column=3)
dummy2 = Label(master, text='', bg='white')
dummy2.grid(row=1, column=4)


root.mainloop()