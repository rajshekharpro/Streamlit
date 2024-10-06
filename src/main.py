import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Simple Data Dashboard")

# uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

uploaded_file = pd.read_csv('github_dataset.csv')  # Update with the correct path

if uploaded_file is not None:
    df = uploaded_file

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select column to filter by", columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select value", unique_values)

    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)

    st.subheader("Plot Data")
    x_column = st.selectbox("Select x-axis column", columns)
    y_column = st.selectbox("Select y-axis column", columns)

    if st.button("Generate Plot"):
        st.line_chart(df.set_index(x_column)[y_column])

    
    # Most Starred Repositories
    st.subheader('Top 10 Most Starred Repositories')
    top_stars = df.nlargest(10, 'stars_count')
    st.bar_chart(top_stars.set_index('repositories')['stars_count'])

    # Language Distribution
    st.subheader('Programming Language Distribution')
    language_counts = df['language'].value_counts()
    st.bar_chart(language_counts)

    # Issues vs Pull Requests
    st.subheader('Issues vs Pull Requests')
    fig, ax = plt.subplots()
    ax.scatter(df['issues_count'], df['pull_requests'])
    ax.set_xlabel('Number of Open Issues')
    ax.set_ylabel('Number of Pull Requests')
    ax.set_title('Issues vs Pull Requests')
    st.pyplot(fig)

    # Calculate average star counts by language
    average_stars = df.groupby('language')['contributors'].mean().reset_index()
    # print(average_stars.shape)
    # st.write(average_stars)
    top_language = average_stars.loc[average_stars['contributors'].idxmax()]


    # Generate insight dynamically
    insight_text = f"""
    ### Insight:
    After analyzing the dataset, it appears that repositories written in **{top_language['language']}** have the highest average star count of **{top_language['contributors']:.2f}** stars. This indicates a strong community interest and engagement with this language. 
    This pattern highlights the importance of programming languages in repository visibility and attractiveness.
    """
    # Calculate the most used languages
    most_used_languages = df['language'].value_counts().reset_index()
    most_used_languages.columns = ['language', 'count']

    top_language_overall = most_used_languages.iloc[0]


    # Display the most used language
    st.subheader('Most Used Programming Language')
    st.markdown(f"The most used programming language across all repositories is **{top_language_overall['language']}** with **{top_language_overall['count']}** occurrences.")


    st.markdown(insight_text) 

else:
    st.write("Waiting on file upload...")






# import streamlit as st
# import dask.dataframe as dd
# import pandas as pd

# st.title("Simple Data Dashboard")

# # Set maximum file upload size (Streamlit does not currently support custom max file sizes)
# st.set_option('server.maxUploadSize')  # Max upload size in MB

# uploaded_file = st.file_uploader("Choose a CSV file", type="csv", accept_multiple_files=False)

# if uploaded_file is not None:
#     # Use Dask to read the CSV file
#     df = dd.read_csv(uploaded_file)

#     # Convert Dask DataFrame to Pandas DataFrame for display
#     st.subheader("Data Preview")
#     st.write(df.head().compute())  # Use compute() to fetch the data

#     st.subheader("Data Summary")
#     st.write(df.describe().compute())  # Compute the summary

#     st.subheader("Filter Data")
#     columns = df.columns.tolist()
#     selected_column = st.selectbox("Select column to filter by", columns)
#     unique_values = df[selected_column].unique().compute()  # Compute unique values
#     selected_value = st.selectbox("Select value", unique_values)

#     filtered_df = df[df[selected_column] == selected_value]
#     st.write(filtered_df.compute())  # Compute the filtered DataFrame

#     st.subheader("Plot Data")
#     x_column = st.selectbox("Select x-axis column", columns)
#     y_column = st.selectbox("Select y-axis column", columns)

#     if st.button("Generate Plot"):
#         # Convert to Pandas for plotting
#         plot_data = filtered_df[[x_column, y_column]].compute()  # Compute the data for plotting
#         st.line_chart(plot_data.set_index(x_column)[y_column])

# else:
#     st.write("Waiting on file upload...")




# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Load data
# @st.cache_resource  
# def load_data():
#     data = pd.read_csv('repository_data.csv')  # Update with the correct path
#     return data

# # Main function to run the app
# def main():
#     # Title of the app
#     st.title("GitHub Repositories Dashboard")

#     # Load dataset
#     df = load_data()

#     # Display dataset overview
#     st.subheader("Dataset Overview")
#     st.dataframe(df.head())
    
#     # Filter by minimum stars
#     min_stars = st.slider("Minimum Stars", 0, df['stars_count'].max(), 0)
#     filtered_data = df[df['stars_count'] >= min_stars]
    
#     # Top Repositories by Stars
#     st.subheader("Top Repositories by Stars")
#     top_stars = filtered_data.nlargest(10, 'stars_count')
#     st.dataframe(top_stars[['repositories', 'stars_count']])

#     # Forks vs Stars scatter plot
#     st.subheader("Forks vs Stars")
#     fig, ax = plt.subplots()
#     sns.scatterplot(data=filtered_data, x='forks_count', y='stars_count', ax=ax)
#     ax.set_title("Forks vs Stars")
#     ax.set_xlabel("Forks Count")
#     ax.set_ylabel("Stars Count")
#     st.pyplot(fig)

