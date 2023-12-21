# CardMetadataExtensionContext.CardMetadata - свойство
Построенная метаинформация по типам карточек, которую расширение может
изменять, или null, если расширение вызвано на этапе, на котором
метаинформация ещё не построена.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ICardMetadata? CardMetadata { get; set; }
VB __Копировать
     Public Property CardMetadata As ICardMetadata
    	Get
    	Set
C++ __Копировать
     public:
    virtual property ICardMetadata^ CardMetadata {
    	ICardMetadata^ get () sealed;
    	void set (ICardMetadata^ value) sealed;
    }
F# __Копировать
     abstract CardMetadata : ICardMetadata with get, set
    override CardMetadata : ICardMetadata with get, set
#### Значение свойства
[ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
#### Реализации
[ICardMetadataExtensionContext.CardMetadata](P_Tessa_Cards_Extensions_ICardMetadataExtensionContext_CardMetadata.htm)  
##  __См. также
#### Ссылки
[CardMetadataExtensionContext -
](T_Tessa_Cards_Extensions_CardMetadataExtensionContext.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
