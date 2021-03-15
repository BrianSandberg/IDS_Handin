import requests
import npyscreen

class App(npyscreen.NPSAppManaged):

    def onStart(self):
        self.addForm('MAIN', FirstForm, name="main")


class FirstForm(npyscreen.ActionFormMinimal):

    def create(self):

      self.add(npyscreen.TitleText, w_id="drink_name", name="Name of drink")
      self.add(npyscreen.TitleText, w_id="ingredient_name", name="Search by ingredient")
      self.add(npyscreen.ButtonPress, name="Search!", when_pressed_function=self.btn_press)
      self.add(npyscreen.ButtonPress, name="Feeling lucky?",when_pressed_function=self.random_drink)
      
      

    def random_drink(self):
      r_temp = requests.get(url=("https://www.thecocktaildb.com/api/json/v1/1/random.php"))
      self.response = r_temp.json()
      
      self.add(npyscreen.TitleText, w_id = "randomDrink", name = self.response["drinks"][0]["strDrink"])
      if self.response["drinks"][0]["strIngredient1"] !=None:
        self.add(npyscreen.TitleText, w_id = "Ingredient1", name = self.response["drinks"][0]["strIngredient1"])
      if self.response["drinks"][0]["strIngredient2"] !=None:
        self.add(npyscreen.TitleText, w_id = "Ingredient2", name = self.response["drinks"][0]["strIngredient2"])
      if self.response["drinks"][0]["strIngredient3"] !=None:
        self.add(npyscreen.TitleText, w_id = "Ingredient3", name = self.response["drinks"][0]["strIngredient3"])
      if self.response["drinks"][0]["strIngredient4"] !=None:
        self.add(npyscreen.TitleText, w_id = "Ingredient4", name = self.response["drinks"][0]["strIngredient4"])
      if self.response["drinks"][0]["strIngredient5"] !=None:
        self.add(npyscreen.TitleText, w_id = "Ingredient5", name = self.response["drinks"][0]["strIngredient5"])
      if self.response["drinks"][0]["strIngredient6"] !=None:
        self.add(npyscreen.TitleText, w_id = "Ingredient6", name = self.response["drinks"][0]["strIngredient6"])
      if self.response["drinks"][0]["strIngredient7"] !=None:
        self.add(npyscreen.TitleText, w_id = "Ingredient7", name = self.response["drinks"][0]["strIngredient7"])
      if self.response["drinks"][0]["strIngredient8"] !=None:
        self.add(npyscreen.TitleText, w_id = "Ingredient8", name = self.response["drinks"][0]["strIngredient8"])
      if self.response["drinks"][0]["strIngredient9"] !=None:
        self.add(npyscreen.TitleText, w_id = "Ingredient9", name = self.response["drinks"][0]["strIngredient9"])
      if self.response["drinks"][0]["strIngredient10"] !=None:
        self.add(npyscreen.TitleText, w_id = "Ingredient10", name = self.response["drinks"][0]["strIngredient10"])
      if self.response["drinks"][0]["strIngredient11"] !=None:
        self.add(npyscreen.TitleText, w_id = "Ingredient11", name = self.response["drinks"][0]["strIngredient11"])
      if self.response["drinks"][0]["strIngredient12"] !=None:
        self.add(npyscreen.TitleText, w_id = "Ingredient12", name = self.response["drinks"][0]["strIngredient12"])
      if self.response["drinks"][0]["strIngredient13"] !=None:
        self.add(npyscreen.TitleText, w_id = "Ingredient13", name = self.response["drinks"][0]["strIngredient13"])
      if self.response["drinks"][0]["strIngredient14"] !=None:
        self.add(npyscreen.TitleText, w_id = "Ingredient14", name = self.response["drinks"][0]["strIngredient14"])
      if self.response["drinks"][0]["strIngredient15"] !=None:
        self.add(npyscreen.TitleText, w_id = "Ingredient15", name = self.response["drinks"][0]["strIngredient15"])
      self.add(npyscreen.TitleText, w_id = "drink_instructions", name = self.response["drinks"][0]["strInstructions"])
      

    def btn_press(self):
      
      if self.get_widget("drink_name").value == "":
        r_temp = requests.get(
  url=("https://www.thecocktaildb.com/api/json/v1/1/filter.php?i=" + f'{self.get_widget("ingredient_name").value}'))
        self.response = r_temp.json()
        self.add(npyscreen.TitleText, w_id = "drinks_containing", name = "Drinks containing " + f'{self.get_widget("ingredient_name").value}')
        self.add(npyscreen.TitleText, w_id = "drink", name = self.response["drinks"][0]["strDrink"])
        self.add(npyscreen.TitleText, w_id = "drink1", name = self.response["drinks"][1]["strDrink"])
        self.add(npyscreen.TitleText, w_id = "drink2", name = self.response["drinks"][2]["strDrink"])
        self.add(npyscreen.TitleText, w_id = "drink3", name = self.response["drinks"][3]["strDrink"])
        self.add(npyscreen.TitleText, w_id = "drink4", name = self.response["drinks"][4]["strDrink"])


      elif self.get_widget("ingredient_name").value == "":
        r_temp = requests.get(url="https://www.thecocktaildb.com/api/json/v1/1/search.php?s=" + f'{self.get_widget("drink_name").value}')
        self.response = r_temp.json()

        self.add(npyscreen.TitleText, w_id = "Name", name = self.response["drinks"][0]["strDrink"])
        self.add(npyscreen.TitleText, w_id="ingredients", name="Ingredients")
        

        if self.response["drinks"][0]["strIngredient1"] !=None:
          self.add(npyscreen.TitleText, w_id = "Ingr_1", name = self.response["drinks"][0]["strIngredient1"])
        if self.response["drinks"][0]["strIngredient2"] !=None:
          self.add(npyscreen.TitleText, w_id = "Ingr_2", name = self.response["drinks"][0]["strIngredient2"])
        if self.response["drinks"][0]["strIngredient3"] !=None:
          self.add(npyscreen.TitleText, w_id = "Ingr_3", name = self.response["drinks"][0]["strIngredient3"])
        if self.response["drinks"][0]["strIngredient4"] !=None:
          self.add(npyscreen.TitleText, w_id = "Ingr_4", name = self.response["drinks"][0]["strIngredient4"])
        if self.response["drinks"][0]["strIngredient5"] !=None:
          self.add(npyscreen.TitleText, w_id = "Ingr_5", name = self.response["drinks"][0]["strIngredient5"])
        if self.response["drinks"][0]["strIngredient6"] !=None:
          self.add(npyscreen.TitleText, w_id = "Ingr_6", name = self.response["drinks"][0]["strIngredient6"])
        if self.response["drinks"][0]["strIngredient7"] !=None:
          self.add(npyscreen.TitleText, w_id = "Ingr_7", name = self.response["drinks"][0]["strIngredient7"])
        if self.response["drinks"][0]["strIngredient8"] !=None:
          self.add(npyscreen.TitleText, w_id = "Ingr_8", name = self.response["drinks"][0]["strIngredient8"])
        if self.response["drinks"][0]["strIngredient9"] !=None:
          self.add(npyscreen.TitleText, w_id = "Ingr_9", name = self.response["drinks"][0]["strIngredient9"])
        if self.response["drinks"][0]["strIngredient10"] !=None:
          self.add(npyscreen.TitleText, w_id = "Ingr_10", name = self.response["drinks"][0]["strIngredient10"])
        if self.response["drinks"][0]["strIngredient11"] !=None:
          self.add(npyscreen.TitleText, w_id = "Ingr_11", name = self.response["drinks"][0]["strIngredient11"])
        if self.response["drinks"][0]["strIngredient12"] !=None:
          self.add(npyscreen.TitleText, w_id = "Ingr_12", name = self.response["drinks"][0]["strIngredient12"])
        if self.response["drinks"][0]["strIngredient13"] !=None:
          self.add(npyscreen.TitleText, w_id = "Ingr_13", name = self.response["drinks"][0]["strIngredient13"])
        if self.response["drinks"][0]["strIngredient14"] !=None:
          self.add(npyscreen.TitleText, w_id = "Ingr_14", name = self.response["drinks"][0]["strIngredient14"])
        if self.response["drinks"][0]["strIngredient15"] !=None:
          self.add(npyscreen.TitleText, w_id = "Ingr_15", name = self.response["drinks"][0]["strIngredient15"])
        self.add(npyscreen.TitleText, w_id= "drink_instructions", name = self.response["drinks"][0]["strInstructions"])
      


    def on_ok(self):
      self.parentApp.switchForm(None)


app = App()
app.run()