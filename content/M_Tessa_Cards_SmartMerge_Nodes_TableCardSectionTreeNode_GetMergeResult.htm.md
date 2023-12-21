# TableCardSectionTreeNode.GetMergeResult - метод
Логика вычисления результата слияния.
## __Definition
 **Пространство имён:**
[Tessa.Cards.SmartMerge.Nodes](N_Tessa_Cards_SmartMerge_Nodes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public override IMergeResultItem<Card> GetMergeResult()
VB __Копировать
     Public Overrides Function GetMergeResult As IMergeResultItem(Of Card)
C++ __Копировать
     public:
    virtual IMergeResultItem<Card^>^ GetMergeResult() override
F# __Копировать
     abstract GetMergeResult : unit -> IMergeResultItem<Card> 
    override GetMergeResult : unit -> IMergeResultItem<Card> 
#### Возвращаемое значение
[IMergeResultItem](T_Tessa_SmartMerge_IMergeResultItem_1.htm)<[Card](T_Tessa_Cards_Card.htm)>  
Результат слияния для узла.
#### Реализации
[ITreeNode<TMergeObject>.GetMergeResult()](M_Tessa_SmartMerge_ITreeNode_1_GetMergeResult.htm)  
##  __См. также
#### Ссылки
[TableCardSectionTreeNode -
](T_Tessa_Cards_SmartMerge_Nodes_TableCardSectionTreeNode.htm)
[Tessa.Cards.SmartMerge.Nodes - пространство
имён](N_Tessa_Cards_SmartMerge_Nodes.htm)
