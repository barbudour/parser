# ReadOnlyNotificationCollection<T> \- класс
Доступная только для чтения обёртка для коллекции, открыто поддерживающая
событие
[CollectionChanged](https://learn.microsoft.com/dotnet/api/system.collections.specialized.inotifycollectionchanged.collectionchanged).
## __Definition
 **Пространство имён:**
[Tessa.Platform.Collections](N_Tessa_Platform_Collections.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class ReadOnlyNotificationCollection<T> : ReadOnlyObservableCollection<T>
VB __Копировать
     Public Class ReadOnlyNotificationCollection(Of T)
    	Inherits ReadOnlyObservableCollection(Of T)
C++ __Копировать
    generic<typename T>
    public ref class ReadOnlyNotificationCollection : public ReadOnlyObservableCollection<T>
F# __Копировать
     type ReadOnlyNotificationCollection<'T> = 
        class
            inherit ReadOnlyObservableCollection<'T>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1)<T> __[ReadOnlyObservableCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlyobservablecollection-1)<T> __ ReadOnlyNotificationCollection<T>
#### Параметры типа
T
    Тип элементов коллекции.
##  __Конструкторы
[ReadOnlyNotificationCollection<T>](M_Tessa_Platform_Collections_ReadOnlyNotificationCollection_1__ctor.htm)|
Создаёт экземпляр класса с указанием коллекции, для которой создаётся
доступная только для чтения обёртка.  
---|---  
## __Свойства
[Count](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1.count#system-
collections-objectmodel-readonlycollection-1-count)| Gets the number of
elements contained in the
[ReadOnlyCollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1)
instance.  
(Унаследован от
[ReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1)<T>)  
---|---  
[Item](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1.item#system-
collections-objectmodel-readonlycollection-1-item\(system-int32\))| Gets the
element at the specified index.  
(Унаследован от
[ReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1)<T>)  
[Items](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1.items#system-
collections-objectmodel-readonlycollection-1-items)| Returns the
[IList<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)
that the
[ReadOnlyCollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1)
wraps.  
(Унаследован от
[ReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1)<T>)  
##  __Методы
[Contains](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1.contains#system-
collections-objectmodel-readonlycollection-1-contains\(-0\))| Determines
whether an element is in the
[ReadOnlyCollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1).  
(Унаследован от
[ReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1)<T>)  
---|---  
[CopyTo](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1.copyto#system-
collections-objectmodel-readonlycollection-1-copyto\(-0\(\)-system-int32\))|
Copies the entire
[ReadOnlyCollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1)
to a compatible one-dimensional
[Array](https://learn.microsoft.com/dotnet/api/system.array), starting at the
specified index of the target array.  
(Унаследован от
[ReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1)<T>)  
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
[ReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1)<T>)  
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
[ReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1)<T>)  
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
[ReadOnlyObservableCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlyobservablecollection-1)<T>)  
[OnPropertyChanged](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlyobservablecollection-1.onpropertychanged#system-
collections-objectmodel-
readonlyobservablecollection-1-onpropertychanged\(system-componentmodel-
propertychangedeventargs\))| Raises the
[PropertyChanged](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlyobservablecollection-1.propertychanged)
event using the provided arguments.  
(Унаследован от
[ReadOnlyObservableCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlyobservablecollection-1)<T>)  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __События
[CollectionChanged](E_Tessa_Platform_Collections_ReadOnlyNotificationCollection_1_CollectionChanged.htm)|
Событие, возникающее при изменении коллекции, для которой создана обёртка.  
---|---  
[PropertyChanged](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlyobservablecollection-1.propertychanged)|
Occurs when a property value changes.  
(Унаследован от
[ReadOnlyObservableCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlyobservablecollection-1)<T>)  
##  __См. также
#### Ссылки
[Tessa.Platform.Collections - пространство
имён](N_Tessa_Platform_Collections.htm)
