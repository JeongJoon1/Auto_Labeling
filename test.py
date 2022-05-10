import pixabay


API_KEY = '26709291-6e479e87405de6d5773773694'

# init pixabay API
px = pixabay.core(API_KEY)

# search for space
space = px.query("car", perPage = 200)


print(len(space))
# get len of hits len(space)
print("{} hits".format(len(space)))

for i in range(500):
    image_name = space[i].getPreviewURL().split('_')[:-1][0] + "_960_720.jpg"
    print(image_name)