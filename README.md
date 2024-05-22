# Perfume Haul

## Author
Chan Nyein Zin

## Project Title
Perfume Recommendation System Using Machine Learning

## Project Description
The Perfume Recommendation System is designed to simplify the exploration of fragrances for users by providing ratings and recommendations. Leveraging Python 3.7+ and machine learning technologies, this platform utilizes Pandas and NumPy for data manipulation, Matplotlib for visual analytics, and Beautiful Soup for web scraping from the VenbaFragrance website. The system employs both collaborative and content-based filtering techniques to help both novices and perfume enthusiasts discover scents that best match their preferences, enhancing the overall user experience.

## Requirements, Features, and User Stories

### Software:
- **Python 3.7+**: Main programming language used for backend development.
- **Jupyter Notebook**: Utilized for interactive development and testing, particularly useful for experimenting with data manipulation and visualization scripts.

## Technical Specification

- **Data Handling**: Python with Pandas and NumPy for managing and analyzing data.
- **Machine Learning**: Collaborative and content-based filtering methods for generating recommendations.

### Libraries and Frameworks:
- **Streamlit**: Used to create the user interface and deploy the interactive web application, allowing users to explore perfume recommendations.
- **Pandas**: Employs its data structures and tools for efficient data manipulation and analysis, crucial for handling the perfume dataset.
- **Pickle**: Utilized for loading and saving pre-processed data and model state, ensuring efficient data persistence.
- **os**: Provides functionalities to interact with the file system, ensuring robust file operations like checking for file existence.
- **scikit-learn (cosine_similarity)**: Facilitates the calculation of similarity scores between various perfumes based on their characteristics, supporting the recommendation logic in the backend.

## System or Software Architecture Diagram
*Include a block-based diagram illustrating the architecture of your software or system. This should include major components, such as user interface elements, back-end services, and data storage, and show how they interact. Tools like Lucidchart, Draw.io, or even hand-drawn diagrams photographed and uploaded are acceptable. The purpose of the diagram is to help us understand the architecture of your solution. Diagram aesthetics do not matter and will not be graded.*

## Potential Challenges and Roadblocks
- **Data Quality**: Ensuring the quality and completeness of the perfume dataset.
- **Algorithm Optimization**: Fine-tuning the recommendation algorithms for better accuracy and performance.
- **Web Scraping**: Handling website changes and updates that may affect data extraction.
- **Deployment**: Ensuring smooth deployment of the web application, considering potential compatibility issues with different environments.

## Additional Resources
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)
- [Beautiful Soup Web Scraper](https://realpython.com/beautiful-soup-web-scraper-python/)

## Conclusion and Future Work
In conclusion, this project aims to deliver a robust and user-friendly perfume recommendation system. Future enhancements may include expanding the dataset, integrating real-time user feedback, and exploring more advanced machine learning models to improve recommendation accuracy.

## Installation
Install the necessary dependencies with the following command:
```bash
pip install -r requirements.txt
```

## How to Run

1. Clone the repository:
    ``` bash
    git clone https://github.com/channyeinzin/Perfume-Recommendation-Engine-.git
    ```
2. Navigate to the Project Directory: Open a terminal or command prompt, and change your directory to the root directory of the project:
    ``` bash
    cd <project_directory>
    ```
3. Install Dependencies: Before running the application, install the required dependencies by executing:
    ``` bash
    pip install -r requirements.txt
    ```
4. Run the Application: Once the dependencies are installed, you can run the Streamlit application by executing:
    ``` bash
    streamlit run app.py
    ```

## How to Use

1. Type or choose from the drop-down bar.
2. After choosing, click on "Show Recommendations".

## Demo

![Demo Screenshot1](/src/img/src.gif)

---

Feel free to copy this and use it in your GitHub repository!
