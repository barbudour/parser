# FileSourceForCard.GetSignaturesCoreAsync - метод
Возвращает коллекцию доступных подписей для заданной версии файла.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected override ValueTask<IFileSignatureResponse> GetSignaturesCoreAsync(
    	IFileVersion version,
    	FileSignatureLoadingMode loadingMode,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overrides Function GetSignaturesCoreAsync ( 
    	version As IFileVersion,
    	loadingMode As FileSignatureLoadingMode,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of IFileSignatureResponse)
C++ __Копировать
     protected:
    virtual ValueTask<IFileSignatureResponse^> GetSignaturesCoreAsync(
    	IFileVersion^ version, 
    	FileSignatureLoadingMode loadingMode, 
    	CancellationToken cancellationToken = CancellationToken()
    ) override
F# __Копировать
     abstract GetSignaturesCoreAsync : 
            version : IFileVersion * 
            loadingMode : FileSignatureLoadingMode * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IFileSignatureResponse> 
    override GetSignaturesCoreAsync : 
            version : IFileVersion * 
            loadingMode : FileSignatureLoadingMode * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IFileSignatureResponse> 
#### Параметры
version [IFileVersion](T_Tessa_Files_IFileVersion.htm)
    Версия файла, для которой требуется получить коллекцию доступных подписей.
loadingMode
[FileSignatureLoadingMode](T_Tessa_Files_FileSignatureLoadingMode.htm)
    Способ загрузки подписей.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[IFileSignatureResponse](T_Tessa_Files_IFileSignatureResponse.htm)>  
Ответ на запрос на получение коллекции доступных подписей для заданной версии
файла.
##  __См. также
#### Ссылки
[FileSourceForCard - ](T_Tessa_Cards_FileSourceForCard.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
