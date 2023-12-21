# PipeClientConnection - класс
Объект соединения клиента с сервером по каналу, по которому клиент может
отправлять сообщения серверу.
## __Definition
 **Пространство имён:** [Tessa.Platform.Pipes](N_Tessa_Platform_Pipes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class PipeClientConnection : IPipeClientConnection, 
    	IAsyncDisposable, IDisposable
VB __Копировать
     Public Class PipeClientConnection
    	Implements IPipeClientConnection, IAsyncDisposable, IDisposable
C++ __Копировать
     public ref class PipeClientConnection : IPipeClientConnection, 
    	IAsyncDisposable, IDisposable
F# __Копировать
     type PipeClientConnection = 
        class
            interface IPipeClientConnection
            interface IAsyncDisposable
            interface IDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ PipeClientConnection
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable), [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable), [IPipeClientConnection](T_Tessa_Platform_Pipes_IPipeClientConnection.htm)
##  __Заметки
Наследники класса могут переопределить методы, а также добавить дополнительные
методы.
## __Конструкторы
[PipeClientConnection](M_Tessa_Platform_Pipes_PipeClientConnection__ctor.htm)|
Создаёт экземпляр класса с указанием его зависимостей.  
---|---  
## __Свойства
[PipeStream](P_Tessa_Platform_Pipes_PipeClientConnection_PipeStream.htm)|
Поток, определяющий клиентское соединение по каналу. Не равен null.  
---|---  
[ResponseParser](P_Tessa_Platform_Pipes_PipeClientConnection_ResponseParser.htm)|
Объект, выполняющий десериализацию объекта ответа на запрос из текста. Не
равен null.  
[Serializer](P_Tessa_Platform_Pipes_PipeClientConnection_Serializer.htm)|
Объект, выполняющий сериализацию и десериализацию данных в потоке. Не равен
null.  
[TraceListener](P_Tessa_Platform_Pipes_PipeClientConnection_TraceListener.htm)|
Объект, уведомляемый о событиях, происходящих в канале со стороны клиента, или
null, если такой объект не используется.  
## __Методы
[Dispose](M_Tessa_Platform_Pipes_PipeClientConnection_Dispose.htm)|
Освобождает ресурсы, занимаемые объектом.  
---|---  
[DisposeAsync](M_Tessa_Platform_Pipes_PipeClientConnection_DisposeAsync.htm)|
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
[SendAsync](M_Tessa_Platform_Pipes_PipeClientConnection_SendAsync.htm)|
Отправляет сообщение серверу и получает ответ. Возвращаемый объект не равен
null.  
[SendCoreAsync](M_Tessa_Platform_Pipes_PipeClientConnection_SendCoreAsync.htm)|
Отправляет сообщение серверу и получает ответ. Возвращаемый объект не равен
null.  
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
