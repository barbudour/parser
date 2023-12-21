# FileSourceForCard.GetLinkCoreAsync(IFileVersion, CancellationToken) - метод
Возвращает ссылку на версию файла.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected override ValueTask<IFileVersionLink> GetLinkCoreAsync(
    	IFileVersion version,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overrides Function GetLinkCoreAsync ( 
    	version As IFileVersion,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of IFileVersionLink)
C++ __Копировать
     protected:
    virtual ValueTask<IFileVersionLink^> GetLinkCoreAsync(
    	IFileVersion^ version, 
    	CancellationToken cancellationToken = CancellationToken()
    ) override
F# __Копировать
     abstract GetLinkCoreAsync : 
            version : IFileVersion * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IFileVersionLink> 
    override GetLinkCoreAsync : 
            version : IFileVersion * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IFileVersionLink> 
#### Параметры
version [IFileVersion](T_Tessa_Files_IFileVersion.htm)
    Версия, для которой требуется получить ссылку.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[IFileVersionLink](T_Tessa_Files_IFileVersionLink.htm)>  
Ссылка на версию файла, которая может использоваться для её открытия.
##  __См. также
#### Ссылки
[FileSourceForCard - ](T_Tessa_Cards_FileSourceForCard.htm)
[GetLinkCoreAsync -
перегрузка](Overload_Tessa_Cards_FileSourceForCard_GetLinkCoreAsync.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
