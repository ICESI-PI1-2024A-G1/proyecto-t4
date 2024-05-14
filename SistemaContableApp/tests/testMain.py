# archivo_principal_tests.py
import unittest

# Importa la clase de test específica
from .oneStopShopTests.oneStopShopCommentsTest import *
from .oneStopShopTests.oneStopShopFormsTest import *
from .oneStopShopTests.oneStopShopHistoryTest import *
from .oneStopShopTests.oneStopShopModelsTest import *
from .oneStopShopTests.oneStopShopModifyState import *
from .oneStopShopTests.oneStopShopPermissionTests import *
from .oneStopShopTests.oneStopShopSearchTest import *
from .oneStopShopTests.oneStopShopStatesTest import *
from .oneStopShopTests.oneStopShopViewsTest import *

from .loginTest.userLoginTestForms import *
from .loginTest.userLoginTestViews import *

from .requestByUserTests.requestByUserFormTests import *
from .requestByUserTests.requestByUserModelTests import *
from .requestByUserTests.requestByUserPermissionTests import *
from .requestByUserTests.requestByUserViewsTests import *

from .ReviewerApproverManager.getUserTest import *
from .ReviewerApproverManager.upDateRoleTest import *

from .updateUserTests.updateUserTests import *
from .updateUserTests.updateUserPermissionTests import *


# Crea la suite de tests
def suite():
    """
    Esta función crea una suite de tests que incluye todos los tests unitarios de la aplicación.

    Retorna:
        suite (unittest.TestSuite): La suite de tests.
    """
    suite = unittest.TestSuite()
    
    # Añade los tests de la clase CommentsTestCase a la suite
    suite.addTests(unittest.makeSuite(CommentsTestCase))
    suite.addTests(unittest.makeSuite(FormTestCase))
    suite.addTests(unittest.makeSuite(HistoryStateTestCase))
    suite.addTests(unittest.makeSuite(ModelTestCase))
    suite.addTests(unittest.makeSuite(ModifyStateTestCase))
    suite.addTests(unittest.makeSuite(OneStopShopViewTestCasePermission))
    suite.addTests(unittest.makeSuite(SearchTestCase))
    suite.addTests(unittest.makeSuite(StatesTestCase))
    suite.addTests(unittest.makeSuite(ViewTestCase))
    
    suite.addTests(unittest.makeSuite(LoginFormTest))
    suite.addTests(unittest.makeSuite(LoginFormAdditionalTest))
    suite.addTests(unittest.makeSuite(CustomUserCreationFormAdditionalTest))
    suite.addTests(unittest.makeSuite(CustomUserCreationFormTestsNew))
    suite.addTests(unittest.makeSuite(LoginFormExtraTestsNew))
    suite.addTests(unittest.makeSuite(CustomUserCreationFormExtraTestsNew))
    suite.addTests(unittest.makeSuite(CustomUserCreationFormTestsExtra))
    suite.addTests(unittest.makeSuite(LoginFormSpecialTests))
    suite.addTests(unittest.makeSuite(CustomUserCreationFormTest))
    suite.addTests(unittest.makeSuite(UserRequestViewsTest2))
    suite.addTests(unittest.makeSuite(UserRequestViewsTest3))
    suite.addTests(unittest.makeSuite(UserRequestViewsTest4))
    
    suite.addTests(unittest.makeSuite(ChargeAccountFormTests))
    suite.addTests(unittest.makeSuite(RequisitionFormTests))
    suite.addTests(unittest.makeSuite(ExteriorPaymentFormTests))
    suite.addTests(unittest.makeSuite(TravelExpensesSolicitationFormTests))
    suite.addTests(unittest.makeSuite(TravelAdvanceSolicitationFormTests))
    suite.addTests(unittest.makeSuite(ChargeAccountModelTests))
    suite.addTests(unittest.makeSuite(RequisitionModelTests))
    suite.addTests(unittest.makeSuite(ExteriorPaymentModelTests))
    suite.addTests(unittest.makeSuite(LegalizationModelTests))
    suite.addTests(unittest.makeSuite(AdvancePaymentModelTests))
    suite.addTests(unittest.makeSuite(FormCreationViewTestCaseP))
    suite.addTests(unittest.makeSuite(IsLateRequestTestCase))
    suite.addTests(unittest.makeSuite(ViewsTestCaseRequests))
    suite.addTests(unittest.makeSuite(ExcelGenerationTestCase))
    
    suite.addTests(unittest.makeSuite(GetUsersTest))
    suite.addTests(unittest.makeSuite(UpdateRoleTest))
    
    suite.addTests(unittest.makeSuite(UserModelTestCase))
    suite.addTests(unittest.makeSuite(UserUpdateFormTestCase))
    suite.addTests(unittest.makeSuite(UserViewTestCase))
    suite.addTests(unittest.makeSuite(updateUserPermissionTestCase))
    
    
    
    return suite

# Ejecuta la suite de tests
if __name__ == '__main__':
    """
    Este es el punto de entrada principal del script.
    Ejecuta la suite de tests cuando el script se ejecuta directamente.
    """
    runner = unittest.TextTestRunner()
    runner.run(suite())