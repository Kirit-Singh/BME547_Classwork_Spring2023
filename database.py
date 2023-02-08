import Blood_Calculator as bc


print("This is the database.py file")
print("Python thinks this is called {}".format(__name__))


HDL = 55


HDL_analysis = bc.HDL_analysis(HDL)


print("The HDL analysis is {}".format(HDL_analysis))


bc.generic_input("Other Test")
print(bc.LDL_analysis(13))
