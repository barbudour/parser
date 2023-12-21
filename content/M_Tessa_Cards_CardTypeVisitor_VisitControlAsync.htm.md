# CardTypeVisitor.VisitControlAsync - метод
Посещает объект [Tessa.Cards.CardTypeControl] в типе карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual ValueTask VisitControlAsync(
    	CardTypeControl control,
    	CardTypeBlock block,
    	CardTypeForm form,
    	CardType type,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Overridable Function VisitControlAsync ( 
    	control As CardTypeControl,
    	block As CardTypeBlock,
    	form As CardTypeForm,
    	type As CardType,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask
C++ __Копировать
     public:
    virtual ValueTask VisitControlAsync(
    	CardTypeControl^ control, 
    	CardTypeBlock^ block, 
    	CardTypeForm^ form, 
    	CardType^ type, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract VisitControlAsync : 
            control : CardTypeControl * 
            block : CardTypeBlock * 
            form : CardTypeForm * 
            type : CardType * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
    override VisitControlAsync : 
            control : CardTypeControl * 
            block : CardTypeBlock * 
            form : CardTypeForm * 
            type : CardType * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
#### Параметры
control [CardTypeControl](T_Tessa_Cards_CardTypeControl.htm)
    Посещаемый объект.
block [CardTypeBlock](T_Tessa_Cards_CardTypeBlock.htm)
    Блок, в котором расположен посещаемый объект.
form [CardTypeForm](T_Tessa_Cards_CardTypeForm.htm)
    Форма, в которой расположен блок с посещаемым объектом.
type [CardType](T_Tessa_Cards_CardType.htm)
    Тип карточки, в котором расположен посещаемый объект.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)  
Асинхронная задача.
#### Реализации
[ICardTypeVisitor.VisitControlAsync(CardTypeControl, CardTypeBlock,
CardTypeForm, CardType,
CancellationToken)](M_Tessa_Cards_ICardTypeVisitor_VisitControlAsync.htm)  
##  __См. также
#### Ссылки
[CardTypeVisitor - ](T_Tessa_Cards_CardTypeVisitor.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
