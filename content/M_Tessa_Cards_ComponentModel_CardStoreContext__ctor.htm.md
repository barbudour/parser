# CardStoreContext - конструктор
Создаёт экземпляр класса с указанием информации, требуемой для сохранения
карточки. Рассмотрите использование статического метода [CreateAsync(Card,
DateTime, ISession, ICardMetadata, IValidationResultBuilder, IQueryExecutor,
IQueryBuilderFactory, Boolean, CardStoreMethod,
CancellationToken)](M_Tessa_Cards_ComponentModel_CardStoreContext_CreateAsync.htm)
для упрощённого создания экземпляра объекта.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardStoreContext(
    	CardStoreMode storeMode,
    	CardStoreMethod storeMethod,
    	DateTime storeDateTime,
    	Guid cardID,
    	Guid cardTypeID,
    	string cardTypeCaption,
    	ICollection<CardSection> sections,
    	ICollection<CardFile> files,
    	ICollection<CardTask> tasks,
    	ICollection<CardTaskHistoryItem> taskHistory,
    	ICollection<CardTaskHistoryGroup> taskHistoryGroups,
    	ISession session,
    	ICardMetadata cardMetadata,
    	ICardMetadata generalMetadata,
    	IValidationResultBuilder validationResult,
    	IQueryExecutor executor,
    	IQueryBuilderFactory builderFactory,
    	bool affectVersion,
    	bool doesNotAffectVersion,
    	bool forceTransaction,
    	bool repairSections,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Sub New ( 
    	storeMode As CardStoreMode,
    	storeMethod As CardStoreMethod,
    	storeDateTime As DateTime,
    	cardID As Guid,
    	cardTypeID As Guid,
    	cardTypeCaption As String,
    	sections As ICollection(Of CardSection),
    	files As ICollection(Of CardFile),
    	tasks As ICollection(Of CardTask),
    	taskHistory As ICollection(Of CardTaskHistoryItem),
    	taskHistoryGroups As ICollection(Of CardTaskHistoryGroup),
    	session As ISession,
    	cardMetadata As ICardMetadata,
    	generalMetadata As ICardMetadata,
    	validationResult As IValidationResultBuilder,
    	executor As IQueryExecutor,
    	builderFactory As IQueryBuilderFactory,
    	affectVersion As Boolean,
    	doesNotAffectVersion As Boolean,
    	forceTransaction As Boolean,
    	repairSections As Boolean,
    	Optional cancellationToken As CancellationToken = Nothing
    )
C++ __Копировать
     public:
    CardStoreContext(
    	CardStoreMode storeMode, 
    	CardStoreMethod storeMethod, 
    	DateTime storeDateTime, 
    	Guid cardID, 
    	Guid cardTypeID, 
    	String^ cardTypeCaption, 
    	ICollection<CardSection^>^ sections, 
    	ICollection<CardFile^>^ files, 
    	ICollection<CardTask^>^ tasks, 
    	ICollection<CardTaskHistoryItem^>^ taskHistory, 
    	ICollection<CardTaskHistoryGroup^>^ taskHistoryGroups, 
    	ISession^ session, 
    	ICardMetadata^ cardMetadata, 
    	ICardMetadata^ generalMetadata, 
    	IValidationResultBuilder^ validationResult, 
    	IQueryExecutor^ executor, 
    	IQueryBuilderFactory^ builderFactory, 
    	bool affectVersion, 
    	bool doesNotAffectVersion, 
    	bool forceTransaction, 
    	bool repairSections, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     new : 
            storeMode : CardStoreMode * 
            storeMethod : CardStoreMethod * 
            storeDateTime : DateTime * 
            cardID : Guid * 
            cardTypeID : Guid * 
            cardTypeCaption : string * 
            sections : ICollection<CardSection> * 
            files : ICollection<CardFile> * 
            tasks : ICollection<CardTask> * 
            taskHistory : ICollection<CardTaskHistoryItem> * 
            taskHistoryGroups : ICollection<CardTaskHistoryGroup> * 
            session : ISession * 
            cardMetadata : ICardMetadata * 
            generalMetadata : ICardMetadata * 
            validationResult : IValidationResultBuilder * 
            executor : IQueryExecutor * 
            builderFactory : IQueryBuilderFactory * 
            affectVersion : bool * 
            doesNotAffectVersion : bool * 
            forceTransaction : bool * 
            repairSections : bool * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> CardStoreContext
#### Параметры
storeMode [CardStoreMode](T_Tessa_Cards_CardStoreMode.htm)
    Способ сохранения карточки.
storeMethod [CardStoreMethod](T_Tessa_Cards_CardStoreMethod.htm)
    Специализация для способа сохранения карточки.
storeDateTime
[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)
    Время сохранения карточки в формате UTC.
cardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор сохраняемой карточки.
cardTypeID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор типа сохраняемой карточки.
cardTypeCaption [String](https://learn.microsoft.com/dotnet/api/system.string)
    Отображаемое имя типа сохраняемой карточки.
sections
[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<[CardSection](T_Tessa_Cards_CardSection.htm)>
    Секции сохраняемой карточки.
files
[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<[CardFile](T_Tessa_Cards_CardFile.htm)>
    Файлы сохраняемой карточки.
tasks
[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<[CardTask](T_Tessa_Cards_CardTask.htm)>
    Задания сохраняемой карточки.
taskHistory
[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<[CardTaskHistoryItem](T_Tessa_Cards_CardTaskHistoryItem.htm)>
    История заданий сохраняемой карточки.
taskHistoryGroups
[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<[CardTaskHistoryGroup](T_Tessa_Cards_CardTaskHistoryGroup.htm)>
    Группы в истории заданий для сохраняемой карточки.
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
    Сессия с пользователем, выполняющим сохранение карточки.
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация по типу сохраняемой карточки.
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
affectVersion [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
    Признак того, что изменения принудительно влияют на проверку и инкремент версии карточки.
doesNotAffectVersion
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
    Признак того, что изменения принудительно не влияют на проверку и инкремент версии карточки.
forceTransaction
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
    Признак того, что будет открыта транзакция независимо от наличия изменений в карточке.
repairSections
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
    Флаг указывает на то, что нужно починить (добавить) строковые секции карточки в случае, если они отсутствуют в БД.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
##  __См. также
#### Ссылки
[CardStoreContext - ](T_Tessa_Cards_ComponentModel_CardStoreContext.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
