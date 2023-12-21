# FileSystemSynchronizationStrategy.CreateFileAsync - метод
Создает новый файл с параметрами и содержимым, заданными в content
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task CreateFileAsync(
    	ApplicationPackageFileContent content,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function CreateFileAsync ( 
    	content As ApplicationPackageFileContent,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ CreateFileAsync(
    	ApplicationPackageFileContent^ content, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract CreateFileAsync : 
            content : ApplicationPackageFileContent * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override CreateFileAsync : 
            content : ApplicationPackageFileContent * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
content
[ApplicationPackageFileContent](T_Tessa_Applications_Package_ApplicationPackageFileContent.htm)
     Контент создаваемого файла 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[IApplicationSynchronizationStrategy.CreateFileAsync(ApplicationPackageFileContent,
CancellationToken)](M_Tessa_Applications_Synchronization_IApplicationSynchronizationStrategy_CreateFileAsync.htm)  
##  __См. также
#### Ссылки
[FileSystemSynchronizationStrategy -
](T_Tessa_Applications_Synchronization_FileSystemSynchronizationStrategy.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
