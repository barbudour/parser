# CardDeleteContext - конструктор
Создаёт экземпляр класса с указанием информации, необходимой для удаления
карточки.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardDeleteContext(
    	Guid cardID,
    	CardDeletionMode deletionMode,
    	ICardMetadata cardMetadata,
    	ICardMetadata generalMetadata,
    	DbManager db,
    	IDeferredQueryExecutor executor,
    	IQueryBuilderFactory builderFactory,
    	IValidationResultBuilder validationResult,
    	bool keepFileContent = false,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Sub New ( 
    	cardID As Guid,
    	deletionMode As CardDeletionMode,
    	cardMetadata As ICardMetadata,
    	generalMetadata As ICardMetadata,
    	db As DbManager,
    	executor As IDeferredQueryExecutor,
    	builderFactory As IQueryBuilderFactory,
    	validationResult As IValidationResultBuilder,
    	Optional keepFileContent As Boolean = false,
    	Optional cancellationToken As CancellationToken = Nothing
    )
C++ __Копировать
     public:
    CardDeleteContext(
    	Guid cardID, 
    	CardDeletionMode deletionMode, 
    	ICardMetadata^ cardMetadata, 
    	ICardMetadata^ generalMetadata, 
    	DbManager^ db, 
    	IDeferredQueryExecutor^ executor, 
    	IQueryBuilderFactory^ builderFactory, 
    	IValidationResultBuilder^ validationResult, 
    	bool keepFileContent = false, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     new : 
            cardID : Guid * 
            deletionMode : CardDeletionMode * 
            cardMetadata : ICardMetadata * 
            generalMetadata : ICardMetadata * 
            db : DbManager * 
            executor : IDeferredQueryExecutor * 
            builderFactory : IQueryBuilderFactory * 
            validationResult : IValidationResultBuilder * 
            ?keepFileContent : bool * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _keepFileContent = defaultArg keepFileContent false
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> CardDeleteContext
#### Параметры
cardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор удаляемой карточки.
deletionMode [CardDeletionMode](T_Tessa_Cards_CardDeletionMode.htm)
    Способ удаления карточки.
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация по типу удаляемой карточки.
generalMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация по типам карточек.
db [DbManager](T_Tessa_Platform_Data_DbManager.htm)
    Объект, осуществляющий прямое взаимодействие с базой данных.
executor
[IDeferredQueryExecutor](T_Tessa_Platform_Data_IDeferredQueryExecutor.htm)
    Объект, осуществляющий отложенное выполнение запросов.
builderFactory
[IQueryBuilderFactory](T_Tessa_Platform_Data_IQueryBuilderFactory.htm)
    Объект, осуществляющий создание запросов.
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
    Объект, выполняющий построение результата валидации.
keepFileContent
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) (Optional)
     Признак того, что контент файлов карточки не будет удалён, при этом все записи о файлах в карточке всё равно будут удалены. При указании true вызывающий код должен заботиться об удалении контента. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
##  __См. также
#### Ссылки
[CardDeleteContext - ](T_Tessa_Cards_ComponentModel_CardDeleteContext.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
