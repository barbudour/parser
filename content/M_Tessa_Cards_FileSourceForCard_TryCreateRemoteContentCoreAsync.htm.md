# FileSourceForCard.TryCreateRemoteContentCoreAsync - метод
Создаёт объект контента, обеспечивающий доступ к файлу удалённо, т.е. без
копирования во временную папку. Возвращает null, если не удалось создать
контент для заданной версии. Любой запрос к контенту файла может привести к
запросу к серверу или к другому способу создать контент.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected override ValueTask<IFileContent> TryCreateRemoteContentCoreAsync(
    	IFileVersion version,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overrides Function TryCreateRemoteContentCoreAsync ( 
    	version As IFileVersion,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of IFileContent)
C++ __Копировать
     protected:
    virtual ValueTask<IFileContent^> TryCreateRemoteContentCoreAsync(
    	IFileVersion^ version, 
    	CancellationToken cancellationToken = CancellationToken()
    ) override
F# __Копировать
     abstract TryCreateRemoteContentCoreAsync : 
            version : IFileVersion * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IFileContent> 
    override TryCreateRemoteContentCoreAsync : 
            version : IFileVersion * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IFileContent> 
#### Параметры
version [IFileVersion](T_Tessa_Files_IFileVersion.htm)
     Версия файла, для которой создаётся объект контента. Чтобы создать объект контента для файла, укажите его последнюю версию. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[IFileContent](T_Tessa_Files_IFileContent.htm)>  
Созданный объект контента или null, если не удалось создать контент для
заданной версии.
## __См. также
#### Ссылки
[FileSourceForCard - ](T_Tessa_Cards_FileSourceForCard.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
