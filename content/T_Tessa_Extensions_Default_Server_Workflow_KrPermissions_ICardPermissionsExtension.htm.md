# ICardPermissionsExtension - интерфейс
Расширение прав на карточку
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrPermissions](N_Tessa_Extensions_Default_Server_Workflow_KrPermissions.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardPermissionsExtension : IExtension
VB __Копировать
     Public Interface ICardPermissionsExtension
    	Inherits IExtension
C++ __Копировать
     public interface class ICardPermissionsExtension : IExtension
F# __Копировать
     type ICardPermissionsExtension = 
        interface
            interface IExtension
        end
Implements
    [IExtension](T_Tessa_Extensions_IExtension.htm)
##  __Методы
[ExtendPermissionsAsync](M_Tessa_Extensions_Default_Server_Workflow_KrPermissions_ICardPermissionsExtension_ExtendPermissionsAsync.htm)|
Метод, расширяющий права на карточку.  
---|---  
[IsPermissionsRecalcRequired](M_Tessa_Extensions_Default_Server_Workflow_KrPermissions_ICardPermissionsExtension_IsPermissionsRecalcRequired.htm)|
Указывает системе на необходимость пересчета прав при сохранении карточки, а
также на получение контента файла и контента версии, несмотря на то, что при
чтении были выданы права на изменение и записаны в токен. Пример: Пользователь
может редактировать договора с суммой до 100р. Он редактирует карточку с
суммой 80р, при запросе прав система выдала права на редактирование и записала
в токен. Это значит, что пользователь сможет поменять сумму на большую чем
100р. Если такое поведение запрещено вашей логикой, то расширение должно
проверить изменилась ли сумма договора из контекста и вернуть true, тогда
система пересчитает права перед сохранением и пользователь получит сообщение о
недостаточности прав для изменения карточки.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrPermissions - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrPermissions.htm)
