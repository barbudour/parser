# Plugin.EntryPointAsync - метод
Асинхронный метод, вызываемый хостом при запуске плагина.
## __Definition
 **Пространство имён:** [Chronos.Contracts](N_Chronos_Contracts.htm)  
 **Сборка:** Chronos.Contracts (в Chronos.Contracts.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract Task EntryPointAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public MustOverride Function EntryPointAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ EntryPointAsync(
    	CancellationToken cancellationToken = CancellationToken()
    ) abstract
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
#### Реализации
[IPlugin.EntryPointAsync(CancellationToken)](M_Chronos_Contracts_IPlugin_EntryPointAsync.htm)  
##  __См. также
#### Ссылки
[Plugin - ](T_Chronos_Contracts_Plugin.htm)
[Chronos.Contracts - пространство имён](N_Chronos_Contracts.htm)
