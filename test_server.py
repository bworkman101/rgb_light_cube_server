import requests


n = 5


"""
total frames 5, curr frame 0, curr cycle 20000, cycles 20000
total frames 5, curr frame 1, curr cycle 20000, cycles 20000
total frames 5, curr frame 2, curr cycle 20000, cycles 20000
total frames 5, curr frame 3, curr cycle 8000, cycles 8000
total frames 5, curr frame 4, curr cycle 8000, cycles 8000
"""


def single_layer_color(layer: int, red: int, green: int, blue: int,
                       red1: int, green1: int, blue1: int):
    colors_arr = [[[{'r': 0, 'g': 0, 'b': 0} for k in range(n)] for j in range(n)] for i in range(n)]
    for xi in range(5):
        for yi in range(5):
            colors_arr[layer][xi][yi] = {'r': red, 'g': green, 'b': blue}
    if layer > 0:
        for xi in range(5):
            for yi in range(5):
                colors_arr[layer-1][xi][yi] = {'r': red1, 'g': green1, 'b': blue1}
    return {'cycles': 1000, 'matrix': colors_arr}


def single_layer_drag(layer: int, red: int, green: int, blue: int):
    colors_arr = [[[{'r': 0, 'g': 0, 'b': 0} for k in range(n)] for j in range(n)] for i in range(n)]
    for xi in range(5):
        for yi in range(5):
            colors_arr[layer][xi][yi] = {'r': red, 'g': green, 'b': blue}
    if layer > 0:
        for xi in range(5):
            for yi in range(5):
                colors_arr[layer-1][xi][yi] = {'r': red*.75, 'g': green*.75, 'b': blue*.75}
    return {'cycles': 500, 'matrix': colors_arr}


def single_layer(layer: int, red: int, green: int, blue: int):
    colors_arr = [[[{'r': 0, 'g': 0, 'b': 0} for k in range(n)] for j in range(n)] for i in range(n)]
    for xi in range(5):
        for yi in range(5):
            colors_arr[layer][xi][yi] = {'r': red, 'g': green, 'b': blue}
    return {'cycles': 1000, 'matrix': colors_arr}


def layers_flow():
    return [single_layer(layer) for layer in range(5)]


r = requests.post('http://127.0.0.1:3000/cube', json={
    # "cube": {
    #     'frames': [single_layer_drag(0, 255, 0, 0),
    #                single_layer_drag(1, 255, 0, 0),
    #                single_layer_drag(2, 255, 0, 0),
    #                single_layer_drag(3, 255, 0, 0),
    #                single_layer_drag(4, 255, 0, 0)
    #                ]
    # }
    "cube": {
        'frames': [single_layer_color(0, 255, 0, 255, 0, 255, 255),
                   single_layer_color(1, 255, 0, 255, 0, 255, 255),
                   single_layer_color(2, 255, 0, 255, 0, 255, 255),
                   single_layer_color(3, 255, 0, 255, 0, 255, 255),
                   single_layer_color(4, 255, 0, 255, 0, 255, 255)
                   ]
    }
})


print(f"Status Code: {r.status_code}, Response: {r.json()}")


"""
r = requests.post('http://127.0.0.1:3000/cube', json={
    "cube": {
        'frames': layers_flow()
    }
})
"""