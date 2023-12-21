# ICardManager.PrepareCardInTemplateForStoringAsync - метод
Подготавливает отредактированную карточку в шаблоне для сериализации и
сохранения в шаблоне.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    Task<(bool Success, Card CardInTemplate)> PrepareCardInTemplateForStoringAsync(
    	IValidationResultBuilder validationResult,
    	Card cardInTemplate,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function PrepareCardInTemplateForStoringAsync ( 
    	validationResult As IValidationResultBuilder,
    	cardInTemplate As Card,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of (Success As Boolean, CardInTemplate As Card))
C++ __Копировать
    Task<ValueTuple<bool, Card^>>^ PrepareCardInTemplateForStoringAsync(
    	IValidationResultBuilder^ validationResult, 
    	Card^ cardInTemplate, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract PrepareCardInTemplateForStoringAsync : 
            validationResult : IValidationResultBuilder * 
            cardInTemplate : Card * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValueTuple<bool, Card>> 
#### Параметры
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
     Результат валидации, содержащий сообщения, возникшие в процессе выполнения действия. Значение параметра не должно быть равно null. 
cardInTemplate [Card](T_Tessa_Cards_Card.htm)
Карточка в шаблоне, которую необходимо сохранить в шаблоне. Значение параметра
не должно быть равно null.
В параметре возвращается подготовленная карточка, которая может совпадать или
не совпадать с исходной карточкой. Т.е. отсутствуют гарантии, что исходная
карточка не будет изменена.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ValueTuple](https://learn.microsoft.com/dotnet/api/system.valuetuple-2)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean),
[Card](T_Tessa_Cards_Card.htm)>>  
Success: true, если карточка была успешно подготовлена; false, если при
подготовке карточки возникли ошибки.
CardInTemplate: подготовленная карточка, которая может совпадать или не
совпадать с исходной карточкой.
##  __См. также
#### Ссылки
[ICardManager - ](T_Tessa_Cards_ICardManager.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
