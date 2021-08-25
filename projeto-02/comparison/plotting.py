import pandas as pd
from os import path, makedirs
import matplotlib as mpl
from matplotlib import pyplot as plt

plt.style.use("seaborn")
mpl.rcParams.update({"axes.titlesize": 18, "axes.labelsize": 16, "xtick.labelsize": 14, "ytick.labelsize": 14})

priority_queues_data = pd.read_csv(path.join(path.curdir, "priority_queues.csv"))

priority_queues_insertion = (
    priority_queues_data[lambda df: (df["Measure"] == "insertion") & (df["Additional text"] == "Yes")]
    .drop(["Measure", "Additional text"], axis=1)
    .set_index("Number of elements")
)
priority_queues_deletion = (
    priority_queues_data[lambda df: (df["Measure"] == "deletion") & (df["Additional text"] == "Yes")]
    .drop(["Measure", "Additional text"], axis=1)
    .set_index("Number of elements")
)
priority_queues_insertion_and_deletion = (
    priority_queues_data[lambda df: (df["Measure"] == "insertion and deletion") & (df["Additional text"] == "Yes")]
    .drop(["Measure", "Additional text"], axis=1)
    .set_index("Number of elements")
)

makedirs(path.join(path.curdir, "graphs"), exist_ok=True)

priority_queues_insertion.plot(
    figsize=(6, 4.5),
    style=["-o", "-s", "-D"],
    ms=10,
    loglog=True,
    title="Inserção",
    ylabel="Tempo(s)",
    xlabel="Quantidade de elementos",
    xticks=[1e1, 1e2, 1e3, 1e4],
).legend(loc="upper left", frameon=True, fancybox=True, fontsize=14)
plt.savefig(path.join(path.curdir, "graphs", "insertion.png"), bbox_inches="tight", dpi=75)

priority_queues_deletion.plot(
    figsize=(6, 4.5),
    style=["-o", "-s", "-D"],
    ms=10,
    loglog=True,
    title="Deleção",
    ylabel="Tempo(s)",
    xlabel="Quantidade de elementos",
    xticks=[1e1, 1e2, 1e3, 1e4],
).legend(loc="upper left", frameon=True, fancybox=True, fontsize=14)
plt.savefig(path.join(path.curdir, "graphs", "deletion.png"), bbox_inches="tight", dpi=75)

priority_queues_insertion_and_deletion.plot(
    figsize=(6, 4.5),
    style=["-o", "-s", "-D"],
    ms=10,
    loglog=True,
    title="Inserção e deleção",
    ylabel="Tempo(s)",
    xlabel="Quantidade de elementos",
    xticks=[1e1, 1e2, 1e3, 1e4],
).legend(loc="upper left", frameon=True, fancybox=True, fontsize=14)
plt.savefig(path.join(path.curdir, "graphs", "insertion_deletion.png"), bbox_inches="tight", dpi=75)
