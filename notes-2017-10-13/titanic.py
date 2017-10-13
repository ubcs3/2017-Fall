import pandas as pd
import re

def preprocessing(data):
    
    data = data.copy()
    
    # Drop PassengerId column
    data = data.drop('PassengerId',axis=1)

    # Convert gender feature to numeric
    data['Gender'] = data['Sex'].map({'male': 0, 'female': 1})
    
    # Extract title from the name column
    # Assign title 'Rare' if no title is found
    def get_title(name):
        try:
            return re.search('[a-zA-Z]+\.',name).group(0)[:-1]
        except:
            return 'Rare'

    data['Title'] = data['Name'].map(get_title)

    # Transform titles into common groups
    # 'Dr','Master','Miss','Mr','Mrs','Rev','Military','Royalty'
    def title_transform(title):
        if title in ['Mr','Mrs','Miss','Master','Rev','Dr']:
            return title
        elif title == 'Mme':
            return 'Mrs'
        elif title in ['Mlle','Ms']:
            return 'Miss'
        elif title in ['Capt', 'Col','Major']:
            return 'Military'
        elif title in ['Jonkheer','Lady','Sir','Don','Dona','Countess']:
            return 'Royalty'
        else:
            return 'Rare'

    data['Title'] = data['Title'].map(title_transform)

    # Convert categorical 'Title' column to numeric using one-hot encoding
    def categorical_to_numeric(df,column_name):
        categories_df = pd.get_dummies(df[column_name],prefix=column_name)
        df = pd.concat([df,categories_df],axis=1)
        categories_list = list(categories_df.columns)
        return df, categories_list
    
    data, title_list = categorical_to_numeric(data,'Title')
    
    # Fill in missing data in 'Age' column using median age by title
    ages = data[data['Age'].notnull()]
    median_age_by_title = ages.groupby('Title')['Age'].median()
    missing_ages = data[data['Age'].isnull()]['Title'].map(median_age_by_title)
    data['Age'] = data['Age'].fillna(missing_ages)
    
    # Fill in missing data in 'Fare' column using median by Pclass
    fares = data[data['Fare'].notnull()]
    median_fare_by_class = fares.groupby('Pclass')['Fare'].median()
    missing_fares = data[data['Fare'].isnull()]['Pclass'].map(median_fare_by_class)
    data['Fare'] = data['Fare'].fillna(missing_fares)
    
    # Create 'Alone' column for passengers travelling alone
    family = data['SibSp'] + data['Parch']
    data['Alone'] = family.map(lambda x: 1 if x == 0 else 0)
    
    # Assign Deck X to missing data in 'Cabin' column
    # Create 'Deck' column from 'Cabin' column
    # Convert categorical 'Deck' column to numeric using one-hot encoding
    data['Cabin'].fillna('X', inplace=True)
    data['Deck'] = data['Cabin'].map(lambda x: x[0])
    data, deck_list = categorical_to_numeric(data,'Deck')
    
    # Fill in missing data in 'Embarked' with most common 'S'
    # Convert categorical 'Embarked' column to numeric using one-hot encoding
    data['Embarked'].fillna('S',inplace=True)
    data, embarked_list = categorical_to_numeric(data,'Embarked')
    
    # Select the features to return
    features = ['Pclass','Age','SibSp','Parch','Fare','Gender','Alone'] + title_list + deck_list + embarked_list
    
    return data[features]