from get_dataframes import alunos, dengue, onibus
import matplotlib
import matplotlib.pyplot as plt
import matplotlib_venn as plt_venn
import os
import pandas as pd
from pathlib import Path
import sys


matplotlib.use('TkAgg')
base_path = str(Path(os.path.abspath(__file__)).resolve().parents[0])
output_path = os.path.join(
    base_path,
    'output/venn' if sys.platform.startswith("linux") else 'output\\venn'
)
if not os.path.exists(output_path):
    try:
        os.mkdir(
            os.path.join(base_path, 'output')
        )
    except:
        pass
    os.mkdir(output_path)

def get_path():
    global output_path
    return output_path

def venn1(equipe: int, show_graph: bool = False):
    circles = plt_venn.venn2(
        [
            set(alunos(equipe)["Nome"].to_list()),
            set(dengue(equipe)["Nome"].to_list()),
        ],
        set_labels=('Alunos', 'Dengue')
    )
    for char in "ABC":
        circles.get_patch_by_id(char).set_edgecolor('black')
        circles.get_patch_by_id(char).set_alpha(0.4)
        circles.get_patch_by_id(char).set_lw(2.0)
        circles.get_patch_by_id(char).set_ls('dashed')
    circles.get_patch_by_id('10').set_ls('solid')
    circles.get_patch_by_id('10').set_alpha(0.8)
    plt.title('Diferença entre Alunos e Dengue')
    plt.savefig(
        os.path.join(
            output_path, f'equipe{equipe}-relatorio1.png'
        )
    )
    if show_graph:
        plt.show()
    plt.clf()

def venn2(equipe: int, show_graph: bool = False):
    circles = plt_venn.venn2(
        [
            set(dengue(equipe)["Nome"].to_list()),
            set(onibus(equipe)["Nome"].to_list()),
        ],
        set_labels=('Dengue', 'Ônibus')
    )
    for char in "ABC":
        circles.get_patch_by_id(char).set_edgecolor('black')
        circles.get_patch_by_id(char).set_alpha(0.4)
        circles.get_patch_by_id(char).set_lw(2.0)
        circles.get_patch_by_id(char).set_ls('dashed')
    circles.get_patch_by_id('11').set_ls('solid')
    circles.get_patch_by_id('11').set_alpha(0.8)
    plt.title('Intersecção entre Dengue e Ônibus')
    plt.savefig(
        os.path.join(
            output_path, f'equipe{equipe}-relatorio2.png'
        )
    )
    if show_graph:
        plt.show()
    plt.clf()

def venn3(equipe: int, show_graph: bool = False):
    circles = plt_venn.venn2(
        [
            set(onibus(equipe)["Nome"].to_list()),
            set(dengue(equipe)["Nome"].to_list()),
        ],
        set_labels=('Ônibus', 'Dengue')
    )
    for char in "ABC":
        circles.get_patch_by_id(char).set_edgecolor('black')
        circles.get_patch_by_id(char).set_alpha(0.4)
        circles.get_patch_by_id(char).set_lw(2.0)
        circles.get_patch_by_id(char).set_ls('dashed')
    circles.get_patch_by_id('10').set_ls('solid')
    circles.get_patch_by_id('10').set_alpha(0.8)
    plt.title('Diferença entre Ônibus e Dengue')
    plt.savefig(
        os.path.join(
            output_path, f'equipe{equipe}-relatorio3.png'
        )
    )
    if show_graph:
        plt.show()
    plt.clf()

def venn4(equipe: int, show_graph: bool = False):
    circles = plt_venn.venn2(
        [
            set(alunos(equipe)["Nome"].to_list()),
            set(dengue(equipe)["Nome"].to_list()),
        ],
        set_labels=('Alunos', 'Dengue')
    )
    for char in "ABC":
        circles.get_patch_by_id(char).set_edgecolor('black')
        circles.get_patch_by_id(char).set_alpha(0.4)
        circles.get_patch_by_id(char).set_lw(2.0)
        circles.get_patch_by_id(char).set_ls('dashed')
    circles.get_patch_by_id('11').set_ls('solid')
    circles.get_patch_by_id('11').set_alpha(0.8)
    plt.title('Intersecção entre Alunos e Dengue')
    plt.savefig(
        os.path.join(
            output_path, f'equipe{equipe}-relatorio4.png'
        )
    )
    if show_graph:
        plt.show()
    plt.clf()

def venn5(equipe: int, show_graph: bool = False):
    circles = plt_venn.venn2(
        [
            set(alunos(equipe)["Nome"].to_list()),
            set(onibus(equipe)["Nome"].to_list()),
        ],
        set_labels=('Alunos', 'Ônibus')
    )
    for char in "ABC":
        circles.get_patch_by_id(char).set_edgecolor('black')
        circles.get_patch_by_id(char).set_alpha(0.4)
        circles.get_patch_by_id(char).set_lw(2.0)
        circles.get_patch_by_id(char).set_ls('dashed')
    circles.get_patch_by_id('11').set_ls('solid')
    circles.get_patch_by_id('11').set_alpha(0.8)
    plt.title('Intersecção entre Alunos e Ônibus')
    plt.savefig(
        os.path.join(
            output_path, f'equipe{equipe}-relatorio4.png'
        )
    )
    if show_graph:
        plt.show()
    plt.clf()

