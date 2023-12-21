# FileSourceForCard.GetVersionsCoreAsync - метод
Возвращает коллекцию доступных версий для заданного файла.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected override ValueTask<IFileVersionResponse> GetVersionsCoreAsync(
    	IFile file,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overrides Function GetVersionsCoreAsync ( 
    	file As IFile,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of IFileVersionResponse)
C++ __Копировать
     protected:
    virtual ValueTask<IFileVersionResponse^> GetVersionsCoreAsync(
    	IFile^ file, 
    	CancellationToken cancellationToken = CancellationToken()
    ) override
F# __Копировать
     abstract GetVersionsCoreAsync : 
            file : IFile * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IFileVersionResponse> 
    override GetVersionsCoreAsync : 
            file : IFile * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IFileVersionResponse> 
#### Параметры
file [IFile](T_Tessa_Files_IFile.htm)
    Файл, для которого требуется получить коллекцию доступных версий.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[IFileVersionResponse](T_Tessa_Files_IFileVersionResponse.htm)>  
Асинхронная задача.
##  __См. также
#### Ссылки
[FileSourceForCard - ](T_Tessa_Cards_FileSourceForCard.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
