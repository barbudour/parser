# CardGetStrategy.TryLoadFileInstancesAsync - метод
Загружает общую информацию по экземплярам файлов, приложенных к заданной
карточке, и возвращает список контекстов операций по загрузке каждого из
файлов или null, если загрузку произвести не удалось.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<IList<CardGetContext>> TryLoadFileInstancesAsync(
    	Guid cardID,
    	Card card,
    	DbManager db,
    	ICardMetadata cardMetadata,
    	IValidationResultBuilder validationResult,
    	CardNewMode newMode = CardNewMode.Default,
    	IEnumerable<Guid> fileRowIDList = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function TryLoadFileInstancesAsync ( 
    	cardID As Guid,
    	card As Card,
    	db As DbManager,
    	cardMetadata As ICardMetadata,
    	validationResult As IValidationResultBuilder,
    	Optional newMode As CardNewMode = CardNewMode.Default,
    	Optional fileRowIDList As IEnumerable(Of Guid) = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of IList(Of CardGetContext))
C++ __Копировать
     public:
    virtual Task<IList<CardGetContext^>^>^ TryLoadFileInstancesAsync(
    	Guid cardID, 
    	Card^ card, 
    	DbManager^ db, 
    	ICardMetadata^ cardMetadata, 
    	IValidationResultBuilder^ validationResult, 
    	CardNewMode newMode = CardNewMode::Default, 
    	IEnumerable<Guid>^ fileRowIDList = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract TryLoadFileInstancesAsync : 
            cardID : Guid * 
            card : Card * 
            db : DbManager * 
            cardMetadata : ICardMetadata * 
            validationResult : IValidationResultBuilder * 
            ?newMode : CardNewMode * 
            ?fileRowIDList : IEnumerable<Guid> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _newMode = defaultArg newMode CardNewMode.Default
            let _fileRowIDList = defaultArg fileRowIDList null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<IList<CardGetContext>> 
    override TryLoadFileInstancesAsync : 
            cardID : Guid * 
            card : Card * 
            db : DbManager * 
            cardMetadata : ICardMetadata * 
            validationResult : IValidationResultBuilder * 
            ?newMode : CardNewMode * 
            ?fileRowIDList : IEnumerable<Guid> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _newMode = defaultArg newMode CardNewMode.Default
            let _fileRowIDList = defaultArg fileRowIDList null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<IList<CardGetContext>> 
#### Параметры
cardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор карточки, информацию по файлам которой требуется загрузить.
card [Card](T_Tessa_Cards_Card.htm)
    Карточка, в которую добавляется информация по файлам.
db [DbManager](T_Tessa_Platform_Data_DbManager.htm)
    Объект, предоставляющий доступ к базе данных.
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация по загружаемым типам файлов. Передайте объект с метаинформацией по всем типам.
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
    Объект, осуществляющий построение результата валидации.
newMode [CardNewMode](T_Tessa_Cards_CardNewMode.htm) (Optional)
    Способ заполнения данных в виртуальных секциях.
fileRowIDList
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
(Optional)
     Список идентификаторов файлов, которые разрешено загружать среди доступных пользователю файлов, или null, если список файлов не ограничивается. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<[CardGetContext](T_Tessa_Cards_ComponentModel_CardGetContext.htm)>>  
Список контекстов операций по загрузке каждого из файлов заданной карточки или
null, если не удалось загрузить информацию о файлах карточки.
#### Реализации
[ICardGetStrategy.TryLoadFileInstancesAsync(Guid, Card, DbManager,
ICardMetadata, IValidationResultBuilder, CardNewMode, IEnumerable<Guid>,
CancellationToken)](M_Tessa_Cards_ComponentModel_ICardGetStrategy_TryLoadFileInstancesAsync.htm)  
##  __См. также
#### Ссылки
[CardGetStrategy - ](T_Tessa_Cards_ComponentModel_CardGetStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
