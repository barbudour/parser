# FileSourceForCard.CreateVersionCoreAsync - метод
Создаёт версию для файла по заданному токену.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected override ValueTask<IFileVersion> CreateVersionCoreAsync(
    	IFileVersionCreationToken token,
    	IFile file,
    	IFileContent content = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overrides Function CreateVersionCoreAsync ( 
    	token As IFileVersionCreationToken,
    	file As IFile,
    	Optional content As IFileContent = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of IFileVersion)
C++ __Копировать
     protected:
    virtual ValueTask<IFileVersion^> CreateVersionCoreAsync(
    	IFileVersionCreationToken^ token, 
    	IFile^ file, 
    	IFileContent^ content = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    ) override
F# __Копировать
     abstract CreateVersionCoreAsync : 
            token : IFileVersionCreationToken * 
            file : IFile * 
            ?content : IFileContent * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _content = defaultArg content null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IFileVersion> 
    override CreateVersionCoreAsync : 
            token : IFileVersionCreationToken * 
            file : IFile * 
            ?content : IFileContent * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _content = defaultArg content null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IFileVersion> 
#### Параметры
token [IFileVersionCreationToken](T_Tessa_Files_IFileVersionCreationToken.htm)
    Токен, по которому создаётся версия файла.
file [IFile](T_Tessa_Files_IFile.htm)
    Файл, для которого создаётся версия.
content [IFileContent](T_Tessa_Files_IFileContent.htm) (Optional)
     Контент версии файла или null, если для версии создаётся отдельный объект контента. Рекомендуется использовать значение null во всех случаях, кроме таких, в которых создаваемая версия должна использовать уже созданный контент. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[IFileVersion](T_Tessa_Files_IFileVersion.htm)>  
Созданная версия файла.
##  __См. также
#### Ссылки
[FileSourceForCard - ](T_Tessa_Cards_FileSourceForCard.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
