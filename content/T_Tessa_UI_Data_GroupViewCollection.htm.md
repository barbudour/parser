# GroupViewCollection - класс
##  __Definition
 **Пространство имён:** [Tessa.UI.Data](N_Tessa_UI_Data.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class GroupViewCollection : ReadOnlyObservableCollection<GroupView>, 
    	IList, ICollection, IEnumerable, INotifyCollectionChanged, INotifyPropertyChanged, 
    	IWeakEventListener
VB __Копировать
     Public NotInheritable Class GroupViewCollection
    	Inherits ReadOnlyObservableCollection(Of GroupView)
    	Implements IList, ICollection, IEnumerable, INotifyCollectionChanged, 
    	INotifyPropertyChanged, IWeakEventListener
C++ __Копировать
     public ref class GroupViewCollection sealed : public ReadOnlyObservableCollection<GroupView^>, 
    	IList, ICollection, IEnumerable, INotifyCollectionChanged, INotifyPropertyChanged, 
    	IWeakEventListener
F# __Копировать
     [<SealedAttribute>]
    type GroupViewCollection = 
        class
            inherit ReadOnlyObservableCollection<GroupView>
            interface IList
            interface ICollection
            interface IEnumerable
            interface INotifyCollectionChanged
            interface INotifyPropertyChanged
            interface IWeakEventListener
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1)<[GroupView](T_Tessa_UI_Data_GroupView.htm)> __[ReadOnlyObservableCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlyobservablecollection-1)<[GroupView](T_Tessa_UI_Data_GroupView.htm)> __ GroupViewCollection
Implements
    [ICollection](https://learn.microsoft.com/dotnet/api/system.collections.icollection), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable), [IList](https://learn.microsoft.com/dotnet/api/system.collections.ilist), [INotifyCollectionChanged](https://learn.microsoft.com/dotnet/api/system.collections.specialized.inotifycollectionchanged), [INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged), [IWeakEventListener](https://learn.microsoft.com/dotnet/api/system.windows.iweakeventlistener)
##  __Конструкторы
[GroupViewCollection](M_Tessa_UI_Data_GroupViewCollection__ctor.htm)|
Инициализирует новый экземпляр класса GroupViewCollection  
---|---  
##  __Свойства
[Count](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1.count#system-
collections-objectmodel-readonlycollection-1-count)| Gets the number of
elements contained in the
[ReadOnlyCollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1)
instance.  
(Унаследован от
[ReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1)<[GroupView](T_Tessa_UI_Data_GroupView.htm)>)  
---|---  
[Item](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1.item#system-
collections-objectmodel-readonlycollection-1-item\(system-int32\))| Gets the
element at the specified index.  
(Унаследован от
[ReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1)<[GroupView](T_Tessa_UI_Data_GroupView.htm)>)  
[Items](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1.items#system-
collections-objectmodel-readonlycollection-1-items)| Returns the
[IList<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)
that the
[ReadOnlyCollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1)
wraps.  
(Унаследован от
[ReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1)<[GroupView](T_Tessa_UI_Data_GroupView.htm)>)  
##  __Методы
[Contains](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1.contains#system-
collections-objectmodel-readonlycollection-1-contains\(-0\))| Determines
whether an element is in the
[ReadOnlyCollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1).  
(Унаследован от
[ReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1)<[GroupView](T_Tessa_UI_Data_GroupView.htm)>)  
---|---  
[CopyTo](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1.copyto#system-
collections-objectmodel-readonlycollection-1-copyto\(-0\(\)-system-int32\))|
Copies the entire
[ReadOnlyCollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1)
to a compatible one-dimensional
[Array](https://learn.microsoft.com/dotnet/api/system.array), starting at the
specified index of the target array.  
(Унаследован от
[ReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1)<[GroupView](T_Tessa_UI_Data_GroupView.htm)>)  
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
[GetEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1.getenumerator#system-
collections-objectmodel-readonlycollection-1-getenumerator)| Returns an
enumerator that iterates through the
[ReadOnlyCollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1).  
(Унаследован от
[ReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1)<[GroupView](T_Tessa_UI_Data_GroupView.htm)>)  
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
[IndexOf](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1.indexof#system-
collections-objectmodel-readonlycollection-1-indexof\(-0\))| Searches for the
specified object and returns the zero-based index of the first occurrence
within the entire
[ReadOnlyCollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1).  
(Унаследован от
[ReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1)<[GroupView](T_Tessa_UI_Data_GroupView.htm)>)  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[OnCollectionChanged](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlyobservablecollection-1.oncollectionchanged#system-
collections-objectmodel-
readonlyobservablecollection-1-oncollectionchanged\(system-collections-
specialized-notifycollectionchangedeventargs\))| Raises the
[CollectionChanged](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlyobservablecollection-1.collectionchanged)
event using the provided arguments.  
(Унаследован от
[ReadOnlyObservableCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlyobservablecollection-1)<[GroupView](T_Tessa_UI_Data_GroupView.htm)>)  
[OnPropertyChanged](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlyobservablecollection-1.onpropertychanged#system-
collections-objectmodel-
readonlyobservablecollection-1-onpropertychanged\(system-componentmodel-
propertychangedeventargs\))| Raises the
[PropertyChanged](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlyobservablecollection-1.propertychanged)
event using the provided arguments.  
(Унаследован от
[ReadOnlyObservableCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlyobservablecollection-1)<[GroupView](T_Tessa_UI_Data_GroupView.htm)>)  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __События
[CollectionChanged](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlyobservablecollection-1.collectionchanged)|
Occurs when an item is added or removed.  
(Унаследован от
[ReadOnlyObservableCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlyobservablecollection-1)<[GroupView](T_Tessa_UI_Data_GroupView.htm)>)  
---|---  
[PropertyChanged](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlyobservablecollection-1.propertychanged)|
Occurs when a property value changes.  
(Унаследован от
[ReadOnlyObservableCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlyobservablecollection-1)<[GroupView](T_Tessa_UI_Data_GroupView.htm)>)  
##  __Методы расширения
[AddRangeForList](M_Tessa_Platform_Collections_Extensions_AddRangeForList.htm)|
Добавляет значения items в коллекцию collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
---|---  
[InsertRangeForList](M_Tessa_Platform_Collections_Extensions_InsertRangeForList.htm)|
Вставляет диапазон элементов в заданный список items, начиная с указанного
индекса index.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[RemoveAllForList](M_Tessa_Platform_Collections_Extensions_RemoveAllForList.htm)|
Удаляет все элементы, совпадающие по заданному предикату. Возвращает
количество удалённых элементов.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
##  __См. также
#### Ссылки
[Tessa.UI.Data - пространство имён](N_Tessa_UI_Data.htm)
