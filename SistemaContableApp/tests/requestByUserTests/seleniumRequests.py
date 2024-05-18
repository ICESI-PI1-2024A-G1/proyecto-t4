import os
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from SistemaContableApp.models import Rol, User
from selenium.webdriver.common.by import By
from mixer.backend.django import mixer
from selenium import webdriver
import time
from unittest import skipUnless
from django.conf import settings


class RequestsTestCase(StaticLiveServerTestCase):
   
    def setUp(self):
        """
        Set up the test environment before running the tests.

        Initializes the web browser (Chrome) and sets up the initial data
        by calling the setup_data() method.
        """
       
        self.browser = webdriver.Chrome()  # O el navegador que prefieras
        self.browser.implicitly_wait(10)
        self.setup_data()

    def tearDown(self):
        """
        Clean up the test environment after running the tests.

        Closes the web browser.
        """
       
        self.browser.quit()

    def type_text(self, element, text):
        """
        Simulate typing text into an input field.

        Args:
            element (WebElement): The DOM element where the text will be typed.
            text (str): The text to be typed into the input field.

        Sends each character of the text to the element with a small delay to avoid
        synchronization issues.
        """
       
        for char in text:
            element.send_keys(char)
            time.sleep(0.02)  # Espera 0.2 segundos después de cada tecla

    def setup_data(self):
        """
        Set up the initial data required for the tests.

        Creates the roles in the database if they don't exist.
        """
       
        self.setup_roles()

    def setup_roles(self):
        """
        Create the roles in the database if they don't exist.

        Utilizes the mixer library to create instances of the roles.
        """
       
        # Crea los roles si no existen
        if not Rol.objects.filter(rol="Administrador").exists():
            mixer.blend(Rol, rol="Administrador")
        if not Rol.objects.filter(rol="Líder").exists():
            mixer.blend(Rol, rol="Líder")
        if not Rol.objects.filter(rol="Gestor").exists():
            mixer.blend(Rol, rol="Gestor")
        if not Rol.objects.filter(rol="Ventanilla única").exists():
            mixer.blend(Rol, rol="Ventanilla única")
        if not Rol.objects.filter(rol="Contable").exists():
            mixer.blend(Rol, rol="Contable")

    def register_user(self, name, last_name, email, rol, password):
        """
        Simulate the registration of a new user in the application.

        Args:
            name (str): The user's first name.
            last_name (str): The user's last name.
            email (str): The user's email address.
            rol (str): The user's role.
            password (str): The user's password.

        Navigates to the registration form, fills in the fields, and verifies that
        the registration was successful.
        """
       
        # Abre la página de registro
        self.browser.get(self.live_server_url + '/registro/')

        # Encuentra los campos del formulario de registro
        name_input = self.browser.find_element(By.ID, 'id_name')
        last_name_input = self.browser.find_element(By.ID, 'id_last_name')
        email_input = self.browser.find_element(By.ID, 'id_email')
        rol_select = self.browser.find_element(By.ID, 'id_rol')
        password1_input = self.browser.find_element(By.ID, 'id_password1')
        password2_input = self.browser.find_element(By.ID, 'id_password2')

        # Llena el formulario con los datos proporcionados
        self.type_text(name_input, name)
        self.type_text(last_name_input, last_name)
        self.type_text(email_input, email)
        rol_select.send_keys(rol)
        self.type_text(password1_input, password)
        self.type_text(password2_input, password)

        # Envía el formulario de registro
        submit_button = self.browser.find_element(By.CSS_SELECTOR, '.btn')
        submit_button.click()

        # Espera un poco para que la página se actualice
        time.sleep(3)

        # Verifica si se ha registrado correctamente
        self.assertIn('Tu cuenta ha sido creada exitosamente.', self.browser.page_source)
        self.assertIn('Registro exitoso.', self.browser.page_source)

    def login_as_admin(self):
        """
        Log in as an admin user in the application.

        Navigates to the login page, fills in the fields with the admin credentials,
        and verifies that the login was successful.
        """
        
        # Abre la página de inicio de sesión
        self.browser.get(self.live_server_url)

        # Encuentra los campos del formulario de inicio de sesión
        username_input = self.browser.find_element(By.NAME, 'email')
        password_input = self.browser.find_element(By.NAME, 'password')

        # Llena el formulario con los datos de inicio de sesión
        self.type_text(username_input, "administrador@example.com")
        self.type_text(password_input, "Adminpass123")

        # Envía el formulario de inicio de sesión
        submit_button = self.browser.find_element(By.CSS_SELECTOR, '.btn')
        submit_button.click()

        # Espera un poco para que la página se actualice
        time.sleep(5)

    def navigate_to_charge_account_form(self):
        """
        Navigate to the charge account request form.

        Interacts with user interface elements (buttons, menus, etc.) to navigate
        to the charge account request form.
        """
       
        menu_button = self.browser.find_element(By.CSS_SELECTOR, 'button.navbar-toggler')
        menu_button.click()

        forms_button = self.browser.find_element(By.CSS_SELECTOR, 'a.nav-link.dropdown-toggle')
        forms_button.click()

        chargeAccount_button = self.browser.find_element(By.XPATH, '//*[@id="offcanvasNavbar"]/div[2]/ul/li[3]/ul/li[1]/a')
        chargeAccount_button.click()
        
    def navigate_to_exterior_payment_form(self):
        """
        Navigate to the exterior payment request form.

        Interacts with user interface elements (buttons, menus, etc.) to navigate
        to the exterior payment request form.
        """
        
        menu_button = self.browser.find_element(By.CSS_SELECTOR, 'button.navbar-toggler')
        menu_button.click()

        forms_button = self.browser.find_element(By.CSS_SELECTOR, 'a.nav-link.dropdown-toggle')
        forms_button.click()

        chargeAccount_button = self.browser.find_element(By.XPATH, '//*[@id="offcanvasNavbar"]/div[2]/ul/li[3]/ul/li[3]/a')
        chargeAccount_button.click()
        
    def navigate_to_requisition_form(self):
        """
        Navigate to the requisition request form.

        Interacts with user interface elements (buttons, menus, etc.) to navigate
        to the requisition request form.
        """
        
        menu_button = self.browser.find_element(By.CSS_SELECTOR, 'button.navbar-toggler')
        menu_button.click()


        forms_button = self.browser.find_element(By.CSS_SELECTOR, 'a.nav-link.dropdown-toggle')

        forms_button.click()

        chargeAccount_button = self.browser.find_element(By.XPATH, '//*[@id="offcanvasNavbar"]/div[2]/ul/li[3]/ul/li[5]/a')
        actions = ActionChains(self.browser)
        actions.move_to_element(chargeAccount_button).perform()

        chargeAccount_button.click()
        
      
    def navigate_to_legalization_form(self):
        """
        Navigate to the legalization request form.

        Interacts with user interface elements (buttons, menus, etc.) to navigate
        to the legalization request form.
        """
        
        menu_button = self.browser.find_element(By.CSS_SELECTOR, 'button.navbar-toggler')
        menu_button.click()

        forms_button = self.browser.find_element(By.CSS_SELECTOR, 'a.nav-link.dropdown-toggle')
        forms_button.click()

        chargeAccount_button = self.browser.find_element(By.XPATH, '//*[@id="offcanvasNavbar"]/div[2]/ul/li[3]/ul/li[2]/a')
        chargeAccount_button.click()
  

        
        
    def navigate_to_advance_form(self):
        """
        Navigate to the advance request form.

        Interacts with user interface elements (buttons, menus, etc.) to navigate
        to the advance request form.
        """
        
        menu_button = self.browser.find_element(By.CSS_SELECTOR, 'button.navbar-toggler')
        menu_button.click()

        forms_button = self.browser.find_element(By.CSS_SELECTOR, 'a.nav-link.dropdown-toggle')
        forms_button.click()

        chargeAccount_button = self.browser.find_element(By.XPATH, '//*[@id="offcanvasNavbar"]/div[2]/ul/li[3]/ul/li[4]/a')
        chargeAccount_button.click()
        

        
        


    def test_charge_account_form(self):
        """
        Test the charge account request form.

        Simulates the registration of an admin user, logs in with that user,
        navigates to the charge account request form, fills in all required fields,
        submits the form, and verifies that a success message is displayed.
        """
        self.register_user("Administrador", "Test", "administrador@example.com", "Administrador", "Adminpass123")
        self.login_as_admin()
        self.navigate_to_charge_account_form()

        # Llenar los campos del formulario
        name_field = self.browser.find_element(By.ID, 'id_name')
        self.type_text(name_field,'John Doe')
        identification_field = self.browser.find_element(By.ID, 'id_identification')
        self.type_text(identification_field,'1234567')
        phone_field = self.browser.find_element(By.ID, 'id_phone')
        self.type_text(phone_field,'123456')
        city_field = self.browser.find_element(By.ID, 'id_city')
        self.type_text(city_field,'Cali')
        addres_field = self.browser.find_element(By.ID, 'id_addres')
        self.type_text(addres_field,'Av. Siempre Viva 1')
        date_field = self.browser.find_element(By.ID, 'id_date')
        self.type_text(date_field,'05-05-2023')
        value_letters_field = self.browser.find_element(By.ID, 'id_value_letters')
        self.type_text(value_letters_field,'Cien mil pesos')
        value_numbers_field = self.browser.find_element(By.ID, 'id_value_numbers')
        self.type_text(value_numbers_field,'100000')
        concept_field = self.browser.find_element(By.ID, 'id_concept')
        self.type_text(concept_field,'Servicios de consultoría')
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'static', 'mediaTest', 'A.docx'))
        file_field = self.browser.find_element(By.ID, 'id_supports')  # Define el campo del archivo
        file_field.send_keys(file_path)  # Envía la ruta del archivo al campo del archivo
        bank_field = self.browser.find_element(By.ID, 'id_bank')
        self.type_text(bank_field,'Bancolombia')
        type_field = self.browser.find_element(By.ID, 'id_type')
        self.type_text(type_field,'De ahorros')
        account_number_field = self.browser.find_element(By.ID, 'id_account_number')
        self.type_text(account_number_field,'1234567890')
        cex_field = self.browser.find_element(By.ID, 'id_cex')
        self.type_text(cex_field,'12345')
        
        retentions_field = self.browser.find_element(By.ID, 'id_retentions')
        retentions_field.click()

        # Encontrar el botón "Enviar"
        submit_button = self.browser.find_element(By.CSS_SELECTOR, 'button.button-enviar')

        # Desplazarse hasta el botón
        actions = ActionChains(self.browser)
        actions.move_to_element(submit_button).perform()

        # Hacer clic en el botón
        submit_button.click()

        # Esperar a que aparezca la notificación de envío exitoso
        wait = WebDriverWait(self.browser, 15)
        success_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.alert.alert-success')))

        # Verificar que la notificación de envío exitoso esté presente
        self.assertTrue(success_message.is_displayed())
        
        
    def test_exterior_payment_form(self):
        """
        Test the exterior payment request form.

        Simulates the registration of an admin user, logs in with that user,
        navigates to the exterior payment request form, fills in all required fields,
        submits the form, and verifies that a success message is displayed.
        """
        
        self.register_user("Administrador", "Test", "administrador@example.com", "Administrador", "Adminpass123")
        self.login_as_admin()
        self.navigate_to_exterior_payment_form()
        
        beneficiary_name_field = self.browser.find_element(By.ID, 'id_beneficiary_name')
        self.type_text(beneficiary_name_field,'John')
        beneficiary_last_name_field = self.browser.find_element(By.ID, 'id_beneficiary_last_name')
        self.type_text(beneficiary_last_name_field,'Doe')
        beneficiary_document_type_field = self.browser.find_element(By.ID, 'id_beneficiary_document_type')
        self.type_text(beneficiary_document_type_field,'Cédula')
        bank_name_field = self.browser.find_element(By.ID, 'id_bank_name')
        self.type_text(bank_name_field,'Banco XYZ')
        beneficiary_document_no_field = self.browser.find_element(By.ID, 'id_beneficiary_document_no')
        self.type_text(beneficiary_document_no_field,'1234567890')
        passport_number_field = self.browser.find_element(By.ID, 'id_passport_number')
        self.type_text(passport_number_field,'ABC123456')
        passport_expedition_city_field = self.browser.find_element(By.ID, 'id_passport_expedition_city')
        self.type_text(passport_expedition_city_field,'Ciudad X')
        address_field = self.browser.find_element(By.ID, 'id_address')
        self.type_text(address_field,'Calle 123, Ciudad Y')
        account_type_field = self.browser.find_element(By.ID, 'id_account_type')
        self.type_text(account_type_field,'Ahorros')
        swift_code_field = self.browser.find_element(By.ID, 'id_swift_code')
        self.type_text(swift_code_field,'ABCDEF')
        iban_aba_code_type_field = self.browser.find_element(By.ID, 'id_iban_aba_code_type')
        self.type_text(iban_aba_code_type_field,'IBAN')
        iban_aba_code_field = self.browser.find_element(By.ID, 'id_iban_aba_code')
        self.type_text(iban_aba_code_field,'GH1234567')
        account_name_field = self.browser.find_element(By.ID, 'id_account_name')
        self.type_text(account_name_field,'John Doe')
        account_number_field = self.browser.find_element(By.ID, 'id_account_number')
        self.type_text(account_number_field,'0987654321')
        bank_address_field = self.browser.find_element(By.ID, 'id_bank_address')
        self.type_text(bank_address_field,'Avenida 456, Ciudad Z')

        # Encontrar el botón "Enviar"
        submit_button = self.browser.find_element(By.CSS_SELECTOR, 'button.button-enviar')

        # Desplazarse hasta el botón
        actions = ActionChains(self.browser)
        actions.move_to_element(submit_button).perform()

        # Hacer clic en el botón
        submit_button.click()

        # Esperar a que aparezca la notificación de envío exitoso
        wait = WebDriverWait(self.browser, 5)
        success_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.alert.alert-success')))

        # Verificar que la notificación de envío exitoso esté presente
        self.assertTrue(success_message.is_displayed())
        
        
    def test_requisition_form(self):
        """
        Test the requisition request form.

        Simulates the registration of an admin user, logs in with that user,
        navigates to the requisition request form, fills in all required fields,
        submits the form, and verifies that a success message is displayed.
        """
        
        self.register_user("Administrador", "Test", "administrador@example.com", "Administrador", "Adminpass123")
        self.login_as_admin()
        self.navigate_to_requisition_form()
         # Llenar los campos del formulario
        date_field = self.browser.find_element(By.ID, 'id_date')
        self.type_text(date_field,'05-05-2023')
        beneficiary_name_field = self.browser.find_element(By.ID, 'id_beneficiaryName')
        self.type_text(beneficiary_name_field,'John Doe')
        id_number_field = self.browser.find_element(By.ID, 'id_idNumber')
        self.type_text(id_number_field,'1234567890')
        charge_field = self.browser.find_element(By.ID, 'id_charge')
        self.type_text(charge_field,'Cargo X')
        dependency_field = self.browser.find_element(By.ID, 'id_dependency')
        self.type_text(dependency_field,'Dependencia Y')
        cenco_field = self.browser.find_element(By.ID, 'id_cenco')
        self.type_text(cenco_field,'CENCO123')
        value_field = self.browser.find_element(By.ID, 'id_value')
        self.type_text(value_field,'100000')
        concept_field = self.browser.find_element(By.ID, 'id_concept')
        self.type_text(concept_field,'Reintegro colaboradores')
        description_field = self.browser.find_element(By.ID, 'id_description')
        self.type_text(description_field,'Descripción de la requisición')
        radicate_field = self.browser.find_element(By.ID, 'id_radicate')
        self.type_text(radicate_field,'RAD123456')
        payment_order_code_field = self.browser.find_element(By.ID, 'id_payment_order_code')
        self.type_text(payment_order_code_field,'OP12345')
        payment_method_field = self.browser.find_element(By.ID, 'id_paymentMethod')
        self.type_text(payment_method_field,'Nomina')
        type_account_field = self.browser.find_element(By.ID, 'id_typeAccount')
        self.type_text(type_account_field,'De ahorros')
        account_number_field = self.browser.find_element(By.ID, 'id_account_number')
        self.type_text(account_number_field,'0987654321')
        author_name_field = self.browser.find_element(By.ID, 'id_authorName')
        self.type_text(author_name_field,'Jane Smith')

        # Encontrar el botón "Enviar"
        submit_button = self.browser.find_element(By.CSS_SELECTOR, 'button.button-enviar')

        # Desplazarse hasta el botón
        actions = ActionChains(self.browser)
        actions.move_to_element(submit_button).perform()

        # Hacer clic en el botón
        submit_button.click()

        # Esperar a que aparezca la notificación de envío exitoso
        wait = WebDriverWait(self.browser, 5)
        success_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.alert.alert-success')))

        # Verificar que la notificación de envío exitoso esté presente
        self.assertTrue(success_message.is_displayed())


    def test_legalization_form(self):
        """
        Test the legalization request form.

        Simulates the registration of an admin user, logs in with that user,
        navigates to the legalization request form, fills in all required fields,
        submits the form, and verifies that a success message is displayed.
        """
        
        self.register_user("Administrador", "Test", "administrador@example.com", "Administrador", "Adminpass123")
        self.login_as_admin()

        # Navegar al formulario de legalización
        self.navigate_to_legalization_form()

        # Llenar los campos del formulario
        legalization_date_field = self.browser.find_element(By.ID, 'id_legalization_date')
        self.type_text(legalization_date_field,'05-05-2023')
        traveler_name_field = self.browser.find_element(By.ID, 'id_traveler_name')
        self.type_text(traveler_name_field,'John Doe')
        identification_field = self.browser.find_element(By.ID, 'id_identification')
        self.type_text(identification_field,'1234567890')
        cost_center_field = self.browser.find_element(By.ID, 'id_cost_center')
        self.type_text(cost_center_field,'CC123')
        dependency_field = self.browser.find_element(By.ID, 'id_dependency')
        self.type_text(dependency_field,'Departamento de Ventas')
        destiny_city_field = self.browser.find_element(By.ID, 'id_destiny_city')
        self.type_text(destiny_city_field,'Nueva York')
        travel_date_field = self.browser.find_element(By.ID, 'id_travel_date')
        self.type_text(travel_date_field,'05-05-2023')
        return_date_field = self.browser.find_element(By.ID, 'id_return_date')
        self.type_text(return_date_field,'05-05-2023')
        motive_field = self.browser.find_element(By.ID, 'id_motive')
        self.type_text(motive_field,'Asistir a una conferencia de ventas')
        motive_field = self.browser.find_element(By.ID, 'id_bank')
        self.type_text(motive_field,'Banco XYZ')
        type_account_field = self.browser.find_element(By.ID, 'id_type_account')
        self.type_text(type_account_field,'De ahorros')
        account_number_field = self.browser.find_element(By.ID, 'id_account_number')
        self.type_text(account_number_field,'1234567890')
        orderer_name_field = self.browser.find_element(By.ID, 'id_orderer_name')
        self.type_text(orderer_name_field,'Jane Smith')
        elaborator_name_field = self.browser.find_element(By.ID, 'id_elaborator_name')
        self.type_text(elaborator_name_field,'Bob Johnson')
        descount_in_one_quote_field = self.browser.find_element(By.ID, 'id_descount_in_one_quote')
        descount_in_one_quote_field.click()
        currency_type_of_advance_value_field = self.browser.find_element(By.ID, 'id_currency_type_of_advance_value')
        self.type_text(currency_type_of_advance_value_field,'DOLARES')
        advance_payment_value_field = self.browser.find_element(By.ID, 'id_advance_payment_value')
        self.type_text(advance_payment_value_field,'1000')
        
        
        category_field = self.browser.find_element(By.ID, 'id_expenses-0-category')
        self.type_text(category_field,'Transporte')
        
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'static', 'mediaTest', 'A.docx'))
        file_field = self.browser.find_element(By.ID, 'id_expenses-0-support')  # Define el campo del archivo
        file_field.send_keys(file_path)  # Envía la ruta del archivo al campo del archivo

        support_no_field = self.browser.find_element(By.ID, 'id_expenses-0-support_no')
        self.type_text(support_no_field, '12345')
        
        third_person_name_field = self.browser.find_element(By.ID, 'id_expenses-0-third_person_name')
        self.type_text(third_person_name_field,'Aerolínea XYZ')
        third_person_nit_field = self.browser.find_element(By.ID, 'id_expenses-0-third_person_nit')
        self.type_text(third_person_nit_field,'1234567890')
        concept_field = self.browser.find_element(By.ID, 'id_expenses-0-concept')
        self.type_text(concept_field,'Tiquete aéreo ida y vuelta')
        money_type_field = self.browser.find_element(By.ID, 'id_expenses-0-money_type')
        self.type_text(money_type_field,'DOLARES')
        money_value_field = self.browser.find_element(By.ID, 'id_expenses-0-money_value')
        self.type_text(money_value_field,'1000')

        # Encontrar el botón "Enviar"
        submit_button = self.browser.find_element(By.CSS_SELECTOR, 'button.button-enviar')

        # Desplazarse hasta el botón
        actions = ActionChains(self.browser)
        actions.move_to_element(submit_button).perform()

        # Hacer clic en el botón
        submit_button.click()

        # Esperar a que aparezca la notificación de envío exitoso
        wait = WebDriverWait(self.browser, 15)
        success_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.alert.alert-success')))

        # Verificar que la notificación de envío exitoso esté presente
        self.assertTrue(success_message.is_displayed())

    def test_advance_payment_form(self):
        """
        Test the advance payment request form.

        Simulates the registration of an admin user, logs in with that user,
        navigates to the advance payment request form, fills in all required fields,
        submits the form, and verifies that a success message is displayed.
        """
        
        self.register_user("Administrador", "Test", "administrador@example.com", "Administrador", "Adminpass123")
        self.login_as_admin()

        # Navegar al formulario de solicitud de anticipo
        self.navigate_to_advance_form()

        # Llenar los campos del formulario
        radicate_field = self.browser.find_element(By.ID, 'id_radicate')
        self.type_text(radicate_field,'RAD123456')
        payment_order_code_field = self.browser.find_element(By.ID, 'id_payment_order_code')
        self.type_text(payment_order_code_field,'OP12345')
        request_date_field = self.browser.find_element(By.ID, 'id_request_date')
        self.type_text(request_date_field,'05-05-2023')
        traveler_name_field = self.browser.find_element(By.ID, 'id_traveler_name')
        self.type_text(traveler_name_field,'John Doe')
        traveler_id_field = self.browser.find_element(By.ID, 'id_traveler_id')
        self.type_text(traveler_id_field,'1234567890')
        cost_center_field = self.browser.find_element(By.ID, 'id_cost_center')
        self.type_text(cost_center_field,'CC123')
        dependency_field = self.browser.find_element(By.ID, 'id_dependency')
        self.type_text(dependency_field,'Departamento de Ventas')
        destiny_city_field = self.browser.find_element(By.ID, 'id_destiny_city')
        self.type_text(destiny_city_field,'Nueva York')
        travel_date_field = self.browser.find_element(By.ID, 'id_travel_date')
        self.type_text(travel_date_field,'05-05-2023')
        return_date_field = self.browser.find_element(By.ID, 'id_return_date')
        self.type_text(return_date_field,'05-05-2023')
        motive_field = self.browser.find_element(By.ID, 'id_motive')
        self.type_text(motive_field,'Asistir a una conferencia de ventas')
        currency_type_of_advance_value_field = self.browser.find_element(By.ID, 'id_currency_type_of_advance_value')
        self.type_text(currency_type_of_advance_value_field,'DOLARES')
        last_day_in_icesi_field = self.browser.find_element(By.ID, 'id_last_day_in_icesi')
        self.type_text(last_day_in_icesi_field,'2023-05-31')
        orderer_name_field = self.browser.find_element(By.ID, 'id_orderer_name')
        self.type_text(orderer_name_field,'Jane Smith')
        elaborator_name_field = self.browser.find_element(By.ID, 'id_elaborator_name')
        self.type_text(elaborator_name_field,'Bob Johnson')
        descount_in_one_quote_field = self.browser.find_element(By.ID, 'id_descount_in_one_quote')
        descount_in_one_quote_field.click()
        
        category_field = self.browser.find_element(By.ID, 'id_expenses-0-category')
        self.type_text(category_field,'Alojamiento')
        money_value_field = self.browser.find_element(By.ID, 'id_expenses-0-money_value')
        self.type_text(money_value_field,'500')

        # Encontrar el botón "Enviar"
        submit_button = self.browser.find_element(By.CSS_SELECTOR, 'button.button-enviar')

        # Desplazarse hasta el botón
        actions = ActionChains(self.browser)
        actions.move_to_element(submit_button).perform()

        # Hacer clic en el botón
        submit_button.click()

        # Esperar a que aparezca la notificación de envío exitoso
        wait = WebDriverWait(self.browser, 15)
        success_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.alert.alert-success')))

        # Verificar que la notificación de envío exitoso esté presente
        self.assertTrue(success_message.is_displayed())