# CardsWebProxy.RequestAsync - метод
Выполняет универсальный запрос к сервису карточек.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<CardResponse> RequestAsync(
    	CardRequest request,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function RequestAsync ( 
    	request As CardRequest,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of CardResponse)
C++ __Копировать
     public:
    Task<CardResponse^>^ RequestAsync(
    	CardRequest^ request, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     member RequestAsync : 
            request : CardRequest * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardResponse> 
#### Параметры
request [CardRequest](T_Tessa_Cards_CardRequest.htm)
    Универсальный запрос к сервису карточек.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[CardResponse](T_Tessa_Cards_CardResponse.htm)>  
Ответ на универсальный запрос к сервису карточек.
##  __См. также
#### Ссылки
[CardsWebProxy - ](T_Tessa_Cards_CardsWebProxy.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
