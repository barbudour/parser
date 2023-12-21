# FileSourceForCard.GetLinkCoreAsync(IFile, CancellationToken) - метод
Возвращает ссылку на файл.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected override ValueTask<IFileLink> GetLinkCoreAsync(
    	IFile file,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overrides Function GetLinkCoreAsync ( 
    	file As IFile,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of IFileLink)
C++ __Копировать
     protected:
    virtual ValueTask<IFileLink^> GetLinkCoreAsync(
    	IFile^ file, 
    	CancellationToken cancellationToken = CancellationToken()
    ) override
F# __Копировать
     abstract GetLinkCoreAsync : 
            file : IFile * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IFileLink> 
    override GetLinkCoreAsync : 
            file : IFile * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IFileLink> 
#### Параметры
file [IFile](T_Tessa_Files_IFile.htm)
    Файл, для которого требуется получить ссылку.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[IFileLink](T_Tessa_Files_IFileLink.htm)>  
Ссылка на файл, которая может использоваться для его открытия.
##  __См. также
#### Ссылки
[FileSourceForCard - ](T_Tessa_Cards_FileSourceForCard.htm)
[GetLinkCoreAsync -
перегрузка](Overload_Tessa_Cards_FileSourceForCard_GetLinkCoreAsync.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
