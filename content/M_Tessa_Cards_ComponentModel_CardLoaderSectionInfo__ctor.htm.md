# CardLoaderSectionInfo - конструктор
Создаёт экземпляр класса с указанием информации по загружаемой секции
карточки.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardLoaderSectionInfo(
    	Guid id,
    	string name,
    	SchemeTableContentType tableType,
    	string queryText,
    	string[] columnNames,
    	CardMetadataType[] columnTypes
    )
VB __Копировать
     Public Sub New ( 
    	id As Guid,
    	name As String,
    	tableType As SchemeTableContentType,
    	queryText As String,
    	columnNames As String(),
    	columnTypes As CardMetadataType()
    )
C++ __Копировать
     public:
    CardLoaderSectionInfo(
    	Guid id, 
    	String^ name, 
    	SchemeTableContentType tableType, 
    	String^ queryText, 
    	array<String^>^ columnNames, 
    	array<CardMetadataType^>^ columnTypes
    )
F# __Копировать
     new : 
            id : Guid * 
            name : string * 
            tableType : SchemeTableContentType * 
            queryText : string * 
            columnNames : string[] * 
            columnTypes : CardMetadataType[] -> CardLoaderSectionInfo
#### Параметры
id [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор загружаемой секции. Идентично идентификатору таблицы.
name [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя загружаемой секции. Идентично имени таблицы.
tableType [SchemeTableContentType](T_Tessa_Scheme_SchemeTableContentType.htm)
    Тип таблицы, в которой сохраняется секция карточки.
queryText [String](https://learn.microsoft.com/dotnet/api/system.string)
    Текст запроса SELECT по загрузке карточки.
columnNames [String](https://learn.microsoft.com/dotnet/api/system.string)[]
     Список колонок, получаемых в результате выполнения запроса queryText. 
columnTypes [CardMetadataType](T_Tessa_Cards_Metadata_CardMetadataType.htm)[]
     Список типов колонок, получаемых в результате выполнения запроса queryText. Аналогичен порядку имён колонок в параметре columnNames. 
## __См. также
#### Ссылки
[CardLoaderSectionInfo -
](T_Tessa_Cards_ComponentModel_CardLoaderSectionInfo.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
