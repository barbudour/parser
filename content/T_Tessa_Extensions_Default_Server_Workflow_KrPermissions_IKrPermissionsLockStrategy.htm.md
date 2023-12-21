# IKrPermissionsLockStrategy - интерфейс
Объект для получения блокировок на чтение и записи правил доступа
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrPermissions](N_Tessa_Extensions_Default_Server_Workflow_KrPermissions.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IKrPermissionsLockStrategy
VB __Копировать
     Public Interface IKrPermissionsLockStrategy
C++ __Копировать
     public interface class IKrPermissionsLockStrategy
F# __Копировать
     type IKrPermissionsLockStrategy = interface end
##  __Методы
[ClearLocksAsync](M_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsLockStrategy_ClearLocksAsync.htm)|
Метод для сброса всех блокировок.  
---|---  
[TryObtainReaderLockAsync](M_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsLockStrategy_TryObtainReaderLockAsync.htm)|
Метод для получения блокировки на чтение правил доступа. Возвращает null, если
блокировку получить не удалось.  
[TryObtainWriterLockAsync](M_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsLockStrategy_TryObtainWriterLockAsync.htm)|
Метод для получения блокировки на запись правил доступа. Возвращает null, если
блокировку получить не удалось.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrPermissions - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrPermissions.htm)
