# ApplicationSynchronizer.SynchronizeAsync - метод
Осуществляет синхронизацию файлов между источником source и целевым объектом
target в окружении ambientContextFactoryAsync.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<ValidationResult> SynchronizeAsync(
    	Func<CancellationToken, ValueTask<IAsyncDisposable>> ambientContextFactoryAsync,
    	ISynchronizationSource source,
    	ISynchronizationTarget target,
    	IInstallationProcessMonitor monitor,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function SynchronizeAsync ( 
    	ambientContextFactoryAsync As Func(Of CancellationToken, ValueTask(Of IAsyncDisposable)),
    	source As ISynchronizationSource,
    	target As ISynchronizationTarget,
    	monitor As IInstallationProcessMonitor,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of ValidationResult)
C++ __Копировать
     public:
    virtual Task<ValidationResult^>^ SynchronizeAsync(
    	Func<CancellationToken, ValueTask<IAsyncDisposable^>>^ ambientContextFactoryAsync, 
    	ISynchronizationSource^ source, 
    	ISynchronizationTarget^ target, 
    	IInstallationProcessMonitor^ monitor, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract SynchronizeAsync : 
            ambientContextFactoryAsync : Func<CancellationToken, ValueTask<IAsyncDisposable>> * 
            source : ISynchronizationSource * 
            target : ISynchronizationTarget * 
            monitor : IInstallationProcessMonitor * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValidationResult> 
    override SynchronizeAsync : 
            ambientContextFactoryAsync : Func<CancellationToken, ValueTask<IAsyncDisposable>> * 
            source : ISynchronizationSource * 
            target : ISynchronizationTarget * 
            monitor : IInstallationProcessMonitor * 
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
#### Реализации
[IApplicationSynchronizer.SynchronizeAsync(Func<CancellationToken,
ValueTask<IAsyncDisposable>>, ISynchronizationSource, ISynchronizationTarget,
IInstallationProcessMonitor,
CancellationToken)](M_Tessa_Applications_Synchronization_IApplicationSynchronizer_SynchronizeAsync.htm)  
##  __См. также
#### Ссылки
[ApplicationSynchronizer -
](T_Tessa_Applications_Synchronization_ApplicationSynchronizer.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
