# CardTypeVisitor.VisitColumnAsync - метод
Посещает объект [Tessa.Cards.CardTypeColumn] в типе карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual ValueTask VisitColumnAsync(
    	CardTypeColumn column,
    	CardTypeTableControl control,
    	CardType type,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Overridable Function VisitColumnAsync ( 
    	column As CardTypeColumn,
    	control As CardTypeTableControl,
    	type As CardType,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask
C++ __Копировать
     public:
    virtual ValueTask VisitColumnAsync(
    	CardTypeColumn^ column, 
    	CardTypeTableControl^ control, 
    	CardType^ type, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract VisitColumnAsync : 
            column : CardTypeColumn * 
            control : CardTypeTableControl * 
            type : CardType * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
    override VisitColumnAsync : 
            column : CardTypeColumn * 
            control : CardTypeTableControl * 
            type : CardType * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
#### Параметры
column [CardTypeColumn](T_Tessa_Cards_CardTypeColumn.htm)
    Посещаемый объект.
control [CardTypeTableControl](T_Tessa_Cards_CardTypeTableControl.htm)
    Элемент управления, в котором расположен посещаемый объект.
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
[ICardTypeVisitor.VisitColumnAsync(CardTypeColumn, CardTypeTableControl,
CardType,
CancellationToken)](M_Tessa_Cards_ICardTypeVisitor_VisitColumnAsync.htm)  
##  __См. также
#### Ссылки
[CardTypeVisitor - ](T_Tessa_Cards_CardTypeVisitor.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
