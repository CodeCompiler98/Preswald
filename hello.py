from preswald import connect, get_df, table, text, slider, query, plotly
import plotly.express as px

#load the dataset (using preswald.toml shortcut)
connect() 
df = get_df("movie")

#query the data to get s subsection of useful info
sql = "SELECT primaryTitle, rank, averageRating, numVotes FROM movie WHERE genres LIKE '%Action%' ORDER BY averageRating DESC"
filter_df = query(sql, "movie")

#allow the user to view and interact with the table
text("## Trends of Action Movies")
rows = slider("Rows to Display", min_val=5, max_val=100, default=50)
threshold = slider("Average Rating", min_val=0, max_val = 10, default=0)
table(filter_df[filter_df["averageRating"] > threshold], limit=rows, title="Action Movies")

#show a plot graph to the user (limit to sample size of 300)
sqlTwo = "SELECT primaryTitle, rank, averageRating, numVotes FROM movie WHERE genres LIKE '%Action%' LIMIT 300"
graph_points = query(sqlTwo, "movie")

text("## Scatter Chart: Rank vs Average Rating")
fig = px.scatter(graph_points , x="rank", y="averageRating", color="numVotes", hover_data=["primaryTitle"],  title='Rank to Average Rating (high rank is better)',
                 labels={'rank': 'Rank', 'averageRating': 'Average Rating'})
plotly(fig)

#show a bar chart to user
text("## Bar Chart: Rank vs Average Rating")

fig_bar = px.line(graph_points, x="rank", y="averageRating", hover_data=["primaryTitle"], labels={"rank": "Rank", "averageRating": "Average Rating"}
)
plotly(fig_bar)