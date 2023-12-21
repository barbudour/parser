# TableTaskSectionTreeNode - конструктор
Инициализирует новый экземпляр класса
[TableTaskSectionTreeNode](T_Tessa_Cards_SmartMerge_Nodes_TaskSections_TableTaskSectionTreeNode.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Cards.SmartMerge.Nodes.TaskSections](N_Tessa_Cards_SmartMerge_Nodes_TaskSections.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public TableTaskSectionTreeNode(
    	Card card,
    	CardTask task,
    	CardSection section,
    	CardRow row,
    	IReadOnlyList<string> ignoredForEqualsColumns,
    	IReadOnlyList<string> keyColumns,
    	string parentKeyColumn,
    	ITreeNode<Card> parent,
    	IReadOnlyList<string> ignoredForModifyColumns = null,
    	bool? ignoreDuplicates = null
    )
VB __Копировать
     Public Sub New ( 
    	card As Card,
    	task As CardTask,
    	section As CardSection,
    	row As CardRow,
    	ignoredForEqualsColumns As IReadOnlyList(Of String),
    	keyColumns As IReadOnlyList(Of String),
    	parentKeyColumn As String,
    	parent As ITreeNode(Of Card),
    	Optional ignoredForModifyColumns As IReadOnlyList(Of String) = Nothing,
    	Optional ignoreDuplicates As Boolean? = Nothing
    )
C++ __Копировать
     public:
    TableTaskSectionTreeNode(
    	Card^ card, 
    	CardTask^ task, 
    	CardSection^ section, 
    	CardRow^ row, 
    	IReadOnlyList<String^>^ ignoredForEqualsColumns, 
    	IReadOnlyList<String^>^ keyColumns, 
    	String^ parentKeyColumn, 
    	ITreeNode<Card^>^ parent, 
    	IReadOnlyList<String^>^ ignoredForModifyColumns = nullptr, 
    	Nullable<bool> ignoreDuplicates = nullptr
    )
F# __Копировать
     new : 
            card : Card * 
            task : CardTask * 
            section : CardSection * 
            row : CardRow * 
            ignoredForEqualsColumns : IReadOnlyList<string> * 
            keyColumns : IReadOnlyList<string> * 
            parentKeyColumn : string * 
            parent : ITreeNode<Card> * 
            ?ignoredForModifyColumns : IReadOnlyList<string> * 
            ?ignoreDuplicates : Nullable<bool> 
    (* Defaults:
            let _ignoredForModifyColumns = defaultArg ignoredForModifyColumns null
            let _ignoreDuplicates = defaultArg ignoreDuplicates null
    *)
    -> TableTaskSectionTreeNode
#### Параметры
card [Card](T_Tessa_Cards_Card.htm)
task [CardTask](T_Tessa_Cards_CardTask.htm)
section [CardSection](T_Tessa_Cards_CardSection.htm)
row [CardRow](T_Tessa_Cards_CardRow.htm)
ignoredForEqualsColumns
[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>
keyColumns
[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>
parentKeyColumn [String](https://learn.microsoft.com/dotnet/api/system.string)
parent
[ITreeNode](T_Tessa_SmartMerge_ITreeNode_1.htm)<[Card](T_Tessa_Cards_Card.htm)>
ignoredForModifyColumns
[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>
(Optional)
ignoreDuplicates
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>
(Optional)
## __См. также
#### Ссылки
[TableTaskSectionTreeNode -
](T_Tessa_Cards_SmartMerge_Nodes_TaskSections_TableTaskSectionTreeNode.htm)
[Tessa.Cards.SmartMerge.Nodes.TaskSections - пространство
имён](N_Tessa_Cards_SmartMerge_Nodes_TaskSections.htm)
