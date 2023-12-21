# CardSectionTreeNodeBase - класс
##  __Definition
 **Пространство имён:**
[Tessa.Cards.SmartMerge.Nodes](N_Tessa_Cards_SmartMerge_Nodes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class CardSectionTreeNodeBase : CardTreeNodeBase
VB __Копировать
     Public MustInherit Class CardSectionTreeNodeBase
    	Inherits CardTreeNodeBase
C++ __Копировать
     public ref class CardSectionTreeNodeBase abstract : public CardTreeNodeBase
F# __Копировать
     [<AbstractClassAttribute>]
    type CardSectionTreeNodeBase = 
        class
            inherit CardTreeNodeBase
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[TreeNodeBase](T_Tessa_SmartMerge_TreeNodeBase_1.htm)<[Card](T_Tessa_Cards_Card.htm)> __[CardTreeNodeBase](T_Tessa_Cards_SmartMerge_Nodes_CardTreeNodeBase.htm) __ CardSectionTreeNodeBase
Derived
[Tessa.Cards.SmartMerge.Nodes.EntryCardSectionTreeNode](T_Tessa_Cards_SmartMerge_Nodes_EntryCardSectionTreeNode.htm)
[Tessa.Cards.SmartMerge.Nodes.TableCardSectionTreeNode](T_Tessa_Cards_SmartMerge_Nodes_TableCardSectionTreeNode.htm)
[Tessa.Cards.SmartMerge.Nodes.TaskSections.TaskTreeNodeBase](T_Tessa_Cards_SmartMerge_Nodes_TaskSections_TaskTreeNodeBase.htm)
##  __Конструкторы
[CardSectionTreeNodeBase](M_Tessa_Cards_SmartMerge_Nodes_CardSectionTreeNodeBase__ctor.htm)|
Инициализирует новый экземпляр класса CardSectionTreeNodeBase  
---|---  
##  __Свойства
[Card](P_Tessa_Cards_SmartMerge_Nodes_CardTreeNodeBase_Card.htm)|  Карточка,
относящаяся к данному узлу.  
(Унаследован от
[CardTreeNodeBase](T_Tessa_Cards_SmartMerge_Nodes_CardTreeNodeBase.htm))  
---|---  
[IDHash](P_Tessa_Cards_SmartMerge_Nodes_CardSectionTreeNodeBase_IDHash.htm)|
Значение, используемое при сопоставлении узлов.  
[IgnoredForEqualsColumns](P_Tessa_Cards_SmartMerge_Nodes_CardSectionTreeNodeBase_IgnoredForEqualsColumns.htm)|
Список колонок секции, которые будут проигнорированы при сравнении узлов по
значениям.  
[IgnoredForModifyColumns](P_Tessa_Cards_SmartMerge_Nodes_CardSectionTreeNodeBase_IgnoredForModifyColumns.htm)|
Список колонок секции, которые будут проигнорированы даже если значения в них
модифицированы.  
[IgnoreDuplicates](P_Tessa_SmartMerge_TreeNodeBase_1_IgnoreDuplicates.htm)|
Отражает должен ли игнорироваться узел если логика сочтет его дубликатом.  
(Унаследован от [TreeNodeBase<T>](T_Tessa_SmartMerge_TreeNodeBase_1.htm))  
[Parent](P_Tessa_SmartMerge_TreeNodeBase_1_Parent.htm)|  Родительский узел.  
(Унаследован от [TreeNodeBase<T>](T_Tessa_SmartMerge_TreeNodeBase_1.htm))  
[Reference](P_Tessa_SmartMerge_TreeNodeBase_1_Reference.htm)|  Ссылка на
сопоставленный узел (в другом дереве слияния).  
(Унаследован от [TreeNodeBase<T>](T_Tessa_SmartMerge_TreeNodeBase_1.htm))  
[Row](P_Tessa_Cards_SmartMerge_Nodes_CardSectionTreeNodeBase_Row.htm)|  Строка
табличнной секции, относящаяся к данному узлу.  
[Section](P_Tessa_Cards_SmartMerge_Nodes_CardSectionTreeNodeBase_Section.htm)|
Секция карточки, относящаяся к данному узлу.  
[State](P_Tessa_SmartMerge_TreeNodeBase_1_State.htm)|  Состояние узла.  
(Унаследован от [TreeNodeBase<T>](T_Tessa_SmartMerge_TreeNodeBase_1.htm))  
[ValueHash](P_Tessa_Cards_SmartMerge_Nodes_CardSectionTreeNodeBase_ValueHash.htm)|
Значение, используемое для сравнения значений узлов.  
## __Методы
[AttachTo](M_Tessa_SmartMerge_TreeNodeBase_1_AttachTo.htm)|  Устанавливает
родительский узел.  
(Унаследован от [TreeNodeBase<T>](T_Tessa_SmartMerge_TreeNodeBase_1.htm))  
---|---  
[CheckTypeAndGetReferenceNode<TNode>](M_Tessa_SmartMerge_TreeNodeBase_1_CheckTypeAndGetReferenceNode__1.htm)|
Проверяет соответствие типа узла, сопоставленного с текущим узлом и получает
его.  
(Унаследован от [TreeNodeBase<T>](T_Tessa_SmartMerge_TreeNodeBase_1.htm))  
[Clone](M_Tessa_SmartMerge_TreeNodeBase_1_Clone.htm)|  Клонирует узел.  
(Унаследован от [TreeNodeBase<T>](T_Tessa_SmartMerge_TreeNodeBase_1.htm))  
[Equals(ITreeNode<T>)](M_Tessa_SmartMerge_TreeNodeBase_1_Equals.htm)|
Indicates whether the current object is equal to another object of the same
type.  
(Унаследован от [TreeNodeBase<T>](T_Tessa_SmartMerge_TreeNodeBase_1.htm))  
[Equals(Object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[EqualsByKey](M_Tessa_SmartMerge_TreeNodeBase_1_EqualsByKey.htm)|  Сравнение
узлов по ключам с учетом уровня сравнения.  
(Унаследован от [TreeNodeBase<T>](T_Tessa_SmartMerge_TreeNodeBase_1.htm))  
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
(Унаследован от [TreeNodeBase<T>](T_Tessa_SmartMerge_TreeNodeBase_1.htm))  
[GetMergeResult](M_Tessa_SmartMerge_TreeNodeBase_1_GetMergeResult.htm)|
Логика вычисления результата слияния.  
(Унаследован от [TreeNodeBase<T>](T_Tessa_SmartMerge_TreeNodeBase_1.htm))  
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
(Унаследован от [TreeNodeBase<T>](T_Tessa_SmartMerge_TreeNodeBase_1.htm))  
[SetState](M_Tessa_SmartMerge_TreeNodeBase_1_SetState.htm)|  Устанавливает
состояние узла.  
(Унаследован от [TreeNodeBase<T>](T_Tessa_SmartMerge_TreeNodeBase_1.htm))  
[ToString](M_Tessa_Cards_SmartMerge_Nodes_CardSectionTreeNodeBase_ToString.htm)|
Returns a string that represents the current object.  
(Переопределяет
[CardTreeNodeBase.ToString()](M_Tessa_Cards_SmartMerge_Nodes_CardTreeNodeBase_ToString.htm))  
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
[Tessa.Cards.SmartMerge.Nodes - пространство
имён](N_Tessa_Cards_SmartMerge_Nodes.htm)
