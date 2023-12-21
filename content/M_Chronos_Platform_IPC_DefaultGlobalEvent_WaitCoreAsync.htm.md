# DefaultGlobalEvent.WaitCoreAsync - метод
Выполняет ожидание момента, когда событие перейдёт в сигнальное состояние.
##  __Definition
 **Пространство имён:** [Chronos.Platform.IPC](N_Chronos_Platform_IPC.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     protected override Task WaitCoreAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overrides Function WaitCoreAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     protected:
    virtual Task^ WaitCoreAsync(
    	CancellationToken cancellationToken = CancellationToken()
    ) override
F# __Копировать
     abstract WaitCoreAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override WaitCoreAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
     Токен для отмены ожидания. Укажите CancellationToken.None, чтобы ожидание не требовалось отменять. 
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[DefaultGlobalEvent - ](T_Chronos_Platform_IPC_DefaultGlobalEvent.htm)
[Chronos.Platform.IPC - пространство имён](N_Chronos_Platform_IPC.htm)
