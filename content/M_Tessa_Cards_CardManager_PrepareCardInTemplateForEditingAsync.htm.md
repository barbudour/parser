# CardManager.PrepareCardInTemplateForEditingAsync - метод
Подготавливает карточку в шаблоне, десериализованную из шаблона, к
редактированию.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<(bool Success, Card CardInTemplate, StringDictionaryStorage<CardRow> SectionRows)> PrepareCardInTemplateForEditingAsync(
    	Card templateCard,
    	IValidationResultBuilder validationResult,
    	Card cardInTemplate,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function PrepareCardInTemplateForEditingAsync ( 
    	templateCard As Card,
    	validationResult As IValidationResultBuilder,
    	cardInTemplate As Card,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of (Success As Boolean, CardInTemplate As Card, SectionRows As StringDictionaryStorage(Of CardRow)))
C++ __Копировать
     public:
    virtual Task<ValueTuple<bool, Card^, StringDictionaryStorage<CardRow^>^>>^ PrepareCardInTemplateForEditingAsync(
    	Card^ templateCard, 
    	IValidationResultBuilder^ validationResult, 
    	Card^ cardInTemplate, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract PrepareCardInTemplateForEditingAsync : 
            templateCard : Card * 
            validationResult : IValidationResultBuilder * 
            cardInTemplate : Card * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValueTuple<bool, Card, StringDictionaryStorage<CardRow>>> 
    override PrepareCardInTemplateForEditingAsync : 
            templateCard : Card * 
            validationResult : IValidationResultBuilder * 
            cardInTemplate : Card * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValueTuple<bool, Card, StringDictionaryStorage<CardRow>>> 
#### Параметры
templateCard [Card](T_Tessa_Cards_Card.htm)
     Карточка шаблона. Значение параметра не должно быть равно null. 
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
     Результат валидации, содержащий сообщения, возникшие в процессе выполнения действия. Значение параметра не должно быть равно null. 
cardInTemplate [Card](T_Tessa_Cards_Card.htm)
Карточка в шаблоне, которая десериализована из шаблона. Значение параметра не
должно быть равно null.
В параметре возвращается подготовленная карточка, которая может совпадать или
не совпадать с исходной карточкой. Т.е. отсутствуют гарантии, что исходная
карточка не будет изменена.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ValueTuple](https://learn.microsoft.com/dotnet/api/system.valuetuple-3)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean),
[Card](T_Tessa_Cards_Card.htm),
[StringDictionaryStorage](T_Tessa_Platform_Storage_StringDictionaryStorage_1.htm)<[CardRow](T_Tessa_Cards_CardRow.htm)>>>  
Success: true, если карточка была успешно подготовлена; false, если при
подготовке карточки возникли ошибки.
CardInTemplate: подготовленная карточка, которая может совпадать или не
совпадать с исходной карточкой.
SectionRows: Строки коллекционных и древовидных секций, которые могут
использоваться для редактирования возвращённой карточки.
#### Реализации
[ICardManager.PrepareCardInTemplateForEditingAsync(Card,
IValidationResultBuilder, Card,
CancellationToken)](M_Tessa_Cards_ICardManager_PrepareCardInTemplateForEditingAsync.htm)  
##  __Исключения
[ArgumentNullException](https://learn.microsoft.com/dotnet/api/system.argumentnullexception)|  
---|---  
##  __См. также
#### Ссылки
[CardManager - ](T_Tessa_Cards_CardManager.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
