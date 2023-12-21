# ICardTypeVisitor.VisitValidatorAsync(CardTypeValidator, CardType,
CancellationToken) - метод
Посещает объект [Tessa.Cards.CardTypeValidator] в типе карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     ValueTask VisitValidatorAsync(
    	CardTypeValidator validator,
    	CardType type,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function VisitValidatorAsync ( 
    	validator As CardTypeValidator,
    	type As CardType,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask
C++ __Копировать
     ValueTask VisitValidatorAsync(
    	CardTypeValidator^ validator, 
    	CardType^ type, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract VisitValidatorAsync : 
            validator : CardTypeValidator * 
            type : CardType * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
#### Параметры
validator [CardTypeValidator](T_Tessa_Cards_CardTypeValidator.htm)
    Посещаемый объект.
type [CardType](T_Tessa_Cards_CardType.htm)
    Тип карточки, в котором расположен посещаемый объект.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)  
Асинхронная задача.
##  __См. также
#### Ссылки
[ICardTypeVisitor - ](T_Tessa_Cards_ICardTypeVisitor.htm)
[VisitValidatorAsync -
перегрузка](Overload_Tessa_Cards_ICardTypeVisitor_VisitValidatorAsync.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
