# IApplicationLaunchingStrategy.UpdateApplicationAsync - метод
Осуществляет обновление приложения
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task<bool> UpdateApplicationAsync(
    	[NotNullAttribute] IInstallationProcessMonitor monitor,
    	bool client64Bit,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function UpdateApplicationAsync ( 
    	<NotNullAttribute> monitor As IInstallationProcessMonitor,
    	client64Bit As Boolean,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Boolean)
C++ __Копировать
    Task<bool>^ UpdateApplicationAsync(
    	[NotNullAttribute] IInstallationProcessMonitor^ monitor, 
    	bool client64Bit, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract UpdateApplicationAsync : 
            [<NotNullAttribute>] monitor : IInstallationProcessMonitor * 
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
## __См. также
#### Ссылки
[IApplicationLaunchingStrategy -
](T_Tessa_Applications_IApplicationLaunchingStrategy.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
