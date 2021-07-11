from os import path, makedirs
from math import log10
import pandas as pd
import matplotlib as mpl
from matplotlib import pyplot as plt

mpl.style.use("seaborn")
mpl.rcParams.update({"axes.titlesize": 18, "axes.labelsize": 16, "xtick.labelsize": 14, "ytick.labelsize": 14})

bubble = pd.read_csv(path.join(path.curdir, "data", "bubble_sort.csv"))
merge = pd.read_csv(path.join(path.curdir, "data", "merge_sort.csv"))
heap = pd.read_csv(path.join(path.curdir, "data", "heap_sort.csv"))

make_title = {"best": "Melhor caso", "random": "Caso médio", "worst": "Pior caso"}

makedirs(path.join(path.curdir, "graphing", "time"), exist_ok=True)
for sort_case in ["best", "random", "worst"]:
    bubble_time = (
        bubble.loc[bubble["case"] == (sort_case + "_case"), ["entries", "time(s)"]]
        .set_index("entries")
        .rename(columns={"time(s)": "Bubble sort"})
    )
    merge_time = (
        merge.loc[merge["case"] == (sort_case + "_case"), ["entries", "time(s)"]]
        .set_index("entries")
        .rename(columns={"time(s)": "Merge sort"})
    )
    heap_time = (
        heap.loc[heap["case"] == (sort_case + "_case"), ["entries", "time(s)"]]
        .set_index("entries")
        .rename(columns={"time(s)": "Heap sort"})
    )
    sorting_time = pd.concat([bubble_time, merge_time, heap_time], axis=1)

    sorting_time.plot(
        style="o-",
        ms=10,
        logx=True,
        logy=True,
        x_compat=True,
        xlabel="Quantidade de elementos",
        ylabel="Tempo(s)",
        title=make_title[sort_case],
    ).legend(loc="lower center", ncol=3, frameon=True, framealpha=0.5, fancybox=True, fontsize=14)
    plt.savefig(path.join(path.curdir, "graphing", "time", f"{sort_case}_case.png"), bbox_inches="tight", dpi=75)

makedirs(path.join(path.curdir, "graphing", "memory"), exist_ok=True)
for sort_case in ["best", "random", "worst"]:
    bubble_memory = (
        bubble.loc[bubble["case"] == (sort_case + "_case"), ["entries", "memory(kb)"]]
        .set_index("entries")
        .rename(columns={"memory(kb)": "Bubble sort"})
    )
    merge_memory = (
        merge.loc[merge["case"] == (sort_case + "_case"), ["entries", "memory(kb)"]]
        .set_index("entries")
        .rename(columns={"memory(kb)": "Merge sort"})
    )
    heap_memory = (
        heap.loc[heap["case"] == (sort_case + "_case"), ["entries", "memory(kb)"]]
        .set_index("entries")
        .rename(columns={"memory(kb)": "Heap sort"})
    )
    sorting_memory = pd.concat([bubble_memory, merge_memory, heap_memory], axis=1)

    err_sorting_memory = pd.DataFrame(index=sorting_memory.index, columns=sorting_memory.columns)
    if sort_case == "best":
        err_sorting_memory.loc[10000, "Bubble sort"] = int(
            bubble.loc[(bubble["case"] != "best_case") & (bubble["entries"] == 10000), ["memory(kb)"]].mean()
        )
        err_sorting_memory.loc[100000, "Bubble sort"] = int(
            bubble.loc[(bubble["case"] != "best_case") & (bubble["entries"] == 100000), ["memory(kb)"]].mean()
        )
        err_sorting_memory = err_sorting_memory.mask(err_sorting_memory.isna(), 0)

    sorting_memory.plot.bar(
        rot=0,
        logy=True,
        xlabel="Quantidade de elementos",
        ylabel="Memória(kb)",
        title=make_title[sort_case],
        yerr=err_sorting_memory if not err_sorting_memory.empty else None,
    ).legend(loc="upper left", frameon=True, framealpha=0.5, fancybox=True, fontsize=14)

    locs, labels = plt.xticks()
    plt.xticks(locs, [f"$10^{log10(int(label.get_text())):.0f}$" for label in labels])

    plt.savefig(path.join(path.curdir, "graphing", "memory", f"{sort_case}_case.png"), bbox_inches="tight", dpi=75)
