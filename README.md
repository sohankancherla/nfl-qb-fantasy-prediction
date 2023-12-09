### NFL QB Fantasy Prediction

**Sohan Kancherla**

#### Executive summary
The goal of this project was to develop a model that can accurately predict the fantasy football points of NFL quarterbacks. The model is trained on NFL data from 2017 to 2022 and includes data from various sources. There isn't a lot of properly labeled NFL historical data that is easy to access which made the project more difficult but overall the model has a safe estimate and can predict slight trends of Quartebacks. This is an example of the model's prediction for Jalen Hurts this year:
![image](https://github.com/sohankancherla/nfl-qb-fantasy-prediction/assets/30853467/815827f9-bb71-4daa-823e-9a02fd527577)

#### Rationale
This project can help Fantasy Football players by providing them the predicted fantasy points so they can start the right quarterback every week. It can also help them understand what factors help quarterbacks perform better and what factors make them perform worse. NFL teams and coaching staff can also take advantage of the positive and negative factors to boost their QBs performance.

#### Research Question
There are two main questions that are getting answered. 1) getting an accurate prediction or trend of a quarterback so fantasy managers can decide who to start. 2) to find factors that make QBs perform better or worse.

#### Data Sources
There was no clean dataset of fantasy points so I scraped and merge the data from the following sites. Scraping and merging scripts can be found int he data directory.
Data Sources:
  - Madden Data (https://maddenratings.weebly.com/)
  - Fantasy Points Data (https://www.fantasypros.com/nfl/reports/leaders/qb.php?year=2023)
  - Schedule Data (https://www.nflweather.com/)

#### Methodology
I initially wanted to use a Time Series model but it would be difficult to include multiple features and I would need a new model for each player. So instead I decided to create both Linear Regression and Neural Network models and add more features that could impact a QB's performance. Here are the features I used:

![image](https://github.com/sohankancherla/nfl-qb-fantasy-prediction/assets/30853467/b588ab60-65c1-4687-a75f-cdc5459961cf)

#### Results
Among the regression models, suprisingly the best model was a simple linear regression with no polynomial features. All the models I tested did have similar MSE but Linear Regression performed the best on the 2023 data and had the fastest training time. Here is a plot of the regression models and mse:
![image](https://github.com/sohankancherla/nfl-qb-fantasy-prediction/assets/30853467/e6926cd4-2167-49e5-bbfe-9d2f0288a71a)

These are the weight with the corresponding featuers:
![image](https://github.com/sohankancherla/nfl-qb-fantasy-prediction/assets/30853467/af5bacbe-b3ea-4c4d-a6de-d0dcd67c0a69)

I also trained different Neural Network models and compared the MSEs. Overall performance is slighly better than the Linear Regression with Model 4 having the best validation MSE out of all of the models:
![image](https://github.com/sohankancherla/nfl-qb-fantasy-prediction/assets/30853467/98cfaf82-244d-405a-8fad-0db8b18e80a3)

Although NN has a better MSE it is not a significant gap to justify the longer fit time. Linear Regression also provides information on each feature based on the coefficents which can be more useful to some users than the actual prediction itself. Here is the prediction of both Linear Regression and Model 4 on Patrick Mahomes in the 2023 season and as you can see there is not much of a difference between both models:
![image](https://github.com/sohankancherla/nfl-qb-fantasy-prediction/assets/30853467/d5dc33d9-c3ab-4ac4-a27f-d1a79517502a)

#### Next steps
My first suggestion would be to train the models again with way more features. I had a hard time finding NFL data and merging it together, but with more features the model will perform much better. NFL QB's performance can rely on so many factors that are not accounted for in my model. Here are some of the features I would like to inlude but don't have data: Weather, Injuries, Age, Is the quarterback hurt, and many more. Also given enough data, the best approach for this problem would be to train an individual LSTM model for each player. This will allow each model to learn the different tendencies of each player instead of generalizing to everyone.

#### Outline of project

- [Link to notebook 1](https://github.com/sohankancherla/nfl-qb-fantasy-prediction/blob/main/qb_prediction.ipynb)


#### Contact and Further Information

Sohan Kancherla

Email: sohank@gmail.com

[LinkedIn](https://www.linkedin.com/in/sohan-kancherla-97821a1a1/)
