question = input('What\'s the weather like today?')
season = input(( "(sunny/rainy/cold/): "))

if season == 'sunny':
    print('Wear a tshirt and sunglasses.')
elif season == 'rainy':
    print('Don\'t forget your umbrella and raincoat.')
elif season == 'cold':
    print('Make sure to wear a warm jacket and gloves.') 
else:
    print('Sorry, I don\'t have recommendations for either choice.')
   