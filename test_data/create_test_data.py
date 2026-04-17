import openpyxl

# create a workbook 
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "PIN Test data"


#add header 
sheet["A1"] = "invalid_pin"
sheet["A2"] = "expected_message"


#Add test data 
sheet["A2"] = "abc"
sheet["B2"] = "Characters are not allowed"

sheet["A3"] = "12@#$"
sheet["B3"] = "Special characters are not allowed"

sheet["A4"] = "123"
sheet["B4"] = "PIN Code must have 6 Digits"

sheet["A5"] = "12 34"
sheet["B5"] = "Characters are not allowed"

# Save the file
workbook.save("test_data/pin_test_data.xlsx")
print("Excel file created successfully!")
