# ApplicationManagerMultiProcessServiceHost - класс
Объект, запускающий или останавливающий группу сервисов
[IApplicationManagerServiceHost](T_Tessa_Applications_Services_ApplicationManager_IApplicationManagerServiceHost.htm).
## __Definition
 **Пространство имён:**
[Tessa.Applications.Services.ApplicationManager](N_Tessa_Applications_Services_ApplicationManager.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ApplicationManagerMultiProcessServiceHost : IApplicationManagerServiceHost, 
    	IAsyncDisposable, IDisposable
VB __Копировать
     Public NotInheritable Class ApplicationManagerMultiProcessServiceHost
    	Implements IApplicationManagerServiceHost, IAsyncDisposable, IDisposable
C++ __Копировать
     public ref class ApplicationManagerMultiProcessServiceHost sealed : IApplicationManagerServiceHost, 
    	IAsyncDisposable, IDisposable
F# __Копировать
     [<SealedAttribute>]
    type ApplicationManagerMultiProcessServiceHost = 
        class
            interface IApplicationManagerServiceHost
            interface IAsyncDisposable
            interface IDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ApplicationManagerMultiProcessServiceHost
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable), [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable), [IApplicationManagerServiceHost](T_Tessa_Applications_Services_ApplicationManager_IApplicationManagerServiceHost.htm)
##  __Конструкторы
[ApplicationManagerMultiProcessServiceHost](M_Tessa_Applications_Services_ApplicationManager_ApplicationManagerMultiProcessServiceHost__ctor.htm)|
Создаёт экземпляр класса с указанием значений его свойств.  
---|---  
## __Свойства
[ServiceStarted](P_Tessa_Applications_Services_ApplicationManager_ApplicationManagerMultiProcessServiceHost_ServiceStarted.htm)|  
---|---  
## __Методы
[Dispose](M_Tessa_Applications_Services_ApplicationManager_ApplicationManagerMultiProcessServiceHost_Dispose.htm)|
Освобождает ресурсы, занимаемые объектом.  
---|---  
[DisposeAsync](M_Tessa_Applications_Services_ApplicationManager_ApplicationManagerMultiProcessServiceHost_DisposeAsync.htm)|
Освобождает ресурсы, занимаемые объектом.  
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
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[StartServiceAsync](M_Tessa_Applications_Services_ApplicationManager_ApplicationManagerMultiProcessServiceHost_StartServiceAsync.htm)|  
[StopServiceAsync](M_Tessa_Applications_Services_ApplicationManager_ApplicationManagerMultiProcessServiceHost_StopServiceAsync.htm)|  
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
[Tessa.Applications.Services.ApplicationManager - пространство
имён](N_Tessa_Applications_Services_ApplicationManager.htm)
