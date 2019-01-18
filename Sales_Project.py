import email

import imaplib

from bs4 import BeautifulSoup

import mimetypes

import os

username = 'selftaughtpythoner@gmail.com'

password = "Shaahin1*"

mail = imaplib.IMAP4_SSL("imap.gmail.com")      #makes the SSL Connection

mail.login(username,password)

mail.select('INBOX')

result,data = mail.uid('search',None,"ALL") #unique identification(command,uid,encoding)

inbox_item_list = data[0].split() #makes a list so we can iterate over it

for item in inbox_item_list:
    
    result2,email_data = mail.uid('fetch',item,'(RFC822)')
    
    raw_email = email_data[0][1].decode('utf-8') #decodes so it's more readable
    
    email_message = email.message_from_string(raw_email) #makes email object from raw_email
    
    to_ = email_message['To']
    
    from_ = email_message['From']
    
    subject_ = email_message['Subject']
    
    counter = 1 # to count the parts
    
    date_ = email_message['date']
    
    for part in email_message.walk():   #generator walks over email tree, yields each subpart
        
        if part.get_content_maintype() == 'multipart':
            
            continue
            
        filename = part.get_filename() # gets the file name if it exists !
        
        content_type = part.get_content_type() # will show the actual content type
        
        if not filename:
            
            #ext = '.html' #file extension
            ext = mimetypes.guess_extension(part.get_content_type()) #it lets the mimetypes to guess the extension
            
            if not ext:  #if mimetypes could'nt guess the extension
                
                ext = '.bin' #it acts like a place holder
            
            filename = 'msg-part-%d%s' %(counter,ext) #digit and str part --> 8 zeros and the digit and str
            
            counter += 1 #keep track of number of parts
            
            save_path = os.path.join(os.getcwd(),'Emails',date_,subject_) #the path to save our files
            
            if not os.path.exists(save_path): # if save_path does not exist
                
                os.makedirs(save_path) # make the path
                
            with open(os.path.join(save_path,filename), 'wb') as fp:
                
                fp.write(part.get_payload(decode = True))
                
email_file = open(os.path.join(save_path,'msg-part-1.bat'),'r') ## can read the file and store in variable

email_file_content = email_file.read()    #read the email

with open('Sales_Report', 'a') as file:    #open the Sales_Report file to append some data
    
    file.write(email_file_content)  #write email content to it.
    
    
    
with open('Sales_Report','r') as file:
    report = file.readlines()

wage = 13


income = 0

for line in report:
    
    splitted_line = line.split()
    
    if len(splitted_line) > 1:
    
        start_h = int(splitted_line[1])
        
        end_h = int(splitted_line[2])
        
        hours = int(end_h - start_h)
        
        bb_sales = int(splitted_line[3])
        
        toy_sales = int(splitted_line[4])
        
        
        
        
        
    
    
        if splitted_line[0].startswith('G'):
            
            if bb_sales < 200:
                
                income = hours * wage
                
                #print(income)
                
                splitted_line.append(income)
                
                #print(splitted_line)
            
            if 200 <= bb_sales < 400:
                
                income = (bb_sales * 0.05) + (hours * wage)
                
                #print(income)
                
                splitted_line.append(income)
                
                #print(splitted_line)
                
                
            if 400 <= bb_sales < 600:
                
                income = (bb_sales * 0.07) + (hours * wage)
                
                #print(income)
                
                splitted_line.append(income)
                
                #print(splitted_line)
                
            if bb_sales > 600:
                
                income = bb_sales * 0.25
                
                #print(income)
                
                splitted_line.append(income)
                
                #print(splitted_line)
                
                
        if splitted_line[0].startswith('T'):
            
            
            toys_commissions = toy_sales * 0.1
                
            if bb_sales < 200:
                
                income = (hours * wage) + toys_commissions
                
                #print(income)
                
                splitted_line.append(income)
                
                #print(splitted_line)
                    
            if 200 <= bb_sales < 400:
                
                income = (bb_sales * 0.05) + (hours * wage) + toys_commissions
                
                #print(income)
                
                splitted_line.append(income)
                
                #print(splitted_line)
                
            if 400 <= bb_sales < 600:
                
                income = (bb_sales * 0.07) + (hours * wage) + toys_commissions
                
                #print(income)
                
                splitted_line.append(income)
                
                #print(splitted_line)
                
                
            if bb_sales > 600:
                
                income = (bb_sales * 0.25) + toys_commissions
                
                #print(income)
                
                splitted_line.append(income)
                
                #print(splitted_line)
                
             
    splitted_line[-1] = str(splitted_line[-1])
    
    print(splitted_line)
    
    splitted_line_text = ' '.join(splitted_line)
                
    with open('Sales_Report_Calculated', 'a') as file:
    
        file.write(str(splitted_line_text + '\n'))




   
    
    
    
#     if 'plain' in content_type:
        
#         print(part.get_payload())
        
#     elif 'html' in content_type:
        
#         html_ = part.get_payload()

#         soup = BeautifulSoup(html_, 'html.parser')
        
#         soup.decode_contents()
        
#         text = soup.get_text()
        
        
#         print(text)

#     elif 'text' in content_type:
        
#         ext = '.txt'
        
    
#     else:
        
#         print(content_type)
        
        
        
        
        
    
# IMPORTANT
# The program will not overwrite files if you run it twice !
# Save_path will show the last email and the last path created by program
# all of the files i need is saved in different directories (dates) but THEY ALL HAVE SAME NAME : msg-part-1.bat
        






