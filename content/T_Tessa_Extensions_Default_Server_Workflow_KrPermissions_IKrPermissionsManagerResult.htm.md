# IKrPermissionsManagerResult - интерфейс
Результат выполнения проверки прав доступа в
[IKrPermissionsManager](T_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManager.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrPermissions](N_Tessa_Extensions_Default_Server_Workflow_KrPermissions.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IKrPermissionsManagerResult
VB __Копировать
     Public Interface IKrPermissionsManagerResult
C++ __Копировать
     public interface class IKrPermissionsManagerResult
F# __Копировать
     type IKrPermissionsManagerResult = interface end
##  __Свойства
[ExtendedCardSettings](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManagerResult_ExtendedCardSettings.htm)|
Набор прав доступа к секциям карточки  
---|---  
[ExtendedTasksSettings](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManagerResult_ExtendedTasksSettings.htm)|
Набор прав доступа к секциям заданий, разбитых по типам заданий  
[FileRules](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManagerResult_FileRules.htm)|
Набор правил доступа для файлов  
[Permissions](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManagerResult_Permissions.htm)|
Набор рассчитанных прав  
[Version](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManagerResult_Version.htm)|
Версия правил доступа  
[WithExtendedSettings](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManagerResult_WithExtendedSettings.htm)|
Определяет, были ли запрошены права на редактирование.  
## __Методы
[CreateExtendedCardSettings](M_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManagerResult_CreateExtendedCardSettings.htm)|
Создает расширенные настройки прав карточки по результату расчета прав
доступа. Если при расчете прав не использовались расширенные настройки
проверки прав доступа, то метод вернет null.  
---|---  
[Has](M_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManagerResult_Has.htm)|
Определяет, что в результате есть данный флаг  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrPermissions - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrPermissions.htm)
