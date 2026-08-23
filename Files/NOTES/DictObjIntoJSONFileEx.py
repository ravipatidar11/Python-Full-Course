#Program for Converting Saving OR Transfering Dict Object into  JSON  File (FileName.json)
#DictObjIntoJSONFileEx.py
import json
print("----------------------------------------------------------------------")
dictobj={'eno': 100, 'name': 'Rossum', 'sal':11.5}
print("Content of Dict Obj={}   Type={}".format(dictobj,type(dictobj)))
print("----------------------------------------------------------------------")
with open("E:\\KVR-PYTHON-7AM\\JSON\\NOTES\\emp.json","w") as fp:
	json.dump(dictobj,fp)
	print("Dict Object Data Saved in JSON File--Verify")
print("----------------------------------------------------------------------")

