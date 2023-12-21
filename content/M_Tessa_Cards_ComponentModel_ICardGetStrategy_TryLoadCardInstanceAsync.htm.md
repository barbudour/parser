# ICardGetStrategy.TryLoadCardInstanceAsync - метод
Загружает общую информацию по экземпляру карточки из таблицы Instances и
возвращает контекст операции или null, если загрузку произвести не удалось.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task<CardGetContext> TryLoadCardInstanceAsync(
    	Guid cardID,
    	DbManager db,
    	ICardMetadata cardMetadata,
    	IValidationResultBuilder validationResult,
    	CardNewMode newMode = CardNewMode.Default,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function TryLoadCardInstanceAsync ( 
    	cardID As Guid,
    	db As DbManager,
    	cardMetadata As ICardMetadata,
    	validationResult As IValidationResultBuilder,
    	Optional newMode As CardNewMode = CardNewMode.Default,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of CardGetContext)
C++ __Копировать
    Task<CardGetContext^>^ TryLoadCardInstanceAsync(
    	Guid cardID, 
    	DbManager^ db, 
    	ICardMetadata^ cardMetadata, 
    	IValidationResultBuilder^ validationResult, 
    	CardNewMode newMode = CardNewMode::Default, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract TryLoadCardInstanceAsync : 
            cardID : Guid * 
            db : DbManager * 
            cardMetadata : ICardMetadata * 
            validationResult : IValidationResultBuilder * 
            ?newMode : CardNewMode * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _newMode = defaultArg newMode CardNewMode.Default
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardGetContext> 
#### Параметры
cardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор загружаемой карточки.
db [DbManager](T_Tessa_Platform_Data_DbManager.htm)
    Объект, предоставляющий доступ к базе данных.
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация по типу загружаемой карточки.
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
    Объект, осуществляющий построение результата валидации.
newMode [CardNewMode](T_Tessa_Cards_CardNewMode.htm) (Optional)
    Способ заполнения данных в виртуальных секциях.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[CardGetContext](T_Tessa_Cards_ComponentModel_CardGetContext.htm)>  
Контекст операции по загрузке заданной карточки или null, если не удалось
загрузить информацию о карточке.
## __См. также
#### Ссылки
[ICardGetStrategy - ](T_Tessa_Cards_ComponentModel_ICardGetStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
