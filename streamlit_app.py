import streamlit as st
import pandas as pd
import numpy as np
from surprise import dump
from datetime import date


# Set page configuration
st.set_page_config(
    page_title='Book Recommendations',
    layout='centered',
    initial_sidebar_state='auto'
)

# Display title and image
st.title('Book Recommendations')
st.image('images/library.jpg', width=600)
st.write('')


# Display user input field
st.markdown("""
    **Please enter the user ID to find 10 books recommended.** 
    Possible inputs are from 1 to 53424.
""")

# Functions

@st.cache_data(show_spinner=False)
def load_csv_data(file_path, index_col=None):
    df = pd.read_csv(file_path, index_col=index_col)
    return df


def preprocess_user_data(user_id, ratings_df):
    """
    New data
    """
    rated_books = set(ratings_df.loc[ratings_df['user_id'] == user_id, 'book_id'])
    all_books = set(ratings_df['book_id'])
    books_unknown_rating = sorted(all_books - rated_books)

    # Create a test set for the user so that it can be used to predict unknown ratings
    user_testset = []
    for i in books_unknown_rating:

        user_testset.append((user_id, i, 3.92))
    
    return user_testset


def get_top_n_recommendations(predictions, n=10):
    """
    Return the top N recommendations (book ids) from a list of predictions 
    made for the user.
    """

    # Append tuples with the book id and predicted rating to a list
    all_predictions = []
    for user_id, book_id, true_rating, rating_est, details in predictions:
        all_predictions.append((book_id, rating_est))

    # Sort the predictions and retrieve the n highest ones
    all_predictions.sort(key=lambda x: x[1], reverse=True)
    top_n_book_ids = [book_id for book_id, rating_est in all_predictions[:n]]

    return top_n_book_ids


def get_book_details(book_id, books_df):

    author = books_df.loc[book_id, 'author']
    title = books_df.loc[book_id, 'title']
    year = books_df.loc[book_id, 'original_publication_year']
    
    return author, title, year

# User Input

user_input = st.text_input('Input your user ID (e.g. 654, 11300)')


# Load Data

path_ratings = 'data/ratings_train.csv'
ratings = load_csv_data(path_ratings)
unique_users = ratings['user_id'].unique()

path_books = 'data/book_details.csv'
index_col_books = 'book_id'
books = load_csv_data(path_books, index_col=index_col_books)


# Check the Input

if user_input:
    try:
        assert user_input[0] != '0'
        user_input_int = int(user_input)
        assert user_input_int in unique_users
    except:
        st.info('There is no profile with this user ID')
        user_input_int = None
else:
    user_input_int = None


# Recommendations (Item-based collaborative filtering)

if user_input_int:
    recommendation_state = st.text('Choosing books...')

    if 'svdpp_model' not in st.session_state:
        path_svdpp = 'svdpp'
        _, svdpp = dump.load(path_svdpp)
        st.session_state['svdpp_model'] = svdpp

    user_testset = preprocess_user_data(user_input_int, ratings)
    user_predictions = st.session_state['svdpp_model'].test(user_testset)
    top_n_book_ids = get_top_n_recommendations(user_predictions, n=10)

    recommendations = []
    for i, book_id in enumerate(top_n_book_ids):
        author, title, year = get_book_details(book_id, books)

        if np.isnan(year):
            recommendations.append(f'{i+1}. **{author}.** {title}.\n')
        else:
            recommendations.append(f'{i+1}. **{author}.** {title}, {int(year)}\n')
    
    recommendations_string = ''.join(recommendations)

    recommendation_state.empty()

    st.subheader('Books you may like:')
    st.markdown(recommendations_string)


## Getting the books of the day
books_df = pd.read_csv('data/book_details.csv')
# Get the book of the day based on the current date
today = date.today()
book_index = today.toordinal() % len(books_df)
book = books_df.iloc[book_index]

    # Display book information
st.markdown('## Book of the Day')
st.markdown(f"**Title**: {book['title']}")
st.markdown(f"**Author**: {book['author']}")