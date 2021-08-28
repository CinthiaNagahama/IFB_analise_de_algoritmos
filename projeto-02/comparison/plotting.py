import pandas as pd
from os import path, makedirs
import matplotlib as mpl
from matplotlib import pyplot as plt


plt.style.use("seaborn")
mpl.rcParams.update({"axes.titlesize": 18, "axes.labelsize": 16, "xtick.labelsize": 14, "ytick.labelsize": 14})

priority_queues_data = pd.read_csv(path.join(path.curdir, "priority_queues.csv"))

priority_queues_25_10_to_100 = (
    priority_queues_data[lambda df: (df["Density (%)"] == 25) & (df["Number of elements"] <= 100)]
    .set_index("Number of elements")
    .drop("Density (%)", axis=1)
)
priority_queues_50_10_to_100 = (
    priority_queues_data[lambda df: (df["Density (%)"] == 50) & (df["Number of elements"] <= 100)]
    .set_index("Number of elements")
    .drop("Density (%)", axis=1)
)
priority_queues_100_10_to_100 = (
    priority_queues_data[lambda df: (df["Density (%)"] == 100) & (df["Number of elements"] <= 100)]
    .set_index("Number of elements")
    .drop("Density (%)", axis=1)
)
priority_queues_25_100_to_1000 = (
    priority_queues_data[lambda df: (df["Density (%)"] == 25) & (df["Number of elements"] >= 100)]
    .set_index("Number of elements")
    .drop("Density (%)", axis=1)
)
priority_queues_50_100_to_1000 = (
    priority_queues_data[lambda df: (df["Density (%)"] == 50) & (df["Number of elements"] >= 100)]
    .set_index("Number of elements")
    .drop("Density (%)", axis=1)
)
priority_queues_100_100_to_1000 = (
    priority_queues_data[lambda df: (df["Density (%)"] == 100) & (df["Number of elements"] >= 100)]
    .set_index("Number of elements")
    .drop("Density (%)", axis=1)
)

makedirs(path.join(path.curdir, "graphs"), exist_ok=True)

priority_queues_25_10_to_100.plot(
    style=["-o", "-s", "-D"],
    ms=10,
    ylabel="Tempo(ms)",
    xlabel="Quantidade de elementos",
    title="Densidade: 25%",
    xticks=[(x + 1) * 1e1 for x in range(10)],
    ylim=(-5e-4, 4e-3),
).legend(loc="upper left", frameon=True, fancybox=True, fontsize=14)

ylocs, _ = plt.yticks()
plt.yticks(ylocs, [f"{(loc * 1000):.1f}" for loc in ylocs])

plt.savefig(path.join(path.curdir, "graphs", "25_10_100.png"), bbox_inches="tight")

priority_queues_50_10_to_100.plot(
    style=["-o", "-s", "-D"],
    ms=10,
    ylabel="Tempo(ms)",
    xlabel="Quantidade de elementos",
    title="Densidade: 50%",
    xticks=[(x + 1) * 1e1 for x in range(10)],
    ylim=(-5e-4, 4e-3),
).legend(loc="upper left", frameon=True, fancybox=True, fontsize=14)

ylocs, _ = plt.yticks()
plt.yticks(ylocs, [f"{(loc * 1000):.1f}" for loc in ylocs])

plt.savefig(path.join(path.curdir, "graphs", "50_10_100.png"), bbox_inches="tight")

priority_queues_100_10_to_100.plot(
    style=["-o", "-s", "-D"],
    ms=10,
    ylabel="Tempo(ms)",
    xlabel="Quantidade de elementos",
    title="Densidade: 100%",
    xticks=[(x + 1) * 1e1 for x in range(10)],
    ylim=(-5e-4, 4e-3),
).legend(loc="upper left", frameon=True, fancybox=True, fontsize=14)

ylocs, _ = plt.yticks()
plt.yticks(ylocs, [f"{(loc * 1000):.1f}" for loc in ylocs])

plt.savefig(path.join(path.curdir, "graphs", "100_10_100.png"), bbox_inches="tight")

priority_queues_25_100_to_1000.plot(
    style=["-o", "-s", "-D"],
    ms=10,
    ylabel="Tempo(ms)",
    xlabel="Quantidade de elementos",
    title="Densidade: 25%",
    xticks=[(x + 1) * 1e2 for x in range(10)],
    ylim=(-5e-2, 7e-1),
).legend(loc="upper left", frameon=True, fancybox=True, fontsize=14)

ylocs, _ = plt.yticks()
plt.yticks(ylocs, [f"{(loc * 1000):.0f}" for loc in ylocs])

plt.savefig(path.join(path.curdir, "graphs", "25_100_1000.png"), bbox_inches="tight")

priority_queues_50_100_to_1000.plot(
    style=["-o", "-s", "-D"],
    ms=10,
    ylabel="Tempo(ms)",
    xlabel="Quantidade de elementos",
    title="Densidade: 50%",
    xticks=[(x + 1) * 1e2 for x in range(10)],
    ylim=(-5e-2, 7e-1),
).legend(loc="upper left", frameon=True, fancybox=True, fontsize=14)

ylocs, _ = plt.yticks()
plt.yticks(ylocs, [f"{(loc * 1000):.0f}" for loc in ylocs])

plt.savefig(path.join(path.curdir, "graphs", "50_100_1000.png"), bbox_inches="tight")

priority_queues_100_100_to_1000.plot(
    style=["-o", "-s", "-D"],
    ms=10,
    ylabel="Tempo(ms)",
    xlabel="Quantidade de elementos",
    title="Densidade: 100%",
    xticks=[(x + 1) * 1e2 for x in range(10)],
    ylim=(-5e-2, 7e-1),
).legend(loc="upper left", frameon=True, fancybox=True, fontsize=14)

ylocs, _ = plt.yticks()
plt.yticks(ylocs, [f"{(loc * 1000):.0f}" for loc in ylocs])

plt.savefig(path.join(path.curdir, "graphs", "100_100_1000.png"), bbox_inches="tight")
