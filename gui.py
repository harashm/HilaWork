import pandas as pd
from max_bipartite_matrching import wrapper

AVAILABLE_DATES = [5, 6, 71, 72, 8, 9, 10]

NOTE = {'Hila': [5, 71, 72, 8, 9, 10],
        'Yana': [6, 71, 72, 8, 9, 10],
        'Anat': [6, 9, 10],
        'Lilach': [5, 71, 72, 9, 10],
        'Moran': [5, 6, 71, 72, 8, 9, 10],
        'Meital': [5, 6, 71, 72, 8, 9],
        'Micha': []
        }

##
df = pd.DataFrame(data=[[key, value] for key, value in NOTE.items()], columns=['Name', 'Dates'])

# import qgrid
# qgrid_widget = qgrid.show_grid(df, show_toolbar=True)
# qgrid_widget
# NOTE = qgrid_widget.get_changed_df()

NOTE = {row['Name']: row['Dates'] for (index, row) in df.iterrows()}

wrapper(AVAILABLE_DATES, NOTE)
