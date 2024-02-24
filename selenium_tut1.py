from selenium import webdriver
from selenium.webdriver.common.by import By


f = open("results.txt", "w")
urlsFile = open("urls.txt", "r")
urls = urlsFile.readlines()
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(60)

for url in urls:
    driver.get(url)
    #cogemos los elementos en este caso el enlace a la seccion de busquedas (lo pulsamos) y los elementos de los juegos que listan
    all_trends = driver.find_element(By.LINK_TEXT, 'Tendencias').click()
    print('\n---------- INSTANT GAMING ----------\n')
    print('------- Juegos en Tendencias -------' + '\n\n')
    trend_games = driver.find_elements(By.XPATH, '//div[@class="search listing-items"]/div/div[@class="information"]')
    #para cada elemento cogemos su nombre y precio y lo guardamos en un archivo txt
    f.write('\n---------- INSTANT GAMING ----------\n')
    f.write('------- Juegos en Tendencias -------' + '\n\n')
    for game in trend_games:
        name = game.find_element(By.XPATH, './/div/div/span[@class="title"]').text
        print(name)
        f.write(name + '\n')
        try:
            price = game.find_element(By.XPATH, './/div[@class="price"]').text
            print(price + '\n')
            f.write(price + '\n')
        except:
            print('Juego para reservar\n')
            f.write('Juego para reservar\n')
            continue
              
driver.quit()        
    

    
