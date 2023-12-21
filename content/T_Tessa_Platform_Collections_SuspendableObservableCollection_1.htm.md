# SuspendableObservableCollection<T> \- класс
Коллекция объектов, для которой доступна возможность подавить уведомления по
событиям
[PropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged.propertychanged)
и
[CollectionChanged](https://learn.microsoft.com/dotnet/api/system.collections.specialized.inotifycollectionchanged.collectionchanged)
вызовом
[SuspendNotifications()](M_Tessa_Platform_Collections_SuspendableObservableCollection_1_SuspendNotifications.htm).
## __Definition
 **Пространство имён:**
[Tessa.Platform.Collections](N_Tessa_Platform_Collections.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class SuspendableObservableCollection<T> : ObservableCollection<T>
VB __Копировать
     Public Class SuspendableObservableCollection(Of T)
    	Inherits ObservableCollection(Of T)
C++ __Копировать
    generic<typename T>
    public ref class SuspendableObservableCollection : public ObservableCollection<T>
F# __Копировать
     type SuspendableObservableCollection<'T> = 
        class
            inherit ObservableCollection<'T>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<T> __[ObservableCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.observablecollection-1)<T> __ SuspendableObservableCollection<T>
Derived
[Tessa.Platform.Collections.ObservableCollection<TItem,
TCollection>](T_Tessa_Platform_Collections_ObservableCollection_2.htm)
[Tessa.UI.Views.Charting.Annotations.AnnotationsCollection](T_Tessa_UI_Views_Charting_Annotations_AnnotationsCollection.htm)
[Tessa.UI.Views.Charting.Series.SeriesCollection](T_Tessa_UI_Views_Charting_Series_SeriesCollection.htm)
#### Параметры типа
T
    Тип элементов в коллекции.
##  __Конструкторы
[SuspendableObservableCollection<T>()](M_Tessa_Platform_Collections_SuspendableObservableCollection_1__ctor.htm)|
Initializes a new instance of the
[ObservableCollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.observablecollection-1)
class.  
---|---  
[SuspendableObservableCollection<T>(IEnumerable<T>)](M_Tessa_Platform_Collections_SuspendableObservableCollection_1__ctor_1.htm)|
Initializes a new instance of the
[ObservableCollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.observablecollection-1)
class that contains elements copied from the specified collection.  
[SuspendableObservableCollection<T>(List<T>)](M_Tessa_Platform_Collections_SuspendableObservableCollection_1__ctor_2.htm)|
Initializes a new instance of the
[ObservableCollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.observablecollection-1)
class that contains elements copied from the specified list.  
##  __Свойства
[CanSuspendNotifications](P_Tessa_Platform_Collections_SuspendableObservableCollection_1_CanSuspendNotifications.htm)|
Признак того, что вызов
[SuspendNotifications()](M_Tessa_Platform_Collections_SuspendableObservableCollection_1_SuspendNotifications.htm)
подавляет уведомления об изменении.  
---|---  
[Count](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1.count#system-
collections-objectmodel-collection-1-count)| Gets the number of elements
actually contained in the
[Collection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1).  
(Унаследован от
[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<T>)  
[Item](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1.item#system-
collections-objectmodel-collection-1-item\(system-int32\))| Gets or sets the
element at the specified index.  
(Унаследован от
[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<T>)  
[Items](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1.items#system-
collections-objectmodel-collection-1-items)| Gets a
[IList<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)
wrapper around the
[Collection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1).  
(Унаследован от
[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<T>)  
##  __Методы
[Add](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1.add#system-
collections-objectmodel-collection-1-add\(-0\))| Adds an object to the end of
the
[Collection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1).  
(Унаследован от
[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<T>)  
---|---  
[BlockReentrancy](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.observablecollection-1.blockreentrancy#system-
collections-objectmodel-observablecollection-1-blockreentrancy)| Disallows
reentrant attempts to change this collection.  
(Унаследован от
[ObservableCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.observablecollection-1)<T>)  
[CheckReentrancy](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.observablecollection-1.checkreentrancy#system-
collections-objectmodel-observablecollection-1-checkreentrancy)| Checks for
reentrant attempts to change this collection.  
(Унаследован от
[ObservableCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.observablecollection-1)<T>)  
[Clear](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1.clear#system-
collections-objectmodel-collection-1-clear)| Removes all elements from the
[Collection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1).  
(Унаследован от
[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<T>)  
[ClearItems](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.observablecollection-1.clearitems#system-
collections-objectmodel-observablecollection-1-clearitems)| Removes all items
from the collection.  
(Унаследован от
[ObservableCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.observablecollection-1)<T>)  
[Contains](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1.contains#system-
collections-objectmodel-collection-1-contains\(-0\))| Determines whether an
element is in the
[Collection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1).  
(Унаследован от
[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<T>)  
[CopyTo](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1.copyto#system-
collections-objectmodel-collection-1-copyto\(-0\(\)-system-int32\))| Copies
the entire
[Collection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)
to a compatible one-dimensional
[Array](https://learn.microsoft.com/dotnet/api/system.array), starting at the
specified index of the target array.  
(Унаследован от
[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<T>)  
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
[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<T>)  
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
[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<T>)  
[Insert](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1.insert#system-
collections-objectmodel-collection-1-insert\(system-int32-0\))| Inserts an
element into the
[Collection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)
at the specified index.  
(Унаследован от
[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<T>)  
[InsertItem](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.observablecollection-1.insertitem#system-
collections-objectmodel-observablecollection-1-insertitem\(system-int32-0\))|
Inserts an item into the collection at the specified index.  
(Унаследован от
[ObservableCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.observablecollection-1)<T>)  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Move](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.observablecollection-1.move#system-
collections-objectmodel-observablecollection-1-move\(system-int32-system-
int32\))| Moves the item at the specified index to a new location in the
collection.  
(Унаследован от
[ObservableCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.observablecollection-1)<T>)  
[MoveItem](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.observablecollection-1.moveitem#system-
collections-objectmodel-observablecollection-1-moveitem\(system-int32-system-
int32\))| Moves the item at the specified index to a new location in the
collection.  
(Унаследован от
[ObservableCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.observablecollection-1)<T>)  
[OnCollectionChanged](M_Tessa_Platform_Collections_SuspendableObservableCollection_1_OnCollectionChanged.htm)|
Raises the
[CollectionChanged](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.observablecollection-1.collectionchanged)
event with the provided arguments.  
(Переопределяет
[ObservableCollection<T>.OnCollectionChanged(NotifyCollectionChangedEventArgs)](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.observablecollection-1.oncollectionchanged#system-
collections-objectmodel-observablecollection-1-oncollectionchanged\(system-
collections-specialized-notifycollectionchangedeventargs\)))  
[OnPropertyChanged](M_Tessa_Platform_Collections_SuspendableObservableCollection_1_OnPropertyChanged.htm)|
Raises the
[PropertyChanged](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.observablecollection-1.propertychanged)
event with the provided arguments.  
(Переопределяет
[ObservableCollection<T>.OnPropertyChanged(PropertyChangedEventArgs)](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.observablecollection-1.onpropertychanged#system-
collections-objectmodel-observablecollection-1-onpropertychanged\(system-
componentmodel-propertychangedeventargs\)))  
[Remove](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1.remove#system-
collections-objectmodel-collection-1-remove\(-0\))| Removes the first
occurrence of a specific object from the
[Collection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1).  
(Унаследован от
[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<T>)  
[RemoveAt](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1.removeat#system-
collections-objectmodel-collection-1-removeat\(system-int32\))| Removes the
element at the specified index of the
[Collection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1).  
(Унаследован от
[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<T>)  
[RemoveItem](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.observablecollection-1.removeitem#system-
collections-objectmodel-observablecollection-1-removeitem\(system-int32\))|
Removes the item at the specified index of the collection.  
(Унаследован от
[ObservableCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.observablecollection-1)<T>)  
[SetItem](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.observablecollection-1.setitem#system-
collections-objectmodel-observablecollection-1-setitem\(system-int32-0\))|
Replaces the element at the specified index.  
(Унаследован от
[ObservableCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.observablecollection-1)<T>)  
[SuspendNotifications](M_Tessa_Platform_Collections_SuspendableObservableCollection_1_SuspendNotifications.htm)|
Предотвращает обновления об изменении коллекции, пока не будет вызван метод
[Dispose()](M_Tessa_Platform_Collections_SuspendableObservableCollection_1_SuspendChangesScope_Dispose.htm)
на возвращённом объекте.
Если метод вызван несколько раз, то для всех объектов должен быть вызван метод
[Dispose()](M_Tessa_Platform_Collections_SuspendableObservableCollection_1_SuspendChangesScope_Dispose.htm).  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __События
[CollectionChanged](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.observablecollection-1.collectionchanged)|
Occurs when an item is added, removed, changed, moved, or the entire list is
refreshed.  
(Унаследован от
[ObservableCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.observablecollection-1)<T>)  
---|---  
[PropertyChanged](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.observablecollection-1.propertychanged)|
Occurs when a property value changes.  
(Унаследован от
[ObservableCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.observablecollection-1)<T>)  
##  __См. также
#### Ссылки
[Tessa.Platform.Collections - пространство
имён](N_Tessa_Platform_Collections.htm)
