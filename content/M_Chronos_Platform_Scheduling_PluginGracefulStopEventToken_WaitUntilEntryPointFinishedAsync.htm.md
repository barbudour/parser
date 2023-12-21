# PluginGracefulStopEventToken.WaitUntilEntryPointFinishedAsync - метод
Ожидает, пока метод
[EntryPointAsync(CancellationToken)](M_Chronos_Contracts_IPlugin_EntryPointAsync.htm)
плагина не будет завершён.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Scheduling](N_Chronos_Platform_Scheduling.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public Task WaitUntilEntryPointFinishedAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function WaitUntilEntryPointFinishedAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ WaitUntilEntryPointFinishedAsync(
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract WaitUntilEntryPointFinishedAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override WaitUntilEntryPointFinishedAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[IGracefulStopToken.WaitUntilEntryPointFinishedAsync(CancellationToken)](M_Chronos_Contracts_IGracefulStopToken_WaitUntilEntryPointFinishedAsync.htm)  
##  __Заметки
Метод может быть безопасно вызван после вызова
[Dispose()](M_Chronos_Platform_Scheduling_PluginGracefulStopEventToken_Dispose.htm).
## __См. также
#### Ссылки
[PluginGracefulStopEventToken -
](T_Chronos_Platform_Scheduling_PluginGracefulStopEventToken.htm)
[Chronos.Platform.Scheduling - пространство
имён](N_Chronos_Platform_Scheduling.htm)
