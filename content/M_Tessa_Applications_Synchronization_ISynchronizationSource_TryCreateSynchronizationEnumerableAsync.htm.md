# ISynchronizationSource.TryCreateSynchronizationEnumerableAsync - метод
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
     Task<IApplicationPackageFileEnumerable> TryCreateSynchronizationEnumerableAsync(
    	[CanBeNullAttribute] ApplicationPackage currentState,
    	[NotNullAttribute] IValidationResultBuilder validationResultBuilder,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function TryCreateSynchronizationEnumerableAsync ( 
    	<CanBeNullAttribute> currentState As ApplicationPackage,
    	<NotNullAttribute> validationResultBuilder As IValidationResultBuilder,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of IApplicationPackageFileEnumerable)
C++ __Копировать
    Task<IApplicationPackageFileEnumerable^>^ TryCreateSynchronizationEnumerableAsync(
    	[CanBeNullAttribute] ApplicationPackage^ currentState, 
    	[NotNullAttribute] IValidationResultBuilder^ validationResultBuilder, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract TryCreateSynchronizationEnumerableAsync : 
            [<CanBeNullAttribute>] currentState : ApplicationPackage * 
            [<NotNullAttribute>] validationResultBuilder : IValidationResultBuilder * 
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
## __См. также
#### Ссылки
[ISynchronizationSource -
](T_Tessa_Applications_Synchronization_ISynchronizationSource.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
