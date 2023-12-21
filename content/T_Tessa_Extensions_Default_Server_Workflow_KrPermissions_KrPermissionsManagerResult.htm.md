# KrPermissionsManagerResult - класс
Результат выполнения проверки прав доступа в
[IKrPermissionsManager](T_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManager.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrPermissions](N_Tessa_Extensions_Default_Server_Workflow_KrPermissions.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class KrPermissionsManagerResult : IKrPermissionsManagerResult
VB __Копировать
     Public NotInheritable Class KrPermissionsManagerResult
    	Implements IKrPermissionsManagerResult
C++ __Копировать
     public ref class KrPermissionsManagerResult sealed : IKrPermissionsManagerResult
F# __Копировать
     [<SealedAttribute>]
    type KrPermissionsManagerResult = 
        class
            interface IKrPermissionsManagerResult
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ KrPermissionsManagerResult
Implements
    [IKrPermissionsManagerResult](T_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManagerResult.htm)
##  __Конструкторы
[KrPermissionsManagerResult](M_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerResult__ctor.htm)|
Инициализирует новый экземпляр класса KrPermissionsManagerResult  
---|---  
##  __Свойства
[ExtendedCardSettings](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerResult_ExtendedCardSettings.htm)|
Набор прав доступа к секциям карточки  
---|---  
[ExtendedTasksSettings](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerResult_ExtendedTasksSettings.htm)|
Набор прав доступа к секциям заданий, разбитых по типам заданий  
[FileRules](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerResult_FileRules.htm)|
Набор правил доступа для файлов  
[Permissions](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerResult_Permissions.htm)|
Набор рассчитанных прав  
[Version](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerResult_Version.htm)|
Версия правил доступа  
[WithExtendedSettings](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerResult_WithExtendedSettings.htm)|
Определяет, были ли запрошены права на редактирование.  
## __Методы
[CreateExtendedCardSettings](M_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerResult_CreateExtendedCardSettings.htm)|
Создает расширенные настройки прав карточки по результату расчета прав
доступа. Если при расчете прав не использовались расширенные настройки
проверки прав доступа, то метод вернет null.  
---|---  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Has](M_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerResult_Has.htm)|
Определяет, что в результате есть данный флаг  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Поля
[Empty](F_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerResult_Empty.htm)|  
---|---  
## __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrPermissions - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrPermissions.htm)
