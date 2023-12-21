# CommandCollection - класс
Represents an collection of Command child elements.
## __Definition
 **Пространство имён:**
[Tessa.Platform.CommandLine](N_Tessa_Platform_CommandLine.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CommandCollection : KeyedCollection<string, Command>
VB __Копировать
     Public NotInheritable Class CommandCollection
    	Inherits KeyedCollection(Of String, Command)
C++ __Копировать
     public ref class CommandCollection sealed : public KeyedCollection<String^, Command^>
F# __Копировать
     [<SealedAttribute>]
    type CommandCollection = 
        class
            inherit KeyedCollection<string, Command>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<[Command](T_Tessa_Platform_CommandLine_Command.htm)> __[KeyedCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.keyedcollection-2)<[String](https://learn.microsoft.com/dotnet/api/system.string), [Command](T_Tessa_Platform_CommandLine_Command.htm)> __ CommandCollection
##  __Конструкторы
[CommandCollection](M_Tessa_Platform_CommandLine_CommandCollection__ctor.htm)|
Initializes a new instance of the CommandCollection class.  
---|---  
## __Свойства
[Comparer](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.keyedcollection-2.comparer#system-
collections-objectmodel-keyedcollection-2-comparer)| Gets the generic equality
comparer that is used to determine equality of keys in the collection.  
(Унаследован от
[KeyedCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.keyedcollection-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Command](T_Tessa_Platform_CommandLine_Command.htm)>)  
---|---  
[Count](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1.count#system-
collections-objectmodel-collection-1-count)| Gets the number of elements
actually contained in the
[Collection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1).  
(Унаследован от
[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<[Command](T_Tessa_Platform_CommandLine_Command.htm)>)  
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.keyedcollection-2.dictionary#system-
collections-objectmodel-keyedcollection-2-dictionary)| Gets the lookup
dictionary of the [KeyedCollection<TKey,
TItem>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.keyedcollection-2).  
(Унаследован от
[KeyedCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.keyedcollection-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Command](T_Tessa_Platform_CommandLine_Command.htm)>)  
[Item[Int32]](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1.item#system-
collections-objectmodel-collection-1-item\(system-int32\))| Gets or sets the
element at the specified index.  
(Унаследован от
[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<[Command](T_Tessa_Platform_CommandLine_Command.htm)>)  
[Item[TKey]](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.keyedcollection-2.item#system-
collections-objectmodel-keyedcollection-2-item\(-0\))| Gets the element with
the specified key.  
(Унаследован от
[KeyedCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.keyedcollection-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Command](T_Tessa_Platform_CommandLine_Command.htm)>)  
[Items](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1.items#system-
collections-objectmodel-collection-1-items)| Gets a
[IList<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)
wrapper around the
[Collection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1).  
(Унаследован от
[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<[Command](T_Tessa_Platform_CommandLine_Command.htm)>)  
##  __Методы
[Add](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1.add#system-
collections-objectmodel-collection-1-add\(-0\))| Adds an object to the end of
the
[Collection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1).  
(Унаследован от
[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<[Command](T_Tessa_Platform_CommandLine_Command.htm)>)  
---|---  
[ChangeItemKey](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.keyedcollection-2.changeitemkey#system-
collections-objectmodel-keyedcollection-2-changeitemkey\(-1-0\))| Changes the
key associated with the specified element in the lookup dictionary.  
(Унаследован от
[KeyedCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.keyedcollection-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Command](T_Tessa_Platform_CommandLine_Command.htm)>)  
[Clear](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1.clear#system-
collections-objectmodel-collection-1-clear)| Removes all elements from the
[Collection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1).  
(Унаследован от
[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<[Command](T_Tessa_Platform_CommandLine_Command.htm)>)  
[ClearItems](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.keyedcollection-2.clearitems#system-
collections-objectmodel-keyedcollection-2-clearitems)| Removes all elements
from the [KeyedCollection<TKey,
TItem>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.keyedcollection-2).  
(Унаследован от
[KeyedCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.keyedcollection-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Command](T_Tessa_Platform_CommandLine_Command.htm)>)  
[Contains(T)](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1.contains#system-
collections-objectmodel-collection-1-contains\(-0\))| Determines whether an
element is in the
[Collection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1).  
(Унаследован от
[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<[Command](T_Tessa_Platform_CommandLine_Command.htm)>)  
[Contains(TKey)](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.keyedcollection-2.contains#system-
collections-objectmodel-keyedcollection-2-contains\(-0\))| Determines whether
the collection contains an element with the specified key.  
(Унаследован от
[KeyedCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.keyedcollection-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Command](T_Tessa_Platform_CommandLine_Command.htm)>)  
[CopyTo](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1.copyto#system-
collections-objectmodel-collection-1-copyto\(-0\(\)-system-int32\))| Copies
the entire
[Collection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)
to a compatible one-dimensional
[Array](https://learn.microsoft.com/dotnet/api/system.array), starting at the
specified index of the target array.  
(Унаследован от
[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<[Command](T_Tessa_Platform_CommandLine_Command.htm)>)  
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
[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<[Command](T_Tessa_Platform_CommandLine_Command.htm)>)  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetKeyForItem](M_Tessa_Platform_CommandLine_CommandCollection_GetKeyForItem.htm)|
When implemented in a derived class, extracts the key from the specified
element.  
(Переопределяет [KeyedCollection<TKey,
TItem>.GetKeyForItem(TItem)](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.keyedcollection-2.getkeyforitem#system-
collections-objectmodel-keyedcollection-2-getkeyforitem\(-1\)))  
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
[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<[Command](T_Tessa_Platform_CommandLine_Command.htm)>)  
[Insert](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1.insert#system-
collections-objectmodel-collection-1-insert\(system-int32-0\))| Inserts an
element into the
[Collection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)
at the specified index.  
(Унаследован от
[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<[Command](T_Tessa_Platform_CommandLine_Command.htm)>)  
[InsertItem](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.keyedcollection-2.insertitem#system-
collections-objectmodel-keyedcollection-2-insertitem\(system-int32-1\))|
Inserts an element into the [KeyedCollection<TKey,
TItem>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.keyedcollection-2)
at the specified index.  
(Унаследован от
[KeyedCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.keyedcollection-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Command](T_Tessa_Platform_CommandLine_Command.htm)>)  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Remove(T)](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1.remove#system-
collections-objectmodel-collection-1-remove\(-0\))| Removes the first
occurrence of a specific object from the
[Collection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1).  
(Унаследован от
[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<[Command](T_Tessa_Platform_CommandLine_Command.htm)>)  
[Remove(TKey)](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.keyedcollection-2.remove#system-
collections-objectmodel-keyedcollection-2-remove\(-0\))| Removes the element
with the specified key from the [KeyedCollection<TKey,
TItem>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.keyedcollection-2).  
(Унаследован от
[KeyedCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.keyedcollection-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Command](T_Tessa_Platform_CommandLine_Command.htm)>)  
[RemoveAt](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1.removeat#system-
collections-objectmodel-collection-1-removeat\(system-int32\))| Removes the
element at the specified index of the
[Collection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1).  
(Унаследован от
[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<[Command](T_Tessa_Platform_CommandLine_Command.htm)>)  
[RemoveItem](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.keyedcollection-2.removeitem#system-
collections-objectmodel-keyedcollection-2-removeitem\(system-int32\))| Removes
the element at the specified index of the [KeyedCollection<TKey,
TItem>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.keyedcollection-2).  
(Унаследован от
[KeyedCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.keyedcollection-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Command](T_Tessa_Platform_CommandLine_Command.htm)>)  
[SetItem](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.keyedcollection-2.setitem#system-
collections-objectmodel-keyedcollection-2-setitem\(system-int32-1\))| Replaces
the item at the specified index with the specified item.  
(Унаследован от
[KeyedCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.keyedcollection-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Command](T_Tessa_Platform_CommandLine_Command.htm)>)  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetCommand](M_Tessa_Platform_CommandLine_CommandCollection_TryGetCommand.htm)|
Gets the command with the specified name.  
[TryGetValue](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.keyedcollection-2.trygetvalue#system-
collections-objectmodel-keyedcollection-2-trygetvalue\(-0-1@\))|  
(Унаследован от
[KeyedCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.keyedcollection-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Command](T_Tessa_Platform_CommandLine_Command.htm)>)  
##  __См. также
#### Ссылки
[Tessa.Platform.CommandLine - пространство
имён](N_Tessa_Platform_CommandLine.htm)
