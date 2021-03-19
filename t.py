kpi1_endoint = "https://qovo4nsf3oonbax-db202103111252.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip_rose/kpi1/incvol//"

kpi1_r = requests.get(kpi1_endoint)
kpi1 = kpi1_r.json()["items"]

kpi1_months = []
kpi1_incidences_numbers = []
kpi1_priorities = []

for dict in kpi1:
    kpi1_monthss.append(dict["month"])
    kpi1_incidences_numbers.append(dict["incidences_number"])
    kpi1_priorities.append(dict["priority"])

#print(k1_months)
#print(k1_incidences_numbers)
#print(k1_priorities)


kpi1_df = pd.DataFrame({
    "Months": kpi1_months,
    "Number of incidents": kpi1_incidences_numbers,
    "Priority": kpi1_priorities
})