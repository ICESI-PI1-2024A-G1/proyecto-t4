from django.contrib.auth import authenticate
from django.test import TestCase
from django.test import RequestFactory
from django.contrib.auth.models import User
from SistemaContableApp.models import Following, State, Rol
from django.test import TestCase, Client
from SistemaContableApp.views import summaryOneStopShopView
from django.contrib.auth import get_user_model
from django.http import QueryDict


class SearchTestCase(TestCase):

    def setUp(self):
        """
        Set up the necessary objects and data for the test case.

        This method is called before each individual test method is run.
        It creates a user with the role 'Ventanilla única' and saves it to the database.
        It also initializes a RequestFactory object for creating mock requests.

        Args:
            self: The current instance of the test case.

        Returns:
            None
        """
        User = get_user_model()
        self.rol_ventanilla_unica = Rol.objects.create(rol='Ventanilla única')
        self.user_Ventanilla_unica = User.objects.create_user(
            username='Ventanilla',
            email='Ventanillaúnica@gmail.com',
            name='Ventanilla única',
            password='password'
        )
        self.user_Ventanilla_unica.rol = self.rol_ventanilla_unica
        self.user_Ventanilla_unica.save()

        self.factory = RequestFactory()

    def crear_instancias(self):
        """
        Crea instancias de algunos objetos en la base de datos para realizar pruebas.

        En especial las instancias de los siguientes objetos:
        - EstadoSolicitud
        - TipoSolicitud
        - FechaCreacion
        - FechaCierre

        Returns:
            None
        """
        state1 = State.objects.create(state='Aprobado', color='azul')
        Following.objects.create(
            creationDate='2024-05-12',
            type='requesicion',
            concept='pago',
            moneyType='USD',
            amount=30,
            cenco=30,
            cexNumber=15,
            observations='ninguna',
            currentState=state1,
            closeDate='2025-05-12'
        )

        state2 = State.objects.create(state='Pendiente', color='verde')
        Following.objects.create(
            creationDate='2024-06-12',
            type='adelanto',
            concept='dinero',
            moneyType='COP',
            amount=30,
            cenco=30,
            cexNumber=15,
            observations='ninguna',
            currentState=state2,
            closeDate='2025-06-12'
        )

        state3 = State.objects.create(state='Rechazado', color='rojo')
        Following.objects.create(
            creationDate='2024-07-12',
            type='anticipo',
            concept='billetes',
            moneyType='COP',
            amount=30,
            cenco=30,
            cexNumber=15,
            observations='ninguna',
            currentState=state3,
            closeDate='2025-07-12'
        )

    def test_filtrarSolicitud_estado(self):
        """
        Prueba unitaria para verificar el filtrado por estado de las solicitudes.

        Se crean instancias de solicitudes y se realiza una solicitud GET con el parámetro 'estado',
        en la cual se supone que el estado es "Aprobado". Luego se realiza la solicitud al controlador
        'ventanilla_unica'. Se verifica que la respuesta tenga un código de estado 200 y que el contenido de la
        respuesta contenga la primera solicitud puesto que su estado es "Aprobado".

        Args:
            None

        Returns:
            None
        """
        self.crear_instancias()
        request = self.factory.get('Ventanilla única resumida', {'estado': 'Aprobado'})
        request.user = self.user_Ventanilla_unica

        response = summaryOneStopShopView(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, b'Aprobado')

    def test_busqueda_solicitud(self):
        """
        Prueba la búsqueda de una solicitud.

        Esta prueba verifica que la función `search_ventanilla` responda correctamente a una solicitud GET con un parámetro
        de búsqueda y que devuelva un código de estado 200 junto con el contenido de la solicitud buscada.

        Args:
            None

        Returns:
            None
        """
        self.crear_instancias()
        request = self.factory.get('/')
        request.user = self.user_Ventanilla_unica

        request.method = 'GET'
        request.GET = QueryDict('q=requesicion')  # Crear un nuevo QueryDict mutable

        response = summaryOneStopShopView(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, b'requesicion')

    def test_busqueda(self):
        """
        Prueba la búsqueda de una solicitud.

        Esta prueba verifica que la función `search_ventanilla` responda correctamente a una solicitud GET con cualquier parámetro
        de búsqueda y que devuelva un código de estado 200 junto con el contenido de la solicitud buscada.

        Args:
            None

        Returns:
            None
        """
        self.crear_instancias()
        request = self.factory.get('/')
        request.user = self.user_Ventanilla_unica

        request.method = 'GET'
        request.GET = QueryDict('q=a')  # Crear un nuevo QueryDict mutable

        response = summaryOneStopShopView(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, b'adelanto') 
        self.assertContains(response, b'anticipo') 

    def test_filtrar_solicitud_por_tipo(self):
        """
        Prueba unitaria para verificar el filtrado por tipo de las solicitudes.

        Se crean instancias de solicitudes y se realiza una solicitud GET con el parámetro 'tipo',
        en la cual se supone que el tipo es "adelanto". Luego se realiza la solicitud al controlador
        'ventanilla_unica'. Se verifica que la respuesta tenga un código de estado 200 y que el contenido de la
        respuesta contenga la solicitud cuyo tipo es "adelanto".

        Args:
            None

        Returns:
            None
        """
        self.crear_instancias()
        request = self.factory.get('Ventanilla única resumida', {'tipo': 'adelanto'})
        request.user = self.user_Ventanilla_unica

        response = summaryOneStopShopView(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, b'adelanto')  
    
    def test_filtrar_solicitud_por_fecha(self):
        """
        Prueba unitaria para verificar el filtrado por rango de fechas de las solicitudes.

        Se crean instancias de solicitudes y se realiza una solicitud GET con los parámetros 'fecha_creacion_inicio'
        y 'fecha_creacion_fin', en la cual se supone que el rango de fechas de creación es del '2024-05-01' al '2024-05-18'.
        Luego se realiza la solicitud al controlador 'ventanilla_unica'. Se verifica que la respuesta tenga un código de estado 200
        y que el contenido de la respuesta contenga las filas de la tabla correspondientes a las solicitudes cuyas fechas de creación
        estén dentro del rango especificado.

        Args:
            None

        Returns:
            None
        """
        self.crear_instancias()
        request = self.factory.get('Ventanilla única resumida', {
            'fecha_creacion_inicio': '2024-05-01',
            'fecha_creacion_fin': '2024-05-18'
        })
        request.user = self.user_Ventanilla_unica

        response = summaryOneStopShopView(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, b'May 12, 2024')
        self.assertNotContains(response, b'Jun 6, 2024')
        self.assertNotContains(response, b'July 9, 2024')
     