def venn5(equipe: int, show_graph: bool = False):
    circles = plt_venn.venn2(
        [
            set(alunos(equipe)["Nome"].to_list()),
            set(onibus(equipe)["Nome"].to_list()),
        ],
        set_labels=('Alunos', 'Ônibus')
    )
    for char in "ABC":
        circles.get_patch_by_id(char).set_edgecolor('black')
        circles.get_patch_by_id(char).set_alpha(0.4)
        circles.get_patch_by_id(char).set_lw(2.0)
        circles.get_patch_by_id(char).set_ls('dashed')
    circles.get_patch_by_id('11').set_ls('solid')
    circles.get_patch_by_id('11').set_alpha(0.8)
    plt.title('Intersecção entre Alunos e Ônibus')
    plt.savefig(
        os.path.join(
            output_path, f'equipe{equipe}-relatorio5.png'
        )
    )
    if show_graph:
        plt.show()
    plt.clf()

def venn6(equipe: int, show_graph: bool = False):
    circles = plt_venn.venn2(
        [
            set(dengue(equipe)["Nome"].to_list()),
            set(onibus(equipe)["Nome"].to_list()),
        ],
        set_labels=('Dengue', 'Ônibus')
    )
    for char in "ABC":
        circles.get_patch_by_id(char).set_edgecolor('black')
        circles.get_patch_by_id(char).set_alpha(0.4)
        circles.get_patch_by_id(char).set_lw(2.0)
        circles.get_patch_by_id(char).set_ls('dashed')
    circles.get_patch_by_id('11').set_ls('solid')
    circles.get_patch_by_id('11').set_alpha(0.8)
    plt.title('Intersecção entre Dengue e Ônibus')
    plt.savefig(
        os.path.join(
            output_path, f'equipe{equipe}-relatorio6.png'
        )
    )
    if show_graph:
        plt.show()
    plt.clf()

def venn7(equipe: int, show_graph: bool = False):
    circles = plt_venn.venn3(
        [
            set(alunos(equipe)["Nome"].to_list()),
            set(dengue(equipe)["Nome"].to_list()),
            set(onibus(equipe)["Nome"].to_list()),
        ],
        set_labels=('Alunos', 'Dengue', 'Ônibus')
    )
    for i in range(1, 8):
        patch = bin(i)[2:].zfill(3)
        circles.get_patch_by_id(patch).set_edgecolor('black')
        circles.get_patch_by_id(patch).set_alpha(0.4)
        circles.get_patch_by_id(patch).set_lw(2.0)
        circles.get_patch_by_id(patch).set_ls('dashed')
    circles.get_patch_by_id('111').set_ls('solid')
    circles.get_patch_by_id('111').set_alpha(0.8)
    plt.title('Intersecção entre Alunos, Dengue e Ônibus')
    plt.savefig(
        os.path.join(
            output_path, f'equipe{equipe}-relatorio7.png'
        )
    )
    if show_graph:
        plt.show()
    plt.clf()

def venn8(equipe: int, show_graph: bool = False):
    circles = plt_venn.venn2(
        [
            set(dengue(equipe)["Nome"].to_list()),
            set(onibus(equipe)["Nome"].to_list()),
        ],
        set_labels=('Dengue', 'Ônibus')
    )
    for char in "ABC":
        circles.get_patch_by_id(char).set_edgecolor('black')
        circles.get_patch_by_id(char).set_alpha(0.4)
        circles.get_patch_by_id(char).set_lw(2.0)
        circles.get_patch_by_id(char).set_ls('dashed')
    circles.get_patch_by_id('10').set_ls('solid')
    circles.get_patch_by_id('10').set_alpha(0.8)
    plt.title('Diferença entre Dengue e Ônibus')
    plt.savefig(
        os.path.join(
            output_path, f'equipe{equipe}-relatorio8.png'
        )
    )
    if show_graph:
        plt.show()
    plt.clf()

def venn9(equipe: int, show_graph: bool = False):
    circles = plt_venn.venn2(
        [
            set(dengue(equipe)["Nome"].to_list()),
            set(alunos(equipe)["Nome"].to_list()),
        ],
        set_labels=('Alunos', 'Dengue')
    )
    for char in "ABC":
        circles.get_patch_by_id(char).set_edgecolor('black')
        circles.get_patch_by_id(char).set_alpha(0.4)
        circles.get_patch_by_id(char).set_lw(2.0)
        circles.get_patch_by_id(char).set_ls('dashed')
    circles.get_patch_by_id('10').set_ls('solid')
    circles.get_patch_by_id('10').set_alpha(0.8)
    plt.title('Diferença entre Dengue e Alunos')
    plt.savefig(
        os.path.join(
            output_path, f'equipe{equipe}-relatorio9.png'
        )
    )
    if show_graph:
        plt.show()
    plt.clf()

def venn10(equipe: int, show_graph: bool = False):
    circles = plt_venn.venn3(
        [
            set(alunos(equipe)["Nome"].to_list()),
            set(dengue(equipe)["Nome"].to_list()),
            set(onibus(equipe)["Nome"].to_list()),
        ],
        set_labels=('Alunos', 'Dengue', 'Ônibus')
    )
    for i in range(1, 8):
        patch = bin(i)[2:].zfill(3)
        circles.get_patch_by_id(patch).set_edgecolor('black')
        circles.get_patch_by_id(patch).set_alpha(0.4)
        circles.get_patch_by_id(patch).set_lw(2.0)
        circles.get_patch_by_id(patch).set_ls('dashed')
    circles.get_patch_by_id('010').set_ls('solid')
    circles.get_patch_by_id('010').set_alpha(0.8)
    plt.title('Diferença entre Dengue, Alunos e Ônibus')
    plt.savefig(
        os.path.join(
            output_path, f'equipe{equipe}-relatorio10.png'
        )
    )
    if show_graph:
        plt.show()
    plt.clf()

if __name__ == "__main__":
    fun = locals()[f'venn{sys.argv[1]}']
    fun(int(sys.argv[2]), True)
