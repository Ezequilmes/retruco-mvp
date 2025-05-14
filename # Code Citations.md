# Code Citations

## License: unknown
https://github.com/martygrant/photobooth/tree/cd03332c8f8e05e569d1378848d9e25a5df728e8/GUI.py

```
(background, overlay, x, y):
    background_width = background.shape[1]
    background_height = background.shape[0]

    if x >= background_width or y >= background_height:
        return background

    h, w = overlay.shape[0], overlay.shape[1
```


## License: MIT
https://github.com/jsun/suppl/tree/3e5b44db2b74437474119a0bb75bc11984caa0bc/10.3389/fevo.2021.762173/scripts/make_dragonfly_synthesis.py

```
shape[1]
    background_height = background.shape[0]

    if x >= background_width or y >= background_height:
        return background

    h, w = overlay.shape[0], overlay.shape[1]

    if x + w > background_width:
        w = background_width - x
        overlay
```


## License: MIT
https://github.com/computervisioneng/invoice-logo-classification/tree/ca9fed98df2a2cc686016730911619c2b13552e9/create_object_detection_dataset.py

```
:
        return background

    h, w = overlay.shape[0], overlay.shape[1]

    if x + w > background_width:
        w = background_width - x
        overlay = overlay[:, :w]

    if y + h > background_height:
        h = background_height - y
        overlay =
```


## License: unknown
https://github.com/mikehankey/amscams/tree/c7b3088d57af9dd00897762303c02dbdc1ca1292/pythonv2/lib/Video_Tools_cv.py

```
..., 3:] / 255.0

    background[y:y+h, x:x+w] = (1.0 - mask) * background[y:y+h, x:x+w] + mask * overlay_image

    return background 

#
```


## License: MIT
https://github.com/cabustillo13/Truco-Argentino/tree/84700759176cdfe1c9d7a4852abf63503fa22371/crearPartida.py

```
0

    background[y:y+h, x:x+w] = (1.0 - mask) * background[y:y+h, x:x+w] + mask * overlay_image

    return background 

# Elegir aleatoriamente las 3 cartas
def elegirCarta():
```

