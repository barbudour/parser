# CardExternalSourceLogic.ParseJsonCardAsync - метод
Парсинг карточки в формате Json.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<ParsedCard> ParseJsonCardAsync(
    	ISourceContentProvider sourceContentProvider,
    	Func<string, bool> ignoredFileNamesFunc,
    	bool recalculateHash,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function ParseJsonCardAsync ( 
    	sourceContentProvider As ISourceContentProvider,
    	ignoredFileNamesFunc As Func(Of String, Boolean),
    	recalculateHash As Boolean,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of ParsedCard)
C++ __Копировать
     public:
    virtual Task<ParsedCard^>^ ParseJsonCardAsync(
    	ISourceContentProvider^ sourceContentProvider, 
    	Func<String^, bool>^ ignoredFileNamesFunc, 
    	bool recalculateHash, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract ParseJsonCardAsync : 
            sourceContentProvider : ISourceContentProvider * 
            ignoredFileNamesFunc : Func<string, bool> * 
            recalculateHash : bool * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ParsedCard> 
    override ParseJsonCardAsync : 
            sourceContentProvider : ISourceContentProvider * 
            ignoredFileNamesFunc : Func<string, bool> * 
            recalculateHash : bool * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ParsedCard> 
#### Параметры
sourceContentProvider
[ISourceContentProvider](T_Tessa_Platform_SourceProviders_ISourceContentProvider.htm)
    Провайдер для ресурса - источинка, откуда производится чтение.
ignoredFileNamesFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>
    Функция для вычисления игнорируемых файлов в подпапке карточки.
recalculateHash
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
    Флаг, указывает нужно ли пересчитывать хэш прикрепленных к карточке файлов.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ParsedCard](T_Tessa_Cards_ParsedCard.htm)>  
Результат парсинга карточки.
#### Реализации
[ICardExternalSourceLogic.ParseJsonCardAsync(ISourceContentProvider,
Func<String, Boolean>, Boolean,
CancellationToken)](M_Tessa_Cards_ICardExternalSourceLogic_ParseJsonCardAsync.htm)  
##  __См. также
#### Ссылки
[CardExternalSourceLogic - ](T_Tessa_Cards_CardExternalSourceLogic.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
