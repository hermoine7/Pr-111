import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd

df=pd.read_csv("data.csv")
data=df["reading_time"].tolist()

mean = statistics.mean(data)
sd = statistics.stdev(data)
print("mean: ",mean)
print("Standard deviation: ",sd)

dataset = []
meanList = []
for i in range(0,100):
    for i in range(0,30):
        ran= random.randint(0,len(data)-1)
        v=data[ran]
        dataset.append(v)
    mean2=statistics.mean(dataset)
    meanList.append(mean)
mean3=statistics.mean(meanList)
sd2=statistics.stdev(meanList)

fig = ff.create_distplot([meanList], ["reading time"], show_hist=False)

sd1Start=mean3-sd2
sd1End=mean3+sd2
sd2Start=mean3-(2*sd2)
sd2End=mean3+(2*sd2)
sd3Start=mean3-(3*sd2)
sd3End=mean3+(3*sd2)

fig.add_trace(go.Scatter(x=[mean3, mean3], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[sd1Start, sd1Start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[sd1End, sd1End], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[sd2Start, sd2Start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[sd2End, sd2End], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.show()

zs=(mean3-mean)/sd
print("z-score: ",zs)