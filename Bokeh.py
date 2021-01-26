# Importando módulo Bokeh
import bokeh
from bokeh.io import show, output_notebook
from bokeh.plotting import figure, output_file
from bokeh.models import ColumnDataSource
from bokeh.transform import factor_cmap
from bokeh.palettes import Spectral6


# Carregando o Bokeh
print('Bokeh carregado com sucesso', output_notebook())

# arquivo gerado pela visualização 
output_file('Grafico2-interativo.html')

p = figure()
print(type(p))


p.line([1,2,3,4,5], [6,7,2,4,5], line_width=2)
show(p)