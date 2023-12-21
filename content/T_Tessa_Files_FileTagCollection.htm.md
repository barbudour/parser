# FileTagCollection - класс
Коллекция тегов [IFileTag](T_Tessa_Files_IFileTag.htm).
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    public sealed class FileTagCollection : ObservableCollectionLookup<string, IFileTag, IFileTagCollection>, 
    	IFileTagCollection, IObservableCollectionLookup<string, IFileTag, IFileTagCollection>, 
    	IObservableCollection<IFileTag, IFileTagCollection>, IList<IFileTag>, 
    	ICollection<IFileTag>, IEnumerable<IFileTag>, IEnumerable, 
    	INotifyCollectionChanged, INotifyPropertyChanged, ICloneable, ILookupContainer<string, IFileTag>
VB __Копировать
    <SerializableAttribute>
    Public NotInheritable Class FileTagCollection
    	Inherits ObservableCollectionLookup(Of String, IFileTag, IFileTagCollection)
    	Implements IFileTagCollection, IObservableCollectionLookup(Of String, IFileTag, IFileTagCollection), 
    	IObservableCollection(Of IFileTag, IFileTagCollection), IList(Of IFileTag), 
    	ICollection(Of IFileTag), IEnumerable(Of IFileTag), IEnumerable, 
    	INotifyCollectionChanged, INotifyPropertyChanged, ICloneable, ILookupContainer(Of String, IFileTag)
C++ __Копировать
    [SerializableAttribute]
    public ref class FileTagCollection sealed : public ObservableCollectionLookup<String^, IFileTag^, IFileTagCollection^>, 
    	IFileTagCollection, IObservableCollectionLookup<String^, IFileTag^, IFileTagCollection^>, 
    	IObservableCollection<IFileTag^, IFileTagCollection^>, IList<IFileTag^>, 
    	ICollection<IFileTag^>, IEnumerable<IFileTag^>, IEnumerable, 
    	INotifyCollectionChanged, INotifyPropertyChanged, ICloneable, ILookupContainer<String^, IFileTag^>
