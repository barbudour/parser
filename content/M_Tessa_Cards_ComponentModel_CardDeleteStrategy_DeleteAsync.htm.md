# CardDeleteStrategy.DeleteAsync(Guid, CardDeletionMode, ICardMetadata,
IValidationResultBuilder, Nullable<Guid>, String, Boolean, CancellationToken)
- метод
Удаляет карточку по заданным параметрам. Возвращает тип удаляемой карточки и
список ссылок на контенты файлов для удаления; эти объекты равны null, если
тип определить не удалось и удаление не было выполнено.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<(CardType cardType, List<CardContentContext> contentsToDelete)> DeleteAsync(
    	Guid cardID,
    	CardDeletionMode deletionMode,
    	ICardMetadata cardMetadata,
    	IValidationResultBuilder validationResult,
    	Guid? supposedCardTypeID = null,
    	string supposedCardTypeName = null,
    	bool keepFileContent = false,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function DeleteAsync ( 
    	cardID As Guid,
    	deletionMode As CardDeletionMode,
    	cardMetadata As ICardMetadata,
    	validationResult As IValidationResultBuilder,
    	Optional supposedCardTypeID As Guid? = Nothing,
    	Optional supposedCardTypeName As String = Nothing,
    	Optional keepFileContent As Boolean = false,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of (cardType As CardType, contentsToDelete As List(Of CardContentContext)))
C++ __Копировать
     public:
    virtual Task<ValueTuple<CardType^, List<CardContentContext^>^>>^ DeleteAsync(
    	Guid cardID, 
    	CardDeletionMode deletionMode, 
    	ICardMetadata^ cardMetadata, 
    	IValidationResultBuilder^ validationResult, 
    	Nullable<Guid> supposedCardTypeID = nullptr, 
    	String^ supposedCardTypeName = nullptr, 
    	bool keepFileContent = false, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract DeleteAsync : 
            cardID : Guid * 
            deletionMode : CardDeletionMode * 
            cardMetadata : ICardMetadata * 
            validationResult : IValidationResultBuilder * 
            ?supposedCardTypeID : Nullable<Guid> * 
            ?supposedCardTypeName : string * 
            ?keepFileContent : bool * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _supposedCardTypeID = defaultArg supposedCardTypeID null
            let _supposedCardTypeName = defaultArg supposedCardTypeName null
            let _keepFileContent = defaultArg keepFileContent false
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValueTuple<CardType, List<CardContentContext>>> 
    override DeleteAsync : 
            cardID : Guid * 
            deletionMode : CardDeletionMode * 
            cardMetadata : ICardMetadata * 
            validationResult : IValidationResultBuilder * 
            ?supposedCardTypeID : Nullable<Guid> * 
            ?supposedCardTypeName : string * 
            ?keepFileContent : bool * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _supposedCardTypeID = defaultArg supposedCardTypeID null
            let _supposedCardTypeName = defaultArg supposedCardTypeName null
            let _keepFileContent = defaultArg keepFileContent false
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValueTuple<CardType, List<CardContentContext>>> 
#### Параметры
cardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор удаляемой карточки.
deletionMode [CardDeletionMode](T_Tessa_Cards_CardDeletionMode.htm)
    Способ удаления карточки.
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация по типам карточек.
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
    Объект, выполняющий построение результата валидации.
supposedCardTypeID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
(Optional)
     Предполагаемый идентификатор типа карточки, указанный, например, в запросе на удаление. Если отличен от null, то выполняется проверка на совпадение действительного типа с заданным. 
supposedCardTypeName
[String](https://learn.microsoft.com/dotnet/api/system.string) (Optional)
     Предполагаемое имя типа карточки, указанное, например, в запросе на удаление. Если отлично от null, то выполняется проверка на совпадение действительного типа с заданным. 
keepFileContent
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) (Optional)
     Признак того, что контент файлов карточки не будет удалён, при этом все записи о файлах в карточке всё равно будут удалены. При указании true вызывающий код должен заботиться об удалении контента. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ValueTuple](https://learn.microsoft.com/dotnet/api/system.valuetuple-2)<[CardType](T_Tessa_Cards_CardType.htm),
[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[CardContentContext](T_Tessa_Cards_ComponentModel_CardContentContext.htm)>>>  
Тип удаляемой карточки или null, если тип определить не удалось и удаление не
было выполнено.
#### Реализации
[ICardDeleteStrategy.DeleteAsync(Guid, CardDeletionMode, ICardMetadata,
IValidationResultBuilder, Nullable<Guid>, String, Boolean,
CancellationToken)](M_Tessa_Cards_ComponentModel_ICardDeleteStrategy_DeleteAsync.htm)  
##  __См. также
#### Ссылки
[CardDeleteStrategy - ](T_Tessa_Cards_ComponentModel_CardDeleteStrategy.htm)
[DeleteAsync -
перегрузка](Overload_Tessa_Cards_ComponentModel_CardDeleteStrategy_DeleteAsync.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
