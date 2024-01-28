from django.shortcuts import render
from TelecomPrediction.models import customerInfo
import pickle
pickleFile =  open('./savedModels/model.pkl', 'rb')
vot_clf = pickle.load(pickleFile)

# Create your views here.

def prediction(request):
    if request.method == 'POST' :
        Age = request.POST['Age']
        Tenure_in_Months = request.POST['Tenure_in_Months']
        Offer = request.POST['Offer']
        Internet_Type = request.POST['Internet_Type']
        Avg_Monthly_GB_Download = request.POST['Avg_Monthly_GB_Download']
        Unlimited_Data = request.POST['Unlimited_Data']
        Contract = request.POST['Contract']
        Payment_Method = request.POST['Payment_Method']
        Monthly_Charge = request.POST['Monthly_Charge']
        Total_Extra_Data_Charges = request.POST['Total_Extra_Data_Charges']

        print(Age)
        print(Tenure_in_Months)
        print(Offer)
        print(Internet_Type)
        print(Avg_Monthly_GB_Download)
        print(Unlimited_Data)
        print(Contract)
        print(Payment_Method)
        print(Monthly_Charge)
        print(Total_Extra_Data_Charges)
        y_pred = vot_clf.predict([[int(Age),int(Tenure_in_Months),int(Offer),int(Internet_Type),int(Avg_Monthly_GB_Download),int(Unlimited_Data),int(Contract),int(Payment_Method),int(Monthly_Charge),int(Total_Extra_Data_Charges)]])

        if y_pred[0] == 0:
                 y_pred = "Churned"
        else:
                 y_pred = "Stayed"   
        ins = customerInfo(Age=Age,Tenure_in_Months=Tenure_in_Months,Offer=Offer,Internet_Type=Internet_Type,Avg_Monthly_GB_Download=Avg_Monthly_GB_Download,Unlimited_Data=Unlimited_Data,Contract=Contract,Payment_Method=Payment_Method,Monthly_Charge=Monthly_Charge,Total_Extra_Data_Charges=Total_Extra_Data_Charges,prediction=y_pred)
        ins.save()
        print("The data has been written to the DB")
        return render(request, 'user.html',{'result': y_pred})     

    return render(request,'user.html')
