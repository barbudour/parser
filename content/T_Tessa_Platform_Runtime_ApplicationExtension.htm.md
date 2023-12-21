# ApplicationExtension - класс
Базовый класс для расширения, связанного с жизненным циклом приложения.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class ApplicationExtension : IApplicationExtension, 
    	IExtension
VB __Копировать
     Public MustInherit Class ApplicationExtension
    	Implements IApplicationExtension, IExtension
C++ __Копировать
     public ref class ApplicationExtension abstract : IApplicationExtension, 
    	IExtension
F# __Копировать
     [<AbstractClassAttribute>]
    type ApplicationExtension = 
        class
            interface IApplicationExtension
            interface IExtension
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ApplicationExtension
Derived
[Tessa.Extensions.Default.Client.Notifications.KrNotificationsApplicationExtension](T_Tessa_Extensions_Default_Client_Notifications_KrNotificationsApplicationExtension.htm)
[Tessa.Extensions.Platform.Client.Application.ClientApplicationExtension](T_Tessa_Extensions_Platform_Client_Application_ClientApplicationExtension.htm)
[Tessa.Extensions.Platform.Client.Application.FileFinalizationApplicationExtension](T_Tessa_Extensions_Platform_Client_Application_FileFinalizationApplicationExtension.htm)
[Tessa.Extensions.Platform.Client.Application.WorkplacesExtension](T_Tessa_Extensions_Platform_Client_Application_WorkplacesExtension.htm)
Implements
    [IExtension](T_Tessa_Extensions_IExtension.htm), [IApplicationExtension](T_Tessa_Platform_Runtime_IApplicationExtension.htm)
##  __Конструкторы
[ApplicationExtension](M_Tessa_Platform_Runtime_ApplicationExtension__ctor.htm)|
Инициализирует новый экземпляр класса ApplicationExtension  
---|---  
##  __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
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
[Initialize](M_Tessa_Platform_Runtime_ApplicationExtension_Initialize.htm)|
Метод, выполняемый при инициализации приложения, когда основные подсистемы уже
инициализированы.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Shutdown](M_Tessa_Platform_Runtime_ApplicationExtension_Shutdown.htm)| Метод,
выполняемый при завершении работы приложения.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
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
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
