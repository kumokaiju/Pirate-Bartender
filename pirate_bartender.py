questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

#creating a new dictionary for responses
preferences={}

def custom_order():
    for n in questions:
        response=input(questions[n])
        if response==1:
            response=True
        else:
            response=False
        preferences[n]=response
        print(n)
            
if __name__=='__main__':
    custom_order()
    
def construct(preferences):
    drink_order=[]
    for n in preferences:
        if preferences[n]==True:
            drink_order.append(ingredients[n])
    print(drink_order)
    
if __name__=='__main__':
    construct(preferences)
