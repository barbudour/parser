# GroupView - класс
##  __Definition
 **Пространство имён:** [Tessa.UI.Data](N_Tessa_UI_Data.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class GroupView : ReadOnlyObservableCollection<Object>, 
    	ICollectionView, IEnumerable, INotifyCollectionChanged, INotifyPropertyChanged, IList, 
    	ICollection, IWeakEventListener
VB __Копировать
     Public NotInheritable Class GroupView
    	Inherits ReadOnlyObservableCollection(Of Object)
    	Implements ICollectionView, IEnumerable, INotifyCollectionChanged, INotifyPropertyChanged, 
    	IList, ICollection, IWeakEventListener
C++ __Копировать
     public ref class GroupView sealed : public ReadOnlyObservableCollection<Object^>, 
    	ICollectionView, IEnumerable, INotifyCollectionChanged, INotifyPropertyChanged, IList, 
    	ICollection, IWeakEventListener
F# __Копировать
     [<SealedAttribute>]
    type GroupView = 
        class
            inherit ReadOnlyObservableCollection<Object>
            interface ICollectionView
            interface IEnumerable
            interface INotifyCollectionChanged
            interface INotifyPropertyChanged
            interface IList
            interface ICollection
            interface IWeakEventListener
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1)<[Object](https://learn.microsoft.com/dotnet/api/system.object)> __[ReadOnlyObservableCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlyobservablecollection-1)<[Object](https://learn.microsoft.com/dotnet/api/system.object)> __ GroupView
Implements
    [ICollection](https://learn.microsoft.com/dotnet/api/system.collections.icollection), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable), [IList](https://learn.microsoft.com/dotnet/api/system.collections.ilist), [INotifyCollectionChanged](https://learn.microsoft.com/dotnet/api/system.collections.specialized.inotifycollectionchanged), [ICollectionView](https://learn.microsoft.com/dotnet/api/system.componentmodel.icollectionview), [INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged), [IWeakEventListener](https://learn.microsoft.com/dotnet/api/system.windows.iweakeventlistener)
##  __Свойства
[Count](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1.count#system-
collections-objectmodel-readonlycollection-1-count)| Gets the number of
elements contained in the
[ReadOnlyCollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1)
instance.  
(Унаследован от
[ReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1)<[Object](https://learn.microsoft.com/dotnet/api/system.object)>)  
---|---  
[IsExpanded](P_Tessa_UI_Data_GroupView_IsExpanded.htm)|  
[IsUnnamed](P_Tessa_UI_Data_GroupView_IsUnnamed.htm)|  
[Item](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1.item#system-
collections-objectmodel-readonlycollection-1-item\(system-int32\))| Gets the
element at the specified index.  
(Унаследован от
[ReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1)<[Object](https://learn.microsoft.com/dotnet/api/system.object)>)  
[Items](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1.items#system-
collections-objectmodel-readonlycollection-1-items)| Returns the
[IList<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)
that the
[ReadOnlyCollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1)
wraps.  
(Унаследован от
[ReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1)<[Object](https://learn.microsoft.com/dotnet/api/system.object)>)  
[Name](P_Tessa_UI_Data_GroupView_Name.htm)|  
## __Методы
[Contains](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1.contains#system-
collections-objectmodel-readonlycollection-1-contains\(-0\))| Determines
whether an element is in the
[ReadOnlyCollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1).  
(Унаследован от
[ReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1)<[Object](https://learn.microsoft.com/dotnet/api/system.object)>)  
---|---  
[CopyTo](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1.copyto#system-
collections-objectmodel-readonlycollection-1-copyto\(-0\(\)-system-int32\))|
Copies the entire
[ReadOnlyCollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1)
to a compatible one-dimensional
[Array](https://learn.microsoft.com/dotnet/api/system.array), starting at the
specified index of the target array.  
(Унаследован от
[ReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1)<[Object](https://learn.microsoft.com/dotnet/api/system.object)>)  
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
[ReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1)<[Object](https://learn.microsoft.com/dotnet/api/system.object)>)  
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
[ReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1)<[Object](https://learn.microsoft.com/dotnet/api/system.object)>)  
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
[ReadOnlyObservableCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlyobservablecollection-1)<[Object](https://learn.microsoft.com/dotnet/api/system.object)>)  
[OnPropertyChanged](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlyobservablecollection-1.onpropertychanged#system-
collections-objectmodel-
readonlyobservablecollection-1-onpropertychanged\(system-componentmodel-
propertychangedeventargs\))| Raises the
[PropertyChanged](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlyobservablecollection-1.propertychanged)
event using the provided arguments.  
(Унаследован от
[ReadOnlyObservableCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlyobservablecollection-1)<[Object](https://learn.microsoft.com/dotnet/api/system.object)>)  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __События
[CollectionChanged](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlyobservablecollection-1.collectionchanged)|
Occurs when an item is added or removed.  
(Унаследован от
[ReadOnlyObservableCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlyobservablecollection-1)<[Object](https://learn.microsoft.com/dotnet/api/system.object)>)  
---|---  
[PropertyChanged](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlyobservablecollection-1.propertychanged)|
Occurs when a property value changes.  
(Унаследован от
[ReadOnlyObservableCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlyobservablecollection-1)<[Object](https://learn.microsoft.com/dotnet/api/system.object)>)  
##  __Поля
[CultureProperty](F_Tessa_UI_Data_GroupView_CultureProperty.htm)|  
---|---  
[CurrentItemProperty](F_Tessa_UI_Data_GroupView_CurrentItemProperty.htm)|  
[CurrentPositionProperty](F_Tessa_UI_Data_GroupView_CurrentPositionProperty.htm)|  
[IsCurrentAfterLastProperty](F_Tessa_UI_Data_GroupView_IsCurrentAfterLastProperty.htm)|  
[IsCurrentBeforeFirstProperty](F_Tessa_UI_Data_GroupView_IsCurrentBeforeFirstProperty.htm)|  
[IsEmptyProperty](F_Tessa_UI_Data_GroupView_IsEmptyProperty.htm)|  
[IsExpandedProperty](F_Tessa_UI_Data_GroupView_IsExpandedProperty.htm)|  
[NameProperty](F_Tessa_UI_Data_GroupView_NameProperty.htm)|  
## __Методы расширения
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
