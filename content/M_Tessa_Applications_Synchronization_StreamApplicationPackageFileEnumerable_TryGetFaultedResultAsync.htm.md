# StreamApplicationPackageFileEnumerable.TryGetFaultedResultAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<ValidationResult> TryGetFaultedResultAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function TryGetFaultedResultAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of ValidationResult)
C++ __Копировать
     public:
    virtual Task<ValidationResult^>^ TryGetFaultedResultAsync(
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract TryGetFaultedResultAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValidationResult> 
    override TryGetFaultedResultAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValidationResult> 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm)>
#### Реализации
[IApplicationPackageFileEnumerable.TryGetFaultedResultAsync(CancellationToken)](M_Tessa_Applications_Synchronization_IApplicationPackageFileEnumerable_TryGetFaultedResultAsync.htm)  
##  __См. также
#### Ссылки
[StreamApplicationPackageFileEnumerable -
](T_Tessa_Applications_Synchronization_StreamApplicationPackageFileEnumerable.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
