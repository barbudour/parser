# CardMetadataSchemeInfoProvider.CreateForCardType - метод
Создает экземпляр
[ICardSchemeInfoProvider](T_Tessa_Cards_ICardSchemeInfoProvider.htm),
содержащий таблицы из основной схемы и виртуальной схемы типа карточки
cardType.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ICardSchemeInfoProvider CreateForCardType(
    	CardType cardType
    )
VB __Копировать
     Public Function CreateForCardType ( 
    	cardType As CardType
    ) As ICardSchemeInfoProvider
C++ __Копировать
     public:
    virtual ICardSchemeInfoProvider^ CreateForCardType(
    	CardType^ cardType
    ) sealed
F# __Копировать
     abstract CreateForCardType : 
            cardType : CardType -> ICardSchemeInfoProvider 
    override CreateForCardType : 
            cardType : CardType -> ICardSchemeInfoProvider 
#### Параметры
cardType [CardType](T_Tessa_Cards_CardType.htm)
    Тип карточки, для которого создаётся метаинформация. Не должен быть равен null.
#### Возвращаемое значение
[ICardSchemeInfoProvider](T_Tessa_Cards_ICardSchemeInfoProvider.htm)  
Созданный объект.
#### Реализации
[ICardSchemeInfoProvider.CreateForCardType(CardType)](M_Tessa_Cards_ICardSchemeInfoProvider_CreateForCardType.htm)  
##  __См. также
#### Ссылки
[CardMetadataSchemeInfoProvider -
](T_Tessa_Cards_CardMetadataSchemeInfoProvider.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
