# LinuxGlobalMutex.WaitCoreAsync - метод
Ожидает и получает блокировку на текущий мьютекс. После взятия блокировки её
необходимо освободить методом Release.
## __Definition
 **Пространство имён:** [Chronos.Platform.IPC](N_Chronos_Platform_IPC.htm)  
 **Сборка:** Chronos.Platform.Linux (в Chronos.Platform.Linux.dll) Версия:
3.6.0.17
C# __Копировать
     protected override Task<bool> WaitCoreAsync(
    	int millisecondsTimeout,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overrides Function WaitCoreAsync ( 
    	millisecondsTimeout As Integer,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Boolean)
C++ __Копировать
     protected:
    virtual Task<bool>^ WaitCoreAsync(
    	int millisecondsTimeout, 
    	CancellationToken cancellationToken = CancellationToken()
    ) override
F# __Копировать
     abstract WaitCoreAsync : 
            millisecondsTimeout : int * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<bool> 
    override WaitCoreAsync : 
            millisecondsTimeout : int * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<bool> 
#### Параметры
millisecondsTimeout
[Int32](https://learn.microsoft.com/dotnet/api/system.int32)
     Таймаут в миллисекундах на ожидание мьютекса. Укажите -1 для ожидания без таймаута. Укажите 0 для быстрой проверки без блокировки. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если блокировка на мьютекс была успешно взята; false в противном случае.
## __См. также
#### Ссылки
[LinuxGlobalMutex - ](T_Chronos_Platform_IPC_LinuxGlobalMutex.htm)
[Chronos.Platform.IPC - пространство имён](N_Chronos_Platform_IPC.htm)
