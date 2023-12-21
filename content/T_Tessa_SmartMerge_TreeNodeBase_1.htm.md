# TreeNodeBase<T> \- класс
##  __Definition
 **Пространство имён:** [Tessa.SmartMerge](N_Tessa_SmartMerge.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class TreeNodeBase<T> : ITreeNode<T>, 
    	IEquatable<ITreeNode<T>>
VB __Копировать
     Public MustInherit Class TreeNodeBase(Of T)
    	Implements ITreeNode(Of T), IEquatable(Of ITreeNode(Of T))
C++ __Копировать
    generic<typename T>
    public ref class TreeNodeBase abstract : ITreeNode<T>, 
    	IEquatable<ITreeNode<T>^>
F# __Копировать
     [<AbstractClassAttribute>]
    type TreeNodeBase<'T> = 
        class
            interface ITreeNode<'T>
            interface IEquatable<ITreeNode<'T>>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ TreeNodeBase<T>
Derived
[Tessa.Cards.SmartMerge.Nodes.CardTreeNodeBase](T_Tessa_Cards_SmartMerge_Nodes_CardTreeNodeBase.htm)
Implements
    [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<[ITreeNode](T_Tessa_SmartMerge_ITreeNode_1.htm)<T>>, [ITreeNode](T_Tessa_SmartMerge_ITreeNode_1.htm)<T>
#### Параметры типа
T
##  __Конструкторы
[TreeNodeBase<T>](M_Tessa_SmartMerge_TreeNodeBase_1__ctor.htm)| Инициализирует
новый экземпляр класса TreeNodeBase<T>  
---|---  
##  __Свойства
[IgnoreDuplicates](P_Tessa_SmartMerge_TreeNodeBase_1_IgnoreDuplicates.htm)|
Отражает должен ли игнорироваться узел если логика сочтет его дубликатом.  
---|---  
[Parent](P_Tessa_SmartMerge_TreeNodeBase_1_Parent.htm)|  Родительский узел.  
[Reference](P_Tessa_SmartMerge_TreeNodeBase_1_Reference.htm)|  Ссылка на
сопоставленный узел (в другом дереве слияния).  
[State](P_Tessa_SmartMerge_TreeNodeBase_1_State.htm)|  Состояние узла.  
## __Методы
[AttachTo](M_Tessa_SmartMerge_TreeNodeBase_1_AttachTo.htm)|  Устанавливает
родительский узел.  
---|---  
[CheckTypeAndGetReferenceNode<TNode>](M_Tessa_SmartMerge_TreeNodeBase_1_CheckTypeAndGetReferenceNode__1.htm)|
Проверяет соответствие типа узла, сопоставленного с текущим узлом и получает
его.  
[Clone](M_Tessa_SmartMerge_TreeNodeBase_1_Clone.htm)|  Клонирует узел.  
[Equals(ITreeNode<T>)](M_Tessa_SmartMerge_TreeNodeBase_1_Equals.htm)|
Indicates whether the current object is equal to another object of the same
type.  
[Equals(Object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[EqualsByKey](M_Tessa_SmartMerge_TreeNodeBase_1_EqualsByKey.htm)|  Сравнение
узлов по ключам с учетом уровня сравнения.  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode(Int32)](M_Tessa_SmartMerge_TreeNodeBase_1_GetHashCode.htm)|
Получить хэш-код объекта в зависимости от уровня сравнения.  
[GetMergeResult](M_Tessa_SmartMerge_TreeNodeBase_1_GetMergeResult.htm)|
Логика вычисления результата слияния.  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[SetReference](M_Tessa_SmartMerge_TreeNodeBase_1_SetReference.htm)|
Сопоставляет данный узел с узлом в другом дереве слияния.  
[SetState](M_Tessa_SmartMerge_TreeNodeBase_1_SetState.htm)|  Устанавливает
состояние узла.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.SmartMerge - пространство имён](N_Tessa_SmartMerge.htm)
