# LinkedFreezableCollection<T> \- класс
##  __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class LinkedFreezableCollection<T> : Freezable, 
    	IList<T>, ICollection<T>, IEnumerable<T>, IEnumerable, IList, 
    	ICollection, IReadOnlyList<T>, IReadOnlyCollection<T>
    where T : LinkedFreezable
VB __Копировать
     Public MustInherit Class LinkedFreezableCollection(Of T As LinkedFreezable)
    	Inherits Freezable
    	Implements IList(Of T), ICollection(Of T), 
    	IEnumerable(Of T), IEnumerable, IList, ICollection, IReadOnlyList(Of T), 
    	IReadOnlyCollection(Of T)
C++ __Копировать
    generic<typename T>
    where T : LinkedFreezable
    public ref class LinkedFreezableCollection abstract : public Freezable, 
    	IList<T>, ICollection<T>, IEnumerable<T>, IEnumerable, IList, 
    	ICollection, IReadOnlyList<T>, IReadOnlyCollection<T>
F# __Копировать
     [<AbstractClassAttribute>]
    type LinkedFreezableCollection<'T when 'T : LinkedFreezable> = 
        class
            inherit Freezable
            interface IList<'T>
            interface ICollection<'T>
            interface IEnumerable<'T>
            interface IEnumerable
            interface IList
            interface ICollection
            interface IReadOnlyList<'T>
            interface IReadOnlyCollection<'T>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[DispatcherObject](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject) __[DependencyObject](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject) __[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable) __ LinkedFreezableCollection<T>
