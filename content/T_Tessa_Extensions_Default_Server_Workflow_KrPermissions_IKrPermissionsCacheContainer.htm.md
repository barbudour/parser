# IKrPermissionsCacheContainer - интерфейс
Контейнер кеша правил доступа.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrPermissions](N_Tessa_Extensions_Default_Server_Workflow_KrPermissions.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IKrPermissionsCacheContainer
VB __Копировать
     Public Interface IKrPermissionsCacheContainer
C++ __Копировать
     public interface class IKrPermissionsCacheContainer
F# __Копировать
     type IKrPermissionsCacheContainer = interface end
##  __Методы
[GetVersionAsync](M_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsCacheContainer_GetVersionAsync.htm)|
Метод для получения номер текущей версии кеша правил доступа.  
---|---  
[TryGetCacheAsync](M_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsCacheContainer_TryGetCacheAsync.htm)|
Метод для получения объекта кеша правил доступа. Возвращает null и пишет
ошибку в validationResult, если не удалось получить объект кеша.  
[UpdateVersionAsync](M_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsCacheContainer_UpdateVersionAsync.htm)|
Метод для обновления версии кеша.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrPermissions - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrPermissions.htm)
