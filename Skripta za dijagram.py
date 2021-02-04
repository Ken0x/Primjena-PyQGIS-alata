lyr = iface.activeLayer()

diagram = QgsPieDiagram()

ds = QgsDiagramSettings()

dColors = {'PGDS': QColor("#3727fa"),
           'PLDS': QColor("#6810ff")}
ds.categoryColors = dColors.values()
ds.categoryAttributes = dColors.keys()
ds.categoryLabels = ds.categoryAttributes

dr = QgsLinearlyInterpolatedDiagramRenderer()
dr.setUpperValue(100)  # Here you should set the maximum value of both attributes
dr.setUpperSize(QSizeF(10, 10))
dr.setClassificationField('PGDS')
dr.setDiagram(diagram)
dr.setDiagramSettings(ds)

# Set diagram layer settings:
lyr.setDiagramRenderer(dr)
dls = QgsDiagramLayerSettings()

lyr.setDiagramLayerSettings(dls)
lyr.triggerRepaint()