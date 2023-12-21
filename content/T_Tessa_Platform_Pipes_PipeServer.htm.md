# PipeServer - класс
Сервер, выполняющий обработку сообщений, полученных по каналу.
## __Definition
 **Пространство имён:** [Tessa.Platform.Pipes](N_Tessa_Platform_Pipes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class PipeServer : IPipeServer
VB __Копировать
     Public Class PipeServer
    	Implements IPipeServer
C++ __Копировать
     public ref class PipeServer : IPipeServer
F# __Копировать
     type PipeServer = 
        class
            interface IPipeServer
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ PipeServer
Implements
    [IPipeServer](T_Tessa_Platform_Pipes_IPipeServer.htm)
##  __Конструкторы
[PipeServer](M_Tessa_Platform_Pipes_PipeServer__ctor.htm)|  Создаёт экземпляр
класса с указанием его зависимостей.  
---|---  
## __Свойства
[InputBufferSize](P_Tessa_Platform_Pipes_PipeServer_InputBufferSize.htm)|
Буфер для чтения входящих сообщений. По умолчанию равен 4096.  
---|---  
[InstanceResolverFactory](P_Tessa_Platform_Pipes_PipeServer_InstanceResolverFactory.htm)|
Фабрика объектов
[IPipeInstanceResolver](T_Tessa_Platform_Pipes_IPipeInstanceResolver.htm). Не
равна null.  
[MessageFactory](P_Tessa_Platform_Pipes_PipeServer_MessageFactory.htm)|
Объект, выполняющий создание сообщение, полученных по каналу. Не равен null.  
[OutputBufferSize](P_Tessa_Platform_Pipes_PipeServer_OutputBufferSize.htm)|
Буфер для чтения исходящих сообщений. По умолчанию равен 4096.  
[RequestParser](P_Tessa_Platform_Pipes_PipeServer_RequestParser.htm)|  Объект,
выполняющий десериализацию объекта запроса из текста. Не равен null.  
[Serializer](P_Tessa_Platform_Pipes_PipeServer_Serializer.htm)|  Объект,
выполняющий сериализацию и десериализацию данных в потоке. Не равен null.  
## __Методы
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
[ListenAsync](M_Tessa_Platform_Pipes_PipeServer_ListenAsync.htm)|  Выполняет
открытие канала, по которому объект получает сообщения от единственного
клиента и обрабатывает их посредством переданного объекта router.
Прослушивание завершается, если клиент отключился от канала или операция была
отменена посредством токена cancellationToken. Один вызванный метод
обслуживает ровно одного клиента, если требуется обслуживать несколько
клиентов, то надо запустить несколько асинхронных задач Task.Run, в каждом из
которых будет вызван свой метод прослушивания, после завершения которого он
вызывается ещё раз.  
[ListenCoreAsync](M_Tessa_Platform_Pipes_PipeServer_ListenCoreAsync.htm)|
Выполняет открытие канала, по которому объект получает сообщения от
единственного клиента и обрабатывает их посредством переданного объекта
router. Прослушивание завершается, если клиент отключился от канала или
операция была отменена посредством токена cancellationToken. Один вызванный
метод обслуживает ровно одного клиента, если требуется обслуживать несколько
клиентов, то надо запустить несколько асинхронных задач Task.Run, в каждом из
которых будет вызван свой метод прослушивания, после завершения которого он
вызывается ещё раз.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
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
[Tessa.Platform.Pipes - пространство имён](N_Tessa_Platform_Pipes.htm)
