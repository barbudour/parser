# FileSystemSynchronizationStrategy.OnSynchronizationCompletedAsync - метод
Вызывается при завершении синхронизации элементов
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task OnSynchronizationCompletedAsync(
    	ApplicationPackage applicationPackage,
    	ValidationResultBuilder validationResultBuilder,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function OnSynchronizationCompletedAsync ( 
    	applicationPackage As ApplicationPackage,
    	validationResultBuilder As ValidationResultBuilder,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ OnSynchronizationCompletedAsync(
    	ApplicationPackage^ applicationPackage, 
    	ValidationResultBuilder^ validationResultBuilder, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract OnSynchronizationCompletedAsync : 
            applicationPackage : ApplicationPackage * 
            validationResultBuilder : ValidationResultBuilder * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override OnSynchronizationCompletedAsync : 
            applicationPackage : ApplicationPackage * 
            validationResultBuilder : ValidationResultBuilder * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
applicationPackage
[ApplicationPackage](T_Tessa_Applications_Package_ApplicationPackage.htm)
     Пакет приложения 
validationResultBuilder
[ValidationResultBuilder](T_Tessa_Platform_Validation_ValidationResultBuilder.htm)
     Построитель результатов валидации 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[IApplicationSynchronizationStrategy.OnSynchronizationCompletedAsync(ApplicationPackage,
ValidationResultBuilder,
CancellationToken)](M_Tessa_Applications_Synchronization_IApplicationSynchronizationStrategy_OnSynchronizationCompletedAsync.htm)  
##  __Исключения
[UnauthorizedAccessException](https://learn.microsoft.com/dotnet/api/system.unauthorizedaccessexception)|
The caller does not have the required permission.-or- path specified a file
that is read-only.  
---|---  
[DirectoryNotFoundException](https://learn.microsoft.com/dotnet/api/system.io.directorynotfoundexception)|
The specified path is invalid (for example, it is on an unmapped drive).  
[IOException](https://learn.microsoft.com/dotnet/api/system.io.ioexception)|
An I/O error occurred while creating the file.  
[ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception)|
path is a zero-length string, contains only white space, or contains one or
more invalid characters as defined by
[InvalidPathChars](https://learn.microsoft.com/dotnet/api/system.io.path.invalidpathchars).  
[ArgumentNullException](https://learn.microsoft.com/dotnet/api/system.argumentnullexception)|
path is null.  
[PathTooLongException](https://learn.microsoft.com/dotnet/api/system.io.pathtoolongexception)|
The specified path, file name, or both exceed the system-defined maximum
length. For example, on Windows-based platforms, paths must be less than 248
characters, and file names must be less than 260 characters.  
[NotSupportedException](https://learn.microsoft.com/dotnet/api/system.notsupportedexception)|
path is in an invalid format.  
## __См. также
#### Ссылки
[FileSystemSynchronizationStrategy -
](T_Tessa_Applications_Synchronization_FileSystemSynchronizationStrategy.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
