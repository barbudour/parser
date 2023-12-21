# NumberHelper.ProcessExtensionsWhileClosingOrRefreshingCardAsync - метод
Выполняет расширения и обрабатывает очередь действий для события закрытия
вкладки карточки или обновления карточки
[ProcessingQueueWhileClosingOrRefreshingCard](F_Tessa_Cards_Numbers_NumberEventTypes_ProcessingQueueWhileClosingOrRefreshingCard.htm).
Рекомендуется вызывать метод на клиенте, где доступны клиентские зависимости и
текущий контекст UIContext.Current. Однако, это не является требованием
платформы, т.е. при использовании реализации
[INumberDirector](T_Tessa_Cards_Numbers_INumberDirector.htm) из типового
решения возможно выполнение метода и на сервере. Метод может потребоваться
вызвать вручную, например, если запросом [NewAsync(CardNewRequest,
CancellationToken)](M_Tessa_Cards_ICardRepository_NewAsync.htm) была создана
(но не сохранена) карточка, для которой в настройках указано "выделять номер
при создании". В этом случае номер будет зарезервирован, но не освобождён, и
для выполнения всех действий, связанных с освобождением номеров, требуется
вызвать этот метод, но только если карточка не будет сохранена запросом
[StoreAsync(CardStoreRequest,
CancellationToken)](M_Tessa_Cards_ICardRepository_StoreAsync.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task ProcessExtensionsWhileClosingOrRefreshingCardAsync(
    	Card card,
    	CardType cardType,
    	Dictionary<string, Object> contextInfo,
    	INumberDirectorContainer numberDirectorContainer,
    	IValidationResultBuilder validationResult,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function ProcessExtensionsWhileClosingOrRefreshingCardAsync ( 
    	card As Card,
    	cardType As CardType,
    	contextInfo As Dictionary(Of String, Object),
    	numberDirectorContainer As INumberDirectorContainer,
    	validationResult As IValidationResultBuilder,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    static Task^ ProcessExtensionsWhileClosingOrRefreshingCardAsync(
    	Card^ card, 
    	CardType^ cardType, 
    	Dictionary<String^, Object^>^ contextInfo, 
    	INumberDirectorContainer^ numberDirectorContainer, 
    	IValidationResultBuilder^ validationResult, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member ProcessExtensionsWhileClosingOrRefreshingCardAsync : 
            card : Card * 
            cardType : CardType * 
            contextInfo : Dictionary<string, Object> * 
            numberDirectorContainer : INumberDirectorContainer * 
            validationResult : IValidationResultBuilder * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
card [Card](T_Tessa_Cards_Card.htm)
    Карточка, для которой выполняется действие. В ней должны быть доступны данные для всех секций.
cardType [CardType](T_Tessa_Cards_CardType.htm)
    Тип карточки.
contextInfo
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
     Информация для расширений, доступная для некоторого "внешнего" контекста, или null, если такой контекст отсутствует. Для карточки, доступной в UI, это ICardModel.Info. Если метод вызывается из другого расширения на карточку, то это context.Request.Info. 
numberDirectorContainer
[INumberDirectorContainer](T_Tessa_Cards_Numbers_INumberDirectorContainer.htm)
    Объект, предоставляющий доступ к API номеров.
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
    Результат валидации, в который будут записаны сообщения, в т.ч. ошибки в процессе выполнения.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[NumberHelper - ](T_Tessa_Cards_Numbers_NumberHelper.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
