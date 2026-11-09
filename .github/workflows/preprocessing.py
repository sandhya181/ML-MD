improt pandas as pd 
from sklearn.compose import CloumnTransfromer
from sklearn.dataset import make_classification
from sklearn.impute import SimpleImputer
from sklearn.pipeline import oneHotEncoder,StandardScaler
from sklearn.model_selection import train_test_split
def crate_pipeline():
  #Define which features are numeric vs categorical
  numeric_features = ['age','income']
  categorical_feature = ['city',occupation]
  #Preprocessing for numerical data (impute missing, then scale)
  numeric_transformer = Pipeline(steps=[('imputer',SimpleImputer(strategy='median')),('scaler',StandardScaler())])
  #Preprocessing for categorical data (impute mising,then one-hot encode)
  categorical_transformer = PPipeline(steps=[('imputer',SimpleImputer(strategy='constant'.fill_value='missing')),
   (OneHotEncoder(handel_unknown='ignore')) ])
  #Combine into a single ColumnTransformer
   preprocessor = ColumnTransformer(transformer=[('num',numeric_transformer,numeric_features),('cat',categorical_transfomer,numerical_features) ])
return preprocessor
if _name_ =="_main_":
  print("Preprocessing pipeline template ready.")
