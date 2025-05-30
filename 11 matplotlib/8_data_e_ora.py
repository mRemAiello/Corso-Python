from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
from datetime import datetime, timedelta

plt.style.use("ggplot")


x = [
    datetime(2024, 1, 10),
    datetime(2024, 1, 15),
    datetime(2024, 1, 20),
    datetime(2024, 1, 25),
    datetime(2024, 1, 30)
]

y = [5, 5.8, 4, 8, 9]
date_formattate = mpl_dates.DateFormatter("%d %b")
print(date_formattate)

plt.plot_date(x, y, linestyle="solid")
plt.gcf().autofmt_xdate()
plt.gca().xaxis.set_major_formatter(date_formattate)


plt.title("Valutazione sul 2024")
plt.show()