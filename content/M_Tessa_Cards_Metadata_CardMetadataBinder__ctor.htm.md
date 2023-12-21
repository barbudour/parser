# CardMetadataBinder - конструктор
Создаёт экземпляр класса с указанием карточки и метаинформации, которая может
быть использована для карточки заданного типа.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardMetadataBinder(
    	Card card,
    	ICardMetadata cardMetadata
    )
VB __Копировать
     Public Sub New ( 
    	card As Card,
    	cardMetadata As ICardMetadata
    )
C++ __Копировать
     public:
    CardMetadataBinder(
    	Card^ card, 
    	ICardMetadata^ cardMetadata
    )
F# __Копировать
     new : 
            card : Card * 
            cardMetadata : ICardMetadata -> CardMetadataBinder
#### Параметры
card [Card](T_Tessa_Cards_Card.htm)
    Карточка, для которой требуется создать вспомогательный класс.
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация, которая может быть использована для карточки заданного типа.
##  __См. также
#### Ссылки
[CardMetadataBinder - ](T_Tessa_Cards_Metadata_CardMetadataBinder.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
