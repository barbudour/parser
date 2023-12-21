# IKrPermissionsRuleExtension - интерфейс
Расширение проверки прав по карточке правил доступа
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrPermissions](N_Tessa_Extensions_Default_Server_Workflow_KrPermissions.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IKrPermissionsRuleExtension : IExtension
VB __Копировать
     Public Interface IKrPermissionsRuleExtension
    	Inherits IExtension
C++ __Копировать
     public interface class IKrPermissionsRuleExtension : IExtension
F# __Копировать
     type IKrPermissionsRuleExtension = 
        interface
            interface IExtension
        end
Implements
    [IExtension](T_Tessa_Extensions_IExtension.htm)
##  __Методы
[CheckRuleAsync](M_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsRuleExtension_CheckRuleAsync.htm)|
Метод для расширения проверки доступа по правилу доступа. В методе можно
проверить дополнительные поля, добавленные через карточки расширения правил
доступа. Если данное правило не подходит, следует установить свойство
[Cancel](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsRuleExtensionContext_Cancel.htm)  
---|---  
##  __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrPermissions - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrPermissions.htm)
