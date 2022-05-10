import pandas as pd
import dataframe_image as dfi
df = pd.DataFrame([('0.01697', '50'),
                   ('0.00423', '12.5'),
                   ('0.00923', '25')],
                    columns=('W_m [N]', 'Longitud [mm]' ))
df = df.rename_axis(None)
dfi.export(df,"Tabla.png")