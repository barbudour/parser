# CardGetContext - конструктор
Создаёт экземпляр класса с указанием информации, необходимой для загрузки
карточки.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardGetContext(
    	Guid cardID,
    	Guid cardTypeID,
    	Card card,
    	ICardMetadata cardMetadata,
    	IValidationResultBuilder validationResult,
    	DbManager db,
    	CardNewMode newMode,
    	List<Guid> sectionsToExclude = null,
    	bool warningIfEntryNotFound = false
    )
VB __Копировать
     Public Sub New ( 
    	cardID As Guid,
    	cardTypeID As Guid,
    	card As Card,
    	cardMetadata As ICardMetadata,
    	validationResult As IValidationResultBuilder,
    	db As DbManager,
    	newMode As CardNewMode,
    	Optional sectionsToExclude As List(Of Guid) = Nothing,
    	Optional warningIfEntryNotFound As Boolean = false
    )
C++ __Копировать
     public:
    CardGetContext(
    	Guid cardID, 
    	Guid cardTypeID, 
    	Card^ card, 
    	ICardMetadata^ cardMetadata, 
    	IValidationResultBuilder^ validationResult, 
    	DbManager^ db, 
    	CardNewMode newMode, 
    	List<Guid>^ sectionsToExclude = nullptr, 
    	bool warningIfEntryNotFound = false
    )
F# __Копировать
     new : 
            cardID : Guid * 
            cardTypeID : Guid * 
            card : Card * 
            cardMetadata : ICardMetadata * 
            validationResult : IValidationResultBuilder * 
            db : DbManager * 
            newMode : CardNewMode * 
            ?sectionsToExclude : List<Guid> * 
            ?warningIfEntryNotFound : bool 
    (* Defaults:
            let _sectionsToExclude = defaultArg sectionsToExclude null
            let _warningIfEntryNotFound = defaultArg warningIfEntryNotFound false
    *)
    -> CardGetContext
#### Параметры
cardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор загружаемой карточки.
cardTypeID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Тип загружаемой карточки.
card [Card](T_Tessa_Cards_Card.htm)
    Загружаемая карточка.
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация по типу загружаемой карточки.
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
    Объект, выполняющий построение результата валидации.
db [DbManager](T_Tessa_Platform_Data_DbManager.htm)
    Объект, осуществляющий взаимодействие с базой данных.
newMode [CardNewMode](T_Tessa_Cards_CardNewMode.htm)
    Способ заполнения данных для виртуальных секций.
sectionsToExclude
[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
(Optional)
     Список идентификаторов физических секций, загрузку которых не следует выполнять или null, если загружаются все секции или незагружаемые секции указываются позже. 
warningIfEntryNotFound
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) (Optional)
     Флаг, указывающий на то, что в случае отсутствия строковой секции в БД, будет сгенерировано предупреждение, а не ошибка. 
## __См. также
#### Ссылки
[CardGetContext - ](T_Tessa_Cards_ComponentModel_CardGetContext.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
