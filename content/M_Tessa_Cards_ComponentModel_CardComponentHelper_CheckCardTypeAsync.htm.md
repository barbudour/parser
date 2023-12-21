# CardComponentHelper.CheckCardTypeAsync - метод
Метод выполняет проверку предполагаемого типа карточки с актуальным, если
информация по предполагаемому типу была указана. В случае несовпадения в
результат валидации validationResult будет записано сообщение об ошибке, а
метод вернёт false.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static ValueTask<bool> CheckCardTypeAsync(
    	Guid actualCardTypeID,
    	Guid? supposedCardTypeID,
    	string supposedCardTypeName,
    	ICardMetadata cardMetadata,
    	IValidationResultBuilder validationResult,
    	Object validationObject,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function CheckCardTypeAsync ( 
    	actualCardTypeID As Guid,
    	supposedCardTypeID As Guid?,
    	supposedCardTypeName As String,
    	cardMetadata As ICardMetadata,
    	validationResult As IValidationResultBuilder,
    	validationObject As Object,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of Boolean)
C++ __Копировать
     public:
    static ValueTask<bool> CheckCardTypeAsync(
    	Guid actualCardTypeID, 
    	Nullable<Guid> supposedCardTypeID, 
    	String^ supposedCardTypeName, 
    	ICardMetadata^ cardMetadata, 
    	IValidationResultBuilder^ validationResult, 
    	Object^ validationObject, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member CheckCardTypeAsync : 
            actualCardTypeID : Guid * 
            supposedCardTypeID : Nullable<Guid> * 
            supposedCardTypeName : string * 
            cardMetadata : ICardMetadata * 
            validationResult : IValidationResultBuilder * 
            validationObject : Object * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<bool> 
#### Параметры
actualCardTypeID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Действительный идентификатор типа карточки.
supposedCardTypeID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
     Предполагаемый идентификатор типа карточки или null, если идентификатор не указан, и выполнять проверку не требуется. 
supposedCardTypeName
[String](https://learn.microsoft.com/dotnet/api/system.string)
     Предполагаемое имя типа карточки или null, если имя не указано, и выполнять проверку не требуется. 
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация по типам карточек.
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
    Объект, выполняющий построение результата валидации.
validationObject
[Object](https://learn.microsoft.com/dotnet/api/system.object)
    Объект, для которого записываются сообщения валидации. Может быть равен null.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если предполагаемый тип карточки успешно проверен на соответствие
действительному типу или не был указан; false в противном случае.
## __См. также
#### Ссылки
[CardComponentHelper - ](T_Tessa_Cards_ComponentModel_CardComponentHelper.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
