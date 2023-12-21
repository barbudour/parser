# FileSourceForCard.CreateFileCoreAsync - метод
Создаёт файл по заданному токену.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected override ValueTask<IFile> CreateFileCoreAsync(
    	IFileCreationToken token,
    	IFileContent content = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overrides Function CreateFileCoreAsync ( 
    	token As IFileCreationToken,
    	Optional content As IFileContent = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of IFile)
C++ __Копировать
     protected:
    virtual ValueTask<IFile^> CreateFileCoreAsync(
    	IFileCreationToken^ token, 
    	IFileContent^ content = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    ) override
F# __Копировать
     abstract CreateFileCoreAsync : 
            token : IFileCreationToken * 
            ?content : IFileContent * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _content = defaultArg content null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IFile> 
    override CreateFileCoreAsync : 
            token : IFileCreationToken * 
            ?content : IFileContent * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _content = defaultArg content null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IFile> 
#### Параметры
token [IFileCreationToken](T_Tessa_Files_IFileCreationToken.htm)
    Токен, по которому создаётся файл.
content [IFileContent](T_Tessa_Files_IFileContent.htm) (Optional)
     Контент файла или null, если для файла создаётся отдельный объект контента. Рекомендуется использовать значение null во всех случаях, кроме таких, в которых создаваемый файл должен использовать уже созданный контент. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[IFile](T_Tessa_Files_IFile.htm)>  
Созданный файл.
##  __См. также
#### Ссылки
[FileSourceForCard - ](T_Tessa_Cards_FileSourceForCard.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
