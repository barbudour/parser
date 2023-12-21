# IPlugin.EntryPointAsync - метод
Асинхронный метод, вызываемый хостом при запуске плагина.
## __Definition
 **Пространство имён:** [Chronos.Contracts](N_Chronos_Contracts.htm)  
 **Сборка:** Chronos.Contracts (в Chronos.Contracts.dll) Версия: 3.6.0.17
C# __Копировать
     Task EntryPointAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function EntryPointAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
    Task^ EntryPointAsync(
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract EntryPointAsync : 
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
Асинхронная задача, завершаемая при завершении плагина.
##  __См. также
#### Ссылки
[IPlugin - ](T_Chronos_Contracts_IPlugin.htm)
[Chronos.Contracts - пространство имён](N_Chronos_Contracts.htm)
