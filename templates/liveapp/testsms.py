import json
dt = [{"farmer_telephone": "+254797916851", "cow_type": "dairy", "farmer_lname": "muriithi", "number_of_animals": 25, "breed": "Borana", "farming_method": "zero_grazing", "farmer_fname": "derrick"}, {"farmer_telephone": "+254797916852", "farmer_lname": "mwenje", "number_of_animals": 100, "breed": "local breed", "farming_method": "zero_grazing", "farmer_fname": "dom"}, {"farmer_telephone": "+254797916850", "farmer_lname": "mwenje", "number_of_animals": 100, "breed": "local breed", "farming_method": "zero_grazing", "farmer_fname": "dom"}]

res = {}
nos = []
st2 = ""
for line in dt:
	res.update(line)
	nos.append(res['farmer_telephone'])

x = ",".join(nos)
print x


