# CardMetadataSchemeInfoProvider(ICardMetadata, CardType) - конструктор
Создаёт экземпляр класса с указанием его зависимостей.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardMetadataSchemeInfoProvider(
    	ICardMetadata cardMetadata,
    	CardType cardType
    )
VB __Копировать
     Public Sub New ( 
    	cardMetadata As ICardMetadata,
    	cardType As CardType
    )
C++ __Копировать
     public:
    CardMetadataSchemeInfoProvider(
    	ICardMetadata^ cardMetadata, 
    	CardType^ cardType
    )
F# __Копировать
     new : 
            cardMetadata : ICardMetadata * 
            cardType : CardType -> CardMetadataSchemeInfoProvider
#### Параметры
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация по карточкам, по которой строятся таблицы.
cardType [CardType](T_Tessa_Cards_CardType.htm)
     Тип карточки, для которого создаётся объект, или null, если объект будет возвращать информацию по таблицам для всех типов карточек. 
## __См. также
#### Ссылки
[CardMetadataSchemeInfoProvider -
](T_Tessa_Cards_CardMetadataSchemeInfoProvider.htm)
[CardMetadataSchemeInfoProvider -
перегрузка](Overload_Tessa_Cards_CardMetadataSchemeInfoProvider__ctor.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
