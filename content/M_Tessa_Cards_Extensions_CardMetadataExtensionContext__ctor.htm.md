# CardMetadataExtensionContext - конструктор
Создаёт экземпляр класса с указанием значений его свойств.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardMetadataExtensionContext(
    	CardTypeCollection cardTypes,
    	ISchemeService schemeService,
    	ISerializableObject? info = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Sub New ( 
    	cardTypes As CardTypeCollection,
    	schemeService As ISchemeService,
    	Optional info As ISerializableObject = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    )
C++ __Копировать
     public:
    CardMetadataExtensionContext(
    	CardTypeCollection^ cardTypes, 
    	ISchemeService^ schemeService, 
    	ISerializableObject^ info = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     new : 
            cardTypes : CardTypeCollection * 
            schemeService : ISchemeService * 
            ?info : ISerializableObject * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _info = defaultArg info null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> CardMetadataExtensionContext
#### Параметры
cardTypes [CardTypeCollection](T_Tessa_Cards_CardTypeCollection.htm)
    Типы карточек, используемые для построения метаинформации.
schemeService [ISchemeService](T_Tessa_Scheme_ISchemeService.htm)
    Объект, обеспечивающий доступ к схеме данных.
info [ISerializableObject](T_Tessa_Platform_Storage_ISerializableObject.htm)
(Optional)
    Информация, используемая для передачи между расширениями в цепочке.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
##  __См. также
#### Ссылки
[CardMetadataExtensionContext -
](T_Tessa_Cards_Extensions_CardMetadataExtensionContext.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
