# -*- coding: utf-8 -*-
"""
MÓDULO DE MAPAS INTERACTIVOS
Visualización profesional de rutas sobre mapas reales de Neiva usando Folium
"""

import folium
from folium import plugins
import webbrowser
import os
from datetime import datetime


class MapaInteractivoSETP:
    """Crea mapas interactivos profesionales con las rutas del SETP"""
    
    def __init__(self, base_conocimiento):
        """
        Inicializa el visualizador de mapas
        
        Args:
            base_conocimiento: Instancia de BaseConocimiento con estaciones y conexiones
        """
        self.base = base_conocimiento
        # Centro de Neiva
        self.centro_neiva = [2.9273, -75.2819]
        
        # Opciones de tiles gratuitos (sin API key)
        self.tiles_options = {
            'osm': {
                'tiles': 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
                'attr': '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
                'name': 'OpenStreetMap'
            },
            'carto_light': {
                'tiles': 'https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png',
                'attr': '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
                'name': 'CartoDB Light'
            },
            'carto_dark': {
                'tiles': 'https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png',
                'attr': '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
                'name': 'CartoDB Dark'
            },
            'esri_world': {
                'tiles': 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}',
                'attr': 'Tiles &copy; Esri &mdash; Source: Esri, DeLorme, NAVTEQ, USGS, Intermap, iPC, NRCAN, Esri Japan, METI, Esri China (Hong Kong), Esri (Thailand), TomTom, 2012',
                'name': 'Esri World Street'
            },
            'esri_satellite': {
                'tiles': 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                'attr': 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community',
                'name': 'Esri Satellite'
            }
        }
        
        # Tile predeterminado (cambiar aquí para probar diferentes estilos)
        self.tile_default = 'carto_light'  # Opciones: 'osm', 'carto_light', 'carto_dark', 'esri_world', 'esri_satellite'
        
        # Paleta de colores profesional
        self.colores = {
            'ruta': '#2E86AB',           # Azul profesional para la ruta
            'origen': '#06A77D',          # Verde para origen
            'destino': '#D00000',         # Rojo para destino
            'parada': '#F77F00',          # Naranja para paradas intermedias
            'red': '#95A3A4',             # Gris para conexiones de la red
            'estacion_inactiva': '#BDC3C7'  # Gris claro para estaciones no usadas
        }
    
    def crear_mapa_ruta(self, origen, destino, ruta, costo, tiempo_estimado, abrir=True):
        """
        Crea un mapa interactivo mostrando la ruta óptima encontrada
        
        Args:
            origen (str): Estación de origen
            destino (str): Estación de destino
            ruta (list): Lista de estaciones en la ruta
            costo (float): Distancia total en km
            tiempo_estimado (int): Tiempo estimado en minutos
            abrir (bool): Si True, abre el mapa automáticamente en el navegador
            
        Returns:
            str: Ruta del archivo HTML generado
        """
        # Obtener configuración de tiles
        tile_config = self.tiles_options[self.tile_default]
        
        # Crear mapa centrado en Neiva
        mapa = folium.Map(
            location=self.centro_neiva,
            zoom_start=13,
            tiles=tile_config['tiles'],
            attr=tile_config['attr'],
            control_scale=True
        )
        
        # Título personalizado
        titulo = f"""
        <div style="position: fixed; 
                    top: 10px; 
                    left: 50px; 
                    width: 400px; 
                    height: auto; 
                    background-color: white; 
                    border: 2px solid #2E86AB; 
                    border-radius: 10px;
                    padding: 15px;
                    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                    z-index: 9999;
                    font-family: Arial, sans-serif;">
            <h3 style="margin: 0 0 10px 0; color: #2E86AB; font-size: 18px;">
                🚍 SETP Neiva - Ruta Óptima
            </h3>
            <p style="margin: 5px 0; font-size: 14px;">
                <strong>Origen:</strong> <span style="color: #06A77D;">{origen}</span>
            </p>
            <p style="margin: 5px 0; font-size: 14px;">
                <strong>Destino:</strong> <span style="color: #D00000;">{destino}</span>
            </p>
            <p style="margin: 5px 0; font-size: 14px;">
                <strong>Distancia:</strong> {costo:.2f} km
            </p>
            <p style="margin: 5px 0; font-size: 14px;">
                <strong>Tiempo estimado:</strong> {tiempo_estimado} minutos
            </p>
            <p style="margin: 5px 0; font-size: 14px;">
                <strong>Paradas:</strong> {len(ruta) - 1}
            </p>
        </div>
        """
        mapa.get_root().html.add_child(folium.Element(titulo))
        
        # Dibujar la ruta principal con línea gruesa
        coordenadas_ruta = []
        for estacion in ruta:
            lat, lon = self.base.obtener_coordenadas(estacion)
            if lat and lon:
                coordenadas_ruta.append([lat, lon])
        
        # Línea de la ruta con efecto de animación
        folium.PolyLine(
            coordenadas_ruta,
            color=self.colores['ruta'],
            weight=6,
            opacity=0.8,
            tooltip="Ruta óptima seleccionada"
        ).add_to(mapa)
        
        # Añadir marcadores para cada estación en la ruta
        for i, estacion in enumerate(ruta):
            lat, lon = self.base.obtener_coordenadas(estacion)
            if not lat or not lon:
                continue
            
            # Determinar el tipo de estación
            if i == 0:  # Origen
                color = 'green'
                icon = 'play'
                popup_text = f"<b>ORIGEN</b><br>{estacion}"
            elif i == len(ruta) - 1:  # Destino
                color = 'red'
                icon = 'stop'
                popup_text = f"<b>DESTINO</b><br>{estacion}"
            else:  # Paradas intermedias
                color = 'orange'
                icon = 'info-sign'
                popup_text = f"<b>Parada {i}</b><br>{estacion}"
            
            # Crear marcador
            folium.Marker(
                location=[lat, lon],
                popup=folium.Popup(popup_text, max_width=200),
                tooltip=estacion,
                icon=folium.Icon(color=color, icon=icon, prefix='glyphicon')
            ).add_to(mapa)
            
            # Añadir número de orden con CircleMarker
            if 0 < i < len(ruta) - 1:
                folium.CircleMarker(
                    location=[lat, lon],
                    radius=15,
                    popup=f"Parada {i}",
                    color='white',
                    fill=True,
                    fillColor=self.colores['parada'],
                    fillOpacity=0.9,
                    weight=2
                ).add_to(mapa)
        
        # Mostrar red completa en gris claro (conexiones no usadas)
        estaciones_ruta = set(ruta)
        for origen_conn, destino_conn, distancia, tiempo in self.base.conexiones:
            # Solo mostrar conexiones que NO son parte de la ruta
            conexion_en_ruta = False
            for i in range(len(ruta) - 1):
                if (ruta[i] == origen_conn and ruta[i+1] == destino_conn) or \
                   (ruta[i] == destino_conn and ruta[i+1] == origen_conn):
                    conexion_en_ruta = True
                    break
            
            if not conexion_en_ruta:
                lat1, lon1 = self.base.obtener_coordenadas(origen_conn)
                lat2, lon2 = self.base.obtener_coordenadas(destino_conn)
                if lat1 and lon1 and lat2 and lon2:
                    folium.PolyLine(
                        [[lat1, lon1], [lat2, lon2]],
                        color=self.colores['red'],
                        weight=2,
                        opacity=0.3,
                        dash_array='5, 5',
                        tooltip=f"{origen_conn} ↔ {destino_conn} ({distancia} km)"
                    ).add_to(mapa)
        
        # Añadir mini mapa para navegación
        minimap = plugins.MiniMap(toggle_display=True)
        mapa.add_child(minimap)
        
        # Añadir botón de pantalla completa
        plugins.Fullscreen(
            position='topright',
            title='Pantalla completa',
            title_cancel='Salir de pantalla completa',
            force_separate_button=True
        ).add_to(mapa)
        
        # Añadir medidor de distancias
        plugins.MeasureControl(
            position='topleft',
            primary_length_unit='kilometers',
            secondary_length_unit='meters',
            primary_area_unit='sqkilometers',
            secondary_area_unit='sqmeters'
        ).add_to(mapa)
        
        # Guardar el mapa
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        # Incluir el estilo en el nombre del archivo para identificarlo
        estilo_actual = self.tile_default
        nombre_archivo = f"mapa_ruta_{origen.replace(' ', '_')}_{destino.replace(' ', '_')}_{estilo_actual}_{timestamp}.html"
        ruta_archivo = os.path.join('outputs', nombre_archivo)
        
        # Crear directorio si no existe
        os.makedirs('outputs', exist_ok=True)
        
        mapa.save(ruta_archivo)
        print(f"\n✅ Mapa guardado en: {ruta_archivo}")
        
        # Abrir automáticamente en el navegador
        if abrir:
            ruta_completa = os.path.abspath(ruta_archivo)
            webbrowser.open('file://' + ruta_completa)
            print(f"🌐 Abriendo mapa en el navegador...")
        
        return ruta_archivo
    
    def crear_mapa_red_completa(self, abrir=True):
        """
        Crea un mapa mostrando toda la red de transporte SETP
        
        Args:
            abrir (bool): Si True, abre el mapa automáticamente en el navegador
            
        Returns:
            str: Ruta del archivo HTML generado
        """
        # Obtener configuración de tiles
        tile_config = self.tiles_options[self.tile_default]
        
        # Crear mapa centrado en Neiva
        mapa = folium.Map(
            location=self.centro_neiva,
            zoom_start=13,
            tiles=tile_config['tiles'],
            attr=tile_config['attr'],
            control_scale=True
        )
        
        # Título
        titulo = """
        <div style="position: fixed; 
                    top: 10px; 
                    left: 50px; 
                    width: 350px; 
                    background-color: white; 
                    border: 2px solid #2E86AB; 
                    border-radius: 10px;
                    padding: 15px;
                    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                    z-index: 9999;
                    font-family: Arial, sans-serif;">
            <h3 style="margin: 0 0 10px 0; color: #2E86AB;">
                🗺️ Red Completa SETP Neiva
            </h3>
            <p style="margin: 5px 0; font-size: 13px;">
                Visualización de todas las estaciones y conexiones
            </p>
        </div>
        """
        mapa.get_root().html.add_child(folium.Element(titulo))
        
        # Dibujar todas las conexiones
        for origen, destino, distancia, tiempo in self.base.conexiones:
            lat1, lon1 = self.base.obtener_coordenadas(origen)
            lat2, lon2 = self.base.obtener_coordenadas(destino)
            if lat1 and lon1 and lat2 and lon2:
                folium.PolyLine(
                    [[lat1, lon1], [lat2, lon2]],
                    color=self.colores['ruta'],
                    weight=4,
                    opacity=0.7,
                    tooltip=f"{origen} ↔ {destino}<br>Distancia: {distancia} km<br>Tiempo: {tiempo} min"
                ).add_to(mapa)
        
        # Añadir marcadores para todas las estaciones
        for estacion in self.base.obtener_estaciones():
            lat, lon = self.base.obtener_coordenadas(estacion)
            if lat and lon:
                folium.Marker(
                    location=[lat, lon],
                    popup=folium.Popup(f"<b>{estacion}</b>", max_width=200),
                    tooltip=estacion,
                    icon=folium.Icon(color='blue', icon='home', prefix='glyphicon')
                ).add_to(mapa)
        
        # Añadir controles
        plugins.MiniMap(toggle_display=True).add_to(mapa)
        plugins.Fullscreen(position='topright', force_separate_button=True).add_to(mapa)
        
        # Guardar
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        # Incluir el estilo en el nombre del archivo
        estilo_actual = self.tile_default
        nombre_archivo = f"mapa_red_completa_{estilo_actual}_{timestamp}.html"
        ruta_archivo = os.path.join('outputs', nombre_archivo)
        os.makedirs('outputs', exist_ok=True)
        
        mapa.save(ruta_archivo)
        print(f"\n✅ Mapa de red completa guardado en: {ruta_archivo}")
        
        if abrir:
            ruta_completa = os.path.abspath(ruta_archivo)
            webbrowser.open('file://' + ruta_completa)
            print(f"🌐 Abriendo mapa en el navegador...")
        
        return ruta_archivo
