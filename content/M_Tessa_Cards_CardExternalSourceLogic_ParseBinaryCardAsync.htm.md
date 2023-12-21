# CardExternalSourceLogic.ParseBinaryCardAsync - метод
Парсинг карточки в Binary формате.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<ParsedCard> ParseBinaryCardAsync(
    	Stream sourceStream,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function ParseBinaryCardAsync ( 
    	sourceStream As Stream,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of ParsedCard)
C++ __Копировать
     public:
    virtual Task<ParsedCard^>^ ParseBinaryCardAsync(
    	Stream^ sourceStream, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract ParseBinaryCardAsync : 
            sourceStream : Stream * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ParsedCard> 
    override ParseBinaryCardAsync : 
            sourceStream : Stream * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ParsedCard> 
#### Параметры
sourceStream [Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)
    Поток источинка карточки, откуда производится чтение.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ParsedCard](T_Tessa_Cards_ParsedCard.htm)>  
Результат парсинга карточки.
#### Реализации
[ICardExternalSourceLogic.ParseBinaryCardAsync(Stream,
CancellationToken)](M_Tessa_Cards_ICardExternalSourceLogic_ParseBinaryCardAsync.htm)  
##  __См. также
#### Ссылки
[CardExternalSourceLogic - ](T_Tessa_Cards_CardExternalSourceLogic.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
