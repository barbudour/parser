# TessaBackgroundService - класс
Сервис асинхронной обработки действий на стороне веб-сервера. Производит
обработку действий, поставленных в очередь асинхронной обработки
[IWebBackgroundServiceQueue](T_Tessa_Web_Services_IWebBackgroundServiceQueue.htm).
## __Definition
 **Пространство имён:** [Tessa.Web.Services](N_Tessa_Web_Services.htm)  
 **Сборка:** Tessa.Web (в Tessa.Web.dll) Версия: 3.6.0.17
C# __Копировать
     public class TessaBackgroundService : IHostedService, 
    	IDisposable
VB __Копировать
     Public Class TessaBackgroundService
    	Implements IHostedService, IDisposable
C++ __Копировать
     public ref class TessaBackgroundService : IHostedService, 
    	IDisposable
F# __Копировать
     type TessaBackgroundService = 
        class
            interface IHostedService
            interface IDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ TessaBackgroundService
Implements
    [IHostedService](https://learn.microsoft.com/dotnet/api/microsoft.extensions.hosting.ihostedservice), [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)
##  __Конструкторы
[TessaBackgroundService](M_Tessa_Web_Services_TessaBackgroundService__ctor.htm)|
Инициализирует новый экземпляр класса TessaBackgroundService  
---|---  
##  __Методы
[Dispose](M_Tessa_Web_Services_TessaBackgroundService_Dispose.htm)| Performs
application-defined tasks associated with freeing, releasing, or resetting
unmanaged resources.  
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
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[StartAsync](M_Tessa_Web_Services_TessaBackgroundService_StartAsync.htm)|
Triggered when the application host is ready to start the service.  
[StopAsync](M_Tessa_Web_Services_TessaBackgroundService_StopAsync.htm)|
Triggered when the application host is performing a graceful shutdown.  
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
[Tessa.Web.Services - пространство имён](N_Tessa_Web_Services.htm)
