# GlobalMutexBase.WaitCoreAsync - метод
Ожидает и получает блокировку на текущий мьютекс. После взятия блокировки её
необходимо освободить методом Release.
## __Definition
 **Пространство имён:** [Tessa.Platform.IPC](N_Tessa_Platform_IPC.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected abstract Task<bool> WaitCoreAsync(
    	int millisecondsTimeout,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected MustOverride Function WaitCoreAsync ( 
    	millisecondsTimeout As Integer,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Boolean)
C++ __Копировать
     protected:
    virtual Task<bool>^ WaitCoreAsync(
    	int millisecondsTimeout, 
    	CancellationToken cancellationToken = CancellationToken()
    ) abstract
F# __Копировать
     abstract WaitCoreAsync : 
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
[GlobalMutexBase - ](T_Tessa_Platform_IPC_GlobalMutexBase.htm)
[Tessa.Platform.IPC - пространство имён](N_Tessa_Platform_IPC.htm)
