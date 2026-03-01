import pandas as pd
import matplotlib.pyplot as plt

# Sample Salary Data
salary_data = {
    'Country': ['USA', 'India', 'Germany', 'USA', 'India', 'Germany', 'UK', 'UK'],
    'Job_Title': ['Dev', 'Dev', 'Analyst', 'Analyst', 'Dev', 'Dev', 'Dev', 'Analyst'],
    'Salary': [95000, 25000, 70000, 85000, 22000, 68000, 60000, 58000]
}

df = pd.DataFrame(salary_data)

# Calculate Average Salary per Country
avg_salary = df.groupby('Country')['Salary'].mean().sort_values(ascending=False)

print("Average Salary by Country:")
print(avg_salary)

# Graphing the comparison
avg_salary.plot(kind='pie', autopct='%1.1f%%', startangle=140)
plt.title('Salary Distribution by Country')
plt.ylabel('') # Hides the 'Salary' label on the side
plt.show()