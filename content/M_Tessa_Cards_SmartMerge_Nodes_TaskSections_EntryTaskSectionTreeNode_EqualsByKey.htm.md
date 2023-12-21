# EntryTaskSectionTreeNode.EqualsByKey - метод
Сравнение узлов по ключам с учетом уровня сравнения.
## __Definition
 **Пространство имён:**
[Tessa.Cards.SmartMerge.Nodes.TaskSections](N_Tessa_Cards_SmartMerge_Nodes_TaskSections.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public override bool EqualsByKey(
    	ITreeNode<Card> other,
    	int compareLevel
    )
VB __Копировать
     Public Overrides Function EqualsByKey ( 
    	other As ITreeNode(Of Card),
    	compareLevel As Integer
    ) As Boolean
C++ __Копировать
     public:
    virtual bool EqualsByKey(
    	ITreeNode<Card^>^ other, 
    	int compareLevel
    ) override
F# __Копировать
     abstract EqualsByKey : 
            other : ITreeNode<Card> * 
            compareLevel : int -> bool 
    override EqualsByKey : 
            other : ITreeNode<Card> * 
            compareLevel : int -> bool 
#### Параметры
other
[ITreeNode](T_Tessa_SmartMerge_ITreeNode_1.htm)<[Card](T_Tessa_Cards_Card.htm)>
    Узел для сравнения.
compareLevel [Int32](https://learn.microsoft.com/dotnet/api/system.int32)
    Уровень сравнения.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
#### Реализации
[ITreeNode<TMergeObject>.EqualsByKey(ITreeNode<TMergeObject>,
Int32)](M_Tessa_SmartMerge_ITreeNode_1_EqualsByKey.htm)  
##  __См. также
#### Ссылки
[EntryTaskSectionTreeNode -
](T_Tessa_Cards_SmartMerge_Nodes_TaskSections_EntryTaskSectionTreeNode.htm)
[Tessa.Cards.SmartMerge.Nodes.TaskSections - пространство
имён](N_Tessa_Cards_SmartMerge_Nodes_TaskSections.htm)
