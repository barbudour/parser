# ApplicationLaunchingStrategy.UpdateApplicationAsync - метод
Осуществляет обновление приложения
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<bool> UpdateApplicationAsync(
    	IInstallationProcessMonitor monitor,
    	bool client64Bit,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function UpdateApplicationAsync ( 
    	monitor As IInstallationProcessMonitor,
    	client64Bit As Boolean,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Boolean)
C++ __Копировать
     public:
    virtual Task<bool>^ UpdateApplicationAsync(
    	IInstallationProcessMonitor^ monitor, 
    	bool client64Bit, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract UpdateApplicationAsync : 
            monitor : IInstallationProcessMonitor * 
            client64Bit : bool * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<bool> 
    override UpdateApplicationAsync : 
            monitor : IInstallationProcessMonitor * 
            client64Bit : bool * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<bool> 
#### Параметры
monitor
[IInstallationProcessMonitor](T_Tessa_Applications_Synchronization_IInstallationProcessMonitor.htm)
     Монитор процесса установки приложения 
client64Bit [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
     Признак того, что разрядность обновляемого приложения должна быть 64-битной. Может отличаться от разрядности приложения перед обновлением. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если приложение успешно обновлено; false в противном случае.
#### Реализации
[IApplicationLaunchingStrategy.UpdateApplicationAsync(IInstallationProcessMonitor,
Boolean,
CancellationToken)](M_Tessa_Applications_IApplicationLaunchingStrategy_UpdateApplicationAsync.htm)  
##  __См. также
#### Ссылки
[ApplicationLaunchingStrategy -
](T_Tessa_Applications_ApplicationLaunchingStrategy.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
