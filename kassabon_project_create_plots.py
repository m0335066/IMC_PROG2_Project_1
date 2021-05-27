import matplotlib.pyplot as plt

#######################################################################PLOTS
def create_plot(cat_count,cat_labels):
    fig, ax = plt.subplots()
    ax.pie(cat_count,labels=cat_labels,autopct='%.1f%%')
    plt.legend()
    plt.show()