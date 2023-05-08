# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 19:37:53 2019

@author: User
"""

def pdf1():                                          #Creating the pdf of the bill
    
###########################################################################################################

##########################################################################################################
    
    class PDF(FPDF):
        def header(self):
            
            self.image("E:\sed.jpg", 10,8,33)
            # Arial bold 15
            self.set_font('Arial', 'B', 15)
            # Move to the right
            self.cell(80)
            # Title
            self.cell(0, 6, 'Receipt', 0, 1, 'L')
            # Line break
            self.ln(20)

        # Page footer
        def footer(self):
            # Position at 1.5 cm from bottom
            self.set_y(-15)
            # Arial italic 8
            self.set_font('Arial', 'I', 8)
            # Page number
            self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 1, 1, 'C')

    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    for i in range(1):
        far_in=f1.capitalize()
        loddu=l
        mobi_dn=str(m)
        free_fire=str(fees)
        cbbr=gst1(fees)
        as_cbbr=str(cbbr)
        pdf.cell(0, 10, 'Name                : ' + far_in, 0, 1)
        pdf.cell(0, 10, 'Address             : ' + loddu, 0, 1)
        pdf.cell(0, 10, 'Mobile Number       : ' + mobi_dn, 0, 1)
        pdf.cell(0, 10, 'Time In             : ' + tmin1, 0, 1)
        pdf.cell(0, 10, 'Time Out            : ' + tmout, 0, 1)
        pdf.cell(0, 10, 'Shop Address        : ' + 'Somewhere, somewhere', 0, 1)
        pdf.cell(0, 10, 'Price(Non Gaming)   : ' + 'Rs 0.5/min', 0, 1)
        pdf.cell(0, 10, 'Price(Gaming)       : ' + 'Rs 0.25/min', 0, 1)
        pdf.cell(0, 10, 'Original Amount     : ' + free_fire, 0, 1)
        pdf.cell(0, 10, 'GST                 : ' + '0.046%', 0, 1)
        pdf.cell(0, 10, 'Paid Amount         : ' + as_cbbr, 0, 1)
      
    
    genius="F:/Cyber_cafe (INVESTIG)/Software/Receipt/"+askey              # Have to specify the path
    pdf.output(genius, 'F')
    sql = "UPDATE tblusers SET RECEIPT_ID = %s WHERE Username = %s"
    val = (ask_for,f1)

    cursor.execute(sql, val)

    mycon.commit()
    
    print("Successfully! Printed")
    clear_all()