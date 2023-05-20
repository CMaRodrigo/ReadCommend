## Project Objective
The objective of this project is to develop a book recommender system that provides personalized recommendations to users based on their ratings. By utilizing the SVD++ (Singular Value Decomposition ++) algorithm, the system takes into account both explicit ratings and implicit feedback, enhancing the accuracy of the recommendations.

## Motivation

I love to read so I wanna do something related to it, and I feel that today we have't many programs or apps about it.


## Process

Finding a suitable API proved to be quite challenging. I explored options ranging from Goodreads to Google Books, but unfortunately, I was unable to utilize any of the available APIs. As a result, I decided to gather the maximum amount of data from Goodreads that was still accessible on the web, even though it was originally retrieved via API years ago. To ensure scalability and the potential for future enhancements, I opted to store this data in MySQL. This way, I can continue expanding my system and accommodating additional data in the future.


## The Algorithm
SVD++ (Singular Value Decomposition ++) is an advanced collaborative filtering algorithm widely used in recommender systems. It factors in user biases, implicit feedback, and explicit ratings to generate accurate and personalized book recommendations. The algorithm decomposes the user-item rating matrix into lower-dimensional representations, capturing latent factors associated with user preferences and book characteristics. Additionally, it incorporates a user bias vector to account for individual biases and tendencies. By training the model and optimizing its parameters, SVD++ predicts ratings for unseen items and generates recommendations tailored to each user, resulting in improved user satisfaction and engagement.

With the utilization of SVD++ algorithm, this book recommender system offers a powerful and effective approach to help users discover new books that align with their interests and preferences.


## Next Steps

If I had the credits to utilize the Chat GPT API, I would undoubtedly incorporate it into my application. This powerful tool has the potential to enhance my application by providing valuable suggestions and delivering more precise information about the books.
To further improve the process, I attempted to incorporate user input via the interface, store this data in a database, and then perform the necessary calculations. However, despite investing several hours, I encountered difficulties and was unable to successfully implement this step. Nevertheless, I believe that pursuing this approach could be a viable next step in enhancing the overall functionality of the system.





