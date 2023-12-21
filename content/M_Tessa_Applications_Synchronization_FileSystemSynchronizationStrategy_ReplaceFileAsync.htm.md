# FileSystemSynchronizationStrategy.ReplaceFileAsync - метод
Заменяет файл с параметрами и содержимым, заданными в content
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task ReplaceFileAsync(
    	ApplicationPackageFileContent content,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function ReplaceFileAsync ( 
    	content As ApplicationPackageFileContent,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ ReplaceFileAsync(
    	ApplicationPackageFileContent^ content, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract ReplaceFileAsync : 
            content : ApplicationPackageFileContent * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override ReplaceFileAsync : 
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
[IApplicationSynchronizationStrategy.ReplaceFileAsync(ApplicationPackageFileContent,
CancellationToken)](M_Tessa_Applications_Synchronization_IApplicationSynchronizationStrategy_ReplaceFileAsync.htm)  
##  __См. также
#### Ссылки
[FileSystemSynchronizationStrategy -
](T_Tessa_Applications_Synchronization_FileSystemSynchronizationStrategy.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
