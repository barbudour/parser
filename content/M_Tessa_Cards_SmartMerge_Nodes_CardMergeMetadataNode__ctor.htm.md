# CardMergeMetadataNode - конструктор
Инициализирует новый экземпляр класса
[CardMergeMetadataNode](T_Tessa_Cards_SmartMerge_Nodes_CardMergeMetadataNode.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Cards.SmartMerge.Nodes](N_Tessa_Cards_SmartMerge_Nodes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardMergeMetadataNode(
    	string sectionName,
    	string sectionParentName,
    	string sectionParentColumnName,
    	IReadOnlyList<string> sectionIgnoredForEqualsColumns,
    	IReadOnlyList<string> keyColumns,
    	IReadOnlyList<string> sectionIgnoredForModifyColumns,
    	bool isIgnored,
    	bool? ignoreDuplicateRows,
    	CardMergeMetaType metaType,
    	Guid? cardID,
    	IReadOnlyList<string> fileContentColumns = null,
    	IReadOnlyList<string> fileIncludedColumns = null
    )
VB __Копировать
     Public Sub New ( 
    	sectionName As String,
    	sectionParentName As String,
    	sectionParentColumnName As String,
    	sectionIgnoredForEqualsColumns As IReadOnlyList(Of String),
    	keyColumns As IReadOnlyList(Of String),
    	sectionIgnoredForModifyColumns As IReadOnlyList(Of String),
    	isIgnored As Boolean,
    	ignoreDuplicateRows As Boolean?,
    	metaType As CardMergeMetaType,
    	cardID As Guid?,
    	Optional fileContentColumns As IReadOnlyList(Of String) = Nothing,
    	Optional fileIncludedColumns As IReadOnlyList(Of String) = Nothing
    )
C++ __Копировать
     public:
    CardMergeMetadataNode(
    	String^ sectionName, 
    	String^ sectionParentName, 
    	String^ sectionParentColumnName, 
    	IReadOnlyList<String^>^ sectionIgnoredForEqualsColumns, 
    	IReadOnlyList<String^>^ keyColumns, 
    	IReadOnlyList<String^>^ sectionIgnoredForModifyColumns, 
    	bool isIgnored, 
    	Nullable<bool> ignoreDuplicateRows, 
    	CardMergeMetaType metaType, 
    	Nullable<Guid> cardID, 
    	IReadOnlyList<String^>^ fileContentColumns = nullptr, 
    	IReadOnlyList<String^>^ fileIncludedColumns = nullptr
    )
F# __Копировать
     new : 
            sectionName : string * 
            sectionParentName : string * 
            sectionParentColumnName : string * 
            sectionIgnoredForEqualsColumns : IReadOnlyList<string> * 
            keyColumns : IReadOnlyList<string> * 
            sectionIgnoredForModifyColumns : IReadOnlyList<string> * 
            isIgnored : bool * 
            ignoreDuplicateRows : Nullable<bool> * 
            metaType : CardMergeMetaType * 
            cardID : Nullable<Guid> * 
            ?fileContentColumns : IReadOnlyList<string> * 
            ?fileIncludedColumns : IReadOnlyList<string> 
    (* Defaults:
            let _fileContentColumns = defaultArg fileContentColumns null
            let _fileIncludedColumns = defaultArg fileIncludedColumns null
    *)
    -> CardMergeMetadataNode
#### Параметры
sectionName [String](https://learn.microsoft.com/dotnet/api/system.string)
sectionParentName
[String](https://learn.microsoft.com/dotnet/api/system.string)
sectionParentColumnName
[String](https://learn.microsoft.com/dotnet/api/system.string)
sectionIgnoredForEqualsColumns
[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>
keyColumns
[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>
sectionIgnoredForModifyColumns
[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>
isIgnored [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
ignoreDuplicateRows
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>
metaType [CardMergeMetaType](T_Tessa_Cards_SmartMerge_CardMergeMetaType.htm)
cardID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
fileContentColumns
[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>
(Optional)
fileIncludedColumns
[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>
(Optional)
## __См. также
#### Ссылки
[CardMergeMetadataNode -
](T_Tessa_Cards_SmartMerge_Nodes_CardMergeMetadataNode.htm)
[Tessa.Cards.SmartMerge.Nodes - пространство
имён](N_Tessa_Cards_SmartMerge_Nodes.htm)
