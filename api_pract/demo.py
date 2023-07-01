import requests

url = "https://dog.ceo/api/breeds/list/all"
random = "https://dog.ceo/api/breeds/image/random"

response = requests.get(url)
# response = requests.get(random)

# if response.status_code == 200:
#     data = response.json()
#     # Process the data here
#     print(data["message"])
# else:
#     print("Error: ", response.status_code)




if response.status_code == 200:
    data = response.json()
    # Process the data here
    dogs = data
    for dogsreader in dogs['message']:
        if dogsreader.startswith('a'):
            print(dogsreader)
else:
    print("Error: ", response.status_code)



# dogs = {'message':
#  {'affenpinscher': [],
#   'african': [],
#   'airedale': [],
#   'akita': [], 'appenzeller': [], 'australian': ['shepherd'], 'basenji': [], 'beagle': [], 'bluetick': [], 'borzoi': [], 'bouvier': [], 'boxer': [], 'brabancon': [], 'briard': [], 'buhund': ['norwegian'], 'bulldog': ['boston', 'english', 'french'], 'bullterrier': ['staffordshire'], 'cattledog': ['australian'], 'chihuahua': [], 'chow': [], 'clumber': [], 'cockapoo': [], 'collie': ['border'], 'coonhound': [], 'corgi': ['cardigan'], 'cotondetulear': [], 'dachshund': [], 'dalmatian': [], 'dane': ['great'], 'deerhound': ['scottish'], 'dhole': [], 'dingo': [], 'doberman': [], 'elkhound': ['norwegian'], 'entlebucher': [], 'eskimo': [], 'finnish': ['lapphund'], 'frise': ['bichon'], 'germanshepherd': [], 'greyhound': ['italian'], 'groenendael': [], 'havanese': [], 'hound': ['afghan', 'basset', 'blood', 'english', 'ibizan', 'plott', 'walker'], 'husky': [], 'keeshond': [], 'kelpie': [], 'komondor': [], 'kuvasz': [], 'labradoodle': [], 'labrador': [], 'leonberg': [], 'lhasa': [], 'malamute': [], 'malinois': [], 'maltese': [], 'mastiff': ['bull', 'english', 'tibetan'], 'mexicanhairless': [], 'mix': [], 'mountain': ['bernese', 'swiss'], 'newfoundland': [], 'otterhound': [], 'ovcharka': ['caucasian'], 'papillon': [], 'pekinese': [], 'pembroke': [], 'pinscher': ['miniature'], 'pitbull': [], 'pointer': ['german', 'germanlonghair'], 'pomeranian': [], 'poodle': ['medium', 'miniature', 'standard', 'toy'], 'pug': [], 'puggle': [], 'pyrenees': [], 'redbone': [], 'retriever': ['chesapeake', 'curly', 'flatcoated', 'golden'], 'ridgeback': ['rhodesian'], 'rottweiler': [], 'saluki': [], 'samoyed': [], 'schipperke': [], 'schnauzer': ['giant', 'miniature'], 'segugio': ['italian'], 'setter': ['english', 'gordon', 'irish'], 'sharpei': [], 'sheepdog': ['english', 'shetland'], 'shiba': [], 'shihtzu': [], 'spaniel': ['blenheim', 'brittany', 'cocker', 'irish', 'japanese', 'sussex', 'welsh'], 'spitz': ['japanese'], 'springer': ['english'], 'stbernard': [], 'terrier': ['american', 'australian', 'bedlington', 'border', 'cairn', 'dandie', 'fox', 'irish', 'kerryblue', 'lakeland', 'norfolk', 'norwich', 'patterdale', 'russell', 'scottish', 'sealyham', 'silky', 'tibetan', 'toy', 'welsh', 'westhighland', 'wheaten', 'yorkshire'], 'tervuren': [], 'vizsla': [], 'waterdog': ['spanish'], 'weimaraner': [], 'whippet': [], 'wolfhound': ['irish']
#   }, 'status': 'success'}
