# EntryCardSectionTreeNode - конструктор
Инициализирует новый экземпляр класса
[EntryCardSectionTreeNode](T_Tessa_Cards_SmartMerge_Nodes_EntryCardSectionTreeNode.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Cards.SmartMerge.Nodes](N_Tessa_Cards_SmartMerge_Nodes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public EntryCardSectionTreeNode(
    	Card card,
    	CardSection section,
    	IReadOnlyList<string> ignoredForEqualsColumns = null,
    	IReadOnlyList<string> ignoredForModifyColumns = null
    )
VB __Копировать
     Public Sub New ( 
    	card As Card,
    	section As CardSection,
    	Optional ignoredForEqualsColumns As IReadOnlyList(Of String) = Nothing,
    	Optional ignoredForModifyColumns As IReadOnlyList(Of String) = Nothing
    )
C++ __Копировать
     public:
    EntryCardSectionTreeNode(
    	Card^ card, 
    	CardSection^ section, 
    	IReadOnlyList<String^>^ ignoredForEqualsColumns = nullptr, 
    	IReadOnlyList<String^>^ ignoredForModifyColumns = nullptr
    )
F# __Копировать
     new : 
            card : Card * 
            section : CardSection * 
            ?ignoredForEqualsColumns : IReadOnlyList<string> * 
            ?ignoredForModifyColumns : IReadOnlyList<string> 
    (* Defaults:
            let _ignoredForEqualsColumns = defaultArg ignoredForEqualsColumns null
            let _ignoredForModifyColumns = defaultArg ignoredForModifyColumns null
    *)
    -> EntryCardSectionTreeNode
#### Параметры
card [Card](T_Tessa_Cards_Card.htm)
section [CardSection](T_Tessa_Cards_CardSection.htm)
ignoredForEqualsColumns
[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>
(Optional)
ignoredForModifyColumns
[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>
(Optional)
## __См. также
#### Ссылки
[EntryCardSectionTreeNode -
](T_Tessa_Cards_SmartMerge_Nodes_EntryCardSectionTreeNode.htm)
[Tessa.Cards.SmartMerge.Nodes - пространство
имён](N_Tessa_Cards_SmartMerge_Nodes.htm)
