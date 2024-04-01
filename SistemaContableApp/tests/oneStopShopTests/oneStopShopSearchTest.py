from django.http import HttpRequest
from django.test import TestCase
from SistemaContableApp.models import Following, State
from SistemaContableApp.views import summaryOneStopShopView

class SearchTestCase(TestCase):
   
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

    def testFiltrarSolicitudPorEstado(self):
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
        request = HttpRequest()
        request.method = 'GET'
        request.GET['estado'] = 'Aprobado' 

        response = summaryOneStopShopView(request)
        
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, b'Aprobado')  # Verifica que el estado "Aprobado" esté presente
     
        
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
        request = HttpRequest()
        

        request.method = 'GET'
        request.GET['q'] = 'requesicion'
        

        response = summaryOneStopShopView(request)

        assert response.status_code == 200
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, b'requesicion')  # Verifica que el tipo "requesicion" esté presente en la respuesta
