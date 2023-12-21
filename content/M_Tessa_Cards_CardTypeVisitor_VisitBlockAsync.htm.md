# CardTypeVisitor.VisitBlockAsync - метод
Посещает объект [Tessa.Cards.CardTypeBlock] в типе карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual ValueTask VisitBlockAsync(
    	CardTypeBlock block,
    	CardTypeForm form,
    	CardType type,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Overridable Function VisitBlockAsync ( 
    	block As CardTypeBlock,
    	form As CardTypeForm,
    	type As CardType,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask
C++ __Копировать
     public:
    virtual ValueTask VisitBlockAsync(
    	CardTypeBlock^ block, 
    	CardTypeForm^ form, 
    	CardType^ type, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract VisitBlockAsync : 
            block : CardTypeBlock * 
            form : CardTypeForm * 
            type : CardType * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
    override VisitBlockAsync : 
            block : CardTypeBlock * 
            form : CardTypeForm * 
            type : CardType * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
#### Параметры
block [CardTypeBlock](T_Tessa_Cards_CardTypeBlock.htm)
    Посещаемый объект.
form [CardTypeForm](T_Tessa_Cards_CardTypeForm.htm)
    Форма, в которой расположен посещаемый объект.
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
[ICardTypeVisitor.VisitBlockAsync(CardTypeBlock, CardTypeForm, CardType,
CancellationToken)](M_Tessa_Cards_ICardTypeVisitor_VisitBlockAsync.htm)  
##  __См. также
#### Ссылки
[CardTypeVisitor - ](T_Tessa_Cards_CardTypeVisitor.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