#     # Most Active Repositories
#     st.subheader("Most Active Repositories")
#     active_repos = filtered_data.nlargest(10, 'issues_count')
#     st.dataframe(active_repos[['repositories', 'issues_count', 'pull_requests']])

#     # Language Distribution
#     st.subheader("Language Distribution")
#     language_counts = filtered_data['language'].value_counts()
#     fig, ax = plt.subplots()
#     language_counts.plot(kind='bar', ax=ax)
#     ax.set_title("Number of Repositories by Language")
#     ax.set_xlabel("Programming Language")
#     ax.set_ylabel("Number of Repositories")
#     st.pyplot(fig)

#     # Contributors vs Stars
#     st.subheader("Contributors vs Stars")
#     fig, ax = plt.subplots()
#     sns.scatterplot(data=filtered_data, x='contributors', y='stars_count', ax=ax)
#     ax.set_title("Contributors vs Stars")
#     ax.set_xlabel("Number of Contributors")
#     ax.set_ylabel("Stars Count")
#     st.pyplot(fig)

#     # Average Stars per Language
#     st.subheader("Average Stars per Language")
#     avg_stars_language = filtered_data.groupby('language')['stars_count'].mean().sort_values(ascending=False)
#     fig, ax = plt.subplots()
#     avg_stars_language.plot(kind='bar', ax=ax)
#     ax.set_title("Average Stars per Language")
#     ax.set_xlabel("Programming Language")
#     ax.set_ylabel("Average Stars Count")
#     st.pyplot(fig)

# # Run the app
# if __name__ == "__main__":
#     main()


# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Load data
# @st.cache_data
# def load_data():
#     data = pd.read_csv('repository_data.csv')  # Update with the correct path
#     data['created_at'] = pd.to_datetime(data['created_at'])  # Convert to datetime
#     return data

# # Main function to run the app
# def main():
#     # Title of the app
#     st.title("GitHub Repositories Dashboard")

#     # Load dataset
#     df = load_data()

#     # Display dataset overview
#     st.subheader("Dataset Overview")
#     st.dataframe(df.head())

#     # Filter by minimum stars
#     min_stars = st.slider("Minimum Stars", 0, df['stars_count'].max(), 0)
#     filtered_data = df[df['stars_count'] >= min_stars]

#     # Top Repositories by Stars
#     st.subheader("Top Repositories by Stars")
#     top_stars = filtered_data.nlargest(10, 'stars_count')
#     st.dataframe(top_stars[['name', 'stars_count']])

#     # Forks vs Stars scatter plot
#     st.subheader("Forks vs Stars")
#     fig, ax = plt.subplots()
#     sns.scatterplot(data=filtered_data, x='forks_count', y='stars_count', ax=ax)
#     ax.set_title("Forks vs Stars")
#     ax.set_xlabel("Forks Count")
#     ax.set_ylabel("Stars Count")
#     st.pyplot(fig)

#     # Most Active Repositories (based on Pull Requests)
#     st.subheader("Most Active Repositories by Pull Requests")
#     active_repos = filtered_data.nlargest(10, 'pull_requests')
#     st.dataframe(active_repos[['name', 'pull_requests', 'stars_count']])

#     # Language Distribution
#     st.subheader("Primary Language Distribution")
#     language_counts = filtered_data['primary_language'].value_counts()
#     fig, ax = plt.subplots()
#     language_counts.plot(kind='bar', ax=ax)
#     ax.set_title("Number of Repositories by Primary Language")
#     ax.set_xlabel("Primary Language")
#     ax.set_ylabel("Number of Repositories")
#     st.pyplot(fig)

#     # Commit Count vs Stars
#     st.subheader("Commit Count vs Stars")
#     fig, ax = plt.subplots()
#     sns.scatterplot(data=filtered_data, x='commit_count', y='stars_count', ax=ax)
#     ax.set_title("Commit Count vs Stars")
#     ax.set_xlabel("Commit Count")
#     ax.set_ylabel("Stars Count")
#     st.pyplot(fig)

#     # Repositories Created Over Time
#     st.subheader("Repositories Created Over Time")
#     df['year_created'] = df['created_at'].dt.year
#     repo_per_year = df['year_created'].value_counts().sort_index()
#     fig, ax = plt.subplots()
#     repo_per_year.plot(kind='line', ax=ax)
#     ax.set_title("Repositories Created Over Years")
#     ax.set_xlabel("Year")
#     ax.set_ylabel("Number of Repositories")
#     st.pyplot(fig)

#     # License Distribution
#     st.subheader("License Distribution")
#     license_counts = filtered_data['license'].value_counts()
#     fig, ax = plt.subplots()
#     license_counts.plot(kind='bar', ax=ax)
#     ax.set_title("Number of Repositories by License")
#     ax.set_xlabel("License Type")
#     ax.set_ylabel("Number of Repositories")
#     st.pyplot(fig)

# # Run the app
# if __name__ == "__main__":
#     main()
