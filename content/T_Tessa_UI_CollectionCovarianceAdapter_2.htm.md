# CollectionCovarianceAdapter<TDerived, TBase> \- класс
##  __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CollectionCovarianceAdapter<TDerived, TBase> : Collection<TBase>
    where TDerived : TBase
VB __Копировать
     Public NotInheritable Class CollectionCovarianceAdapter(Of TDerived As TBase, TBase)
    	Inherits Collection(Of TBase)
C++ __Копировать
    generic<typename TDerived, typename TBase>
    where TDerived : TBase
    public ref class CollectionCovarianceAdapter sealed : public Collection<TBase>
F# __Копировать
     [<SealedAttribute>]
    type CollectionCovarianceAdapter<'TDerived, 'TBase when 'TDerived : 'TBase> = 
        class
            inherit Collection<'TBase>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<TBase> __ CollectionCovarianceAdapter<TDerived, TBase>
#### Параметры типа
TDerived
TBase
##  __Конструкторы
[CollectionCovarianceAdapter<TDerived,
TBase>](M_Tessa_UI_CollectionCovarianceAdapter_2__ctor.htm)| Инициализирует
новый экземпляр класса CollectionCovarianceAdapter<TDerived, TBase>  
---|---  
##  __Свойства
[Count](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1.count#system-
collections-objectmodel-collection-1-count)| Gets the number of elements
actually contained in the
[Collection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1).  
(Унаследован от
[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<TBase>)  
---|---  
[Item](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1.item#system-
collections-objectmodel-collection-1-item\(system-int32\))| Gets or sets the
element at the specified index.  
(Унаследован от
[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<TBase>)  
[Items](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1.items#system-
collections-objectmodel-collection-1-items)| Gets a
[IList<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)
wrapper around the
[Collection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1).  
(Унаследован от
[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<TBase>)  
##  __Методы
[Add](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1.add#system-
collections-objectmodel-collection-1-add\(-0\))| Adds an object to the end of
the
[Collection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1).  
(Унаследован от
[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<TBase>)  
---|---  
[Clear](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1.clear#system-
collections-objectmodel-collection-1-clear)| Removes all elements from the
[Collection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1).  
(Унаследован от
[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<TBase>)  
[ClearItems](M_Tessa_UI_CollectionCovarianceAdapter_2_ClearItems.htm)|  
(Переопределяет
[Collection<T>.ClearItems()](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1.clearitems#system-
collections-objectmodel-collection-1-clearitems))  
[Contains](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1.contains#system-
collections-objectmodel-collection-1-contains\(-0\))| Determines whether an
element is in the
[Collection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1).  
(Унаследован от
[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<TBase>)  
[CopyTo](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1.copyto#system-
collections-objectmodel-collection-1-copyto\(-0\(\)-system-int32\))| Copies
the entire
[Collection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)
to a compatible one-dimensional
[Array](https://learn.microsoft.com/dotnet/api/system.array), starting at the
specified index of the target array.  
(Унаследован от
[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<TBase>)  
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
[GetEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1.getenumerator#system-
collections-objectmodel-collection-1-getenumerator)| Returns an enumerator
that iterates through the
[Collection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1).  
(Унаследован от
[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<TBase>)  
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
[IndexOf](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1.indexof#system-
collections-objectmodel-collection-1-indexof\(-0\))| Searches for the
specified object and returns the zero-based index of the first occurrence
within the entire
[Collection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1).  
(Унаследован от
[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<TBase>)  
[Insert](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1.insert#system-
collections-objectmodel-collection-1-insert\(system-int32-0\))| Inserts an
element into the
[Collection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)
at the specified index.  
(Унаследован от
[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<TBase>)  
[InsertItem](M_Tessa_UI_CollectionCovarianceAdapter_2_InsertItem.htm)|  
(Переопределяет [Collection<T>.InsertItem(Int32,
T)](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1.insertitem#system-
collections-objectmodel-collection-1-insertitem\(system-int32-0\)))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Remove](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1.remove#system-
collections-objectmodel-collection-1-remove\(-0\))| Removes the first
occurrence of a specific object from the
[Collection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1).  
(Унаследован от
[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<TBase>)  
[RemoveAt](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1.removeat#system-
collections-objectmodel-collection-1-removeat\(system-int32\))| Removes the
element at the specified index of the
[Collection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1).  
(Унаследован от
[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<TBase>)  
[RemoveItem](M_Tessa_UI_CollectionCovarianceAdapter_2_RemoveItem.htm)|  
(Переопределяет
[Collection<T>.RemoveItem(Int32)](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1.removeitem#system-
collections-objectmodel-collection-1-removeitem\(system-int32\)))  
[SetItem](M_Tessa_UI_CollectionCovarianceAdapter_2_SetItem.htm)|  
(Переопределяет [Collection<T>.SetItem(Int32,
T)](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1.setitem#system-
collections-objectmodel-collection-1-setitem\(system-int32-0\)))  
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
[Tessa.UI - пространство имён](N_Tessa_UI.htm)
