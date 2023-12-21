# FileModifyTokenActionAsync - делегат
Метод, выполняющий изменение файла и его версии перед созданием.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public delegate Task FileModifyTokenActionAsync(
    	IFileCreationToken fileToken,
    	IFileVersionCreationToken versionToken,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Delegate Function FileModifyTokenActionAsync ( 
    	fileToken As IFileCreationToken,
    	versionToken As IFileVersionCreationToken,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public delegate Task^ FileModifyTokenActionAsync(
    	IFileCreationToken^ fileToken, 
    	IFileVersionCreationToken^ versionToken, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     type FileModifyTokenActionAsync = 
        delegate of 
            fileToken : IFileCreationToken * 
            versionToken : IFileVersionCreationToken * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task
#### Параметры
fileToken [IFileCreationToken](T_Tessa_Files_IFileCreationToken.htm)
    Токен с параметрами создаваемого файла.
versionToken
[IFileVersionCreationToken](T_Tessa_Files_IFileVersionCreationToken.htm)
    Токен с параметрами создаваемой версии файла.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
