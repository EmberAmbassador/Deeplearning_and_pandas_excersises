# Oschegow Nicolaj, Bruder Luca
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ex28_data.csv",index_col=0,dtype={0:'Int64'})

# a)

seenAny = df[['age']].loc[(df['seen_any_film'] == 'Yes')]
seen4to6 = df[['age']].loc[(df['seen_ep1'] == 'No') & (df['seen_ep2'] == 'No') & (df['seen_ep3'] == 'No') & (df['seen_ep4'] == 'Yes') & (df['seen_ep5'] == 'Yes') & (df['seen_ep6'] == 'Yes')]

# Make the values in seeAny numeric so they can be ploted
seenAny = seenAny.replace('18-29', 1)
seenAny = seenAny.replace('30-44', 2)
seenAny = seenAny.replace('45-60', 3)
seenAny = seenAny.replace('> 60', 4)

# Make the values in seen4to6 numeric so they can be ploted
seen4to6 = seen4to6.replace('18-29', 1)
seen4to6 = seen4to6.replace('45-60', 2)
seen4to6 = seen4to6.replace('30-44', 3)
seen4to6 = seen4to6.replace('> 60', 4)

fig = seenAny.plot.hist(bins=7)

# Set up the x axis in a way which properly displays the values
fig.set_xticks((1.2,2.05,2.95,3.8))
fig.set_xticklabels(['18-29', '30-44', '45-60', '> 60'])

plt.show()

fig2 = seen4to6.plot.hist(bins=7)
fig2.set_xticks((1.2,2.05,2.95,3.8))
fig2.set_xticklabels(['18-29', '30-44', '45-60', '> 60'])
plt.show()

# Two things about the two groups can be noted. Firstly a lot more people have watched at least one of the Star Wars movies, than have watched
# episode 4, 5 and 6 but none of the later trilogy.
# Secondly the people who watched only the first trology but none of the later movies are on average older than the first group.

# b)

# Since the string 'Unfamiliar (N/A)' only occurs in one of the 'like_charX' columns, we can just check whether the string is found anywhere in the row.
unfamiliar = df[['seen_any_film', 'like_char1', 'like_char2', 'like_char3', 'like_char4', 'like_char5', 'like_char6', 'like_char7', 'like_char8', 'like_char9', 'like_char10', 'like_char11', 'like_char12', 'like_char13', 'like_char14']].loc[(df['seen_any_film'] == 'Yes') & (df.isin(['Unfamiliar (N/A)']).any(axis=1))]
abs = (len(unfamiliar.index) - 1)
tot = (len(seenAny.index) - 1)

print(str(tot) + " people have seen at least one of the Star Wars movies.")
print("Of those " + str(abs) + " are unfamiliar with at least one character.")
print("Thus about " + str(round((abs/tot)*100, 2)) + "% of people have watched at least one Star Wars movie but are unfamiliar with at least one character.")

# c)


watchedAll = df[['seen_ep1', 'seen_ep2', 'seen_ep3', 'seen_ep4', 'seen_ep5', 'seen_ep6', 'rank_ep1', 'rank_ep2', 'rank_ep3', 'rank_ep4', 'rank_ep5', 'rank_ep6', ]].loc[(df['seen_ep1'] == 'Yes') & (df['seen_ep2'] == 'Yes') & (df['seen_ep3'] == 'Yes') & (df['seen_ep4'] == 'Yes') & (df['seen_ep5'] == 'Yes') & (df['seen_ep6'] == 'Yes')]
print(str(len(watchedAll.index) - 1) + " people have watched all six movies.")

mean1 = watchedAll['rank_ep1'].mean()
median1 = watchedAll['rank_ep1'].median()

mean2 = watchedAll['rank_ep2'].mean()
median2 = watchedAll['rank_ep2'].median()

mean3 = watchedAll['rank_ep3'].mean()
median3 = watchedAll['rank_ep3'].median()

mean4 = watchedAll['rank_ep4'].mean()
median4 = watchedAll['rank_ep4'].median()

mean5 = watchedAll['rank_ep5'].mean()
median5 = watchedAll['rank_ep5'].median()

mean6 = watchedAll['rank_ep6'].mean()
median6 = watchedAll['rank_ep6'].median()

means = [mean1, mean2, mean3, mean4, mean5, mean6]
medians = [median1, median2, median3, median4, median5, median6]
print("The means for episode 1 to 6 are: " + str(means))
print("The medians for episode 1 to 6 are: " + str(medians))
print("It thus appears, that episode 2 is the least liked episode of the six.")

# d)

menLike = df[['like_char1', 'like_char2', 'like_char3', 'like_char4', 'like_char5', 'like_char6', 'like_char7', 'like_char8', 'like_char9', 'like_char10', 'like_char11', 'like_char12', 'like_char13', 'like_char14']].loc[(df['gender'] == 'Male')]
menLike = menLike.apply(pd.to_numeric, errors='coerce')
womenLike = df[['like_char1', 'like_char2', 'like_char3', 'like_char4', 'like_char5', 'like_char6', 'like_char7', 'like_char8', 'like_char9', 'like_char10', 'like_char11', 'like_char12', 'like_char13', 'like_char14']].loc[(df['gender'] == 'Female')]
womenLike = womenLike.apply(pd.to_numeric, errors='coerce')

print("The least liked character by men is: " + menLike.mean(axis=0).idxmin())
print("The most liked character by women is: " + womenLike.mean(axis=0).idxmax())