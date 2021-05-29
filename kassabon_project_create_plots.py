import matplotlib.pyplot as plt

#######################################################################PLOTS
def create_plot_item_pie(cat_count,cat_labels):
    fig, ax = plt.subplots()
    ax.pie(cat_count,labels=cat_labels,autopct='%.1f%%',shadow = True)
    plt.title('item distribution per category')
    plt.legend()
    plt.show()


def create_plot_price_pie(cat_sum,cat_labels):
    fig, ax = plt.subplots()
    ax.pie(cat_sum,labels=cat_labels,autopct='%.1f%%')
    plt.title('price distribution per category')
    plt.legend()
    plt.show()