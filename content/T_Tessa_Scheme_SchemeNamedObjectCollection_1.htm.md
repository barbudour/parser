# SchemeNamedObjectCollection<T> \- класс
##  __Definition
 **Пространство имён:** [Tessa.Scheme](N_Tessa_Scheme.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class SchemeNamedObjectCollection<T> : SchemeObjectCollection<T>
    where T : SchemeNamedObject
VB __Копировать
     Public MustInherit Class SchemeNamedObjectCollection(Of T As SchemeNamedObject)
    	Inherits SchemeObjectCollection(Of T)
C++ __Копировать
    generic<typename T>
    where T : SchemeNamedObject
    public ref class SchemeNamedObjectCollection abstract : public SchemeObjectCollection<T>
F# __Копировать
     [<AbstractClassAttribute>]
    type SchemeNamedObjectCollection<'T when 'T : SchemeNamedObject> = 
        class
            inherit SchemeObjectCollection<'T>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[SchemeObjectCollection](T_Tessa_Scheme_SchemeObjectCollection_1.htm)<T> __ SchemeNamedObjectCollection<T>
Derived
[Tessa.Scheme.SchemeColumnCollection](T_Tessa_Scheme_SchemeColumnCollection.htm)
[Tessa.Scheme.SchemeConstraintCollection](T_Tessa_Scheme_SchemeConstraintCollection.htm)
[Tessa.Scheme.SchemeFunctionCollection](T_Tessa_Scheme_SchemeFunctionCollection.htm)
[Tessa.Scheme.SchemeIndexCollection](T_Tessa_Scheme_SchemeIndexCollection.htm)
[Tessa.Scheme.SchemeMigrationCollection](T_Tessa_Scheme_SchemeMigrationCollection.htm)
[Tessa.Scheme.SchemePartitionCollection](T_Tessa_Scheme_SchemePartitionCollection.htm)
[Tessa.Scheme.SchemeProcedureCollection](T_Tessa_Scheme_SchemeProcedureCollection.htm)
[Tessa.Scheme.SchemeTableCollection](T_Tessa_Scheme_SchemeTableCollection.htm)
Подробнее __Less __
#### Параметры типа
T
##  __Свойства
[Count](P_Tessa_Scheme_SchemeObjectCollection_1_Count.htm)|  
(Унаследован от
[SchemeObjectCollection<T>](T_Tessa_Scheme_SchemeObjectCollection_1.htm))  
---|---  
[IsSealed](P_Tessa_Scheme_SchemeObjectCollection_1_IsSealed.htm)|  
(Унаследован от
[SchemeObjectCollection<T>](T_Tessa_Scheme_SchemeObjectCollection_1.htm))  
[Item[Guid]](P_Tessa_Scheme_SchemeNamedObjectCollection_1_Item.htm)|  
[Item[Int32]](P_Tessa_Scheme_SchemeObjectCollection_1_Item.htm)|  
(Унаследован от
[SchemeObjectCollection<T>](T_Tessa_Scheme_SchemeObjectCollection_1.htm))  
[Item[String]](P_Tessa_Scheme_SchemeNamedObjectCollection_1_Item_1.htm)|  
[Parent](P_Tessa_Scheme_SchemeObjectCollection_1_Parent.htm)|  
(Унаследован от
[SchemeObjectCollection<T>](T_Tessa_Scheme_SchemeObjectCollection_1.htm))  
##  __Методы
[Add](M_Tessa_Scheme_SchemeObjectCollection_1_Add.htm)|  
(Унаследован от
[SchemeObjectCollection<T>](T_Tessa_Scheme_SchemeObjectCollection_1.htm))  
---|---  
[CheckIsSealed](M_Tessa_Scheme_SchemeObjectCollection_1_CheckIsSealed.htm)|  
(Унаследован от
[SchemeObjectCollection<T>](T_Tessa_Scheme_SchemeObjectCollection_1.htm))  
[Clear](M_Tessa_Scheme_SchemeObjectCollection_1_Clear.htm)|  
(Унаследован от
[SchemeObjectCollection<T>](T_Tessa_Scheme_SchemeObjectCollection_1.htm))  
[ClearItems](M_Tessa_Scheme_SchemeObjectCollection_1_ClearItems.htm)|  
(Унаследован от
[SchemeObjectCollection<T>](T_Tessa_Scheme_SchemeObjectCollection_1.htm))  
[Construct](M_Tessa_Scheme_SchemeObjectCollection_1_Construct.htm)|  
(Унаследован от
[SchemeObjectCollection<T>](T_Tessa_Scheme_SchemeObjectCollection_1.htm))  
[Contains(Guid)](M_Tessa_Scheme_SchemeNamedObjectCollection_1_Contains.htm)|  
[Contains(T)](M_Tessa_Scheme_SchemeObjectCollection_1_Contains.htm)|  
(Унаследован от
[SchemeObjectCollection<T>](T_Tessa_Scheme_SchemeObjectCollection_1.htm))  
[Contains(String)](M_Tessa_Scheme_SchemeNamedObjectCollection_1_Contains_1.htm)|  
[Copy](M_Tessa_Scheme_SchemeObjectCollection_1_Copy.htm)|  
(Унаследован от
[SchemeObjectCollection<T>](T_Tessa_Scheme_SchemeObjectCollection_1.htm))  
[CopyTo](M_Tessa_Scheme_SchemeObjectCollection_1_CopyTo.htm)|  
(Унаследован от
[SchemeObjectCollection<T>](T_Tessa_Scheme_SchemeObjectCollection_1.htm))  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetEnumerator](M_Tessa_Scheme_SchemeObjectCollection_1_GetEnumerator.htm)|  
(Унаследован от
[SchemeObjectCollection<T>](T_Tessa_Scheme_SchemeObjectCollection_1.htm))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[HaveSameKey](M_Tessa_Scheme_SchemeNamedObjectCollection_1_HaveSameKey.htm)|  
(Переопределяет [SchemeObjectCollection<T>.HaveSameKey(T,
T)](M_Tessa_Scheme_SchemeObjectCollection_1_HaveSameKey.htm))  
[IndexOf(Guid)](M_Tessa_Scheme_SchemeNamedObjectCollection_1_IndexOf.htm)|  
[IndexOf(T)](M_Tessa_Scheme_SchemeObjectCollection_1_IndexOf.htm)|  
(Унаследован от
[SchemeObjectCollection<T>](T_Tessa_Scheme_SchemeObjectCollection_1.htm))  
[IndexOf(String)](M_Tessa_Scheme_SchemeNamedObjectCollection_1_IndexOf_1.htm)|  
[Insert](M_Tessa_Scheme_SchemeObjectCollection_1_Insert.htm)|  
(Унаследован от
[SchemeObjectCollection<T>](T_Tessa_Scheme_SchemeObjectCollection_1.htm))  
[InsertItem](M_Tessa_Scheme_SchemeObjectCollection_1_InsertItem.htm)|  
(Унаследован от
[SchemeObjectCollection<T>](T_Tessa_Scheme_SchemeObjectCollection_1.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MoveItem](M_Tessa_Scheme_SchemeObjectCollection_1_MoveItem.htm)|  
(Унаследован от
[SchemeObjectCollection<T>](T_Tessa_Scheme_SchemeObjectCollection_1.htm))  
[Remove(Guid)](M_Tessa_Scheme_SchemeNamedObjectCollection_1_Remove.htm)|  
[Remove(T)](M_Tessa_Scheme_SchemeObjectCollection_1_Remove.htm)|  
(Унаследован от
[SchemeObjectCollection<T>](T_Tessa_Scheme_SchemeObjectCollection_1.htm))  
[Remove(String)](M_Tessa_Scheme_SchemeNamedObjectCollection_1_Remove_1.htm)|  
[RemoveAt](M_Tessa_Scheme_SchemeObjectCollection_1_RemoveAt.htm)|  
(Унаследован от
[SchemeObjectCollection<T>](T_Tessa_Scheme_SchemeObjectCollection_1.htm))  
[RemoveItem](M_Tessa_Scheme_SchemeObjectCollection_1_RemoveItem.htm)|  
(Унаследован от
[SchemeObjectCollection<T>](T_Tessa_Scheme_SchemeObjectCollection_1.htm))  
[ReplaceItem](M_Tessa_Scheme_SchemeObjectCollection_1_ReplaceItem.htm)|  
(Унаследован от
[SchemeObjectCollection<T>](T_Tessa_Scheme_SchemeObjectCollection_1.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetItem(Func<T, Int32, Boolean>,
T)](M_Tessa_Scheme_SchemeObjectCollection_1_TryGetItem.htm)|  
(Унаследован от
[SchemeObjectCollection<T>](T_Tessa_Scheme_SchemeObjectCollection_1.htm))  
[TryGetItem(Guid,
T)](M_Tessa_Scheme_SchemeNamedObjectCollection_1_TryGetItem.htm)|  
[TryGetItem(Int32,
T)](M_Tessa_Scheme_SchemeObjectCollection_1_TryGetItem_1.htm)|  
(Унаследован от
[SchemeObjectCollection<T>](T_Tessa_Scheme_SchemeObjectCollection_1.htm))  
[TryGetItem(String,
T)](M_Tessa_Scheme_SchemeNamedObjectCollection_1_TryGetItem_1.htm)|  
[ValidateInsertingItem](M_Tessa_Scheme_SchemeObjectCollection_1_ValidateInsertingItem.htm)|  
(Унаследован от
[SchemeObjectCollection<T>](T_Tessa_Scheme_SchemeObjectCollection_1.htm))  
[ValidateItemUniqueness](M_Tessa_Scheme_SchemeNamedObjectCollection_1_ValidateItemUniqueness.htm)|  
(Переопределяет [SchemeObjectCollection<T>.ValidateItemUniqueness(T,
T)](M_Tessa_Scheme_SchemeObjectCollection_1_ValidateItemUniqueness.htm))  
[ValidateRemovingItem](M_Tessa_Scheme_SchemeObjectCollection_1_ValidateRemovingItem.htm)|  
(Унаследован от
[SchemeObjectCollection<T>](T_Tessa_Scheme_SchemeObjectCollection_1.htm))  
##  __События
[CollectionChanged](E_Tessa_Scheme_SchemeObjectCollection_1_CollectionChanged.htm)|  
(Унаследован от
[SchemeObjectCollection<T>](T_Tessa_Scheme_SchemeObjectCollection_1.htm))  
---|---  
[PropertyChanged](E_Tessa_Scheme_SchemeObjectCollection_1_PropertyChanged.htm)|  
(Унаследован от
[SchemeObjectCollection<T>](T_Tessa_Scheme_SchemeObjectCollection_1.htm))  
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
[Tessa.Scheme - пространство имён](N_Tessa_Scheme.htm)
