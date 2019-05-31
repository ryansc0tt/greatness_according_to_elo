#### Udacity Data Analyst Nanodegree | Communicate Data Findings - Project Submission
Ryan Middleton, May 2019

# Greatness According to Elo
As a lifelong fan of the San Antonio Spurs (objectively* the greatest sports franchise of all time), I have always had an interest in how great teams are measured and perceived. But "greatness" in sport is difficult to quantify, and impossible to prove.

A great metric for the National Basketball Association (NBA) is [FiveThirtyEight](https://fivethirtyeight.com/) 's Elo ratings. This project endeavors to get to know Elo and how it might help us understand historical greatness in the NBA. 

<sub>*subjectively, if we're being honest :)</sub>

## Dataset
In 2015, FiveThirtyEight introduced their NBA Elo rating. Based on a rating system for chess players originally developed by Arpad Elo (and since adapted for many competitive games), this Elo is a game-by-game calculation derived from (1) scoring margin and (2) where a game is played. More information on the calculation can be found [here](https://fivethirtyeight.com/features/how-we-calculate-nba-elo-ratings/).

FiveThirtyEight regularly updates their NBA Elo ratings data on [Github](https://github.com/fivethirtyeight/data/tree/master/nba-carmelo). This project utilizes an instance of the dataset downloaded in May 2019 ([nba_elo.csv](nba_elo.csv)). The data also includes more recent "[CARMELO](https://projects.fivethirtyeight.com/carmelo/)" ratings, which considers player depth charts and performance. However, since CARMELO is very experimental and only applicable to recent seasons, it is not used here.

This project also utilizes historical NBA data compiled from [Basketball Reference](https://www.basketball-reference.com/).

Documentation on data exploration steps taken for this project can be found in the Jupyter notebook [exploration.ipynb](exploration.ipynb).

## Summary of Findings

- Based on FiveThirtyEight's Elo categorical descriptions, we can derive ranges for interpreting "playoff" and "title contender" teams in each season.

- Per-team Elo distribution shows a split between high- and low-performing seasons for "great" teams, with top teams peaking in "title contender" range.

- Elo fluctuates a lot in early years - specifically before the NBA/ABA league merger in 1976. Considering the "modern era" makes for a more consistent analysis.

- Results from grouping team Elo ratings by season supports the idea that we could use this metric as a proxy for historical "greatness,"  specifically seasons categorized as "title contending."

- Comparing aggregate Elo metrics to championship results provides some evidence that previous "greatness" may have some impact on a team's success. Season average and cumulative ratings are useful. However, it is not necessarily predictive in a given season. 

- Compared to the top seed (i.e. top record) in a given season, Elo does predict championships a bit better. This supports the idea that Elo is predictive - not just descriptive - of playoff success. It also supports the idea that historically great teams tend to set themselves apart in the playoffs.

- There is a divergence between Elo delta during a win streak and length of the streak - possibly due to the "grinding" nature of some win streaks vs. "hot" streaks of others.

## Key Insights for Presentation

Overall, Elo allows for a more granular look at team performance over time than just win/loss record, and certainly more than gut feeling or reputation. It is also useful as a more analogous comparison of regular season vs. playoff performance.

A summary of insights presented in [slide_deck.ipynb](slide_deck.ipynb) / [slide_deck.slides.html](slide_deck.slides.html):
1. A look at the per-season historical ratings of the Boston Celtics serves to demonstrate Elo's usefulness.
2. Charting all title contenders in the modern era allows for historical comparison between teams, and highlights a few interesting outliers.
3. Assessing the change in Elo rating over various win streaks shows that the greatest streaks are not necessarily the longest.
