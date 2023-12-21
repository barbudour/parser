# FileSystemSynchronizationSource.TryCreateSynchronizationEnumerableAsync -
метод
Осуществляет попытку создания перечислителя файлов необходимых для
синхронизации элементов между файлами находящимися в источнике и текущем
состоянии пакета приложения находящегося в состоянии currentState. В случае
если не при создании произошли ошибки, то ошибки помещаются в
validationResultBuilder, и возвращается null
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<IApplicationPackageFileEnumerable> TryCreateSynchronizationEnumerableAsync(
    	ApplicationPackage currentState,
    	IValidationResultBuilder validationResultBuilder,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function TryCreateSynchronizationEnumerableAsync ( 
    	currentState As ApplicationPackage,
    	validationResultBuilder As IValidationResultBuilder,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of IApplicationPackageFileEnumerable)
C++ __Копировать
     public:
    virtual Task<IApplicationPackageFileEnumerable^>^ TryCreateSynchronizationEnumerableAsync(
    	ApplicationPackage^ currentState, 
    	IValidationResultBuilder^ validationResultBuilder, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract TryCreateSynchronizationEnumerableAsync : 
            currentState : ApplicationPackage * 
            validationResultBuilder : IValidationResultBuilder * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<IApplicationPackageFileEnumerable> 
    override TryCreateSynchronizationEnumerableAsync : 
            currentState : ApplicationPackage * 
            validationResultBuilder : IValidationResultBuilder * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<IApplicationPackageFileEnumerable> 
#### Параметры
currentState
[ApplicationPackage](T_Tessa_Applications_Package_ApplicationPackage.htm)
     Текущее состояние пакета приложения 
validationResultBuilder
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
     Построитель результатов валидации 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[IApplicationPackageFileEnumerable](T_Tessa_Applications_Synchronization_IApplicationPackageFileEnumerable.htm)>  
Перечислитель файлов
#### Реализации
[ISynchronizationSource.TryCreateSynchronizationEnumerableAsync(ApplicationPackage,
IValidationResultBuilder,
CancellationToken)](M_Tessa_Applications_Synchronization_ISynchronizationSource_TryCreateSynchronizationEnumerableAsync.htm)  
##  __См. также
#### Ссылки
[FileSystemSynchronizationSource -
](T_Tessa_Applications_Synchronization_FileSystemSynchronizationSource.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
