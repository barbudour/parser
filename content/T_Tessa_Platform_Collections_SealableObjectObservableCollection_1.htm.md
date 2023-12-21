# SealableObjectObservableCollection<T> \- класс
Коллекция, поддерживающая защиту от изменений и уведомления об изменении.
Вложенные в коллекцию объекты также защищаются от изменений, а их значения
никогда не равны null.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Collections](N_Tessa_Platform_Collections.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    public class SealableObjectObservableCollection<T> : SealableObservableCollection<T>
    where T : class, ISealable
VB __Копировать
    <SerializableAttribute>
    Public Class SealableObjectObservableCollection(Of T As {Class, ISealable})
    	Inherits SealableObservableCollection(Of T)
C++ __Копировать
    [SerializableAttribute]
    generic<typename T>
    where T : ref class, ISealable
    public ref class SealableObjectObservableCollection : public SealableObservableCollection<T>
F# __Копировать
     [<SerializableAttribute>]
    type SealableObjectObservableCollection<'T when 'T : not struct and ISealable> = 
        class
            inherit SealableObservableCollection<'T>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<T> __[ObservableCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.observablecollection-1)<T> __[SealableObservableCollection](T_Tessa_Platform_Collections_SealableObservableCollection_1.htm)<T> __ SealableObjectObservableCollection<T>
Derived
[Tessa.UI.Tiles.TileCollection](T_Tessa_UI_Tiles_TileCollection.htm)
#### Параметры типа
T
    Ссылочный тип элементов коллекции, реализующих интерфейс [ISealable](T_Tessa_Platform_ISealable.htm).
##  __Конструкторы
[SealableObjectObservableCollection<T>()](M_Tessa_Platform_Collections_SealableObjectObservableCollection_1__ctor.htm)|
Создаёт экземпляр класса с параметрами по умолчанию.  
---|---  
[SealableObjectObservableCollection<T>(Boolean)](M_Tessa_Platform_Collections_SealableObjectObservableCollection_1__ctor_1.htm)|
Создаёт экземпляр класса с указанием признака того, что объект должен быть
защищён от изменений.  
[SealableObjectObservableCollection<T>(IEnumerable<T>)](M_Tessa_Platform_Collections_SealableObjectObservableCollection_1__ctor_2.htm)|
Создаёт экземпляр класса с указанием коллекции элементов, используемой для
инициализации списка.  
[SealableObjectObservableCollection<T>(List<T>)](M_Tessa_Platform_Collections_SealableObjectObservableCollection_1__ctor_4.htm)|
Создаёт экземпляр класса с указанием списка элементов, используемого для
инициализации списка.  
[SealableObjectObservableCollection<T>(IEnumerable<T>,
Boolean)](M_Tessa_Platform_Collections_SealableObjectObservableCollection_1__ctor_3.htm)|
Создаёт экземпляр класса с указанием коллекции элементов, используемой для
инициализации списка, и признака того, что объект должен быть защищён от
изменений.  
[SealableObjectObservableCollection<T>(List<T>,
Boolean)](M_Tessa_Platform_Collections_SealableObjectObservableCollection_1__ctor_5.htm)|
Создаёт экземпляр класса с указанием списка элементов, используемого для
инициализации списка, и признака того, что объект должен быть защищён от
изменений.  
## __Свойства
[Count](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1.count#system-
collections-objectmodel-collection-1-count)| Gets the number of elements
actually contained in the
[Collection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1).  
(Унаследован от
[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<T>)  
---|---  
[IsSealed](P_Tessa_Platform_Collections_SealableObservableCollection_1_IsSealed.htm)|
Признак того, что объект был защищён от изменений.  
(Унаследован от
[SealableObservableCollection<T>](T_Tessa_Platform_Collections_SealableObservableCollection_1.htm))  
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
[CheckSealed](M_Tessa_Platform_Collections_SealableObservableCollection_1_CheckSealed.htm)|
Выбрасывает исключение [Tessa.Platform.ObjectSealedException], если объект был
защищён от изменений.  
(Унаследован от
[SealableObservableCollection<T>](T_Tessa_Platform_Collections_SealableObservableCollection_1.htm))  
[Clear](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1.clear#system-
collections-objectmodel-collection-1-clear)| Removes all elements from the
[Collection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1).  
(Унаследован от
[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<T>)  
[ClearItems](M_Tessa_Platform_Collections_SealableObservableCollection_1_ClearItems.htm)|
Удаляет все элементы из коллекции.  
(Унаследован от
[SealableObservableCollection<T>](T_Tessa_Platform_Collections_SealableObservableCollection_1.htm))  
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
[InsertItem](M_Tessa_Platform_Collections_SealableObjectObservableCollection_1_InsertItem.htm)|
Вставляет в коллекцию заданный элемент по указанному индексу.  
(Переопределяет [SealableObservableCollection<T>.InsertItem(Int32,
T)](M_Tessa_Platform_Collections_SealableObservableCollection_1_InsertItem.htm))  
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
[OnCollectionChanged](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.observablecollection-1.oncollectionchanged#system-
collections-objectmodel-observablecollection-1-oncollectionchanged\(system-
collections-specialized-notifycollectionchangedeventargs\))| Raises the
[CollectionChanged](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.observablecollection-1.collectionchanged)
event with the provided arguments.  
(Унаследован от
[ObservableCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.observablecollection-1)<T>)  
[OnPropertyChanged](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.observablecollection-1.onpropertychanged#system-
collections-objectmodel-observablecollection-1-onpropertychanged\(system-
componentmodel-propertychangedeventargs\))| Raises the
[PropertyChanged](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.observablecollection-1.propertychanged)
event with the provided arguments.  
(Унаследован от
[ObservableCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.observablecollection-1)<T>)  
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
[RemoveItem](M_Tessa_Platform_Collections_SealableObservableCollection_1_RemoveItem.htm)|
Удаляет элемент из коллекции по заданному индексу.  
(Унаследован от
[SealableObservableCollection<T>](T_Tessa_Platform_Collections_SealableObservableCollection_1.htm))  
[Seal](M_Tessa_Platform_Collections_SealableObservableCollection_1_Seal.htm)|
Защищает объект от изменений.  
(Унаследован от
[SealableObservableCollection<T>](T_Tessa_Platform_Collections_SealableObservableCollection_1.htm))  
[SealInternal](M_Tessa_Platform_Collections_SealableObjectObservableCollection_1_SealInternal.htm)|
Защищает объект от изменений.
Метод может быть переопределён в классах-наследниках.
(Переопределяет
[SealableObservableCollection<T>.SealInternal()](M_Tessa_Platform_Collections_SealableObservableCollection_1_SealInternal.htm))  
[SetItem](M_Tessa_Platform_Collections_SealableObjectObservableCollection_1_SetItem.htm)|
Замещает заданный элемент по указанному индексу коллекции.  
(Переопределяет [SealableObservableCollection<T>.SetItem(Int32,
T)](M_Tessa_Platform_Collections_SealableObservableCollection_1_SetItem.htm))  
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
