# KrPermissionsManager - класс
Объект, который выполняет проверку прав доступа
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrPermissions](N_Tessa_Extensions_Default_Server_Workflow_KrPermissions.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class KrPermissionsManager : IKrPermissionsManager
VB __Копировать
     Public NotInheritable Class KrPermissionsManager
    	Implements IKrPermissionsManager
C++ __Копировать
     public ref class KrPermissionsManager sealed : IKrPermissionsManager
F# __Копировать
     [<SealedAttribute>]
    type KrPermissionsManager = 
        class
            interface IKrPermissionsManager
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ KrPermissionsManager
Implements
    [IKrPermissionsManager](T_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManager.htm)
##  __Конструкторы
[KrPermissionsManager](M_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManager__ctor.htm)|
Инициализирует новый экземпляр класса KrPermissionsManager  
---|---  
##  __Свойства
[IgnoreSections](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManager_IgnoreSections.htm)|
Список секций, проверка которых игнорируется при проверке прав доступа  
---|---  
## __Методы
[CheckRequiredPermissionsAsync](M_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManager_CheckRequiredPermissionsAsync.htm)|
Метод для проверки доступа. Если при проверке прав доступа будут обнаружены
ошибки, они будут записаны в context в свойство
[ValidationResult](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManagerContext_ValidationResult.htm)  
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
[GetEffectivePermissionsAsync](M_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManager_GetEffectivePermissionsAsync.htm)|
Метод для получения списка прав доступа к карточке.  
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
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryCreateContextAsync](M_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManager_TryCreateContextAsync.htm)|
Метод для создания контекста проверки прав доступа. Метод формирует контекст
прав доступа с учетом полученных данных. Если данных для создания контекста
недостаточно, то метод выбросит исключение.  
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
