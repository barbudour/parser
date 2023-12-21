# CardStoreContext.CreateAsync - метод
Создаёт экземпляр класса с указанием информации, требуемой для сохранения
заданной карточки [Card](T_Tessa_Cards_Card.htm).
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static ValueTask<CardStoreContext> CreateAsync(
    	Card card,
    	DateTime storeDateTime,
    	ISession session,
    	ICardMetadata generalMetadata,
    	IValidationResultBuilder validationResult,
    	IQueryExecutor executor,
    	IQueryBuilderFactory builderFactory,
    	bool repairSections,
    	CardStoreMethod storeMethod = CardStoreMethod.Default,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function CreateAsync ( 
    	card As Card,
    	storeDateTime As DateTime,
    	session As ISession,
    	generalMetadata As ICardMetadata,
    	validationResult As IValidationResultBuilder,
    	executor As IQueryExecutor,
    	builderFactory As IQueryBuilderFactory,
    	repairSections As Boolean,
    	Optional storeMethod As CardStoreMethod = CardStoreMethod.Default,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of CardStoreContext)
C++ __Копировать
     public:
    static ValueTask<CardStoreContext^> CreateAsync(
    	Card^ card, 
    	DateTime storeDateTime, 
    	ISession^ session, 
    	ICardMetadata^ generalMetadata, 
    	IValidationResultBuilder^ validationResult, 
    	IQueryExecutor^ executor, 
    	IQueryBuilderFactory^ builderFactory, 
    	bool repairSections, 
    	CardStoreMethod storeMethod = CardStoreMethod::Default, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member CreateAsync : 
            card : Card * 
            storeDateTime : DateTime * 
            session : ISession * 
            generalMetadata : ICardMetadata * 
            validationResult : IValidationResultBuilder * 
            executor : IQueryExecutor * 
            builderFactory : IQueryBuilderFactory * 
            repairSections : bool * 
            ?storeMethod : CardStoreMethod * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _storeMethod = defaultArg storeMethod CardStoreMethod.Default
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<CardStoreContext> 
#### Параметры
card [Card](T_Tessa_Cards_Card.htm)
    Сохраняемая карточка.
storeDateTime
[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)
    Дата и время сохранения карточки.
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
    Сессия с пользователем, выполняющим сохранение карточки.
generalMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Общая метаинформация по типам карточек.
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
    Объект, выполняющий построение результата валидации.
executor [IQueryExecutor](T_Tessa_Platform_Data_IQueryExecutor.htm)
    Объект, выполняющий SQL-команды по сохранению карточки.
builderFactory
[IQueryBuilderFactory](T_Tessa_Platform_Data_IQueryBuilderFactory.htm)
    Объект, помогающий создавать SQL-команды для сохранения карточки.
repairSections
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
    Флаг указывает на то, что нужно починить (добавить) строковые секции карточки в случае, если они отсутствуют в БД.
storeMethod [CardStoreMethod](T_Tessa_Cards_CardStoreMethod.htm) (Optional)
    Специализация для способа сохранения карточки.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[CardStoreContext](T_Tessa_Cards_ComponentModel_CardStoreContext.htm)>  
Асинхронная задача.
##  __См. также
#### Ссылки
[CardStoreContext - ](T_Tessa_Cards_ComponentModel_CardStoreContext.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
