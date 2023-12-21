# IPipeClient - интерфейс
Клиент, выполняющий отправку сообщений по каналу.
## __Definition
 **Пространство имён:** [Tessa.Platform.Pipes](N_Tessa_Platform_Pipes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IPipeClient
VB __Копировать
     Public Interface IPipeClient
C++ __Копировать
     public interface class IPipeClient
F# __Копировать
     type IPipeClient = interface end
##  __Методы
[ConnectAsync](M_Tessa_Platform_Pipes_IPipeClient_ConnectAsync.htm)|
Соединяется с сервером в соответствии с настройками подключения и возвращает
объект соединения, для которого вызов [SendAsync(IPipeRequest,
CancellationToken)](M_Tessa_Platform_Pipes_IPipeClientConnection_SendAsync.htm)
отправляет очередное сообщение, а вызов
[DisposeAsync()](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable.disposeasync#system-
iasyncdisposable-disposeasync) закрывает соединение.  
---|---  
## __См. также
#### Ссылки
[Tessa.Platform.Pipes - пространство имён](N_Tessa_Platform_Pipes.htm)
