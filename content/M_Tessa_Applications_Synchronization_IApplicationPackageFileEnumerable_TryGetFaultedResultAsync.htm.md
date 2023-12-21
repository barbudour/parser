# IApplicationPackageFileEnumerable.TryGetFaultedResultAsync - метод
Возвращает ошибки при загрузке приложения. Метод может выполнить запрос к
серверу. Результат не равен null, но может быть пустым
[Empty](P_Tessa_Platform_Validation_ValidationResult_Empty.htm).
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    Task<ValidationResult> TryGetFaultedResultAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
    <NotNullAttribute>
    Function TryGetFaultedResultAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of ValidationResult)
C++ __Копировать
    [NotNullAttribute]
    Task<ValidationResult^>^ TryGetFaultedResultAsync(
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     [<NotNullAttribute>]
    abstract TryGetFaultedResultAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValidationResult> 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm)>  
Ошибки при загрузке приложения.
##  __См. также
#### Ссылки
[IApplicationPackageFileEnumerable -
](T_Tessa_Applications_Synchronization_IApplicationPackageFileEnumerable.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
