import pytest
from django.contrib.auth.models import User
from django.http import HttpRequest
from SistemaContableApp.models import Following
from SistemaContableApp.views import ventanilla_unica
from django.test import TestCase

class SearchTestCase(TestCase):


    def testFiltrarSolicitudPorEstado(self):
        """
        Prueba unitaria para verificar el filtrado por estado de las solicitudes.

        Se crean instancias de solicitudes y se realiza una solicitud GET con el parámetro 'estado' establecido en '1',
        que supone que el ID del estado "Aprobado" es 1. Luego se autentica al usuario y se realiza la solicitud al
        controlador 'programas'. Se verifica que la respuesta tenga un código de estado 200 y que el contenido de la
        respuesta contenga el programa 1, pero no el programa 2 ni el programa 3, ya que su estado no es "Aprobado".

        Args:
            None

        Returns:
            None
        """
        
        def crear_instancias():
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


            Following1 = Following.objects.create(state='Aprobado', color='azul', creation_date='2024-5-12', type='requesicion', concept='pago', money_type='USD', amount=30, cenco=30, cex_number=15, observations='ninguna', close_date='2025-5-12')
            Following2 = Following.objects.create(state='Pendiente', color='verde', creation_date='2024-6-12', type='adelanto', concept='dinero', money_type='COP', amount=30, cenco=30, cex_number=15, observations='ninguna', close_date='2025-6-12')
            Following2 = Following.objects.create(state='Rechazado', color='rojo', creation_date='2024-7-12', type='anticipo', concept='billetes', money_type='COP', amount=30, cenco=30, cex_number=15, observations='ninguna', close_date='2025-7-12')  

        crear_instancias()
        request = HttpRequest()
        request.method = 'GET'
        request.GET['estado'] = '1'  # Suponiendo que el ID del estado "Aprobado" es 1
    

        response = ventanilla_unica(request)
            
        assert response.status_code == 200
        assert b'Solicitud 1' in response.content  # Suponiendo que el estado "Aprobado" está asociado al following 1
        assert b'Solicitud 2' not in response.content  # Following 2 no debería estar presente, ya que su estado no es "Aprobado"
        assert b'Solicitud 3' not in response.content  # Following 3 no debería estar presente, ya que su estado no es "Aprobado"

        