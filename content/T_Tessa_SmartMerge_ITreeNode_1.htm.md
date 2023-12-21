# ITreeNode<TMergeObject> \- интерфейс
Представляет узел для дерева слияния.
## __Definition
 **Пространство имён:** [Tessa.SmartMerge](N_Tessa_SmartMerge.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ITreeNode<TMergeObject> : IEquatable<ITreeNode<TMergeObject>>
VB __Копировать
     Public Interface ITreeNode(Of TMergeObject)
    	Inherits IEquatable(Of ITreeNode(Of TMergeObject))
C++ __Копировать
    generic<typename TMergeObject>
    public interface class ITreeNode : IEquatable<ITreeNode<TMergeObject>^>
F# __Копировать
     type ITreeNode<'TMergeObject> = 
        interface
            interface IEquatable<ITreeNode<'TMergeObject>>
        end
Implements
    [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<ITreeNode<TMergeObject>>
#### Параметры типа
TMergeObject
    Тип объектов для которых производится слияние.
##  __Заметки
Для вывода текстовой информации по узлу переопределите ToString() в
реализациях узлов.
##  __Свойства
[IgnoreDuplicates](P_Tessa_SmartMerge_ITreeNode_1_IgnoreDuplicates.htm)|
Отражает должен ли игнорироваться узел если логика сочтет его дубликатом.  
---|---  
[Parent](P_Tessa_SmartMerge_ITreeNode_1_Parent.htm)|  Родительский узел.  
[Reference](P_Tessa_SmartMerge_ITreeNode_1_Reference.htm)|  Ссылка на
сопоставленный узел (в другом дереве слияния).  
[State](P_Tessa_SmartMerge_ITreeNode_1_State.htm)|  Состояние узла.  
## __Методы
[AttachTo](M_Tessa_SmartMerge_ITreeNode_1_AttachTo.htm)|  Устанавливает
родительский узел.  
---|---  
[Clone](M_Tessa_SmartMerge_ITreeNode_1_Clone.htm)|  Клонирует узел.  
[Equals](https://learn.microsoft.com/dotnet/api/system.iequatable-1.equals#system-
iequatable-1-equals\(-0\))| Indicates whether the current object is equal to
another object of the same type.  
(Унаследован от
[IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<ITreeNode<TMergeObject>>)  
[EqualsByKey](M_Tessa_SmartMerge_ITreeNode_1_EqualsByKey.htm)|  Сравнение
узлов по ключам с учетом уровня сравнения.  
[GetHashCode](M_Tessa_SmartMerge_ITreeNode_1_GetHashCode.htm)|  Получить хэш-
код объекта в зависимости от уровня сравнения.  
[GetMergeResult](M_Tessa_SmartMerge_ITreeNode_1_GetMergeResult.htm)|  Логика
вычисления результата слияния.  
[SetReference](M_Tessa_SmartMerge_ITreeNode_1_SetReference.htm)|  Сопоставляет
данный узел с узлом в другом дереве слияния.  
[SetState](M_Tessa_SmartMerge_ITreeNode_1_SetState.htm)|  Устанавливает
состояние узла.  
## __См. также
#### Ссылки
[Tessa.SmartMerge - пространство имён](N_Tessa_SmartMerge.htm)
