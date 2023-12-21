# CardMetadataColumn(CardMetadataColumn, Guid) - конструктор
Создаёт экземпляр класса с указанием копируемого объекта и идентификатора типа
карточек.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardMetadataColumn(
    	CardMetadataColumn column,
    	Guid cardTypeID
    )
VB __Копировать
     Public Sub New ( 
    	column As CardMetadataColumn,
    	cardTypeID As Guid
    )
C++ __Копировать
     public:
    CardMetadataColumn(
    	CardMetadataColumn^ column, 
    	Guid cardTypeID
    )
F# __Копировать
     new : 
            column : CardMetadataColumn * 
            cardTypeID : Guid -> CardMetadataColumn
#### Параметры
column [CardMetadataColumn](T_Tessa_Cards_Metadata_CardMetadataColumn.htm)
     Объект, для которого создаётся полная копия, за исключением списка типов карточек. 
cardTypeID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
     Идентификатор типа карточки, который представлен как единственный для создаваемого объекта. 
## __См. также
#### Ссылки
[CardMetadataColumn - ](T_Tessa_Cards_Metadata_CardMetadataColumn.htm)
[CardMetadataColumn -
перегрузка](Overload_Tessa_Cards_Metadata_CardMetadataColumn__ctor.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
