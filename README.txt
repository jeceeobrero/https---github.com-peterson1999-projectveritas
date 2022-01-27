Project Veritas
To address growing concerns with media integrity and increasing public distrust, Project Veritas offers a solution for netizens who consume news information through online to sift through fake news without actually having to do the tedious manual filtering themselves. With Project Veritas' news aggregation and credibility ranking features, all types of news are aggregated and sorted based on credibility to satisfy the growing number of information-sensitive netizens looking for more insights on the content they consume as well as its sources. 

Getting Started
To get a copy of the project up and running on your local machine, here are the following instructions needed to follow:
    GwteZip

1.) Download
Prerequisites
Here are the prerequisites with its following versions to be installed for Project Veritas to run locally:
[  ] beautifulsoup4==4.10.0
[  ] Django==3.2.8
[  ] h5py==3.1.0
[  ] keras==2.6.0
[  ] Keras-Preprocessing==1.1.2
[  ] mysqlclient==2.0.3
[  ] newspaper3k==0.2.8
[  ] nltk==3.6.3
[  ] numpy==1.19.5
[  ] pandas==1.3.3
[  ] Pillow==8.3.2
[  ] protobuf==3.18.1
[  ] pytz==2021.3
[  ] sqlparse==0.4.2
[  ] tensorboard==2.6.0
[  ] tensorboard-data-server==0.6.1
[  ] tensorboard-plugin-wit==1.8.0
[  ] tensorflow-estimator==2.6.0
[  ] tensorflow-cpu==2.6.0
[  ] tensorflow-hub==0.12.0
[  ] tldextract==3.1.2
[  ] tqdm==4.62.3
[  ] validators==0.18.2
[  ] whitenoise==5.3.0 

Running the Program
There are two ways on how to run Project Veritas either through local or online.

--Local--

1.) Download the zip copy of Project Veritas or clone the repo: https://github.com/jeceeobrero/projectveritas.git
2.) Install all the prerequisites mentioned above.
3.) Go to the root directory of Project Veritas.
4.) In your command terminal/bash, enter "python manage.py runserver" to finally run Project Veritas.
5.) Check the credibility of your news article and news outlet now!

--Online--

1.) Visit the url in your chosen web browser. (The url is not finalized as of the moment, please ask Innovateam for the url.)
2.) Check the credibility of your news article and news outlet now! 

Features and How to Access Them
The software contains 2 key features that extend to several sub-features.
[  ]  News Article Credibility Checker
Project Veritas checks the credibility of the news article based on four metrics namely: how relevant it is to today's current events, how opinionated the content is, how click-baiting is its news title, and how sensational is the whole article. 
1.) In any page of the website, enter in the topmost portion the url of the article you wish to check its credibility.
2.) Click the "Check" button.
3.) Wait for the website's machine learning to smartly check the news article.
4.) View the credibility scores of each metric and its overall. 
- Subfeatures
The data obtained from user submissions give host to several other features which are mainly limited to key insights that can be obtained from the same dataset such as (most credible articles and news outlets and a news outlet’s credibility performance over time).

News Article Credibility Ranking System

1.) In the Home Page, view the top 10 credible news articles displayed with its following credibility metric scores. 

News Outlet Credibility Ranking System

1.) In the same Home Page, view the top 10 credible news outlets displayed with its following overall credibility score.

News Outlet Credibility Performance

1.) In the same Home Page, choose a news outlet you wish to view its performance.
2.) In the left side of the news outlet page, a doughnut chart is displayed which visually shows each metric's credibility score.
3.) At the right side of it, a line chart which depicts the performance of the news outlet over time is displayed. To see the performance in detail, you may customize the chart by date and by category (day, month, year).
4.) At the bottom, its news articles are displayed which are sorted based on its credibility in descending order.
[  ] News Search & Aggregation System
Users may enter a news topic they are interested in however, unlike Google and Yahoo, Project Veritas recommends specific articles based on its credibility rankings as opposed to the article’s popularity.
1.) In any page of the website, enter a chosen topic at the topmost part.
2.) Click the "Search" button.
3.) View the related news articles which are sorted based on its credibility scores. 

Scope of Software
Project Veritas has its limited scopes in each category:
[  ] Browsers
At most all browsers across different platforms, such as mobile, supports Project Veritas. Here are few of the browsers that supports the said project:
-Google Chrome
-Brave
-Firefox
-Microsoft Edge
-Opera
-Siri
-Other Chromium-based Browsers
[  ] News Articles
As of now, Project Veritas can only check news articles that are in English language. The team is still actively working on how to accommodate all types of news articles in various languages to help netizens in different parts of the world to fact-check the information they consume online.
[  ] URLs
Project Veritas follows the standard url form