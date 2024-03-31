from django.http import HttpRequest
from SistemaContableApp.models import Following
from SistemaContableApp.views import ventanilla_unica
from django.test import TestCase

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
        Following.objects.create(state='Aprobado', color='azul', creation_date='2024-5-12', type='requesicion', concept='pago', money_type='USD', amount=30, cenco=30, cex_number=15, observations='ninguna', close_date='2025-5-12')
        Following.objects.create(state='Pendiente', color='verde', creation_date='2024-6-12', type='adelanto', concept='dinero', money_type='COP', amount=30, cenco=30, cex_number=15, observations='ninguna', close_date='2025-6-12')
        Following.objects.create(state='Rechazado', color='rojo', creation_date='2024-7-12', type='anticipo', concept='billetes', money_type='COP', amount=30, cenco=30, cex_number=15, observations='ninguna', close_date='2025-7-12')  

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

        response = ventanilla_unica(request)
        
        
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
        

        response = ventanilla_unica(request)

        assert response.status_code == 200
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, b'requesicion')  # Verifica que el tipo "requesicion" esté presente en la respuesta
        
        
      

