import streamlit as st
from PIL import Image
import requests
import pandas as pd

def Bank_Data_Finder(IFSC_Code):
    try:
        url = 'https://ifsc.razorpay.com/' + IFSC_Code
        bank_info = requests.get(url).json()
        all_details = []
        bank_name = bank_info['BANK']
        branch = bank_info['BRANCH']
        address = bank_info['ADDRESS']
        city = bank_info['CITY']
        state = bank_info['STATE']
        bank_code = bank_info['BANKCODE']
        ifsc = bank_info['IFSC']
        micr = bank_info['MICR']
        contact = bank_info['CONTACT'] 
        upi = 'UPI: ' + 'Available' if bank_info['UPI'] == True else 'Not Available'
        rtgs = 'RTGS: ' + 'Available' if bank_info['RTGS'] == True else 'Not Available'
        neft = "NEFT: " + 'Available' if bank_info['NEFT'] == True else 'Not Available'
        imps = 'IMPS: ' + 'Available' if bank_info['IMPS'] == True else 'Not Available'

        all_details.append(bank_name)
        all_details.append(branch)
        all_details.append(address)
        all_details.append(city)
        all_details.append(state)
        all_details.append(bank_code)
        all_details.append(ifsc)
        all_details.append(micr)
        all_details.append(contact)
        all_details.append(upi)
        all_details.append(rtgs)
        all_details.append(neft)
        all_details.append(imps)

        return all_details

    except Exception as e:
        print(e)

def run():
    img1 = Image.open('ifsc-icon.jpg')
    img1 = img1.resize((300,170))
    st.image(img1,use_column_width=True)
    st.title("Bank Details Checker Using IFSC")

    st.text("- IFSC code should be 11 characters in size.")
    st.text("- IFSC code is contains a combination of alphabets and numbers.")
    st.text("- First 4 characters are alphabetic characters representing the bank name.")
    st.text("- 5th character is 0 (zero) and reserved for future use.")
    st.text("- Last 6 characters are usually numbers but can also be alphabets. These represent a branch of the bank.")

    ## IFSC
    ifsc = st.text_input('Enter your Bank IFSC Code')
    if st.button("Search"):
        bank_data = Bank_Data_Finder(ifsc)
        # data = pd.DataFrame(bank_data)
        if bank_data:
            index_name = ['Bank Name','Branch','Address','City','State','Bank-Code', 'IFSC','MICR', 'Contact','UPI','RTGS','NEFT','IMPS']
            df = pd.DataFrame({'Details': bank_data},index = index_name)
            st.dataframe(df)
        else:
            st.info("Invalid IFSC! Check Once Again and Retry!!")


run()

