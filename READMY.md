##  AUTOMATIZAR URBAN ROUTES PARA PEDIR UN TAXI
### Descripcion del proyecto

- El proposito del proyecto es automatizar las  pruebas para comprobar la funcionalidad de Urban Routes;
- Escribir las pruebas automatizadas que cubran el proceso completo de pedir un taxi;

- El proyecto, trata de incorporar el patron de diseño  POM para hacer el codigo mas ordenado y facil de entender;

### PROCESO
- Iniciar con la instalación de python 3 y Pycharm para crear el entorno de pruebas
- Clonar repositorio Github 

#### Abrir Pycharm y comenzar con la automatizacion 
##### instalar dependencias al proyecto
- Importar dependencias selenium, webdriver, pytest;
- Definir localizadores, y metodos necesarios en la clase_UrbanRoutesPage;
- Definir las pruebas en la clase TestUrbanRoutes ;
- Consolidar Funciones, en el archivo helpers.py para colocar funciones específicas, como "retrieve_phone_code", en un solo archivo;
- Crear  archivo "urban_routes_page.py" el cual puede contener, localizadores y funciones;
- Crear archivo main.py donde realizaremos los test 

# Configuracion, Tests

#### Localizadores y sus funciones

- Para establecer nuestros localizaedores usaremos webdriver y la pagina de Urban Routes.
- Dentro de la pagina presionamos click derecho encima del campó, boton, slider, imagenes que queremos localizar, al hacer esto damos click en inspeccionar y se nos abrira la pagina dev tools con la dirección que estamos buscando;
- Una vez tenemos localizado el campó copiamos la direccion a nuestro proyecto y utilizaremos las distintas clases como By.XPATH, By.CSS_SELECTOR, By.ID, By_CLASS, etc;
- Utilizamos la funcion find_element o find_elements si son varios elementos;

