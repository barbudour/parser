# IPipeClientTraceListener - интерфейс
Объект, уведомляемый о событиях, происходящих в канале со стороны клиента.
## __Definition
 **Пространство имён:** [Tessa.Platform.Pipes](N_Tessa_Platform_Pipes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IPipeClientTraceListener
VB __Копировать
     Public Interface IPipeClientTraceListener
C++ __Копировать
     public interface class IPipeClientTraceListener
F# __Копировать
     type IPipeClientTraceListener = interface end
##  __Методы
[OnClientConnectedAsync](M_Tessa_Platform_Pipes_IPipeClientTraceListener_OnClientConnectedAsync.htm)|
Уведомляет о событии установки соединения с сервером.  
---|---  
[OnClientDisconnectedAsync](M_Tessa_Platform_Pipes_IPipeClientTraceListener_OnClientDisconnectedAsync.htm)|
Уведомляет о событии закрытия соединения с сервером.  
[OnExceptionAsync](M_Tessa_Platform_Pipes_IPipeClientTraceListener_OnExceptionAsync.htm)|
Уведомляет о событии возникновения исключения при обработке запроса.
Исключение от сервера приходит как
[ValidationException](T_Tessa_Platform_Validation_ValidationException.htm).  
[OnRequestPreparedAsync](M_Tessa_Platform_Pipes_IPipeClientTraceListener_OnRequestPreparedAsync.htm)|
Уведомляет о событии подготовки запроса к отправке на сервер.  
[OnResponseReceivedAsync](M_Tessa_Platform_Pipes_IPipeClientTraceListener_OnResponseReceivedAsync.htm)|
Уведомляет о событии получения ответа на запрос от сервера. Ответ на запрос не
является исключением.  
## __См. также
#### Ссылки
[Tessa.Platform.Pipes - пространство имён](N_Tessa_Platform_Pipes.htm)
