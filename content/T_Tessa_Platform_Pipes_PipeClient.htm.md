# PipeClient - класс
Клиент, выполняющий отправку сообщений по каналу. Использует объект настроек
[PipeClientOptions](T_Tessa_Platform_Pipes_PipeClientOptions.htm).
## __Definition
 **Пространство имён:** [Tessa.Platform.Pipes](N_Tessa_Platform_Pipes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class PipeClient : IPipeClient
VB __Копировать
     Public Class PipeClient
    	Implements IPipeClient
C++ __Копировать
     public ref class PipeClient : IPipeClient
F# __Копировать
     type PipeClient = 
        class
            interface IPipeClient
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ PipeClient
Implements
    [IPipeClient](T_Tessa_Platform_Pipes_IPipeClient.htm)
##  __Заметки
Наследники класса могут переопределить или добавить методы.
## __Конструкторы
[PipeClient](M_Tessa_Platform_Pipes_PipeClient__ctor.htm)|  Создаёт экземпляр
класса с указанием его зависимостей.  
---|---  
## __Свойства
[ResponseParser](P_Tessa_Platform_Pipes_PipeClient_ResponseParser.htm)|
Объект, выполняющий десериализацию объекта ответа на запрос из текста. Не
равен null.  
---|---  
[Serializer](P_Tessa_Platform_Pipes_PipeClient_Serializer.htm)|  Объект,
выполняющий сериализацию и десериализацию данных в потоке. Не равен null.  
## __Методы
[ConnectAsync](M_Tessa_Platform_Pipes_PipeClient_ConnectAsync.htm)|
Соединяется с сервером в соответствии с настройками подключения и возвращает
объект соединения, для которого вызов [SendAsync(IPipeRequest,
CancellationToken)](M_Tessa_Platform_Pipes_IPipeClientConnection_SendAsync.htm)
отправляет очередное сообщение, а вызов
[DisposeAsync()](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable.disposeasync#system-
iasyncdisposable-disposeasync) закрывает соединение.  
---|---  
[ConnectCoreAsync](M_Tessa_Platform_Pipes_PipeClient_ConnectCoreAsync.htm)|
Соединяется с сервером в соответствии с настройками подключения и возвращает
объект соединения, для которого вызов [SendAsync(IPipeRequest,
CancellationToken)](M_Tessa_Platform_Pipes_IPipeClientConnection_SendAsync.htm)
отправляет очередное сообщение, а вызов
[DisposeAsync()](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable.disposeasync#system-
iasyncdisposable-disposeasync) закрывает соединение.  
[CreateConnection](M_Tessa_Platform_Pipes_PipeClient_CreateConnection.htm)|
Создаёт объект соединения клиента с сервером по каналу.  
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
