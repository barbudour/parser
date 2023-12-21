# CardMetadataColumn(Guid, String, SchemeType, CardMetadataColumnType,
SealableList<Guid>, Object, Object, CardMetadataSectionReference,
CardMetadataSectionReference, Int16, Boolean) - конструктор
Создаёт экземпляр класса с указанием свойств колонки.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardMetadataColumn(
    	Guid id,
    	string name,
    	SchemeType schemeType,
    	CardMetadataColumnType columnType,
    	SealableList<Guid> cardTypeIDList,
    	Object defaultValue,
    	Object defaultValidValue,
    	CardMetadataSectionReference parentRowSection,
    	CardMetadataSectionReference referencedSection,
    	short complexColumnIndex,
    	bool isReference
    )
VB __Копировать
     Public Sub New ( 
    	id As Guid,
    	name As String,
    	schemeType As SchemeType,
    	columnType As CardMetadataColumnType,
    	cardTypeIDList As SealableList(Of Guid),
    	defaultValue As Object,
    	defaultValidValue As Object,
    	parentRowSection As CardMetadataSectionReference,
    	referencedSection As CardMetadataSectionReference,
    	complexColumnIndex As Short,
    	isReference As Boolean
    )
C++ __Копировать
     public:
    CardMetadataColumn(
    	Guid id, 
    	String^ name, 
    	SchemeType^ schemeType, 
    	CardMetadataColumnType columnType, 
    	SealableList<Guid>^ cardTypeIDList, 
    	Object^ defaultValue, 
    	Object^ defaultValidValue, 
    	CardMetadataSectionReference^ parentRowSection, 
    	CardMetadataSectionReference^ referencedSection, 
    	short complexColumnIndex, 
    	bool isReference
    )
F# __Копировать
     new : 
            id : Guid * 
            name : string * 
            schemeType : SchemeType * 
            columnType : CardMetadataColumnType * 
            cardTypeIDList : SealableList<Guid> * 
            defaultValue : Object * 
            defaultValidValue : Object * 
            parentRowSection : CardMetadataSectionReference * 
            referencedSection : CardMetadataSectionReference * 
            complexColumnIndex : int16 * 
            isReference : bool -> CardMetadataColumn
#### Параметры
id [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор создаваемой колонки.
name [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя создаваемой колонки.
schemeType [SchemeType](T_Tessa_Scheme_SchemeType.htm)
    Тип колонки из схемы.
columnType
[CardMetadataColumnType](T_Tessa_Cards_Metadata_CardMetadataColumnType.htm)
    Тип колонки.
cardTypeIDList
[SealableList](T_Tessa_Platform_Collections_SealableList_1.htm)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
    Список типов карточек.
defaultValue [Object](https://learn.microsoft.com/dotnet/api/system.object)
    Значение колонки по умолчанию.
defaultValidValue
[Object](https://learn.microsoft.com/dotnet/api/system.object)
    Значение колонки по умолчанию, которое всегда является валидным при сохранении.
parentRowSection
[CardMetadataSectionReference](T_Tessa_Cards_Metadata_CardMetadataSectionReference.htm)
    Секция, на строку которой ссылается текущая колонка.
referencedSection
[CardMetadataSectionReference](T_Tessa_Cards_Metadata_CardMetadataSectionReference.htm)
     Секция, на которую ссылается комплексная колонка, или null, если колонка является физической. 
complexColumnIndex
[Int16](https://learn.microsoft.com/dotnet/api/system.int16)
     Уникальный в пределах таблицы отсчитываемый от нуля индекс, если текущая колонка комплексная, или индекс комплексной колонки, в которую включена текущая физическая колонка, или -1, если текущая физическая колонка не включена в комплексную колонку. 
isReference [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
     Признак того, что колонка является ссылочной и входит во внешний ключ при его наличии. Значение актуально только для физических колонок. 
## __См. также
#### Ссылки
[CardMetadataColumn - ](T_Tessa_Cards_Metadata_CardMetadataColumn.htm)
[CardMetadataColumn -
перегрузка](Overload_Tessa_Cards_Metadata_CardMetadataColumn__ctor.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
