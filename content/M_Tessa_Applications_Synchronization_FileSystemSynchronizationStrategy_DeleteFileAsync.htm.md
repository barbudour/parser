# FileSystemSynchronizationStrategy.DeleteFileAsync - метод
Удаляет файл заданный в file
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task DeleteFileAsync(
    	ApplicationPackageFile file,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function DeleteFileAsync ( 
    	file As ApplicationPackageFile,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ DeleteFileAsync(
    	ApplicationPackageFile^ file, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract DeleteFileAsync : 
            file : ApplicationPackageFile * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override DeleteFileAsync : 
            file : ApplicationPackageFile * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
file
[ApplicationPackageFile](T_Tessa_Applications_Package_ApplicationPackageFile.htm)
     Описание удаляемого файла 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[IApplicationSynchronizationStrategy.DeleteFileAsync(ApplicationPackageFile,
CancellationToken)](M_Tessa_Applications_Synchronization_IApplicationSynchronizationStrategy_DeleteFileAsync.htm)  
##  __См. также
#### Ссылки
[FileSystemSynchronizationStrategy -
](T_Tessa_Applications_Synchronization_FileSystemSynchronizationStrategy.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
