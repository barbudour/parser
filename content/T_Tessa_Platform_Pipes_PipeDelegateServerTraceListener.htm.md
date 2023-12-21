# PipeDelegateServerTraceListener - класс
Объект, уведомляемый о событиях, происходящих в канале со стороны сервера, где
обработчики событий передаются как делегаты в конструкторе.
## __Definition
 **Пространство имён:** [Tessa.Platform.Pipes](N_Tessa_Platform_Pipes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class PipeDelegateServerTraceListener : PipeServerTraceListener
VB __Копировать
     Public Class PipeDelegateServerTraceListener
    	Inherits PipeServerTraceListener
C++ __Копировать
     public ref class PipeDelegateServerTraceListener : public PipeServerTraceListener
F# __Копировать
     type PipeDelegateServerTraceListener = 
        class
            inherit PipeServerTraceListener
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[PipeServerTraceListener](T_Tessa_Platform_Pipes_PipeServerTraceListener.htm) __ PipeDelegateServerTraceListener
##  __Заметки
Наследники класса могут переопределять методы и изменять значения свойств.
## __Конструкторы
[PipeDelegateServerTraceListener](M_Tessa_Platform_Pipes_PipeDelegateServerTraceListener__ctor.htm)|
Создаёт экземпляр класса с указанием делегатов, определяющий поведение его
методов.  
---|---  
## __Свойства
[OnClientConnectedFuncAsync](P_Tessa_Platform_Pipes_PipeDelegateServerTraceListener_OnClientConnectedFuncAsync.htm)|
Уведомляет о событии подключения клиента к серверу.  
---|---  
[OnClientDisconnectedFuncAsync](P_Tessa_Platform_Pipes_PipeDelegateServerTraceListener_OnClientDisconnectedFuncAsync.htm)|
Уведомляет о событии отключения клиента от сервера.  
[OnExceptionFuncAsync](P_Tessa_Platform_Pipes_PipeDelegateServerTraceListener_OnExceptionFuncAsync.htm)|
Уведомляет о событии возникновения исключения в процессе обработки запроса.  
[OnRequestHandledFuncAsync](P_Tessa_Platform_Pipes_PipeDelegateServerTraceListener_OnRequestHandledFuncAsync.htm)|
Уведомляет о событии окончания обработки запроса, полученного от клиента.
Обработка запроса не завершена с исключением.  
[OnRequestReceivedFuncAsync](P_Tessa_Platform_Pipes_PipeDelegateServerTraceListener_OnRequestReceivedFuncAsync.htm)|
Уведомляет о событии получения запроса от клиента.  
[OnServerShutdownFuncAsync](P_Tessa_Platform_Pipes_PipeDelegateServerTraceListener_OnServerShutdownFuncAsync.htm)|
Уведомляет о событии завершения работы сервера. Выполняется в случаях, если
клиент подключился и затем отключился, а также если сервер завершил работу в
результате невосстановимой ошибки, такой, как ошибка чтения из канала или
записи в канал.  
[OnServerStartupFuncAsync](P_Tessa_Platform_Pipes_PipeDelegateServerTraceListener_OnServerStartupFuncAsync.htm)|
Уведомляет о событии запуска сервера.  
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
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[OnClientConnectedAsync](M_Tessa_Platform_Pipes_PipeDelegateServerTraceListener_OnClientConnectedAsync.htm)|
Уведомляет о событии подключения клиента к серверу.  
(Переопределяет
[PipeServerTraceListener.OnClientConnectedAsync(CancellationToken)](M_Tessa_Platform_Pipes_PipeServerTraceListener_OnClientConnectedAsync.htm))  
[OnClientDisconnectedAsync](M_Tessa_Platform_Pipes_PipeDelegateServerTraceListener_OnClientDisconnectedAsync.htm)|
Уведомляет о событии отключения клиента от сервера.  
(Переопределяет
[PipeServerTraceListener.OnClientDisconnectedAsync(CancellationToken)](M_Tessa_Platform_Pipes_PipeServerTraceListener_OnClientDisconnectedAsync.htm))  
[OnExceptionAsync](M_Tessa_Platform_Pipes_PipeDelegateServerTraceListener_OnExceptionAsync.htm)|
Уведомляет о событии возникновения исключения в процессе обработки запроса.  
(Переопределяет [PipeServerTraceListener.OnExceptionAsync(Exception,
CancellationToken)](M_Tessa_Platform_Pipes_PipeServerTraceListener_OnExceptionAsync.htm))  
[OnRequestHandledAsync](M_Tessa_Platform_Pipes_PipeDelegateServerTraceListener_OnRequestHandledAsync.htm)|
Уведомляет о событии окончания обработки запроса, полученного от клиента.
Обработка запроса не завершена с исключением.  
(Переопределяет [PipeServerTraceListener.OnRequestHandledAsync(IPipeRequest,
IPipeResponse,
CancellationToken)](M_Tessa_Platform_Pipes_PipeServerTraceListener_OnRequestHandledAsync.htm))  
[OnRequestReceivedAsync](M_Tessa_Platform_Pipes_PipeDelegateServerTraceListener_OnRequestReceivedAsync.htm)|
Уведомляет о событии получения запроса от клиента.  
(Переопределяет [PipeServerTraceListener.OnRequestReceivedAsync(IPipeRequest,
CancellationToken)](M_Tessa_Platform_Pipes_PipeServerTraceListener_OnRequestReceivedAsync.htm))  
[OnServerShutdownAsync](M_Tessa_Platform_Pipes_PipeDelegateServerTraceListener_OnServerShutdownAsync.htm)|
Уведомляет о событии завершения работы сервера. Выполняется в случаях, если
клиент подключился и затем отключился, а также если сервер завершил работу в
результате невосстановимой ошибки, такой, как ошибка чтения из канала или
записи в канал.  
(Переопределяет
[PipeServerTraceListener.OnServerShutdownAsync(CancellationToken)](M_Tessa_Platform_Pipes_PipeServerTraceListener_OnServerShutdownAsync.htm))  
[OnServerStartupAsync](M_Tessa_Platform_Pipes_PipeDelegateServerTraceListener_OnServerStartupAsync.htm)|
Уведомляет о событии запуска сервера.  
(Переопределяет
[PipeServerTraceListener.OnServerStartupAsync(CancellationToken)](M_Tessa_Platform_Pipes_PipeServerTraceListener_OnServerStartupAsync.htm))  
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
