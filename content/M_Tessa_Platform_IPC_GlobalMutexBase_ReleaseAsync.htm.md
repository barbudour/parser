# GlobalMutexBase.ReleaseAsync - метод
Освобождает блокировку на текущий мьютекс. Не выполняет действий, если
блокировка не была взята.
## __Definition
 **Пространство имён:** [Tessa.Platform.IPC](N_Tessa_Platform_IPC.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask ReleaseAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function ReleaseAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask
C++ __Копировать
     public:
    virtual ValueTask ReleaseAsync(
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract ReleaseAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
    override ReleaseAsync : 
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
[IGlobalMutex.ReleaseAsync(CancellationToken)](M_Tessa_Platform_IPC_IGlobalMutex_ReleaseAsync.htm)  
##  __Исключения
[System.ObjectDisposedException]| Ресурсы, занимаемые объектом, были
освобождены.  
---|---  
##  __См. также
#### Ссылки
[GlobalMutexBase - ](T_Tessa_Platform_IPC_GlobalMutexBase.htm)
[Tessa.Platform.IPC - пространство имён](N_Tessa_Platform_IPC.htm)
[System.ObjectDisposedException]
