# ICardExternalSourceLogic.ParseBinaryCardAsync - метод
Парсинг карточки в Binary формате.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task<ParsedCard> ParseBinaryCardAsync(
    	Stream sourceStream,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function ParseBinaryCardAsync ( 
    	sourceStream As Stream,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of ParsedCard)
C++ __Копировать
    Task<ParsedCard^>^ ParseBinaryCardAsync(
    	Stream^ sourceStream, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract ParseBinaryCardAsync : 
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
##  __См. также
#### Ссылки
[ICardExternalSourceLogic - ](T_Tessa_Cards_ICardExternalSourceLogic.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
