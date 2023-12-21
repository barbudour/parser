# CardHelper.CreateFromTemplateAsync - метод
Создаёт карточку по шаблону и возвращает её.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task<(CardNewRequest Request, CardNewResponse Response)> CreateFromTemplateAsync(
    	Card templateCard,
    	ICardMetadata cardMetadata,
    	ICardManager cardManager,
    	Dictionary<string, Object> templateInfo = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function CreateFromTemplateAsync ( 
    	templateCard As Card,
    	cardMetadata As ICardMetadata,
    	cardManager As ICardManager,
    	Optional templateInfo As Dictionary(Of String, Object) = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of (Request As CardNewRequest, Response As CardNewResponse))
C++ __Копировать
     public:
    static Task<ValueTuple<CardNewRequest^, CardNewResponse^>>^ CreateFromTemplateAsync(
    	Card^ templateCard, 
    	ICardMetadata^ cardMetadata, 
    	ICardManager^ cardManager, 
    	Dictionary<String^, Object^>^ templateInfo = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member CreateFromTemplateAsync : 
            templateCard : Card * 
            cardMetadata : ICardMetadata * 
            cardManager : ICardManager * 
            ?templateInfo : Dictionary<string, Object> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _templateInfo = defaultArg templateInfo null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValueTuple<CardNewRequest, CardNewResponse>> 
#### Параметры
templateCard [Card](T_Tessa_Cards_Card.htm)
    Карточка шаблона, по которой требуется создать карточку.
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация по типам карточек.
cardManager [ICardManager](T_Tessa_Cards_ICardManager.htm)
    Объект, управляющий операциями с карточками.
templateInfo
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)> (Optional)
     Дополнительная информация, помещаемая в запрос на создание карточки по шаблону, или null, если дополнительная информация отсутствует. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ValueTuple](https://learn.microsoft.com/dotnet/api/system.valuetuple-2)<[CardNewRequest](T_Tessa_Cards_CardNewRequest.htm),
[CardNewResponse](T_Tessa_Cards_CardNewResponse.htm)>>  
Результат операции, т.е. внутренний запрос на создание карточки по шаблону и
ответ на него. Внутренний запрос может иметь значение null, если его не
удалось создать.
## __См. также
#### Ссылки
[CardHelper - ](T_Tessa_Cards_CardHelper.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
