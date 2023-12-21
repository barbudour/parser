# CardService.NewAsync - метод
Возвращает заполненную структуру карточки по заданному запросу. Физически
карточка не создаётся.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<CardNewResponse> NewAsync(
    	CardNewRequest request,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function NewAsync ( 
    	request As CardNewRequest,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of CardNewResponse)
C++ __Копировать
     public:
    virtual Task<CardNewResponse^>^ NewAsync(
    	CardNewRequest^ request, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract NewAsync : 
            request : CardNewRequest * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardNewResponse> 
    override NewAsync : 
            request : CardNewRequest * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardNewResponse> 
#### Параметры
request [CardNewRequest](T_Tessa_Cards_CardNewRequest.htm)
    Запрос, содержащий информацию по карточке, структуру которой необходимо заполнить.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[CardNewResponse](T_Tessa_Cards_CardNewResponse.htm)>  
Ответ на запрос, содержащий заполненную структуру карточки.
#### Реализации
[ICardService.NewAsync(CardNewRequest,
CancellationToken)](M_Tessa_Cards_ICardService_NewAsync.htm)  
##  __См. также
#### Ссылки
[CardService - ](T_Tessa_Cards_CardService.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
