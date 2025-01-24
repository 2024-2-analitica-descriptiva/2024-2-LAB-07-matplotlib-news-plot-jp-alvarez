"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
    import pandas as pd
    import os

    df = pd.read_csv('files/input/news.csv', encoding='utf-8', index_col=0, sep=',')

    import matplotlib.pyplot as plt # type: ignore

    # Crear figura
    plt.Figure()

    # Diccionario de colores para cada medio
    media_colors = {
        'Television': 'dimgray',
        'Newspaper': 'grey',
        'Internet': 'tab:blue',
        'Radio': 'lightgrey'
    }

    # Diccionario de orden de capas para cada medio
    media_zorder = {
        'Television': 1,
        'Newspaper': 1,
        'Internet': 2,
        'Radio': 1
    }

    # Diccionario de grosores de línea para cada medio
    media_linewidths = {
        'Television': 2,
        'Newspaper': 2,
        'Internet': 3,
        'Radio': 2
    }

    # Graficar cada columna del DataFrame
    for media in df.columns:
        plt.plot(df[media],
                color=media_colors[media],
                label=media,
                zorder=media_zorder[media],
                linewidth=media_linewidths[media]
                )

    # Configurar título y ejes del gráfico
    plt.title('How people get their news', fontsize=16)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)
   
    # Añadir puntos y etiquetas para el primer y último año
    for media in df.columns:
        first_year = df.index[0]
        plt.scatter(
            x=first_year,
            y=df[media][first_year],
            color=media_colors[media],
            zorder=media_zorder[media]
        )

        plt.text(
            first_year - 0.2,
            df[media][first_year],
            media + " " + str(df[media][first_year]) + "%",
            ha='right',
            va='center',
            color=media_colors[media]
        )

        last_year = df.index[-1]
        plt.scatter(
            x=last_year,
            y=df[media][last_year],
            color=media_colors[media],
            zorder=media_zorder[media]
        )

        plt.text(
            last_year + 0.2,
            df[media][last_year],
            str(df[media][last_year]) + "%",
            ha='left',
            va='center',
            color=media_colors[media]
    )
            
    # Crear directorio si no existe
    output_dir = "files/plots"
    os.makedirs(output_dir, exist_ok=True)

    # Guardar la figura
    plt.savefig(os.path.join(output_dir, "news.png"))
    plt.close()