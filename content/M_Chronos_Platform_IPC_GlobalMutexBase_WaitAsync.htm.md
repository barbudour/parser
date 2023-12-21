# GlobalMutexBase.WaitAsync - метод
Ожидает и получает блокировку на текущий мьютекс. После взятия блокировки её
необходимо освободить методом Release.
## __Definition
 **Пространство имён:** [Chronos.Platform.IPC](N_Chronos_Platform_IPC.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<bool> WaitAsync(
    	int millisecondsTimeout = -1,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function WaitAsync ( 
    	Optional millisecondsTimeout As Integer = -1,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Boolean)
C++ __Копировать
     public:
    virtual Task<bool>^ WaitAsync(
    	int millisecondsTimeout = -1, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract WaitAsync : 
            ?millisecondsTimeout : int * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _millisecondsTimeout = defaultArg millisecondsTimeout -1
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<bool> 
    override WaitAsync : 
            ?millisecondsTimeout : int * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _millisecondsTimeout = defaultArg millisecondsTimeout -1
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<bool> 
#### Параметры
millisecondsTimeout
[Int32](https://learn.microsoft.com/dotnet/api/system.int32) (Optional)
     Таймаут в миллисекундах на ожидание мьютекса. Укажите -1 для ожидания без таймаута. Укажите 0 для быстрой проверки без блокировки. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если блокировка на мьютекс была успешно взята; false в противном случае.
#### Реализации
[IGlobalMutex.WaitAsync(Int32,
CancellationToken)](M_Chronos_Platform_IPC_IGlobalMutex_WaitAsync.htm)  
##  __Исключения
[System.ObjectDisposedException]| Ресурсы, занимаемые объектом, были
освобождены.  
---|---  
##  __См. также
#### Ссылки
[GlobalMutexBase - ](T_Chronos_Platform_IPC_GlobalMutexBase.htm)
[Chronos.Platform.IPC - пространство имён](N_Chronos_Platform_IPC.htm)
[System.ObjectDisposedException]