F# __Копировать
     [<SealedAttribute>]
    [<SerializableAttribute>]
    type FileTagCollection = 
        class
            inherit ObservableCollectionLookup<string, IFileTag, IFileTagCollection>
            interface IFileTagCollection
            interface IObservableCollectionLookup<string, IFileTag, IFileTagCollection>
            interface IObservableCollection<IFileTag, IFileTagCollection>
            interface IList<IFileTag>
            interface ICollection<IFileTag>
            interface IEnumerable<IFileTag>
            interface IEnumerable
            interface INotifyCollectionChanged
            interface INotifyPropertyChanged
            interface ICloneable
            interface ILookupContainer<string, IFileTag>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<[IFileTag](T_Tessa_Files_IFileTag.htm)> __[ObservableCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.observablecollection-1)<[IFileTag](T_Tessa_Files_IFileTag.htm)> __[SuspendableObservableCollection](T_Tessa_Platform_Collections_SuspendableObservableCollection_1.htm)<[IFileTag](T_Tessa_Files_IFileTag.htm)> __[ObservableCollection](T_Tessa_Platform_Collections_ObservableCollection_2.htm)<[IFileTag](T_Tessa_Files_IFileTag.htm), [IFileTagCollection](T_Tessa_Files_IFileTagCollection.htm)> __[ObservableCollectionLookup](T_Tessa_Platform_Collections_ObservableCollectionLookup_3.htm)<[String](https://learn.microsoft.com/dotnet/api/system.string), [IFileTag](T_Tessa_Files_IFileTag.htm), [IFileTagCollection](T_Tessa_Files_IFileTagCollection.htm)> __ FileTagCollection
Implements
    [ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<[IFileTag](T_Tessa_Files_IFileTag.htm)>, [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[IFileTag](T_Tessa_Files_IFileTag.htm)>, [IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<[IFileTag](T_Tessa_Files_IFileTag.htm)>, [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable), [INotifyCollectionChanged](https://learn.microsoft.com/dotnet/api/system.collections.specialized.inotifycollectionchanged), [INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged), [ICloneable](https://learn.microsoft.com/dotnet/api/system.icloneable), [IFileTagCollection](T_Tessa_Files_IFileTagCollection.htm), [ILookupContainer](T_Tessa_Platform_Collections_ILookupContainer_2.htm)<[String](https://learn.microsoft.com/dotnet/api/system.string), [IFileTag](T_Tessa_Files_IFileTag.htm)>, [IObservableCollection](T_Tessa_Platform_Collections_IObservableCollection_2.htm)<[IFileTag](T_Tessa_Files_IFileTag.htm), [IFileTagCollection](T_Tessa_Files_IFileTagCollection.htm)>, [IObservableCollectionLookup](T_Tessa_Platform_Collections_IObservableCollectionLookup_3.htm)<[String](https://learn.microsoft.com/dotnet/api/system.string), [IFileTag](T_Tessa_Files_IFileTag.htm), [IFileTagCollection](T_Tessa_Files_IFileTagCollection.htm)>
##  __Конструкторы
[FileTagCollection()](M_Tessa_Files_FileTagCollection__ctor.htm)| Создаёт
экземпляр коллекции с параметрами по умолчанию.  
---|---  
[FileTagCollection(IEnumerable<IFileTag>)](M_Tessa_Files_FileTagCollection__ctor_1.htm)|
Создаёт экземпляр коллекции, в которую копируются элементы из заданной
коллекции. Не выполняет клонирование переданных элементов.  
[FileTagCollection(List<IFileTag>)](M_Tessa_Files_FileTagCollection__ctor_2.htm)|
Создаёт экземпляр коллекции, в которую копируются элементы из заданного
списка. Не выполняет клонирование переданных элементов.  
## __Свойства
[CanSuspendNotifications](P_Tessa_Platform_Collections_SuspendableObservableCollection_1_CanSuspendNotifications.htm)|
Признак того, что вызов
[SuspendNotifications()](M_Tessa_Platform_Collections_SuspendableObservableCollection_1_SuspendNotifications.htm)
подавляет уведомления об изменении.  
(Унаследован от
[SuspendableObservableCollection<T>](T_Tessa_Platform_Collections_SuspendableObservableCollection_1.htm))  
---|---  
[Count](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1.count#system-
collections-objectmodel-collection-1-count)| Gets the number of elements
actually contained in the
[Collection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1).  
(Унаследован от
[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<[IFileTag](T_Tessa_Files_IFileTag.htm)>)  
[Item[Int32]](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1.item#system-
collections-objectmodel-collection-1-item\(system-int32\))| Gets or sets the
element at the specified index.  
(Унаследован от
[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<[IFileTag](T_Tessa_Files_IFileTag.htm)>)  
[Item[TKey]](P_Tessa_Platform_Collections_ObservableCollectionLookup_3_Item.htm)|
Получает одно из значений, доступных по заданному ключу, которое
гарантированно не равно null. При отсутствии таких значений выбрасывает
исключение [System.Collections.Generic.KeyNotFoundException].  
(Унаследован от [ObservableCollectionLookup<TKey, TItem,
TCollection>](T_Tessa_Platform_Collections_ObservableCollectionLookup_3.htm))  
[Items](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1.items#system-
collections-objectmodel-collection-1-items)| Gets a
[IList<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)
wrapper around the
[Collection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1).  
(Унаследован от
[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<[IFileTag](T_Tessa_Files_IFileTag.htm)>)  
##  __Методы
[Add](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1.add#system-
collections-objectmodel-collection-1-add\(-0\))| Adds an object to the end of
the
[Collection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1).  
(Унаследован от
[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<[IFileTag](T_Tessa_Files_IFileTag.htm)>)  
---|---  
[AddIfNotExists](M_Tessa_Files_FileTagCollection_AddIfNotExists.htm)|
Добавляет указанный тег в коллекцию, если он не был добавлен ранее.  
[BlockReentrancy](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.observablecollection-1.blockreentrancy#system-
collections-objectmodel-observablecollection-1-blockreentrancy)| Disallows
reentrant attempts to change this collection.  
(Унаследован от
[ObservableCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.observablecollection-1)<[IFileTag](T_Tessa_Files_IFileTag.htm)>)  
[CheckReentrancy](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.observablecollection-1.checkreentrancy#system-
collections-objectmodel-observablecollection-1-checkreentrancy)| Checks for
reentrant attempts to change this collection.  
(Унаследован от
[ObservableCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.observablecollection-1)<[IFileTag](T_Tessa_Files_IFileTag.htm)>)  
[Clear](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1.clear#system-
collections-objectmodel-collection-1-clear)| Removes all elements from the
[Collection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1).  
(Унаследован от
[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<[IFileTag](T_Tessa_Files_IFileTag.htm)>)  
[ClearItems](M_Tessa_Platform_Collections_ObservableCollectionLookup_3_ClearItems.htm)|
Удаляет все элементы из коллекции.  
(Унаследован от [ObservableCollectionLookup<TKey, TItem,
TCollection>](T_Tessa_Platform_Collections_ObservableCollectionLookup_3.htm))  
[Clone](M_Tessa_Files_FileTagCollection_Clone.htm)|  Выполняет глубокое
копирование коллекции со всеми её элементами. Если элементы поддерживают
[System.ICloneable], то они также клонируются.  
(Переопределяет [ObservableCollection<TItem,
TCollection>.Clone()](M_Tessa_Platform_Collections_ObservableCollection_2_Clone.htm))  
[Contains(T)](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1.contains#system-
collections-objectmodel-collection-1-contains\(-0\))| Determines whether an
element is in the
[Collection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1).  
(Унаследован от
[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<[IFileTag](T_Tessa_Files_IFileTag.htm)>)  
[Contains(TKey)](M_Tessa_Platform_Collections_ObservableCollectionLookup_3_Contains.htm)|
Возвращает признак того, что контейнер содержит хотя бы одно значение по
заданному ключу.  
(Унаследован от [ObservableCollectionLookup<TKey, TItem,
TCollection>](T_Tessa_Platform_Collections_ObservableCollectionLookup_3.htm))  
[CopyTo](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1.copyto#system-
collections-objectmodel-collection-1-copyto\(-0\(\)-system-int32\))| Copies
the entire
[Collection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)
to a compatible one-dimensional
[Array](https://learn.microsoft.com/dotnet/api/system.array), starting at the
specified index of the target array.  
(Унаследован от
[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<[IFileTag](T_Tessa_Files_IFileTag.htm)>)  
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
[GetAll](M_Tessa_Platform_Collections_ObservableCollectionLookup_3_GetAll.htm)|
Возвращает все значения, доступные по заданному ключу. Если таких значений
нет, то возвращается пустая коллекция.  
(Унаследован от [ObservableCollectionLookup<TKey, TItem,
TCollection>](T_Tessa_Platform_Collections_ObservableCollectionLookup_3.htm))  
[GetClonedItems](M_Tessa_Platform_Collections_ObservableCollection_2_GetClonedItems.htm)|
Возвращает текущие элементы, которые клонируются, если они поддерживают
клонирование.  
(Унаследован от [ObservableCollection<TItem,
TCollection>](T_Tessa_Platform_Collections_ObservableCollection_2.htm))  
[GetEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1.getenumerator#system-
collections-objectmodel-collection-1-getenumerator)| Returns an enumerator
that iterates through the
[Collection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1).  
(Унаследован от
[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<[IFileTag](T_Tessa_Files_IFileTag.htm)>)  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetKey](M_Tessa_Files_FileTagCollection_GetKey.htm)|  Возвращает неуникальный
ключ, по которому идентифицируется заданный элемент коллекции.  
(Переопределяет [ObservableCollectionLookup<TKey, TItem,
TCollection>.GetKey(TItem)](M_Tessa_Platform_Collections_ObservableCollectionLookup_3_GetKey.htm))  
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
[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<[IFileTag](T_Tessa_Files_IFileTag.htm)>)  
[Insert](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1.insert#system-
collections-objectmodel-collection-1-insert\(system-int32-0\))| Inserts an
element into the
[Collection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)
at the specified index.  
(Унаследован от
[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<[IFileTag](T_Tessa_Files_IFileTag.htm)>)  
[InsertItem](M_Tessa_Platform_Collections_ObservableCollectionLookup_3_InsertItem.htm)|
Вставляет в коллекцию заданный элемент по указанному индексу.  
(Унаследован от [ObservableCollectionLookup<TKey, TItem,
TCollection>](T_Tessa_Platform_Collections_ObservableCollectionLookup_3.htm))  
[KeyEquals](M_Tessa_Files_FileTagCollection_KeyEquals.htm)| Сравнивает ключи у
двух объектов.  
(Переопределяет [ObservableCollectionLookup<TKey, TItem,
TCollection>.KeyEquals(TKey,
TKey)](M_Tessa_Platform_Collections_ObservableCollectionLookup_3_KeyEquals.htm))  
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
[ObservableCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.observablecollection-1)<[IFileTag](T_Tessa_Files_IFileTag.htm)>)  
[MoveItem](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.observablecollection-1.moveitem#system-
collections-objectmodel-observablecollection-1-moveitem\(system-int32-system-
int32\))| Moves the item at the specified index to a new location in the
collection.  
(Унаследован от
[ObservableCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.observablecollection-1)<[IFileTag](T_Tessa_Files_IFileTag.htm)>)  
[OnCollectionChanged](M_Tessa_Platform_Collections_SuspendableObservableCollection_1_OnCollectionChanged.htm)|
Raises the
[CollectionChanged](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.observablecollection-1.collectionchanged)
event with the provided arguments.  
(Унаследован от
[SuspendableObservableCollection<T>](T_Tessa_Platform_Collections_SuspendableObservableCollection_1.htm))  
[OnPropertyChanged(PropertyChangedEventArgs)](M_Tessa_Platform_Collections_SuspendableObservableCollection_1_OnPropertyChanged.htm)|
Raises the
[PropertyChanged](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.observablecollection-1.propertychanged)
event with the provided arguments.  
(Унаследован от
[SuspendableObservableCollection<T>](T_Tessa_Platform_Collections_SuspendableObservableCollection_1.htm))  
[OnPropertyChanged(String)](M_Tessa_Platform_Collections_ObservableCollection_2_OnPropertyChanged.htm)|
Уведомляет об изменении свойства с заданным именем у объекта.  
(Унаследован от [ObservableCollection<TItem,
TCollection>](T_Tessa_Platform_Collections_ObservableCollection_2.htm))  
[OnPropertyChangedAsync(PropertyChangedEventArgs)](M_Tessa_Platform_Collections_ObservableCollection_2_OnPropertyChangedAsync.htm)|
Уведомляет об изменении свойства с именем, заданным в аргументах события,
асинхронно, в соответствии с принятым для текущего объекта поведением. Если
есть возможность вызвать событие синхронно, то оно вызывается синхронно. Если
объект является моделью представления WPF и текущий поток отличен от потока
диспетчера WPF для приложения (основной поток UI), то выполнение асинхронно
переключается в этот поток. Если это не так, то событие выполняется синхронно.  
(Унаследован от [ObservableCollection<TItem,
TCollection>](T_Tessa_Platform_Collections_ObservableCollection_2.htm))  
[OnPropertyChangedAsync(String)](M_Tessa_Platform_Collections_ObservableCollection_2_OnPropertyChangedAsync_1.htm)|
Уведомляет об изменении свойства с заданным именем у объекта асинхронно, в
соответствии с принятым для текущего объекта поведением. Если есть возможность
вызвать событие синхронно, то оно вызывается синхронно. Если объект является
моделью представления WPF и текущий поток отличен от потока диспетчера WPF для
приложения (основной поток UI), то выполнение асинхронно переключается в этот
поток. Если это не так, то событие выполняется синхронно.  
(Унаследован от [ObservableCollection<TItem,
TCollection>](T_Tessa_Platform_Collections_ObservableCollection_2.htm))  
[Remove(T)](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1.remove#system-
collections-objectmodel-collection-1-remove\(-0\))| Removes the first
occurrence of a specific object from the
[Collection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1).  
(Унаследован от
[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<[IFileTag](T_Tessa_Files_IFileTag.htm)>)  
[Remove(TKey)](M_Tessa_Platform_Collections_ObservableCollectionLookup_3_Remove.htm)|
Удаляет одно из значений, содержащихся в контейнере по заданному ключу.
Возвращает признак того, что одно из значений было удалено.  
(Унаследован от [ObservableCollectionLookup<TKey, TItem,
TCollection>](T_Tessa_Platform_Collections_ObservableCollectionLookup_3.htm))  
[RemoveAll](M_Tessa_Platform_Collections_ObservableCollectionLookup_3_RemoveAll.htm)|
Удаляет все значения, содержащиеся в контейнере по заданному ключу. Возвращает
признак того, что хотя бы одно из значений было удалено.  
(Унаследован от [ObservableCollectionLookup<TKey, TItem,
TCollection>](T_Tessa_Platform_Collections_ObservableCollectionLookup_3.htm))  
[RemoveAt](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1.removeat#system-
collections-objectmodel-collection-1-removeat\(system-int32\))| Removes the
element at the specified index of the
[Collection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1).  
(Унаследован от
[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<[IFileTag](T_Tessa_Files_IFileTag.htm)>)  
[RemoveItem](M_Tessa_Platform_Collections_ObservableCollectionLookup_3_RemoveItem.htm)|
Удаляет элемент из коллекции по заданному индексу.  
(Унаследован от [ObservableCollectionLookup<TKey, TItem,
TCollection>](T_Tessa_Platform_Collections_ObservableCollectionLookup_3.htm))  
[SetItem](M_Tessa_Platform_Collections_ObservableCollectionLookup_3_SetItem.htm)|
Замещает заданный элемент по указанному индексу коллекции.  
(Унаследован от [ObservableCollectionLookup<TKey, TItem,
TCollection>](T_Tessa_Platform_Collections_ObservableCollectionLookup_3.htm))  
[SuspendNotifications](M_Tessa_Platform_Collections_SuspendableObservableCollection_1_SuspendNotifications.htm)|
Предотвращает обновления об изменении коллекции, пока не будет вызван метод
[Dispose()](M_Tessa_Platform_Collections_SuspendableObservableCollection_1_SuspendChangesScope_Dispose.htm)
на возвращённом объекте.
Если метод вызван несколько раз, то для всех объектов должен быть вызван метод
[Dispose()](M_Tessa_Platform_Collections_SuspendableObservableCollection_1_SuspendChangesScope_Dispose.htm).
(Унаследован от
[SuspendableObservableCollection<T>](T_Tessa_Platform_Collections_SuspendableObservableCollection_1.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGet](M_Tessa_Platform_Collections_ObservableCollectionLookup_3_TryGet.htm)|
Возвращает одно из значений по заданному ключу или null, если контейнер не
содержит значений.  
(Унаследован от [ObservableCollectionLookup<TKey, TItem,
TCollection>](T_Tessa_Platform_Collections_ObservableCollectionLookup_3.htm))  
##  __События
[CollectionChanged](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.observablecollection-1.collectionchanged)|
Occurs when an item is added, removed, changed, moved, or the entire list is
refreshed.  
(Унаследован от
[ObservableCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.observablecollection-1)<[IFileTag](T_Tessa_Files_IFileTag.htm)>)  
---|---  
[PropertyChanged](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.observablecollection-1.propertychanged)|
Occurs when a property value changes.  
(Унаследован от
[ObservableCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.observablecollection-1)<[IFileTag](T_Tessa_Files_IFileTag.htm)>)  
##  __Методы расширения
[AddRange<IFileTag>](M_Tessa_Platform_Collections_Extensions_AddRange__1.htm)|
Добавляет значения items в коллекцию collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
---|---  
[AddRange<IFileTag>](M_Tessa_Platform_Collections_Extensions_AddRange__1_1.htm)|
Добавляет значения items в коллекцию collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[AddRangeIfNotExists](M_Tessa_Files_FileExtensions_AddRangeIfNotExists.htm)|
Добавляет указанные теги в коллекцию, если они не были добавлены ранее.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
[AsArray<IFileTag>](M_Tessa_Platform_Collections_EnumerableExtensions_AsArray__1.htm)|
Преобразует коллекцию в массив. В случае, если коллекция не является массивом,
к ней применяется
[ToArray<TSource>(IEnumerable<TSource>)](https://learn.microsoft.com/dotnet/api/system.linq.enumerable.toarray#system-
linq-enumerable-toarray-1\(system-collections-generic-
ienumerable\(\(-0\)\)\)).  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
[ConvertToListDictionaries<IFileTag>](M_Tessa_Views_Mapping_DictionaryConverter_ConvertToListDictionaries__1.htm)|
Осуществляет сопоставлению коллекции source на коллекцию коллекций ключ-
значение в соответствии с контекстом сопоставления по умолчанию  
(Определяется
[DictionaryConverter](T_Tessa_Views_Mapping_DictionaryConverter.htm))  
[ConvertToListDictionaries<IFileTag>](M_Tessa_Views_Mapping_DictionaryConverter_ConvertToListDictionaries__1_1.htm)|
Осуществляет сопоставлению коллекции source на коллекцию коллекций ключ-
значение в соответствии с контекстом сопоставления context  
(Определяется
[DictionaryConverter](T_Tessa_Views_Mapping_DictionaryConverter.htm))  
[ForEach<IFileTag>](M_Tessa_Platform_Collections_EnumerableExtensions_ForEach__1.htm)|
Выполняет указанное действие с каждым элементом коллекции
[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1).  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
[FullOuterJoin<IFileTag, TInner, TKey,
TResult>](M_Tessa_Platform_Collections_Extensions_FullOuterJoin__4.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[IndexOf<IFileTag>](M_Tessa_Platform_Collections_Extensions_IndexOf__1.htm)|
Возвращает индекс первого вхождения элемента в последовательность,
определяемый посредством заданного выражения.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[IndexOf<IFileTag>](M_Tessa_Platform_Collections_Extensions_IndexOf__1_1.htm)|
Возвращает индекс первого вхождения элемента в последовательность,
определяемый посредством заданного компаратора
[IEqualityComparer<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.iequalitycomparer-1).  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[IndexOf<IFileTag>](M_Tessa_Platform_Collections_Extensions_IndexOf__1_2.htm)|
Выполняет поиск элемента, удовлетворяющего условиям указанного предиката, и
возвращает отсчитываемый от нуля индекс первого вхождения в диапазоне
элементов списка, начиная с заданного индекса и заканчивая последним
элементом.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[IndexOf<IFileTag>](M_Tessa_Platform_Collections_Extensions_IndexOf__1_3.htm)|
Выполняет поиск элемента, удовлетворяющего условиям указанного предиката, и
возвращает отсчитываемый от нуля индекс первого вхождения в диапазоне
элементов списка, начинающемся с заданного индекса и содержащем указанное
число элементов.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[InsertRange<IFileTag>](M_Tessa_Platform_Collections_Extensions_InsertRange__1.htm)|
Вставляет диапазон элементов в заданный список items, начиная с указанного
индекса index.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<IFileTag>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<IFileTag>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__1_1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<IFileTag,
TKey>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__2.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<IFileTag,
TKey>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__2_1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByLocalized<IFileTag>](M_Tessa_Platform_PlatformExtensions_OrderByLocalized__1.htm)|
Сортирует значения последовательности по возрастанию по локализованному ключу,
который определяется для каждого элемента.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[OrderByLocalizedDescending<IFileTag>](M_Tessa_Platform_PlatformExtensions_OrderByLocalizedDescending__1.htm)|
Сортирует значения последовательности по убыванию по локализованному ключу,
который определяется для каждого элемента.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[RemoveAll<IFileTag>](M_Tessa_Platform_Collections_Extensions_RemoveAll__1.htm)|
Удаляет все элементы, совпадающие по заданному предикату. Возвращает
количество удалённых элементов.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[RemoveRange<IFileTag>](M_Tessa_Platform_Collections_Extensions_RemoveRange__1.htm)|
Удаляет значения items из коллекции collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[RemoveRange<IFileTag>](M_Tessa_Platform_Collections_Extensions_RemoveRange__1_1.htm)|
Удаляет значения items из коллекции collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[RunWithMaxDegreeOfParallelismAsync<IFileTag>](M_Tessa_Platform_PlatformExtensions_RunWithMaxDegreeOfParallelismAsync__1.htm)|
Выполняет асинхронную обработку элементов с ограничением на максимальное
количество параллельных задач.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[ToDictionaryAsync<IFileTag, TKey,
TElement>](M_Tessa_Platform_PlatformExtensions_ToDictionaryAsync__3.htm)|
Создает словарь [Dictionary<TKey,
TValue>](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)
из объекта
[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)
в соответствии с заданными функциями синхронного селектора ключа и
асинхронного селектора значения.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[ToObservableCollection<IFileTag>](M_Tessa_Platform_Collections_Extensions_ToObservableCollection__1.htm)|
Преобразует коллекцию IEnumerable в ObservableCollection  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[ToSealableList<IFileTag>](M_Tessa_Platform_Collections_Extensions_ToSealableList__1.htm)|
Возвращает список объектов, поддерживающий защиту от изменений. Каждый из
объектов T в списке либо не реализует интерфейс
[ISealable](T_Tessa_Platform_ISealable.htm), либо защита от изменений таких
объектов не активируется вместе со списком.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[ToSealableObjectList<IFileTag>](M_Tessa_Platform_Collections_Extensions_ToSealableObjectList__1.htm)|
Возвращает список объектов, поддерживающий защиту от изменений. Каждый из
объектов T в списке реализует интерфейс
[ISealable](T_Tessa_Platform_ISealable.htm) и защищается от изменений при
активации защиты в списке.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[TryFirst<IFileTag>](M_Tessa_Platform_Collections_EnumerableExtensions_TryFirst__1.htm)|
Возвращает первый элемент последовательности, удовлетворяющий условию.  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
[TrySingleOrDefault<IFileTag>](M_Tessa_Platform_Collections_EnumerableExtensions_TrySingleOrDefault__1.htm)|
Возвращает единственный конкретный элемент коллекции или значение по умолчанию
для типа, если этот элемент не найден.  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