#### Configuracion de localizadores y sus funciones
- Prueba 1 Configurar dirección
url = (http://https://cnt-856ed1f9-2175-4e90-a3a1-c062736f5979.containerhub.tripleten-services.com/?lng=es "Urban Routes")

        -Para configurar la dirección ocupamos rellenar los campos from y to
        -Al buscar elementos vamos utilizar el metodo find_element() 
        -Para buscar por id, utiliza By.ID 

            -     from_field = (By.ID, 'from')
            -     to_field = (By.ID, 'to')

        -Una vez encontrado el campo tenemos que rellenarlo con direcciones validas utilizaremos el metodo send_keys:

                def set_from(self, from_address):
        -self.driver.find_element(*self.from_field).send_keys(from_address)

     -Lo siguiente para completar la prueba es encontrar y dar clic al boton call a taxi se puede utilizar

		call_taxi = (By.XPATH, "//button[text()='Pedir un taxi']")

       - Una vez localizado utilizaremos el auxiliar .click()

        -    def click_ask_for_taxi(self):
        self.driver.find_element(*self.ask_for_taxi).click()

    .Prueba 2 Seleccionar la tarifa Comfort

        -Una vez rellenado los campos from y to, haber hecho click en el boton: "call a taxi", tenemos que seleccionar la tarifa "Comfort"

            comfort_button = (By.XPATH, "//div[text()='Comfort'][1]")

			llamamos a la funcion y hacemos click 

			    def click_comfort_button(self):
        self.driver.find_element(*self.comfort_button).click()

    .Prueba 3 Rellenar el numero de telefono

        -Al realizar las pruebas 1 y 2 con exito se despliga un menu donde podemos asignar un numero de telefono
        -Para rellenar el campo numero de telefono, primero localizamos el campo damos click en el y despues enviamos la información capturamos el codigo enviado mediante el helpers.py retrieve_phone_code y damos click en aceptar 
		-Para rellenar este campo utilizaremos varios localizadores y sus funciones
		
		phone_number = (By.XPATH, "//div[text()='Número de teléfono'][1]")
		number_field = (By.ID, 'phone')
		next_field = (By.XPATH, "(//button[@type='submit'])[1]")
		id_code = (By.ID, 'code')
		confirm_button = (By.XPATH, "(//button[@type='submit'])[2]")

       - sus funciones
	       def click_phone_number(self):
        self.driver.find_element(*self.phone_number).click()

    def fill_number_field(self):
        self.driver.find_element(*self.number_field).send_keys(data.phone_number)

    def click_next_field(self):
        self.driver.find_element(*self.next_field).click()

    def verification_code(self):
        self.driver.find_element(*self.id_code).send_keys(retrieve_phone_code(self.driver))

    def click_confirm_button(self):
        self.driver.find_element(*self.confirm_button).click()

     Prueba 4 Agregar una tarjeta

        -Buscamos el campo metodo de pago, damos click se abre una ventana emergente click en agregar tarjeta
         Se abre la ventana emergete agregar tarjeta, localizamos el campo numero de la tarjeta hacemos click en el
         enviamos el numero, hacemos lo mismo con el campo codigo
        -Hacemos click en una parte afuera de los campos y lo calizamos y damos click al boton add:

		    pay_method = (By.XPATH, "//div[@class='pp-text']")
			add_card = (By.XPATH, "//div[@class='pp-plus-container']")
			add_number = (By.ID, 'number')
			add_code = (By.XPATH, "(//input[@id='code'])[2]")
			other_place_tab = (By.CSS_SELECTOR, "div[class='card-wrapper']")
			confirm_card_button = (By.XPATH, "//button[text()='Agregar']")
			close_button = (By.XPATH, "(//button[@class='close-button section-close'])[3]")

    . Prueba 5 Enviar mensaje al conductor

        - Para enviar mensaje al conductor primero tenemos que localizar el campo y enviar el mensaje mediante la funcion send_keys(texto a enviar)

        -message_driver = (By.ID, 'comment'

		 Su funcion utilizamos data.message_for_driver ya que solo lo vamosa importar de la pagina data.py

-  def set_message_driver(self):
        self.driver.find_element(*self.message_driver).send_keys(data.message_for_driver)


    . Prueba 6 Pedir una manta y pañuelos

        - Primero localizamos el slider y hacemos click en el atravez de By.XPATH con etiqueta span, dentro de esta un atributo class y el tipo de class

- blankets_tissues = (By.XPATH, "(//span[@class='slider round'])[1]"

- En su funcion mandamos el .click()

-  def ask_blankets_tissues(self):
        self.driver.find_element(*self.blankets_tissues).click()

    . Prueba 7: Pedir dos helados

        - Localizamos el boton con el simbolo + realizamos una busqueda atravez de la etiqueta img mediante la clase XPATH y damos click dos veces en el boton + para añadir dos helados

- ice_cream_order = (By.XPATH, "(//div[@class='counter-plus'])[1]")

		En la pagina main.py al hacer el test mandamos el doble click

 def click_ice_cream_order(self):
        self.driver.find_element(*self.ice_cream_order).click()



    . Prueba 8: Aparece el modal para buscar un taxi click en el boton reservar

        - Para que aparesca el modal de buscar taxi tenemos que dar click al boton reservar para esto localizamos el boton y damos  click en el medianto su etiqueta span y la clase CSS_SELECTOR

- search_taxi = (By.CSS_SELECTOR, "span[class='smart-button-main']")

        - Escribimos su funcioncion pára dar el click

-  def click_search_taxi(self):
        self.driver.find_element(*self.search_taxi).click()

    . Prueba 9 Opcional: Esperar a que encuentre un taxi dar click en el boton Detalles

        - AL dar click al boton reservar aparecera una pantalla emergente con dos botones uno de cancelar y otro para ver los detalles de la reserva;
        - Mientras espero a que busque un taxi, busco la etiqueta para el boton de detalles que es un img con un atributo src y el link.

        - Primero encontramos el boton detalles esperamos 30 segundos y damos click 
 - Localizador
 
      def click_details_button(self):
        self.driver.find_element(*self.details_button).click()

#TEST

- Una vez ubicados localizadores y sus funciones procedemos a relizar las pruebas;
- Creamos un archivo main.py;
- importamos la clase UrbanRoutesPage con -> from urban_routes_pages import UrbanRoutesPage;
- Importamos el archivo data.py;
- Creamos la clase TestUrbanRoutes para las pruebas;
- Utilizamos metodos setup_class() y teardown_class() son bloques de codigo que se ejecutan antes o despues de eventos clave, como una inicializacion de test suite;

- Antes de declarar el método, debes escribir @classmethod. Este es un decorador que significa que estamos trabajando con un metodo de clase, pasa cls como argumento;

- Antes de comenzar con las pruebas debemos importar los siguientes archivos

     - import data
     - import pytest
    - import time
    - from urban_routes_page import UrbanRoutesPage
    - from selenium import webdriver
	
- clase para la pagina 

class TestUrbanRoutes:

    driver = None
    initial_header = None
    final_header = None


    @classmethod
    def setup_class(cls):

        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()# desired_capabilities=capabilities
        cls.driver.implicitly_wait(20)

#TEST

- Para realizar las pruebas creamos una funcion seguido del argumento test para indicar que es una prueba; 
- importamos el nombre de la funcion desde UrbanRoutesPage en este caso set_route(self)
-         # Abre la pagina de la aplicación, este paso es unico con el metodo setup_class(cls)
 -       # Crea una clase de objeto de página para la página de inicio de sesión
-        # Crea un objeto de página para la página principal
-        # Llama a las funciones atravez del objeto de pagina
-        # Utiliza assert para comprobar la prueba

## Ejemplo

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to







    .
