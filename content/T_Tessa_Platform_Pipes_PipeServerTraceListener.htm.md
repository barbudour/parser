# PipeServerTraceListener - класс
Объект, уведомляемый о событиях, происходящих в канале со стороны сервера.
## __Definition
 **Пространство имён:** [Tessa.Platform.Pipes](N_Tessa_Platform_Pipes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class PipeServerTraceListener : IPipeServerTraceListener
VB __Копировать
     Public MustInherit Class PipeServerTraceListener
    	Implements IPipeServerTraceListener
C++ __Копировать
     public ref class PipeServerTraceListener abstract : IPipeServerTraceListener
F# __Копировать
     [<AbstractClassAttribute>]
    type PipeServerTraceListener = 
        class
            interface IPipeServerTraceListener
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ PipeServerTraceListener
Derived
[Tessa.Platform.Pipes.PipeAggregateServerTraceListener](T_Tessa_Platform_Pipes_PipeAggregateServerTraceListener.htm)
[Tessa.Platform.Pipes.PipeDelegateServerTraceListener](T_Tessa_Platform_Pipes_PipeDelegateServerTraceListener.htm)
[Tessa.Platform.Pipes.PipeLoggerServerTraceListener](T_Tessa_Platform_Pipes_PipeLoggerServerTraceListener.htm)
Implements
    [IPipeServerTraceListener](T_Tessa_Platform_Pipes_IPipeServerTraceListener.htm)
##  __Заметки
Наследники класса могут переопределять методы.
## __Конструкторы
[PipeServerTraceListener](M_Tessa_Platform_Pipes_PipeServerTraceListener__ctor.htm)|
Инициализирует новый экземпляр класса PipeServerTraceListener  
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
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[OnClientConnectedAsync](M_Tessa_Platform_Pipes_PipeServerTraceListener_OnClientConnectedAsync.htm)|
Уведомляет о событии подключения клиента к серверу.  
[OnClientDisconnectedAsync](M_Tessa_Platform_Pipes_PipeServerTraceListener_OnClientDisconnectedAsync.htm)|
Уведомляет о событии отключения клиента от сервера.  
[OnExceptionAsync](M_Tessa_Platform_Pipes_PipeServerTraceListener_OnExceptionAsync.htm)|
Уведомляет о событии возникновения исключения в процессе обработки запроса.  
[OnRequestHandledAsync](M_Tessa_Platform_Pipes_PipeServerTraceListener_OnRequestHandledAsync.htm)|
Уведомляет о событии окончания обработки запроса, полученного от клиента.
Обработка запроса не завершена с исключением.  
[OnRequestReceivedAsync](M_Tessa_Platform_Pipes_PipeServerTraceListener_OnRequestReceivedAsync.htm)|
Уведомляет о событии получения запроса от клиента.  
[OnServerShutdownAsync](M_Tessa_Platform_Pipes_PipeServerTraceListener_OnServerShutdownAsync.htm)|
Уведомляет о событии завершения работы сервера. Выполняется в случаях, если
клиент подключился и затем отключился, а также если сервер завершил работу в
результате невосстановимой ошибки, такой, как ошибка чтения из канала или
записи в канал.  
[OnServerStartupAsync](M_Tessa_Platform_Pipes_PipeServerTraceListener_OnServerStartupAsync.htm)|
Уведомляет о событии запуска сервера.  
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
