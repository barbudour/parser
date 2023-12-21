# IGlobalEvent - интерфейс
Событие с глобально уникальным именем, используемое для синхронизации между
процессами.
## __Definition
 **Пространство имён:** [Tessa.Platform.IPC](N_Tessa_Platform_IPC.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IGlobalEvent : IAsyncDisposable
VB __Копировать
     Public Interface IGlobalEvent
    	Inherits IAsyncDisposable
C++ __Копировать
     public interface class IGlobalEvent : IAsyncDisposable
F# __Копировать
     type IGlobalEvent = 
        interface
            interface IAsyncDisposable
        end
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable)
##  __Методы
[CleanAsync](M_Tessa_Platform_IPC_IGlobalEvent_CleanAsync.htm)|  Освобождает
ресурсы события, делая невозможным его дальнейшее использование, и удаляет
связанный с ним файл при его наличии. В реализации по умолчанию выполняет
работу по очистке на Linux и игнорируется на Windows.  
---|---  
[CloseFromMainProcessAsync](M_Tessa_Platform_IPC_IGlobalEvent_CloseFromMainProcessAsync.htm)|
Выполняет глобальное закрытие всех ресурсов, связанных с событием. Процессы,
выполняющие ожидание события, могут прекратить ожидание, но на это поведение
нельзя опираться. Рекомендуется не вызывать этот метод, если нельзя определить
текущий процесс как единственный процесс, переводящий событие в сигнальное
состояние. Метод актуален для глобальных событий на Linux.  
[DisposeAsync](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable.disposeasync#system-
iasyncdisposable-disposeasync)| Performs application-defined tasks associated
with freeing, releasing, or resetting unmanaged resources asynchronously.  
(Унаследован от
[IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable))  
[Reset](M_Tessa_Platform_IPC_IGlobalEvent_Reset.htm)|  Переводит событие в
несигнальное состояние, при этом все ожидающие событие подписчики получают
управление.  
[Set](M_Tessa_Platform_IPC_IGlobalEvent_Set.htm)|  Переводит событие в
сигнальное состояние, при этом все ожидающие событие подписчики получают
управление.  
[TryGetWaitHandle](M_Tessa_Platform_IPC_IGlobalEvent_TryGetWaitHandle.htm)|
Возвращает объект WaitHandle для ожидания сигнального состояния у события, или
null, если используемый объект синхронизации не предоставляет объекта
WaitHandle и требуется вызвать метод Wait для ожидания.  
[WaitAsync](M_Tessa_Platform_IPC_IGlobalEvent_WaitAsync.htm)| Выполняет
ожидание момента, когда событие перейдёт в сигнальное состояние.  
##  __См. также
#### Ссылки
[Tessa.Platform.IPC - пространство имён](N_Tessa_Platform_IPC.htm)
