import streamlit as st
from fpdf import FPDF, XPos, YPos
from datetime import datetime
from io import BytesIO
import os



class CertificateGenerator:
    def __init__(self):
        self.pdf = FPDF()
        self.pdf.add_page()
        self.pdf.set_auto_page_break(auto=True, margin=15)

    def header(self):
        if os.path.exists("Picture1.png"):
            self.pdf.image("Picture1.png", x=0, y=0, w=210, h=0)
        self.pdf.ln(40)

    def footer(self):
        self.pdf.set_y(-40)
        self.pdf.set_font("helvetica", "B", 11)
        self.pdf.set_text_color(211,175,55)
        self.pdf.cell(0, 10, "FOR AK ENTERPRISES", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="R")
        self.pdf.cell(0, 10, "(Authorized Signatory)", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="R")

    def generate_pickup_certificate(self, data):
        self.header()
        self.pdf.set_font("helvetica", "B", 12)
        self.pdf.set_text_color(211,175,55)
        self.pdf.cell(0, 10, f"DATED: _{data['date']}_", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="R")
        self.pdf.cell(0,10,"To", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.pdf.set_font("helvetica", "", 10)
        self.pdf.set_text_color(0,0,0)
        self.pdf.cell(0,10,f"{data['name']}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.pdf.cell(50,10,f"{data['address']}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.pdf.ln(10)
        self.pdf.write_html(f"""Subject:- <b>Pick up of fire extinguishers for refilling.</b><br><br><br><br><br><br>
                            &nbsp;&nbsp;&nbsp;&nbsp;This letter is to verify that AK ENTERPRISES has picked up <b>{sum(data['quantity'])} FIRE EXTINGUISHER CYLINDERS</b> from <b>{data['name']}</b>  for refilling of the same on <b>{data['date']}</b>. 
                            <br><br><br><br><br><b>Pick Up Details:- <br><br>
                            Party's Name:- {data['name']}<br><br>
                            Party's address:- {data['address']}</b><br><br><br><br>Quantity:<br><br>""")
        for i in range(len(data['quantity'])):
            self.pdf.write_html(f"<b>{i+1}. {data['capacity'][i]}: {data['quantity'][i]} NOS</b><br><br>")
        self.footer()
        pdf_bytes = BytesIO()
        self.pdf.output(pdf_bytes)
        pdf_bytes.seek(0)
        return pdf_bytes.getvalue()

    def generate_new_certificate(self, data):
        self.header()
        self.pdf.set_font("helvetica", "B", 12)
        self.pdf.set_text_color(211,175,55)
        self.pdf.cell(0, 10, "AGNI PRO/ABC/TC", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.pdf.set_font("helvetica", "B", 11)
        self.pdf.cell(0, 10, f"DATED: _{data['date']}_", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="R")
        self.pdf.set_font("helvetica", "", 10)
        self.pdf.set_text_color(0,0,0)
        self.pdf.write_html(f"""
            1. Party's Name: <b>{data['name']}</b><br><br>
            2. Party address: <b>{data['address']}</b><br><br>
            3. Items: Agni pro Fire Extinguisher<br><br>
            4. BIS Specification: Confirms To IS 15683 : 2018<br><br>
            5. Hydro Test: Tested At 35 Kgf/Cm2<br><br>
            6. Quantity:<br><br> """)
        for i in range(len(data['quantity'])):
            self.pdf.write_html(f"<b>{i+1}. {data['capacity'][i]}: {data['quantity'][i]} NOS</b><br><br>")
        self.pdf.set_y(-130)
        self.pdf.write_html(f"""        
            Fire Extinguishers New Date: {data['date']}<br><br>""")
        self.pdf.set_text_color(255,0,0)
        self.pdf.write_html(f""" 
            Body warranty: {data['warranty']} years <br><br>
            MAP Powder warranty: {data['warranty']} years.<br><br>
            Do Not use the Safety Seal under the warranty period.<br><br>""")
        self.pdf.ln(5)
        self.pdf.set_text_color(0,0,0)
        self.pdf.write_html(f""" 
            The above mentioned goods are warranted against defects in material and workmanship under normal use. 
            The warranty is limited to a period of sixty Month from the date of commissioning or sixty Month from date of supply whichever is earlier. 
            The company's obligation shall be limited to rectifying, repairing or replacing defective parts Ex Factory, 
            provided the purchaser has given immediate written notice upon the discovery of such defects. 
            The company will be automatically relieved of its obligation in case the unit is opened or any changes/repair is made without its prior approval 
            within the warranty period. The warranty accident results from defective and faulty workmanship.<br><br>
            <b>BILL Number: {data['billNo']}</b>""")
        self.footer()
        pdf_bytes = BytesIO()
        self.pdf.output(pdf_bytes)
        pdf_bytes.seek(0)
        return pdf_bytes.getvalue()

    def generate_refill_certificate(self, data):
        self.header()
        self.pdf.set_font("helvetica", "B", 16)
        self.pdf.set_text_color(211, 175, 55)
        self.pdf.cell(0, 10, "ABC Type Fire Extinguisher Refilling Warranty Certificate", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
        self.pdf.set_font("helvetica", "B", 11)
        self.pdf.cell(0, 10, f"DATED: _{data['date']}_", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="R")
        self.pdf.set_font("helvetica", "", 13)
        self.pdf.cell(0, 10, "TO WHOMSOEVER IT MAY CONCERN", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.pdf.ln(5)
        date_obj = datetime.strptime(data['date'], "%d/%m/%Y")
        due_date_obj = date_obj.replace(year=date_obj.year + int(data['warranty']))
        due_date = due_date_obj.strftime("%d/%m/%Y")
        self.pdf.set_font("helvetica", "", 10)
        self.pdf.set_text_color(0, 0, 0)
        
        html1 = f"""
        Party's Name: <b>{data['name']}</b><br><br>
        Party address: <b>{data['address']}</b><br><br><br><br>
        """
        self.pdf.write_html(html1)
        
        self.pdf.set_text_color(211, 175, 55)
        self.pdf.set_font("helvetica", "B", 12)
        self.pdf.write_html("<b>This is to certify that AK Enterprises has refilled:</b><br><br>")
        self.pdf.set_text_color(0, 0, 0)
        self.pdf.set_font("helvetica", "", 10)
        for i in range(len(data['quantity'])):
            self.pdf.write_html(f"<b>{i+1}. {data['capacity'][i]}: {data['quantity'][i]} NOS</b><br><br>")
        self.pdf.set_y(-120)
        self.pdf.set_font("helvetica","B",10)
        self.pdf.set_fill_color(255,0,0)
        self.pdf.cell(0, 5, f"Fire Extinguishers Refilling Date: {data['date']} And Due Date: {due_date}", 
                     border=0, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='L', fill=True)
        self.pdf.set_text_color(255,0,0)
        self.pdf.cell(0,10,f"MAP-90 Powder Warranty: {data['warranty']} years")
        self.pdf.set_text_color(0,0,0)
        self.pdf.set_fill_color(255,255,255)
        self.pdf.cell(0,8,"", border=0, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.pdf.set_y(-90)
        self.pdf.write_html(f"""Vide bill number <b>{data['billNo']}</b> Dated <b>{data['date']}</b>. <br><br>
                            We also take warranty on all refilled fire extinguishers.
                            If any fire extinguisher does not work during this period in any Fire Hazard,
                            we will refill the fire extinguisher free of cost within the said warranty period.""")
        self.footer()
        pdf_bytes = BytesIO()
        self.pdf.output(pdf_bytes)
        pdf_bytes.seek(0)
        return pdf_bytes.getvalue()

# Streamlit App
st.set_page_config(page_title="AK Certificate Maker", layout="wide", initial_sidebar_state="expanded")
st.markdown("🔥 # AK Enterprises Certificate Maker")

# Check if logo exists
logo_status = "✅ Logo Found!" if os.path.exists("Picture1.png") else "❌ Picture1.png missing!"

col1, col2 = st.columns([1, 3])
with col1:
    st.markdown("### 📋 Quick Form")
    cert_type = st.selectbox("Certificate Type", ["Refilling", "New", "Pickup"], key="type")
    name = st.text_input("Party Name", key="name")
    address = st.text_input("Party Address", key="address")
    
    col_date, col_warranty = st.columns(2)
    with col_date:
        selected_date = st.date_input("Date", value=datetime.now())
        date_formatted = selected_date.strftime("%d/%m/%Y")
    with col_warranty:
        warranty = st.number_input("Warranty (Years)", 1, 10, 5, key="warranty")
    
    bill_no = st.text_input("Bill No (optional)", key="billno")

with col2:
    st.markdown("### 🧯 Extinguisher Details")
    st.markdown(logo_status)
    
    # Dynamic extinguisher rows
    extinguishers = []
    if 'extinguishers' not in st.session_state:
        st.session_state.extinguishers = [{"capacity": "ABC Type Fire Extinguisher capacity 4Kg", "quantity": 1}]
    
    for i, ext in enumerate(st.session_state.extinguishers):
        col_cap, col_qty, col_del = st.columns([3, 1, 0.5])
        with col_cap:
            capacity = st.selectbox(
                f"Type {i+1}",
                ["ABC Type Fire Extinguisher capacity 4Kg", "ABC Type Fire Extinguisher capacity 6Kg", 
                 "ABC Type Fire Extinguisher capacity 9Kg", "ABC Type Fire Extinguisher capacity 12Kg",
                 "CO2 Type Fire Extinguisher capacity 4.5Kg"],
                index=0, key=f"cap_{i}"
            )
        with col_qty:
            quantity = st.number_input(f"Qty {i+1}", 1, 100, 1, key=f"qty_{i}")
        with col_del:
            if st.button("🗑️", key=f"del_{i}"):
                st.session_state.extinguishers.pop(i)
                st.rerun()
        extinguishers.append({"capacity": capacity, "quantity": quantity})
    
    if st.button("➕ Add Extinguisher", key="add_ext"):
        st.session_state.extinguishers.append({"capacity": "ABC Type Fire Extinguisher capacity 4Kg", "quantity": 1})
        st.rerun()

# Generate button
if st.button("🎯 Generate Certificate PDF", type="primary", use_container_width=True):
    if name and address:
        with st.spinner("Generating professional certificate..."):
            try:
                data = {
                    'name': name,
                    'address': address,
                    'date': date_formatted,
                    'warranty': str(warranty),
                    'billNo': bill_no or "N/A",
                    'capacity': [ext["capacity"] for ext in extinguishers],
                    'quantity': [ext["quantity"] for ext in extinguishers]
                }
                
                gen = CertificateGenerator()
                
                if cert_type == 'Refilling':
                    pdf_bytes = gen.generate_refill_certificate(data)
                    filename = "certificate_refill.pdf"
                elif cert_type == 'New':
                    pdf_bytes = gen.generate_new_certificate(data)
                    filename = "certificate_new.pdf"
                else:  # Pickup
                    pdf_bytes = gen.generate_pickup_certificate(data)
                    filename = "pickup_verification.pdf"
                
                st.balloons()
                st.success(f"✅ {cert_type} certificate generated successfully!")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.download_button(
                        label="⬇️ Download PDF",
                        data=pdf_bytes,
                        file_name=filename,
                        mime="application/pdf",
                        use_container_width=True
                    )
                
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
    else:
        st.warning("⚠️ Please fill Party Name and Address")

# Footer
st.markdown("---")
st.markdown("*Made for AK Enterprises - Professional Certificate Generation*")
