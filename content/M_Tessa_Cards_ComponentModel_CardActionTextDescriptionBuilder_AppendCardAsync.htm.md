# CardActionTextDescriptionBuilder.AppendCardAsync - метод
Добавляет описание изменений, произошедших в заданной карточке. Актуально
только для действий [Tessa.Cards.CardActionType.Create] и
[Tessa.Cards.CardActionType.Modify].
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<StringBuilder> AppendCardAsync(
    	StringBuilder builder,
    	Card card,
    	DateTime modified,
    	ActionType actionType,
    	CardStoreMethod storeMethod = CardStoreMethod.Default,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function AppendCardAsync ( 
    	builder As StringBuilder,
    	card As Card,
    	modified As DateTime,
    	actionType As ActionType,
    	Optional storeMethod As CardStoreMethod = CardStoreMethod.Default,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of StringBuilder)
C++ __Копировать
     public:
    virtual ValueTask<StringBuilder^> AppendCardAsync(
    	StringBuilder^ builder, 
    	Card^ card, 
    	DateTime modified, 
    	ActionType^ actionType, 
    	CardStoreMethod storeMethod = CardStoreMethod::Default, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract AppendCardAsync : 
            builder : StringBuilder * 
            card : Card * 
            modified : DateTime * 
            actionType : ActionType * 
            ?storeMethod : CardStoreMethod * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _storeMethod = defaultArg storeMethod CardStoreMethod.Default
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<StringBuilder> 
    override AppendCardAsync : 
            builder : StringBuilder * 
            card : Card * 
            modified : DateTime * 
            actionType : ActionType * 
            ?storeMethod : CardStoreMethod * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _storeMethod = defaultArg storeMethod CardStoreMethod.Default
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<StringBuilder> 
#### Параметры
builder
[StringBuilder](https://learn.microsoft.com/dotnet/api/system.text.stringbuilder)
    Объект, содержащий текстовое описание информации о действии.
card [Card](T_Tessa_Cards_Card.htm)
    Создаваемая или изменяемая карточка.
modified [DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)
    Дата и время изменения карточки.
actionType [ActionType](T_Tessa_Platform_Runtime_ActionType.htm)
    Тип действия с карточкой.
storeMethod [CardStoreMethod](T_Tessa_Cards_CardStoreMethod.htm) (Optional)
    Способ сохранения карточки, если описывается сохраняемая карточка.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[StringBuilder](https://learn.microsoft.com/dotnet/api/system.text.stringbuilder)>  
Объект builder для цепочки вызовов.
#### Реализации
[ICardActionDescriptionBuilder.AppendCardAsync(StringBuilder, Card, DateTime,
ActionType, CardStoreMethod,
CancellationToken)](M_Tessa_Cards_ComponentModel_ICardActionDescriptionBuilder_AppendCardAsync.htm)  
##  __См. также
#### Ссылки
[CardActionTextDescriptionBuilder -
](T_Tessa_Cards_ComponentModel_CardActionTextDescriptionBuilder.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
