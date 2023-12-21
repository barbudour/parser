# IPipeServerTraceListener - интерфейс
Объект, уведомляемый о событиях, происходящих в канале со стороны сервера.
## __Definition
 **Пространство имён:** [Tessa.Platform.Pipes](N_Tessa_Platform_Pipes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IPipeServerTraceListener
VB __Копировать
     Public Interface IPipeServerTraceListener
C++ __Копировать
     public interface class IPipeServerTraceListener
F# __Копировать
     type IPipeServerTraceListener = interface end
##  __Методы
[OnClientConnectedAsync](M_Tessa_Platform_Pipes_IPipeServerTraceListener_OnClientConnectedAsync.htm)|
Уведомляет о событии подключения клиента к серверу.  
---|---  
[OnClientDisconnectedAsync](M_Tessa_Platform_Pipes_IPipeServerTraceListener_OnClientDisconnectedAsync.htm)|
Уведомляет о событии отключения клиента от сервера.  
[OnExceptionAsync](M_Tessa_Platform_Pipes_IPipeServerTraceListener_OnExceptionAsync.htm)|
Уведомляет о событии возникновения исключения в процессе обработки запроса.  
[OnRequestHandledAsync](M_Tessa_Platform_Pipes_IPipeServerTraceListener_OnRequestHandledAsync.htm)|
Уведомляет о событии окончания обработки запроса, полученного от клиента.
Обработка запроса не завершена с исключением.  
[OnRequestReceivedAsync](M_Tessa_Platform_Pipes_IPipeServerTraceListener_OnRequestReceivedAsync.htm)|
Уведомляет о событии получения запроса от клиента.  
[OnServerShutdownAsync](M_Tessa_Platform_Pipes_IPipeServerTraceListener_OnServerShutdownAsync.htm)|
Уведомляет о событии завершения работы сервера. Выполняется в случаях, если
клиент подключился и затем отключился, а также если сервер завершил работу в
результате невосстановимой ошибки, такой, как ошибка чтения из канала или
записи в канал.  
[OnServerStartupAsync](M_Tessa_Platform_Pipes_IPipeServerTraceListener_OnServerStartupAsync.htm)|
Уведомляет о событии запуска сервера.  
## __См. также
#### Ссылки
[Tessa.Platform.Pipes - пространство имён](N_Tessa_Platform_Pipes.htm)
