# CardMetadataSection(Guid, String, SchemeTableContentType, CardSectionType,
Int32, CardMetadataSectionFlags, String) - конструктор
Создаёт экземпляр класса с указанием свойств секции.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardMetadataSection(
    	Guid id,
    	string name,
    	SchemeTableContentType tableType,
    	CardSectionType sectionType,
    	int order,
    	CardMetadataSectionFlags flags,
    	string group
    )
VB __Копировать
     Public Sub New ( 
    	id As Guid,
    	name As String,
    	tableType As SchemeTableContentType,
    	sectionType As CardSectionType,
    	order As Integer,
    	flags As CardMetadataSectionFlags,
    	group As String
    )
C++ __Копировать
     public:
    CardMetadataSection(
    	Guid id, 
    	String^ name, 
    	SchemeTableContentType tableType, 
    	CardSectionType sectionType, 
    	int order, 
    	CardMetadataSectionFlags flags, 
    	String^ group
    )
F# __Копировать
     new : 
            id : Guid * 
            name : string * 
            tableType : SchemeTableContentType * 
            sectionType : CardSectionType * 
            order : int * 
            flags : CardMetadataSectionFlags * 
            group : string -> CardMetadataSection
#### Параметры
id [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор создаваемой секции.
name [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя создаваемой секции.
tableType [SchemeTableContentType](T_Tessa_Scheme_SchemeTableContentType.htm)
    Тип таблицы для создаваемой секции.
sectionType [CardSectionType](T_Tessa_Cards_CardSectionType.htm)
    Тип создаваемой секции.
order [Int32](https://learn.microsoft.com/dotnet/api/system.int32)
    Порядок сортировки создаваемой секции.
flags
[CardMetadataSectionFlags](T_Tessa_Cards_Metadata_CardMetadataSectionFlags.htm)
    Флаги секции карточки.
group [String](https://learn.microsoft.com/dotnet/api/system.string)
    Наименование группы секции.
##  __См. также
#### Ссылки
[CardMetadataSection - ](T_Tessa_Cards_Metadata_CardMetadataSection.htm)
[CardMetadataSection -
перегрузка](Overload_Tessa_Cards_Metadata_CardMetadataSection__ctor.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