Derived
[Tessa.UI.Behaviors.BehaviorCollection](T_Tessa_UI_Behaviors_BehaviorCollection.htm)
[Tessa.UI.Behaviors.ColumnCommandCollection](T_Tessa_UI_Behaviors_ColumnCommandCollection.htm)
Implements
    [ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<T>, [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<T>, [IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<T>, [IReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlycollection-1)<T>, [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)<T>, [ICollection](https://learn.microsoft.com/dotnet/api/system.collections.icollection), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable), [IList](https://learn.microsoft.com/dotnet/api/system.collections.ilist)
#### Параметры типа
T
##  __Конструкторы
[LinkedFreezableCollection<T>](M_Tessa_UI_LinkedFreezableCollection_1__ctor.htm)|
Инициализирует новый экземпляр класса LinkedFreezableCollection<T>  
---|---  
##  __Свойства
[CanFreeze](https://learn.microsoft.com/dotnet/api/system.windows.freezable.canfreeze#system-
windows-freezable-canfreeze)| Gets a value that indicates whether the object
can be made unmodifiable.  
(Унаследован от
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable))  
---|---  
[Count](P_Tessa_UI_LinkedFreezableCollection_1_Count.htm)|  
[DependencyObjectType](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject.dependencyobjecttype#system-
windows-dependencyobject-dependencyobjecttype)| Gets the
[DependencyObjectType](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobjecttype)
that wraps the CLR type of this instance.  
(Унаследован от
[DependencyObject](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject))  
[Dispatcher](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject.dispatcher#system-
windows-threading-dispatcherobject-dispatcher)| Gets the
[Dispatcher](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcher)
this
[DispatcherObject](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject)
is associated with.  
(Унаследован от
[DispatcherObject](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject))  
[IsFrozen](https://learn.microsoft.com/dotnet/api/system.windows.freezable.isfrozen#system-
windows-freezable-isfrozen)| Gets a value that indicates whether the object is
currently modifiable.  
(Унаследован от
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable))  
[IsSealed](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject.issealed#system-
windows-dependencyobject-issealed)| Gets a value that indicates whether this
instance is currently sealed (read-only).  
(Унаследован от
[DependencyObject](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject))  
[Item](P_Tessa_UI_LinkedFreezableCollection_1_Item.htm)|  
## __Методы
[Add](M_Tessa_UI_LinkedFreezableCollection_1_Add.htm)|  
---|---  
[CheckAccess](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject.checkaccess#system-
windows-threading-dispatcherobject-checkaccess)| Determines whether the
calling thread has access to this
[DispatcherObject](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject).  
(Унаследован от
[DispatcherObject](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject))  
[Clear](M_Tessa_UI_LinkedFreezableCollection_1_Clear.htm)|  
[ClearItemsCore](M_Tessa_UI_LinkedFreezableCollection_1_ClearItemsCore.htm)|  
[ClearValue(DependencyProperty)](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject.clearvalue#system-
windows-dependencyobject-clearvalue\(system-windows-dependencyproperty\))|
Clears the local value of a property. The property to be cleared is specified
by a
[DependencyProperty](https://learn.microsoft.com/dotnet/api/system.windows.dependencyproperty)
identifier.  
(Унаследован от
[DependencyObject](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject))  
[ClearValue(DependencyPropertyKey)](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject.clearvalue#system-
windows-dependencyobject-clearvalue\(system-windows-dependencypropertykey\))|
Clears the local value of a read-only property. The property to be cleared is
specified by a
[DependencyPropertyKey](https://learn.microsoft.com/dotnet/api/system.windows.dependencypropertykey).  
(Унаследован от
[DependencyObject](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject))  
[Clone](https://learn.microsoft.com/dotnet/api/system.windows.freezable.clone#system-
windows-freezable-clone)| Creates a modifiable clone of the
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable),
making deep copies of the object's values. When copying the object's
dependency properties, this method copies expressions (which might no longer
resolve) but not animations or their current values.  
(Унаследован от
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable))  
[CloneCore](M_Tessa_UI_LinkedFreezableCollection_1_CloneCore.htm)|  
(Переопределяет
[Freezable.CloneCore(Freezable)](https://learn.microsoft.com/dotnet/api/system.windows.freezable.clonecore#system-
windows-freezable-clonecore\(system-windows-freezable\)))  
[CloneCurrentValue](https://learn.microsoft.com/dotnet/api/system.windows.freezable.clonecurrentvalue#system-
windows-freezable-clonecurrentvalue)| Creates a modifiable clone (deep copy)
of the
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable)
using its current values.  
(Унаследован от
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable))  
[CloneCurrentValueCore](M_Tessa_UI_LinkedFreezableCollection_1_CloneCurrentValueCore.htm)|  
(Переопределяет
[Freezable.CloneCurrentValueCore(Freezable)](https://learn.microsoft.com/dotnet/api/system.windows.freezable.clonecurrentvaluecore#system-
windows-freezable-clonecurrentvaluecore\(system-windows-freezable\)))  
[CoerceValue](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject.coercevalue#system-
windows-dependencyobject-coercevalue\(system-windows-dependencyproperty\))|
Coerces the value of the specified dependency property. This is accomplished
by invoking any
[CoerceValueCallback](https://learn.microsoft.com/dotnet/api/system.windows.coercevaluecallback)
function specified in property metadata for the dependency property as it
exists on the calling
[DependencyObject](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject).  
(Унаследован от
[DependencyObject](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject))  
[Contains](M_Tessa_UI_LinkedFreezableCollection_1_Contains.htm)|  
[CopyTo](M_Tessa_UI_LinkedFreezableCollection_1_CopyTo.htm)|  
[CreateInstance](https://learn.microsoft.com/dotnet/api/system.windows.freezable.createinstance#system-
windows-freezable-createinstance)| Initializes a new instance of the
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable)
class.  
(Унаследован от
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable))  
[CreateInstanceCore](https://learn.microsoft.com/dotnet/api/system.windows.freezable.createinstancecore#system-
windows-freezable-createinstancecore)| When implemented in a derived class,
creates a new instance of the
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable)
derived class.  
(Унаследован от
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable))  
[Equals](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject.equals#system-
windows-dependencyobject-equals\(system-object\))| Determines whether a
provided
[DependencyObject](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject)
is equivalent to the current
[DependencyObject](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject).  
(Унаследован от
[DependencyObject](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject))  
[Freeze](https://learn.microsoft.com/dotnet/api/system.windows.freezable.freeze#system-
windows-freezable-freeze)| Makes the current object unmodifiable and sets its
[IsFrozen](https://learn.microsoft.com/dotnet/api/system.windows.freezable.isfrozen#system-
windows-freezable-isfrozen) property to true.  
(Унаследован от
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable))  
[FreezeCore](https://learn.microsoft.com/dotnet/api/system.windows.freezable.freezecore#system-
windows-freezable-freezecore\(system-boolean\))| Makes the
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable)
object unmodifiable or tests whether it can be made unmodifiable.  
(Унаследован от
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable))  
[GetAsFrozen](https://learn.microsoft.com/dotnet/api/system.windows.freezable.getasfrozen#system-
windows-freezable-getasfrozen)| Creates a frozen copy of the
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable),
using base (non-animated) property values. Because the copy is frozen, any
frozen sub-objects are copied by reference.  
(Унаследован от
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable))  
[GetAsFrozenCore](M_Tessa_UI_LinkedFreezableCollection_1_GetAsFrozenCore.htm)|  
(Переопределяет
[Freezable.GetAsFrozenCore(Freezable)](https://learn.microsoft.com/dotnet/api/system.windows.freezable.getasfrozencore#system-
windows-freezable-getasfrozencore\(system-windows-freezable\)))  
[GetCurrentValueAsFrozen](https://learn.microsoft.com/dotnet/api/system.windows.freezable.getcurrentvalueasfrozen#system-
windows-freezable-getcurrentvalueasfrozen)| Creates a frozen copy of the
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable)
using current property values. Because the copy is frozen, any frozen sub-
objects are copied by reference.  
(Унаследован от
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable))  
[GetCurrentValueAsFrozenCore](M_Tessa_UI_LinkedFreezableCollection_1_GetCurrentValueAsFrozenCore.htm)|  
(Переопределяет
[Freezable.GetCurrentValueAsFrozenCore(Freezable)](https://learn.microsoft.com/dotnet/api/system.windows.freezable.getcurrentvalueasfrozencore#system-
windows-freezable-getcurrentvalueasfrozencore\(system-windows-freezable\)))  
[GetEnumerator](M_Tessa_UI_LinkedFreezableCollection_1_GetEnumerator.htm)|  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject.gethashcode#system-
windows-dependencyobject-gethashcode)| Gets a hash code for this
[DependencyObject](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject).  
(Унаследован от
[DependencyObject](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject))  
[GetLocalValueEnumerator](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject.getlocalvalueenumerator#system-
windows-dependencyobject-getlocalvalueenumerator)| Creates a specialized
enumerator for determining which dependency properties have locally set values
on this
[DependencyObject](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject).  
(Унаследован от
[DependencyObject](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject))  
[GetValue](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject.getvalue#system-
windows-dependencyobject-getvalue\(system-windows-dependencyproperty\))|
Returns the current effective value of a dependency property on this instance
of a
[DependencyObject](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject).  
(Унаследован от
[DependencyObject](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject))  
[IndexOf](M_Tessa_UI_LinkedFreezableCollection_1_IndexOf.htm)|  
[Insert](M_Tessa_UI_LinkedFreezableCollection_1_Insert.htm)|  
[InsertItemCore](M_Tessa_UI_LinkedFreezableCollection_1_InsertItemCore.htm)|  
[InvalidateProperty](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject.invalidateproperty#system-
windows-dependencyobject-invalidateproperty\(system-windows-
dependencyproperty\))| Re-evaluates the effective value for the specified
dependency property.  
(Унаследован от
[DependencyObject](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject))  
[OnChanged](https://learn.microsoft.com/dotnet/api/system.windows.freezable.onchanged#system-
windows-freezable-onchanged)| Called when the current
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable)
object is modified.  
(Унаследован от
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable))  
[OnFreezablePropertyChanged(DependencyObject,
DependencyObject)](https://learn.microsoft.com/dotnet/api/system.windows.freezable.onfreezablepropertychanged#system-
windows-freezable-onfreezablepropertychanged\(system-windows-dependencyobject-
system-windows-dependencyobject\))| Ensures that appropriate context pointers
are established for a
[DependencyObjectType](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobjecttype)
data member that has just been set.  
(Унаследован от
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable))  
[OnFreezablePropertyChanged(DependencyObject, DependencyObject,
DependencyProperty)](https://learn.microsoft.com/dotnet/api/system.windows.freezable.onfreezablepropertychanged#system-
windows-freezable-onfreezablepropertychanged\(system-windows-dependencyobject-
system-windows-dependencyobject-system-windows-dependencyproperty\))| This
member supports the Windows Presentation Foundation (WPF) infrastructure and
is not intended to be used directly from your code.  
(Унаследован от
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable))  
[OnPropertyChanged](https://learn.microsoft.com/dotnet/api/system.windows.freezable.onpropertychanged#system-
windows-freezable-onpropertychanged\(system-windows-
dependencypropertychangedeventargs\))| Overrides the
[DependencyObject](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject)
implementation of
[OnPropertyChanged(DependencyPropertyChangedEventArgs)](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject.onpropertychanged#system-
windows-dependencyobject-onpropertychanged\(system-windows-
dependencypropertychangedeventargs\)) to also invoke any
[Changed](https://learn.microsoft.com/dotnet/api/system.windows.freezable.changed)
handlers in response to a changing dependency property of type
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable).  
(Унаследован от
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable))  
[ReadLocalValue](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject.readlocalvalue#system-
windows-dependencyobject-readlocalvalue\(system-windows-dependencyproperty\))|
Returns the local value of a dependency property, if it exists.  
(Унаследован от
[DependencyObject](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject))  
[ReadPreamble](https://learn.microsoft.com/dotnet/api/system.windows.freezable.readpreamble#system-
windows-freezable-readpreamble)| Ensures that the
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable)
is being accessed from a valid thread. Inheritors of
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable)
must call this method at the beginning of any API that reads data members that
are not dependency properties.  
(Унаследован от
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable))  
[Remove](M_Tessa_UI_LinkedFreezableCollection_1_Remove.htm)|  
[RemoveAt](M_Tessa_UI_LinkedFreezableCollection_1_RemoveAt.htm)|  
[RemoveItemCore](M_Tessa_UI_LinkedFreezableCollection_1_RemoveItemCore.htm)|  
[ReplaceItemCore](M_Tessa_UI_LinkedFreezableCollection_1_ReplaceItemCore.htm)|  
[SetCurrentValue](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject.setcurrentvalue#system-
windows-dependencyobject-setcurrentvalue\(system-windows-dependencyproperty-
system-object\))| Sets the value of a dependency property without changing its
value source.  
(Унаследован от
[DependencyObject](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject))  
[SetValue(DependencyProperty,
Object)](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject.setvalue#system-
windows-dependencyobject-setvalue\(system-windows-dependencyproperty-system-
object\))| Sets the local value of a dependency property, specified by its
dependency property identifier.  
(Унаследован от
[DependencyObject](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject))  
[SetValue(DependencyPropertyKey,
Object)](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject.setvalue#system-
windows-dependencyobject-setvalue\(system-windows-dependencypropertykey-
system-object\))| Sets the local value of a read-only dependency property,
specified by the
[DependencyPropertyKey](https://learn.microsoft.com/dotnet/api/system.windows.dependencypropertykey)
identifier of the dependency property.  
(Унаследован от
[DependencyObject](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject))  
[ShouldSerializeProperty](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject.shouldserializeproperty#system-
windows-dependencyobject-shouldserializeproperty\(system-windows-
dependencyproperty\))| Returns a value that indicates whether serialization
processes should serialize the value for the provided dependency property.  
(Унаследован от
[DependencyObject](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject))  
[VerifyAccess](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject.verifyaccess#system-
windows-threading-dispatcherobject-verifyaccess)| Enforces that the calling
thread has access to this
[DispatcherObject](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject).  
(Унаследован от
[DispatcherObject](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject))  
[WritePostscript](https://learn.microsoft.com/dotnet/api/system.windows.freezable.writepostscript#system-
windows-freezable-writepostscript)| Raises the
[Changed](https://learn.microsoft.com/dotnet/api/system.windows.freezable.changed)
event for the
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable)
and invokes its
[OnChanged()](https://learn.microsoft.com/dotnet/api/system.windows.freezable.onchanged#system-
windows-freezable-onchanged) method. Classes that derive from
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable)
should call this method at the end of any API that modifies class members that
are not stored as dependency properties.  
(Унаследован от
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable))  
[WritePreamble](https://learn.microsoft.com/dotnet/api/system.windows.freezable.writepreamble#system-
windows-freezable-writepreamble)| Verifies that the
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable)
is not frozen and that it is being accessed from a valid threading context.
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable)
inheritors should call this method at the beginning of any API that writes to
data members that are not dependency properties.  
(Унаследован от
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable))  
##  __События
[Changed](https://learn.microsoft.com/dotnet/api/system.windows.freezable.changed)|
Occurs when the
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable)
or an object it contains is modified.  
(Унаследован от
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable))  
---|---  
##  __Методы расширения
[AddRange<T>](M_Tessa_Platform_Collections_Extensions_AddRange__1.htm)|
Добавляет значения items в коллекцию collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
---|---  
[AddRange<T>](M_Tessa_Platform_Collections_Extensions_AddRange__1_1.htm)|
Добавляет значения items в коллекцию collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[AddRangeForList](M_Tessa_Platform_Collections_Extensions_AddRangeForList.htm)|
Добавляет значения items в коллекцию collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[AsArray<T>](M_Tessa_Platform_Collections_EnumerableExtensions_AsArray__1.htm)|
Преобразует коллекцию в массив. В случае, если коллекция не является массивом,
к ней применяется
[ToArray<TSource>(IEnumerable<TSource>)](https://learn.microsoft.com/dotnet/api/system.linq.enumerable.toarray#system-
linq-enumerable-toarray-1\(system-collections-generic-
ienumerable\(\(-0\)\)\)).  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
[ConvertToListDictionaries<T>](M_Tessa_Views_Mapping_DictionaryConverter_ConvertToListDictionaries__1.htm)|
Осуществляет сопоставлению коллекции source на коллекцию коллекций ключ-
значение в соответствии с контекстом сопоставления по умолчанию  
(Определяется
[DictionaryConverter](T_Tessa_Views_Mapping_DictionaryConverter.htm))  
[ConvertToListDictionaries<T>](M_Tessa_Views_Mapping_DictionaryConverter_ConvertToListDictionaries__1_1.htm)|
Осуществляет сопоставлению коллекции source на коллекцию коллекций ключ-
значение в соответствии с контекстом сопоставления context  
(Определяется
[DictionaryConverter](T_Tessa_Views_Mapping_DictionaryConverter.htm))  
[ForEach<T>](M_Tessa_Platform_Collections_EnumerableExtensions_ForEach__1.htm)|
Выполняет указанное действие с каждым элементом коллекции
[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1).  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
[FullOuterJoin<T, TInner, TKey,
TResult>](M_Tessa_Platform_Collections_Extensions_FullOuterJoin__4.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[IndexOf<T>](M_Tessa_Platform_Collections_Extensions_IndexOf__1.htm)|
Возвращает индекс первого вхождения элемента в последовательность,
определяемый посредством заданного выражения.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[IndexOf<T>](M_Tessa_Platform_Collections_Extensions_IndexOf__1_2.htm)|
Выполняет поиск элемента, удовлетворяющего условиям указанного предиката, и
возвращает отсчитываемый от нуля индекс первого вхождения в диапазоне
элементов списка, начиная с заданного индекса и заканчивая последним
элементом.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[IndexOf<T>](M_Tessa_Platform_Collections_Extensions_IndexOf__1_1.htm)|
Возвращает индекс первого вхождения элемента в последовательность,
определяемый посредством заданного компаратора
[IEqualityComparer<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.iequalitycomparer-1).  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[IndexOf<T>](M_Tessa_Platform_Collections_Extensions_IndexOf__1_3.htm)|
Выполняет поиск элемента, удовлетворяющего условиям указанного предиката, и
возвращает отсчитываемый от нуля индекс первого вхождения в диапазоне
элементов списка, начинающемся с заданного индекса и содержащем указанное
число элементов.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[InsertRange<T>](M_Tessa_Platform_Collections_Extensions_InsertRange__1.htm)|
Вставляет диапазон элементов в заданный список items, начиная с указанного
индекса index.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[InsertRangeForList](M_Tessa_Platform_Collections_Extensions_InsertRangeForList.htm)|
Вставляет диапазон элементов в заданный список items, начиная с указанного
индекса index.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[LastIndexOf<T>](M_Tessa_Platform_Collections_Extensions_LastIndexOf__1.htm)|
Возвращает индекс последнего вхождения элемента в последовательность,
определяемый посредством заданного выражения.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[LastIndexOf<T>](M_Tessa_Platform_Collections_Extensions_LastIndexOf__1_1.htm)|
Возвращает индекс последнего вхождения элемента в последовательность,
определяемый посредством заданного компаратора
[IEqualityComparer<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.iequalitycomparer-1).  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<T>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<T>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__1_1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<T,
TKey>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__2.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<T,
TKey>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__2_1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByLocalized<T>](M_Tessa_Platform_PlatformExtensions_OrderByLocalized__1.htm)|
Сортирует значения последовательности по возрастанию по локализованному ключу,
который определяется для каждого элемента.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[OrderByLocalizedDescending<T>](M_Tessa_Platform_PlatformExtensions_OrderByLocalizedDescending__1.htm)|
Сортирует значения последовательности по убыванию по локализованному ключу,
который определяется для каждого элемента.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[RemoveAll<T>](M_Tessa_Platform_Collections_Extensions_RemoveAll__1.htm)|
Удаляет все элементы, совпадающие по заданному предикату. Возвращает
количество удалённых элементов.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[RemoveAllForList](M_Tessa_Platform_Collections_Extensions_RemoveAllForList.htm)|
Удаляет все элементы, совпадающие по заданному предикату. Возвращает
количество удалённых элементов.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[RemoveRange<T>](M_Tessa_Platform_Collections_Extensions_RemoveRange__1.htm)|
Удаляет значения items из коллекции collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[RemoveRange<T>](M_Tessa_Platform_Collections_Extensions_RemoveRange__1_1.htm)|
Удаляет значения items из коллекции collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[RunWithMaxDegreeOfParallelismAsync<T>](M_Tessa_Platform_PlatformExtensions_RunWithMaxDegreeOfParallelismAsync__1.htm)|
Выполняет асинхронную обработку элементов с ограничением на максимальное
количество параллельных задач.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[ToDictionaryAsync<T, TKey,
TElement>](M_Tessa_Platform_PlatformExtensions_ToDictionaryAsync__3.htm)|
Создает словарь [Dictionary<TKey,
TValue>](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)
из объекта
[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)
в соответствии с заданными функциями синхронного селектора ключа и
асинхронного селектора значения.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[ToObservableCollection<T>](M_Tessa_Platform_Collections_Extensions_ToObservableCollection__1.htm)|
Преобразует коллекцию IEnumerable в ObservableCollection  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[ToSealableList<T>](M_Tessa_Platform_Collections_Extensions_ToSealableList__1.htm)|
Возвращает список объектов, поддерживающий защиту от изменений. Каждый из
объектов T в списке либо не реализует интерфейс
[ISealable](T_Tessa_Platform_ISealable.htm), либо защита от изменений таких
объектов не активируется вместе со списком.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[TryFirst<T>](M_Tessa_Platform_Collections_EnumerableExtensions_TryFirst__1.htm)|
Возвращает первый элемент последовательности, удовлетворяющий условию.  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
[TrySingleOrDefault<T>](M_Tessa_Platform_Collections_EnumerableExtensions_TrySingleOrDefault__1.htm)|
Возвращает единственный конкретный элемент коллекции или значение по умолчанию
для типа, если этот элемент не найден.  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.UI - пространство имён](N_Tessa_UI.htm)
