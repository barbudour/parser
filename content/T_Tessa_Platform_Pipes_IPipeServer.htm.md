# IPipeServer - интерфейс
Сервер, выполняющий обработку сообщений, полученных по каналу.
## __Definition
 **Пространство имён:** [Tessa.Platform.Pipes](N_Tessa_Platform_Pipes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IPipeServer
VB __Копировать
     Public Interface IPipeServer
C++ __Копировать
     public interface class IPipeServer
F# __Копировать
     type IPipeServer = interface end
##  __Методы
[ListenAsync](M_Tessa_Platform_Pipes_IPipeServer_ListenAsync.htm)|  Выполняет
открытие канала, по которому объект получает сообщения от единственного
клиента и обрабатывает их посредством переданного объекта router.
Прослушивание завершается, если клиент отключился от канала или операция была
отменена посредством токена cancellationToken. Один вызванный метод
обслуживает ровно одного клиента, если требуется обслуживать несколько
клиентов, то надо запустить несколько асинхронных задач Task.Run, в каждом из
которых будет вызван свой метод прослушивания, после завершения которого он
вызывается ещё раз.  
---|---  
## __См. также
#### Ссылки
[Tessa.Platform.Pipes - пространство имён](N_Tessa_Platform_Pipes.htm)
