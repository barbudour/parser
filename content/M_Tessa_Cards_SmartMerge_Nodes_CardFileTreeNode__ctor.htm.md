# CardFileTreeNode - конструктор
Инициализирует новый экземпляр класса
[CardFileTreeNode](T_Tessa_Cards_SmartMerge_Nodes_CardFileTreeNode.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Cards.SmartMerge.Nodes](N_Tessa_Cards_SmartMerge_Nodes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardFileTreeNode(
    	Card card,
    	CardFile file,
    	IReadOnlyList<string> keyColumns = null,
    	IReadOnlyList<string> contentColumns = null,
    	IReadOnlyList<string> includedColumns = null,
    	bool alwaysUpdateContent = false
    )
VB __Копировать
     Public Sub New ( 
    	card As Card,
    	file As CardFile,
    	Optional keyColumns As IReadOnlyList(Of String) = Nothing,
    	Optional contentColumns As IReadOnlyList(Of String) = Nothing,
    	Optional includedColumns As IReadOnlyList(Of String) = Nothing,
    	Optional alwaysUpdateContent As Boolean = false
    )
C++ __Копировать
     public:
    CardFileTreeNode(
    	Card^ card, 
    	CardFile^ file, 
    	IReadOnlyList<String^>^ keyColumns = nullptr, 
    	IReadOnlyList<String^>^ contentColumns = nullptr, 
    	IReadOnlyList<String^>^ includedColumns = nullptr, 
    	bool alwaysUpdateContent = false
    )
F# __Копировать
     new : 
            card : Card * 
            file : CardFile * 
            ?keyColumns : IReadOnlyList<string> * 
            ?contentColumns : IReadOnlyList<string> * 
            ?includedColumns : IReadOnlyList<string> * 
            ?alwaysUpdateContent : bool 
    (* Defaults:
            let _keyColumns = defaultArg keyColumns null
            let _contentColumns = defaultArg contentColumns null
            let _includedColumns = defaultArg includedColumns null
            let _alwaysUpdateContent = defaultArg alwaysUpdateContent false
    *)
    -> CardFileTreeNode
#### Параметры
card [Card](T_Tessa_Cards_Card.htm)
file [CardFile](T_Tessa_Cards_CardFile.htm)
keyColumns
[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>
(Optional)
contentColumns
[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>
(Optional)
includedColumns
[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>
(Optional)
alwaysUpdateContent
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) (Optional)
## __См. также
#### Ссылки
[CardFileTreeNode - ](T_Tessa_Cards_SmartMerge_Nodes_CardFileTreeNode.htm)
[Tessa.Cards.SmartMerge.Nodes - пространство
имён](N_Tessa_Cards_SmartMerge_Nodes.htm)
