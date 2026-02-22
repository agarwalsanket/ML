import matplotlib.pyplot as plt

"""
Binary Classification plotting
"""
def plt_feature_against_class(X, y):
    figure, ax = plt.subplots(nrows=1, ncols=1)


    ax.scatter(X, y, marker='x', c='r', label="Actual Value")
    ax.set_title("Visualizing features against class labels")
    ax.set_ylabel('Fraud Transaction')
    ax.set_xlabel('Feature')
    ax.legend()
