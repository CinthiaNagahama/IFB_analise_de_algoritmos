import pandas as pd
from os import path, makedirs
import matplotlib as mpl
from matplotlib import pyplot as plt


plt.style.use("seaborn")
mpl.rcParams.update({"axes.titlesize": 18, "axes.labelsize": 16, "xtick.labelsize": 14, "ytick.labelsize": 14})

algorithms_data = pd.read_csv(path.join(path.curdir, "algorithms.csv"))

algorithms_25_10_to_100 = (
    algorithms_data[lambda df: (df["Density (%)"] == 25) & (df["Number of elements"] <= 100)]
    .set_index("Number of elements")
    .drop("Density (%)", axis=1)
)
algorithms_50_10_to_100 = (
    algorithms_data[lambda df: (df["Density (%)"] == 50) & (df["Number of elements"] <= 100)]
    .set_index("Number of elements")
    .drop("Density (%)", axis=1)
)
algorithms_100_10_to_100 = (
    algorithms_data[lambda df: (df["Density (%)"] == 100) & (df["Number of elements"] <= 100)]
    .set_index("Number of elements")
    .drop("Density (%)", axis=1)
)
algorithms_25_100_to_1000 = (
    algorithms_data[lambda df: (df["Density (%)"] == 25) & (df["Number of elements"] >= 100)]
    .set_index("Number of elements")
    .drop("Density (%)", axis=1)
)
algorithms_50_100_to_1000 = (
    algorithms_data[lambda df: (df["Density (%)"] == 50) & (df["Number of elements"] >= 100)]
    .set_index("Number of elements")
    .drop("Density (%)", axis=1)
)
algorithms_100_100_to_1000 = (
    algorithms_data[lambda df: (df["Density (%)"] == 100) & (df["Number of elements"] >= 100)]
    .set_index("Number of elements")
    .drop("Density (%)", axis=1)
)

makedirs(path.join(path.curdir, "graphs", "algorithms"), exist_ok=True)

algorithms_25_10_to_100.plot(
    style=["-o", "-s"],
    ms=10,
    ylabel="Tempo(ms)",
    xlabel="Quantidade de elementos",
    title="Densidade: 25%",
    xticks=[(x + 1) * 1e1 for x in range(10)],
    ylim=(-5e-4, 8e-3),
    linewidth=2,
).legend(loc="upper left", frameon=True, fancybox=True, fontsize=14)

ylocs, _ = plt.yticks()
plt.yticks(ylocs, [f"{(loc * 1000):.1f}" for loc in ylocs])

plt.savefig(path.join(path.curdir, "graphs", "algorithms", "25_10_100.png"), bbox_inches="tight")

algorithms_50_10_to_100.plot(
    style=["-o", "-s"],
    ms=10,
    ylabel="Tempo(ms)",
    xlabel="Quantidade de elementos",
    title="Densidade: 50%",
    xticks=[(x + 1) * 1e1 for x in range(10)],
    ylim=(-5e-4, 8e-3),
    linewidth=2,
).legend(loc="upper left", frameon=True, fancybox=True, fontsize=14)

ylocs, _ = plt.yticks()
plt.yticks(ylocs, [f"{(loc * 1000):.1f}" for loc in ylocs])

plt.savefig(path.join(path.curdir, "graphs", "algorithms", "50_10_100.png"), bbox_inches="tight")

algorithms_100_10_to_100.plot(
    style=["-o", "-s"],
    ms=10,
    ylabel="Tempo(ms)",
    xlabel="Quantidade de elementos",
    title="Densidade: 100%",
    xticks=[(x + 1) * 1e1 for x in range(10)],
    ylim=(-5e-4, 8e-3),
    linewidth=2,
).legend(loc="upper left", frameon=True, fancybox=True, fontsize=14)

ylocs, _ = plt.yticks()
plt.yticks(ylocs, [f"{(loc * 1000):.1f}" for loc in ylocs])

plt.savefig(path.join(path.curdir, "graphs", "algorithms", "100_10_100.png"), bbox_inches="tight")

algorithms_25_100_to_1000.plot(
    style=["-o", "-s"],
    ms=10,
    ylabel="Tempo(ms)",
    xlabel="Quantidade de elementos",
    title="Densidade: 25%",
    xticks=[(x + 1) * 1e2 for x in range(10)],
    ylim=(-5e-2, 14e-1),
    linewidth=2,
).legend(loc="upper left", frameon=True, fancybox=True, fontsize=14)

ylocs, _ = plt.yticks()
plt.yticks(ylocs, [f"{(loc * 1000):.0f}" for loc in ylocs])

plt.savefig(path.join(path.curdir, "graphs", "algorithms", "25_100_1000.png"), bbox_inches="tight")

algorithms_50_100_to_1000.plot(
    style=["-o", "-s"],
    ms=10,
    ylabel="Tempo(ms)",
    xlabel="Quantidade de elementos",
    title="Densidade: 50%",
    xticks=[(x + 1) * 1e2 for x in range(10)],
    ylim=(-5e-2, 14e-1),
    linewidth=2,
).legend(loc="upper left", frameon=True, fancybox=True, fontsize=14)

ylocs, _ = plt.yticks()
plt.yticks(ylocs, [f"{(loc * 1000):.0f}" for loc in ylocs])

plt.savefig(path.join(path.curdir, "graphs", "algorithms", "50_100_1000.png"), bbox_inches="tight")

algorithms_100_100_to_1000.plot(
    style=["-o", "-s"],
    ms=10,
    ylabel="Tempo(ms)",
    xlabel="Quantidade de elementos",
    title="Densidade: 100%",
    xticks=[(x + 1) * 1e2 for x in range(10)],
    ylim=(-5e-2, 14e-1),
    linewidth=2,
).legend(loc="upper left", frameon=True, fancybox=True, fontsize=14)

ylocs, _ = plt.yticks()
plt.yticks(ylocs, [f"{(loc * 1000):.0f}" for loc in ylocs])

plt.savefig(path.join(path.curdir, "graphs", "algorithms", "100_100_1000.png"), bbox_inches="tight")
# plt.show()
