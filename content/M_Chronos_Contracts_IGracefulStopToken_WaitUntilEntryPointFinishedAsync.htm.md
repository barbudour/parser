# IGracefulStopToken.WaitUntilEntryPointFinishedAsync - метод
Ожидает, пока метод
[EntryPointAsync(CancellationToken)](M_Chronos_Contracts_IPlugin_EntryPointAsync.htm)
плагина не будет завершён.
## __Definition
 **Пространство имён:** [Chronos.Contracts](N_Chronos_Contracts.htm)  
 **Сборка:** Chronos.Contracts (в Chronos.Contracts.dll) Версия: 3.6.0.17
C# __Копировать
     Task WaitUntilEntryPointFinishedAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function WaitUntilEntryPointFinishedAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
    Task^ WaitUntilEntryPointFinishedAsync(
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract WaitUntilEntryPointFinishedAsync : 
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
##  __См. также
#### Ссылки
[IGracefulStopToken - ](T_Chronos_Contracts_IGracefulStopToken.htm)
[Chronos.Contracts - пространство имён](N_Chronos_Contracts.htm)
