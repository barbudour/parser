# CardNewContext - конструктор
Создаёт экземпляр класса с указанием информации, необходимой для создания
карточки.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardNewContext(
    	Guid cardTypeID,
    	CardNewMode mode,
    	ICardMetadata cardMetadata
    )
VB __Копировать
     Public Sub New ( 
    	cardTypeID As Guid,
    	mode As CardNewMode,
    	cardMetadata As ICardMetadata
    )
C++ __Копировать
     public:
    CardNewContext(
    	Guid cardTypeID, 
    	CardNewMode mode, 
    	ICardMetadata^ cardMetadata
    )
F# __Копировать
     new : 
            cardTypeID : Guid * 
            mode : CardNewMode * 
            cardMetadata : ICardMetadata -> CardNewContext
#### Параметры
cardTypeID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор типа создаваемой карточки.
mode [CardNewMode](T_Tessa_Cards_CardNewMode.htm)
    Способ создания карточки.
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация по типам карточек.
##  __См. также
#### Ссылки
[CardNewContext - ](T_Tessa_Cards_ComponentModel_CardNewContext.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
