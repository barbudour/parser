# IApplicationSynchronizationStrategy.CreateFileAsync - метод
Создает новый файл с параметрами и содержимым, заданными в content
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task CreateFileAsync(
    	[NotNullAttribute] ApplicationPackageFileContent content,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function CreateFileAsync ( 
    	<NotNullAttribute> content As ApplicationPackageFileContent,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
    Task^ CreateFileAsync(
    	[NotNullAttribute] ApplicationPackageFileContent^ content, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract CreateFileAsync : 
            [<NotNullAttribute>] content : ApplicationPackageFileContent * 
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
##  __См. также
#### Ссылки
[IApplicationSynchronizationStrategy -
](T_Tessa_Applications_Synchronization_IApplicationSynchronizationStrategy.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
