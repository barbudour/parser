# GlobalEventBase.CloseFromMainProcessAsync - метод
Выполняет глобальное закрытие всех ресурсов, связанных с событием. Процессы,
выполняющие ожидание события, могут прекратить ожидание, но на это поведение
нельзя опираться. Рекомендуется не вызывать этот метод, если нельзя определить
текущий процесс как единственный процесс, переводящий событие в сигнальное
состояние. Метод актуален для глобальных событий на Linux.
## __Definition
 **Пространство имён:** [Chronos.Platform.IPC](N_Chronos_Platform_IPC.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask CloseFromMainProcessAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function CloseFromMainProcessAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask
C++ __Копировать
     public:
    virtual ValueTask CloseFromMainProcessAsync(
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract CloseFromMainProcessAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
    override CloseFromMainProcessAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)  
Асинхронная задача.
#### Реализации
[IGlobalEvent.CloseFromMainProcessAsync(CancellationToken)](M_Chronos_Platform_IPC_IGlobalEvent_CloseFromMainProcessAsync.htm)  
##  __Исключения
[System.ObjectDisposedException]| Ресурсы, занимаемые объектом, были
освобождены.  
---|---  
##  __См. также
#### Ссылки
[GlobalEventBase - ](T_Chronos_Platform_IPC_GlobalEventBase.htm)
[Chronos.Platform.IPC - пространство имён](N_Chronos_Platform_IPC.htm)
[System.ObjectDisposedException]
