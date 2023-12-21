# TypeExtensionContext - конструктор
Создаёт экземпляр класса с указанием значений его свойств.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public TypeExtensionContext(
    	Card mainCard,
    	CardType mainCardType,
    	ICardMetadata cardMetadata,
    	IValidationResultBuilder validationResult,
    	Object externalContext = null,
    	Dictionary<string, Object> info = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Sub New ( 
    	mainCard As Card,
    	mainCardType As CardType,
    	cardMetadata As ICardMetadata,
    	validationResult As IValidationResultBuilder,
    	Optional externalContext As Object = Nothing,
    	Optional info As Dictionary(Of String, Object) = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    )
C++ __Копировать
     public:
    TypeExtensionContext(
    	Card^ mainCard, 
    	CardType^ mainCardType, 
    	ICardMetadata^ cardMetadata, 
    	IValidationResultBuilder^ validationResult, 
    	Object^ externalContext = nullptr, 
    	Dictionary<String^, Object^>^ info = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     new : 
            mainCard : Card * 
            mainCardType : CardType * 
            cardMetadata : ICardMetadata * 
            validationResult : IValidationResultBuilder * 
            ?externalContext : Object * 
            ?info : Dictionary<string, Object> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _externalContext = defaultArg externalContext null
            let _info = defaultArg info null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> TypeExtensionContext
#### Параметры
mainCard [Card](T_Tessa_Cards_Card.htm)
     Карточка, в рамках которой выполняется расширение. Не должно быть равно null. Устанавливает свойства [MainCard](P_Tessa_Cards_TypeExtensionContext_MainCard.htm) и [Card](P_Tessa_Cards_TypeExtensionContext_Card.htm). 
mainCardType [CardType](T_Tessa_Cards_CardType.htm)
     Тип карточки, в рамках которого выполняется расширение. Не должен быть равен null. Устанавливает свойства [MainCardType](P_Tessa_Cards_TypeExtensionContext_MainCardType.htm) и [CardType](P_Tessa_Cards_TypeExtensionContext_CardType.htm). 
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
     Метаинформация по типам карточек, файлов и заданий. 
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
     Конструктор результата валидации. 
externalContext [Object](https://learn.microsoft.com/dotnet/api/system.object)
(Optional)
     Внешний контекст расширения, в рамках которого выполняется расширение на тип карточки, или null, если такой контекст неизвестен. 
info
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)> (Optional)
     Дополнительная информация, связанная с контекстом, или null, если дополнительная информация не задана. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
##  __См. также
#### Ссылки
[TypeExtensionContext - ](T_Tessa_Cards_TypeExtensionContext.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
