import pandas as pd
import matplotlib.pyplot as plt

# 1. Create Sample Data (Simulating a Netflix CSV)
data = {
    'Title': ['Stranger Things', 'Wednesday', 'The Crown', 'Dark', 'Money Heist', 'Squid Game'],
    'Genre': ['Sci-Fi', 'Fantasy', 'Drama', 'Sci-Fi', 'Crime', 'Thriller'],
    'Release_Year': [2016, 2022, 2016, 2017, 2017, 2021]
}

# 2. Load into a DataFrame
df = pd.DataFrame(data)

# 3. Exploratory Data Analysis (EDA)
print("--- Netflix Dataset Overview ---")
print(df.head())

# 4. Cleaning/Counting Genres
genre_counts = df['Genre'].value_counts()
print("\n--- Genre Breakdown ---")
print(genre_counts)

# 5. Visualization
genre_counts.plot(kind='bar', color='red')
plt.title('Top Netflix Genres in our Sample')
plt.xlabel('Genre')
plt.ylabel('Number of Shows')
plt.show()