import json
import pickle
import numpy as np

class car_ownership():
    def __init__(self,data):
        self.data=data

    def loading_files(self):
        with open(r'artifacts/model_rf.pkl','rb') as file:
           self.rf2=pickle.load(file)  

        with open(r'artifacts/pca.pkl','rb') as file:
           self.pca = pickle.load(file)

        with open(r'artifacts/project_data.json','r') as file:
            self.project_data = json.load(file)   

            
    def car_owner_predict(self):
        self.loading_files()

        user_data = np.zeros(len(self.project_data['columns']))

        Monthly_Income = self.data['html_Monthly_Income']
        Credit_Score = self.data['html_Credit_Score']
        Years_of_Employment = self.data['html_Years_of_Employment']
        Finance_Status = self.data['html_Finance_Status']
        Number_of_Children = self.data['html_Number_of_Children']
        Occupation = self.data['html_Occupation']
        Finance_History = self.data['html_Finance_History']

        user_data[0] = Monthly_Income
        user_data[1] = Credit_Score
        user_data[2] = Years_of_Employment
        user_data[3] =self. project_data['Finance Status'][Finance_Status]
        user_data[4] = Number_of_Children
        user_data[5] = self.project_data['Finance History'][Finance_History]
        occupation = 'Occupation_'+Occupation
        index1 = self.project_data['columns'].index(occupation)           ## list method
        user_data[index1] = 1



        pca_trans =self.pca.transform([user_data])
        result =self.rf2.predict(pca_trans)
        return int(result[0])