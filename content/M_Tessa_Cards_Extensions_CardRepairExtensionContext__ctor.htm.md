# CardRepairExtensionContext - конструктор
Создаёт экземпляр класса с указанием значений его свойств.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardRepairExtensionContext(
    	Card card,
    	CardType cardType,
    	string cardTypeName,
    	ICardMetadata cardMetadata,
    	ICardRepairManager defaultManager,
    	ICardRepairManager extendedManager,
    	ICardRepairExtensionContext parentContext = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Sub New ( 
    	card As Card,
    	cardType As CardType,
    	cardTypeName As String,
    	cardMetadata As ICardMetadata,
    	defaultManager As ICardRepairManager,
    	extendedManager As ICardRepairManager,
    	Optional parentContext As ICardRepairExtensionContext = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    )
C++ __Копировать
     public:
    CardRepairExtensionContext(
    	Card^ card, 
    	CardType^ cardType, 
    	String^ cardTypeName, 
    	ICardMetadata^ cardMetadata, 
    	ICardRepairManager^ defaultManager, 
    	ICardRepairManager^ extendedManager, 
    	ICardRepairExtensionContext^ parentContext = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     new : 
            card : Card * 
            cardType : CardType * 
            cardTypeName : string * 
            cardMetadata : ICardMetadata * 
            defaultManager : ICardRepairManager * 
            extendedManager : ICardRepairManager * 
            ?parentContext : ICardRepairExtensionContext * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _parentContext = defaultArg parentContext null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> CardRepairExtensionContext
#### Параметры
card [Card](T_Tessa_Cards_Card.htm)
    Карточка, для которой выполняется исправление структуры.
cardType [CardType](T_Tessa_Cards_CardType.htm)
    Тип карточки или null, если тип карточки неизвестен.
cardTypeName [String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя типа карточки или null, если имя типа неизвестно. Имя может быть задано для несуществующего типа карточки. 
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация по типам карточек.
defaultManager [ICardRepairManager](T_Tessa_Cards_ICardRepairManager.htm)
    Объект, управляющий исправлением структуры карточки без расширений.
extendedManager [ICardRepairManager](T_Tessa_Cards_ICardRepairManager.htm)
    Объект, управляющий исправлением структуры карточки с расширениями.
parentContext
[ICardRepairExtensionContext](T_Tessa_Cards_Extensions_ICardRepairExtensionContext.htm)
(Optional)
     Контекст по исправлению родительской карточки или null, если текущая исправляемая карточка не связана с родительской карточкой, т.е. не является сателлитом. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
##  __См. также
#### Ссылки
[CardRepairExtensionContext -
](T_Tessa_Cards_Extensions_CardRepairExtensionContext.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
