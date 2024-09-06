import os
import pandas as pd

def ExtractData():
    folder_path=os.path.join('.','data')

    csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

    dataframes = {}

    for file in csv_files:
        file_path = os.path.join(folder_path, file)  # Create the full file path
        df_name = os.path.splitext(file)[0]  # Use the filename (without extension) as the key
        dataframes[df_name] = pd.read_csv(file_path)

    # Automated processing of DataFrames
    for df_name, df in dataframes.items():
        print(f"Processing {df_name}")
        # Example operation: Add a new column with the row count
        df['row_count'] = df.shape[0]
        # Save the processed DataFrame back to the dictionary
        dataframes[df_name] = df
    
    combined_df = pd.concat(dataframes.values(),ignore_index=True)

    return combined_df

def Preprocess(data):
    df = data[data['product'] == 'pink morsel'].copy()
    df['price']=df['price'].str[1:]
    df['price']=pd.to_numeric(df['price']).astype('Int64')
    df['Sales']=pd.to_numeric(df['price'], errors='coerce').astype('Int64')*df['quantity']
    df['date']=pd.to_datetime(df['date'])
    FormatedData=df[['Sales','date','region']]
    return FormatedData



def main():
    
    data=ExtractData()
    data=Preprocess(data)
    data.to_csv('FormatedOutput.csv',index=False)
    

if __name__=='__main__':
    main()