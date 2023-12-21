# CardTypeVisitor.VisitExtensionAsync - метод
Посещает объект [Tessa.Cards.CardTypeExtension] в типе карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual ValueTask VisitExtensionAsync(
    	CardTypeExtension extension,
    	CardType type,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Overridable Function VisitExtensionAsync ( 
    	extension As CardTypeExtension,
    	type As CardType,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask
C++ __Копировать
     public:
    virtual ValueTask VisitExtensionAsync(
    	CardTypeExtension^ extension, 
    	CardType^ type, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract VisitExtensionAsync : 
            extension : CardTypeExtension * 
            type : CardType * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
    override VisitExtensionAsync : 
            extension : CardTypeExtension * 
            type : CardType * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
#### Параметры
extension [CardTypeExtension](T_Tessa_Cards_CardTypeExtension.htm)
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
#### Реализации
[ICardTypeVisitor.VisitExtensionAsync(CardTypeExtension, CardType,
CancellationToken)](M_Tessa_Cards_ICardTypeVisitor_VisitExtensionAsync.htm)  
##  __См. также
#### Ссылки
[CardTypeVisitor - ](T_Tessa_Cards_CardTypeVisitor.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
