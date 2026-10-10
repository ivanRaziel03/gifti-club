# Perrijo & Gatijo — tema Shopify OS 2.0

Tema inicial en español para productos y regalos personalizados de mascotas. Incluye plantillas JSON OS 2.0, cabecera y pie editables, banner, cuadrícula de productos, producto personalizable, carrito lateral AJAX y páginas de colección, búsqueda, carrito, páginas y 404.

## Instalar

1. Comprime el contenido de esta carpeta en ZIP, o usa `perrijo-gatijo-shopify-theme.zip` que acompaña esta entrega.
2. En Shopify Admin: **Tienda online → Temas → Añadir tema → Subir archivo ZIP**.
3. Previsualiza el tema sin publicarlo y ajústalo desde el editor visual.
4. Selecciona una colección en **Colección destacada**, agrega imágenes, y revisa las opciones de pagos/envío de tu tienda.

## Personalización

En el editor del tema puedes editar colores, umbral de envío gratis, anuncio, contenido del hero, imagen principal y campos para producto (especie, nombre, foto y grabado). Los datos escritos se añaden a las propiedades del artículo. El umbral se expresa en pesos mexicanos.

## Antes de usar en producción

- Configura en Shopify los métodos reales de pago (incluidos OXXO/SPEI, si están disponibles en tu país/cuenta), envíos, impuestos, políticas, dominio e información legal. El tema no activa pasarelas de pago.
- La disponibilidad de campos para subir foto como propiedad depende del flujo de carga de archivos admitido por Shopify en el canal/checkout de la tienda; prueba con un pedido de prueba. Si no aparece correctamente, usa una app de personalización de producto compatible y conecta sus campos.
- Es un punto de partida funcional, no una garantía de Lighthouse 95+, cumplimiento legal ni compatibilidad verificada con todas las apps. Prueba en una copia/tema de desarrollo con Shopify Theme Check y en móvil antes de publicar.
- El bloque de país/idioma solo aparece si hay más de una opción activa en la configuración Markets/locales.

## Empaquetar otra vez

Desde el directorio padre del tema ejecuta:

```bash
python3 build_theme.py
```

El script crea el ZIP con `assets/`, `config/`, `layout/`, `locales/`, `sections/`, `snippets/` y `templates/` en la raíz del archivo, como espera Shopify.
