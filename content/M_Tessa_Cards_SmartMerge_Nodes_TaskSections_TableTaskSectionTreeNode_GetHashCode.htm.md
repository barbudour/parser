# TableTaskSectionTreeNode.GetHashCode(Int32) - метод
Получить хэш-код объекта в зависимости от уровня сравнения.
## __Definition
 **Пространство имён:**
[Tessa.Cards.SmartMerge.Nodes.TaskSections](N_Tessa_Cards_SmartMerge_Nodes_TaskSections.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public override int? GetHashCode(
    	int compareLevel
    )
VB __Копировать
     Public Overrides Function GetHashCode ( 
    	compareLevel As Integer
    ) As Integer?
C++ __Копировать
     public:
    virtual Nullable<int> GetHashCode(
    	int compareLevel
    ) override
F# __Копировать
     abstract GetHashCode : 
            compareLevel : int -> Nullable<int> 
    override GetHashCode : 
            compareLevel : int -> Nullable<int> 
#### Параметры
compareLevel [Int32](https://learn.microsoft.com/dotnet/api/system.int32)
    Уровень сравнения.
#### Возвращаемое значение
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Int32](https://learn.microsoft.com/dotnet/api/system.int32)>  
#### Реализации
[ITreeNode<TMergeObject>.GetHashCode(Int32)](M_Tessa_SmartMerge_ITreeNode_1_GetHashCode.htm)  
##  __См. также
#### Ссылки
[TableTaskSectionTreeNode -
](T_Tessa_Cards_SmartMerge_Nodes_TaskSections_TableTaskSectionTreeNode.htm)
[GetHashCode -
перегрузка](Overload_Tessa_Cards_SmartMerge_Nodes_TaskSections_TableTaskSectionTreeNode_GetHashCode.htm)
[Tessa.Cards.SmartMerge.Nodes.TaskSections - пространство
имён](N_Tessa_Cards_SmartMerge_Nodes_TaskSections.htm)
