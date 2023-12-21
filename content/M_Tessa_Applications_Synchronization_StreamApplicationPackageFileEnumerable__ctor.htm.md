# StreamApplicationPackageFileEnumerable - конструктор
Инициализирует новый экземпляр класса
[StreamApplicationPackageFileEnumerable](T_Tessa_Applications_Synchronization_StreamApplicationPackageFileEnumerable.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public StreamApplicationPackageFileEnumerable(
    	[NotNullAttribute] Stream sourceStream,
    	ApplicationDownloadFlags readerFlags = ApplicationDownloadFlags.None,
    	[CanBeNullAttribute] Func<Guid, CancellationToken, Task<ValidationResult>> tryGetFaultedResultFuncAsync = null
    )
VB __Копировать
     Public Sub New ( 
    	<NotNullAttribute> sourceStream As Stream,
    	Optional readerFlags As ApplicationDownloadFlags = ApplicationDownloadFlags.None,
    	<CanBeNullAttribute> Optional tryGetFaultedResultFuncAsync As Func(Of Guid, CancellationToken, Task(Of ValidationResult)) = Nothing
    )
C++ __Копировать
     public:
    StreamApplicationPackageFileEnumerable(
    	[NotNullAttribute] Stream^ sourceStream, 
    	ApplicationDownloadFlags readerFlags = ApplicationDownloadFlags::None, 
    	[CanBeNullAttribute] Func<Guid, CancellationToken, Task<ValidationResult^>^>^ tryGetFaultedResultFuncAsync = nullptr
    )
F# __Копировать
     new : 
            [<NotNullAttribute>] sourceStream : Stream * 
            ?readerFlags : ApplicationDownloadFlags * 
            [<CanBeNullAttribute>] ?tryGetFaultedResultFuncAsync : Func<Guid, CancellationToken, Task<ValidationResult>> 
    (* Defaults:
            let _readerFlags = defaultArg readerFlags ApplicationDownloadFlags.None
            let _tryGetFaultedResultFuncAsync = defaultArg tryGetFaultedResultFuncAsync null
    *)
    -> StreamApplicationPackageFileEnumerable
#### Параметры
sourceStream [Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)
readerFlags
[ApplicationDownloadFlags](T_Tessa_Applications_Services_TessaServer_ApplicationDownloadFlags.htm)
(Optional)
tryGetFaultedResultFuncAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-3)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid),
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm)>>
(Optional)
## __См. также
#### Ссылки
[StreamApplicationPackageFileEnumerable -
](T_Tessa_Applications_Synchronization_StreamApplicationPackageFileEnumerable.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
