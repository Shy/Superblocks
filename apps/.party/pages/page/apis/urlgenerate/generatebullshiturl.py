import random
randomBullshit = f'https://api.netlify.com/api/v1/badges/3e50af34-b732-408f-9fd8-deecd7d00f81/deploy-status/?cachebust={random.randint(0,1000)}'
print(randomBullshit)
return randomBullshit

