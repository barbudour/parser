# TessaApplicationProcessServiceClient - класс
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Services.PlatformApplication](N_Tessa_Applications_Services_PlatformApplication.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class TessaApplicationProcessServiceClient : ITessaApplicationServiceHost, 
    	IAsyncDisposable, IDisposable, ITessaApplicationPipeService
VB __Копировать
     Public NotInheritable Class TessaApplicationProcessServiceClient
    	Implements ITessaApplicationServiceHost, IAsyncDisposable, IDisposable, ITessaApplicationPipeService
C++ __Копировать
     public ref class TessaApplicationProcessServiceClient sealed : ITessaApplicationServiceHost, 
    	IAsyncDisposable, IDisposable, ITessaApplicationPipeService
F# __Копировать
     [<SealedAttribute>]
    type TessaApplicationProcessServiceClient = 
        class
            interface ITessaApplicationServiceHost
            interface IAsyncDisposable
            interface IDisposable
            interface ITessaApplicationPipeService
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ TessaApplicationProcessServiceClient
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable), [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable), [ITessaApplicationPipeService](T_Tessa_Applications_Pipes_ITessaApplicationPipeService.htm), [ITessaApplicationServiceHost](T_Tessa_Applications_Services_PlatformApplication_ITessaApplicationServiceHost.htm)
##  __Конструкторы
[TessaApplicationProcessServiceClient](M_Tessa_Applications_Services_PlatformApplication_TessaApplicationProcessServiceClient__ctor.htm)|
Инициализирует новый экземпляр класса TessaApplicationProcessServiceClient  
---|---  
##  __Свойства
[ServiceAddress](P_Tessa_Applications_Services_PlatformApplication_TessaApplicationProcessServiceClient_ServiceAddress.htm)|
Gets Адрес сервиса по которому диспетчер приложений может отправлять
экземпляру приложений сообщения.  
---|---  
[ServiceStarted](P_Tessa_Applications_Services_PlatformApplication_TessaApplicationProcessServiceClient_ServiceStarted.htm)|
Gets a value indicating whether Признак нахождения сервиса в запущенном
состоянии  
## __Методы
[Dispose](M_Tessa_Applications_Services_PlatformApplication_TessaApplicationProcessServiceClient_Dispose.htm)|
Освобождает ресурсы, занимаемые объектом.  
---|---  
[DisposeAsync](M_Tessa_Applications_Services_PlatformApplication_TessaApplicationProcessServiceClient_DisposeAsync.htm)|
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
[ProcessMessageAsync](M_Tessa_Applications_Services_PlatformApplication_TessaApplicationProcessServiceClient_ProcessMessageAsync.htm)|  
[StartServiceAsync](M_Tessa_Applications_Services_PlatformApplication_TessaApplicationProcessServiceClient_StartServiceAsync.htm)|
Запускает сервис приложения, если он ещё не запущен  
[StopServiceAsync](M_Tessa_Applications_Services_PlatformApplication_TessaApplicationProcessServiceClient_StopServiceAsync.htm)|
Останавливает сервис приложения, если он запущен  
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
[Tessa.Applications.Services.PlatformApplication - пространство
имён](N_Tessa_Applications_Services_PlatformApplication.htm)
