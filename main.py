import os
import zipfile
import pandas as pd


class main():
    '''
    def __init__(cls):
        cls.dataset_path = "C:\\Users\\Asymmetry\\Desktop\\dataset\\"
        cls.zip_path = "loan.csv.zip"
        cls.csv_path = "loan.csv"
    '''

    dataset_path = "C:\\Users\\Asymmetry\\Desktop\\dataset\\"
    zip_path = "loan.csv.zip"
    csv_path = "loan.csv"

    # main function
    @classmethod
    def run_main(cls):
        zip_file_path = os.path.join(cls.dataset_path, cls.zip_path)
        csv_file_path = os.path.join(cls.dataset_path, cls.csv_path)

        # if CSV file is not existing, extract zip file
        if not os.path.exists(csv_file_path):
            with zipfile.ZipFile(zip_file_path) as zf:
                zf.extract(cls.dataset_path)

        # read file
        raw_data = pd.read_csv(csv_file_path)
        # go through dataset
        cls.inspect_data(raw_data)

        # boolean mask as filter
        # isin(): Return a boolean Series showing whether each element in the Series is exactly contained in the passed sequence of values.
        filter_mask = raw_data["loan_status"].isin(["Fully Paid","Charged Off","Default"])
        filter_data = raw_data[filter_mask]
        print(filter_data["loan_status"].value_counts())

        # alter status "Fully Paid" to 0, otherwise to 1
        proc_filter_data = filter_data.copy()
        proc_filter_data["label"] = filter_data["loan_status"].apply(cls.create_label)

        # alter features of "emp_length"
        proc_filter_data["emp_length_feat"] = filter_data["emp_length"].apply(cls.proc_emp_length)

        filter_data.to_csv("C:\\Users\\Asymmetry\\Desktop\\dataset\\output\\proc_loan.csv", index = False)


    @staticmethod
    def create_label(status_val):
        label = 1
        if status_val == "Fully Paid":
            label = 0
        return label


    @staticmethod
    def inspect_data(df_data):
        print("\ndataset preview")
        print(df_data.head())

        print("\ndataset statistical information")
        print(df_data.describe())

        print("\ndataset basic information")
        print(df_data.info())

    @staticmethod
    def proc_emp_length(emp_length_val):
        if emp_length_val.split()[0] == "<" or emp_length_val.split()[0] == "n/a":
            label = 0.5
        elif emp_length_val.split()[0] == "10+":
            label = 10
        else: label = emp_length_val.split()[0]

        return label

    @staticmethod
    def analyze_lending_club_data(lc_data):
        # select specific column
        used_cols = ['loan_amnt', 'term', 'int_rate', 'grade', 'issue_d', 'addr_state', 'loan_status']
        used_data = lc_data[used_cols]
        # check dataset information
        print("\nanalyze dataset preview:")
        print(used_data.head())

        # 1.check different dataset status
        print("\ndata size of each loan status:")
        print(used_data["loan_status"].value_counts())

        # 2. total amount of loan by month
        # data type conversion
        print("convert data type...")
        used_data["issue_d2"] = pd.to_datetime(used_data["issue_d"])
        print("\nanalyze dataset preview:")
        print(used_data.head())
        print("\nanalyze basic information of data set:")
        print(used_data.info())

        data_group_by_date = used_data.groupby(["issue_d2"]).sum()
        data_group_by_date.reset_index(inplace = True)
        data_group_by_date["issue_month"] = data_group_by_date["issue_d2"].apply(lambda x: x.to_period("M"))

        load_amount_group_by_month = data_group_by_date.groupby("issue_month")["load_amnt"].sum()

        # convert to dataframe
        load_amount_group_by_month_df = pd.DataFrame(load_amount_group_by_month).reset_index()
        print("\ntotal loan amount preview by month:")
        print(load_amount_group_by_month_df.head())

        # save the results
        load_amount_group_by_month_df.to_csv("C:\\Users\\Asymmetry\\Desktop\\dataset\\output\\load_amount_by_month.csv", index = False)

        # 3. total amount of loan by state
        data_group_by_state = used_data.groupby(["addr_state"])["loan_amnt"].sum()

        # convert to dataframe
        data_group_by_state_df = pd.DataFrame(data_group_by_state).reset_index()
        print("\ntotal loan amount preview by state:")
        print(data_group_by_state_df.head())
        # save the results
        load_amount_group_by_month_df.to_csv("C:\\Users\\Asymmetry\\Desktop\\dataset\\output\\load_amount_by_state.csv", index = False)

main.run_main()