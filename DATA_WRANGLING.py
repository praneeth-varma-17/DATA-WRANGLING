

import pandas as pd



emp1 = pd.DataFrame({
    "Emp_ID": [101, 102, 103, 104, 105],
    "Name": ["Mithali", "Samiksha", "Jyothish", "Tanish", "Suhani"],
    "Dept": ["IT", "HR", "Finance", "IT", "Marketing"]
})

print("===== EMPLOYEE DATAFRAME 1 =====")
print(emp1)


emp2 = pd.DataFrame({
    "Emp_ID": [106, 107, 108, 109, 110],
    "Name": ["Praneeth", "Ashish", "Lohit", "Tharun", "Ganesh"],
    "Dept": ["HR", "IT", "Finance", "Marketing", "IT"]
})

print("\n===== EMPLOYEE DATAFRAME 2 =====")
print(emp2)




salary = pd.DataFrame({
    "Emp_ID": [101, 102, 103, 104, 105,
               106, 107, 108, 109, 110],
    "Salary": [45000, 40000, 55000, 50000, 42000,
               48000, 46000, 58000, 44000, 52000]
})

print("\n===== SALARY DATAFRAME =====")
print(salary)



emp = pd.concat([emp1, emp2], ignore_index=True)

print("\n===== CONCATENATION =====")
print(emp)




df1 = pd.DataFrame({
    "Name": ["Tanish", "Praneeth", "Ashish"],
    "Age": [20, 21, 20]
})

df2 = pd.DataFrame({
    "Marks": [85, 78, 92],
    "Grade": ["A", "B", "A"]
})

concat_columns = pd.concat([df1, df2], axis=1)

print("\n===== COLUMN-WISE CONCATENATION =====")
print(concat_columns)




inner_merge = pd.merge(
    emp,
    salary,
    on="Emp_ID",
    how="inner"
)

print("\n===== INNER MERGE =====")
print(inner_merge)



left_merge = pd.merge(
    emp,
    salary,
    on="Emp_ID",
    how="left"
)

print("\n===== LEFT MERGE =====")
print(left_merge)



right_merge = pd.merge(
    emp,
    salary,
    on="Emp_ID",
    how="right"
)

print("\n===== RIGHT MERGE =====")
print(right_merge)



outer_merge = pd.merge(
    emp,
    salary,
    on="Emp_ID",
    how="outer"
)

print("\n===== OUTER MERGE =====")
print(outer_merge)




employee = pd.DataFrame({
    "Employee_ID": [101, 102, 103],
    "Name": ["Tanish", "Praneeth", "Ashish"]
})

employee_salary = pd.DataFrame({
    "ID": [101, 102, 103],
    "Salary": [50000, 48000, 46000]
})

merge_different_columns = pd.merge(
    employee,
    employee_salary,
    left_on="Employee_ID",
    right_on="ID"
)

print("\n===== MERGE USING DIFFERENT COLUMN NAMES =====")
print(merge_different_columns)



emp_details = pd.DataFrame({
    "Name": ["Tanish", "Praneeth", "Ashish"],
    "Dept": ["IT", "HR", "Finance"]
}, index=[101, 102, 103])


emp_salary = pd.DataFrame({
    "Salary": [50000, 48000, 46000]
}, index=[101, 102, 103])


join_result = emp_details.join(emp_salary)

print("\n===== JOIN =====")
print(join_result)




left_join = emp_details.join(
    emp_salary,
    how="left"
)

print("\n===== LEFT JOIN =====")
print(left_join)



right_join = emp_details.join(
    emp_salary,
    how="right"
)

print("\n===== RIGHT JOIN =====")
print(right_join)



outer_join = emp_details.join(
    emp_salary,
    how="outer"
)

print("\n===== OUTER JOIN =====")
print(outer_join)




final_df = pd.merge(
    emp,
    salary,
    on="Emp_ID",
    how="inner"
)

print("\n===== FINAL EMPLOYEE DATA =====")
print(final_df)