class Movie:
    catIdMap = dict()

    def __init__(self, entry: list):
        self.id = entry[0]
        self.name = entry[1]
        self.reDate = entry[2]
        self.videoReDate = entry[3]
        self.url = entry[4]
        self.category = []
        category = [entry[i] for i in range(5, len(entry))]

        # Build category list
        for i in range(len(category)):
            if category[i] == '1':
                catName = Movie.catIdMap[i]
                self.category.append(catName)

    @staticmethod
    def initCatIdMap(idMap):
        Movie.catIdMap = idMap

    def show(self):
        output = self.name + ': ' + str.join(', ', self.category)
        print(output)


# Path input
itemPath = input()
catPath = input()

# Load file
movieFile = open(itemPath, 'r', encoding='ISO-8859-1')
catFile = open(catPath, 'r')
# movieFile = open('u.item', 'r')
# catFile = open('u.genre', 'r')

# Build category mapping
catMap = {}
catData = catFile.read()
categories = catData.split('\n')

for cat in categories:
    catEntry = cat.split('|')
    if len(catEntry) == 2:
        catMap[int(catEntry[1])] = catEntry[0]

Movie.initCatIdMap(catMap)

# Handle the movie entry, and Build the movie object list
movieDict = {}
movieData = movieFile.read()
movies = movieData.split('\n')

for movie in movies:
    movieEntry = movie.split('|')
    if len(movieEntry) != 1:
        movieObj = Movie(movieEntry)
        movieDict[movieObj.id] = movieObj

target = input()
if int(target) < len(movieDict):
    movieDict[target].show()
else:
    print('No movie found.')
