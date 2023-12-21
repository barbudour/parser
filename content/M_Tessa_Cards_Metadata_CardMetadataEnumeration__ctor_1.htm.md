# CardMetadataEnumeration(Guid, String,
CardMetadataEnumerationColumnCollection,
SealableObjectList<CardMetadataRecord>) - конструктор
Создаёт экземпляр класса с указанием свойств перечисления.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardMetadataEnumeration(
    	Guid id,
    	string name,
    	CardMetadataEnumerationColumnCollection columns,
    	SealableObjectList<CardMetadataRecord> records
    )
VB __Копировать
     Public Sub New ( 
    	id As Guid,
    	name As String,
    	columns As CardMetadataEnumerationColumnCollection,
    	records As SealableObjectList(Of CardMetadataRecord)
    )
C++ __Копировать
     public:
    CardMetadataEnumeration(
    	Guid id, 
    	String^ name, 
    	CardMetadataEnumerationColumnCollection^ columns, 
    	SealableObjectList<CardMetadataRecord^>^ records
    )
F# __Копировать
     new : 
            id : Guid * 
            name : string * 
            columns : CardMetadataEnumerationColumnCollection * 
            records : SealableObjectList<CardMetadataRecord> -> CardMetadataEnumeration
#### Параметры
id [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор перечисления.
name [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя перечисления.
columns
[CardMetadataEnumerationColumnCollection](T_Tessa_Cards_Metadata_CardMetadataEnumerationColumnCollection.htm)
    Список колонок, ссылка на который даётся в создаваемом объекте.
records
[SealableObjectList](T_Tessa_Platform_Collections_SealableObjectList_1.htm)<[CardMetadataRecord](T_Tessa_Cards_Metadata_CardMetadataRecord.htm)>
    Список записей, ссылка на который даётся в создаваемом объекте.
##  __См. также
#### Ссылки
[CardMetadataEnumeration -
](T_Tessa_Cards_Metadata_CardMetadataEnumeration.htm)
[CardMetadataEnumeration -
перегрузка](Overload_Tessa_Cards_Metadata_CardMetadataEnumeration__ctor.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
