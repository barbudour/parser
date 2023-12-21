# IKrPermissionsManager - интерфейс
Объект, который выполняет проверку прав доступа
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrPermissions](N_Tessa_Extensions_Default_Server_Workflow_KrPermissions.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IKrPermissionsManager
VB __Копировать
     Public Interface IKrPermissionsManager
C++ __Копировать
     public interface class IKrPermissionsManager
F# __Копировать
     type IKrPermissionsManager = interface end
##  __Свойства
[IgnoreSections](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManager_IgnoreSections.htm)|
Список секций, проверка которых игнорируется при проверке прав доступа  
---|---  
## __Методы
[CheckRequiredPermissionsAsync](M_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManager_CheckRequiredPermissionsAsync.htm)|
Метод для проверки доступа. Если при проверке прав доступа будут обнаружены
ошибки, они будут записаны в context в свойство
[ValidationResult](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManagerContext_ValidationResult.htm)  
---|---  
[GetEffectivePermissionsAsync](M_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManager_GetEffectivePermissionsAsync.htm)|
Метод для получения списка прав доступа к карточке.  
[TryCreateContextAsync](M_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManager_TryCreateContextAsync.htm)|
Метод для создания контекста проверки прав доступа. Метод формирует контекст
прав доступа с учетом полученных данных. Если данных для создания контекста
недостаточно, то метод выбросит исключение.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrPermissions - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrPermissions.htm)
