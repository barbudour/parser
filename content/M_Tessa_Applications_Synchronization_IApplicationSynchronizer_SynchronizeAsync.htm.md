# IApplicationSynchronizer.SynchronizeAsync - метод
Осуществляет синхронизацию файлов между источником source и целевым объектом
target в окружении ambientContextFactoryAsync.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    Task<ValidationResult> SynchronizeAsync(
    	[NotNullAttribute] Func<CancellationToken, ValueTask<IAsyncDisposable>> ambientContextFactoryAsync,
    	[NotNullAttribute] ISynchronizationSource source,
    	[NotNullAttribute] ISynchronizationTarget target,
    	[NotNullAttribute] IInstallationProcessMonitor monitor,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
    <NotNullAttribute>
    Function SynchronizeAsync ( 
    	<NotNullAttribute> ambientContextFactoryAsync As Func(Of CancellationToken, ValueTask(Of IAsyncDisposable)),
    	<NotNullAttribute> source As ISynchronizationSource,
    	<NotNullAttribute> target As ISynchronizationTarget,
    	<NotNullAttribute> monitor As IInstallationProcessMonitor,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of ValidationResult)
C++ __Копировать
    [NotNullAttribute]
    Task<ValidationResult^>^ SynchronizeAsync(
    	[NotNullAttribute] Func<CancellationToken, ValueTask<IAsyncDisposable^>>^ ambientContextFactoryAsync, 
    	[NotNullAttribute] ISynchronizationSource^ source, 
    	[NotNullAttribute] ISynchronizationTarget^ target, 
    	[NotNullAttribute] IInstallationProcessMonitor^ monitor, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     [<NotNullAttribute>]
    abstract SynchronizeAsync : 
            [<NotNullAttribute>] ambientContextFactoryAsync : Func<CancellationToken, ValueTask<IAsyncDisposable>> * 
            [<NotNullAttribute>] source : ISynchronizationSource * 
            [<NotNullAttribute>] target : ISynchronizationTarget * 
            [<NotNullAttribute>] monitor : IInstallationProcessMonitor * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValidationResult> 
#### Параметры
ambientContextFactoryAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable)>>
     Функция возвращающая контекст выполнения синхронизации 
source
[ISynchronizationSource](T_Tessa_Applications_Synchronization_ISynchronizationSource.htm)
     Источник синхронизируемых файлов 
target
[ISynchronizationTarget](T_Tessa_Applications_Synchronization_ISynchronizationTarget.htm)
     Целевой объект синхронизации 
monitor
[IInstallationProcessMonitor](T_Tessa_Applications_Synchronization_IInstallationProcessMonitor.htm)
     Мониторинг процесса синхронизации 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm)>  
Результаты процесса синхронизации файлов
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm).
## __См. также
#### Ссылки
[IApplicationSynchronizer -
](T_Tessa_Applications_Synchronization_IApplicationSynchronizer.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
