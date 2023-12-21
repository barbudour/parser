# ShowSplashInTaskbarWhenDeactivated - класс
##  __Definition
 **Пространство имён:** [Tessa.UI.Behaviors](N_Tessa_UI_Behaviors.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ShowSplashInTaskbarWhenDeactivated : ShowInTaskbarWhenDeactivated
VB __Копировать
     Public NotInheritable Class ShowSplashInTaskbarWhenDeactivated
    	Inherits ShowInTaskbarWhenDeactivated
C++ __Копировать
     public ref class ShowSplashInTaskbarWhenDeactivated sealed : public ShowInTaskbarWhenDeactivated
F# __Копировать
     [<SealedAttribute>]
    type ShowSplashInTaskbarWhenDeactivated = 
        class
            inherit ShowInTaskbarWhenDeactivated
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[DispatcherObject](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject) __[DependencyObject](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject) __[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable) __[LinkedFreezable](T_Tessa_UI_LinkedFreezable.htm) __[Behavior](T_Tessa_UI_Behaviors_Behavior.htm) __[Behavior](T_Tessa_UI_Behaviors_Behavior_1.htm)<[Window](https://learn.microsoft.com/dotnet/api/system.windows.window)> __[ShowInTaskbarWhenDeactivated](T_Tessa_UI_Behaviors_ShowInTaskbarWhenDeactivated.htm) __ ShowSplashInTaskbarWhenDeactivated
##  __Конструкторы
[ShowSplashInTaskbarWhenDeactivated](M_Tessa_UI_Behaviors_ShowSplashInTaskbarWhenDeactivated__ctor.htm)|
Инициализирует новый экземпляр класса ShowSplashInTaskbarWhenDeactivated  
---|---  
##  __Свойства
[AssociatedObject](P_Tessa_UI_Behaviors_Behavior_1_AssociatedObject.htm)|  
(Унаследован от [Behavior<T>](T_Tessa_UI_Behaviors_Behavior_1.htm))  
---|---  
[CanFreeze](https://learn.microsoft.com/dotnet/api/system.windows.freezable.canfreeze#system-
windows-freezable-canfreeze)| Gets a value that indicates whether the object
can be made unmodifiable.  
(Унаследован от
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable))  
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
##  __Методы
[CheckAccess](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject.checkaccess#system-
windows-threading-dispatcherobject-checkaccess)| Determines whether the
calling thread has access to this
[DispatcherObject](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject).  
(Унаследован от
[DispatcherObject](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject))  
---|---  
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
[CloneCore](https://learn.microsoft.com/dotnet/api/system.windows.freezable.clonecore#system-
windows-freezable-clonecore\(system-windows-freezable\))| Makes the instance a
clone (deep copy) of the specified
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable)
using base (non-animated) property values.  
(Унаследован от
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable))  
[CloneCurrentValue](https://learn.microsoft.com/dotnet/api/system.windows.freezable.clonecurrentvalue#system-
windows-freezable-clonecurrentvalue)| Creates a modifiable clone (deep copy)
of the
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable)
using its current values.  
(Унаследован от
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable))  
[CloneCurrentValueCore](https://learn.microsoft.com/dotnet/api/system.windows.freezable.clonecurrentvaluecore#system-
windows-freezable-clonecurrentvaluecore\(system-windows-freezable\))| Makes
the instance a modifiable clone (deep copy) of the specified
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable)
using current property values.  
(Унаследован от
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable))  
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
[CreateInstance](https://learn.microsoft.com/dotnet/api/system.windows.freezable.createinstance#system-
windows-freezable-createinstance)| Initializes a new instance of the
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable)
class.  
(Унаследован от
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable))  
[CreateInstanceCore](M_Tessa_UI_Behaviors_ShowInTaskbarWhenDeactivated_CreateInstanceCore.htm)|  
(Унаследован от
[ShowInTaskbarWhenDeactivated](T_Tessa_UI_Behaviors_ShowInTaskbarWhenDeactivated.htm))  
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
[GetAsFrozenCore](https://learn.microsoft.com/dotnet/api/system.windows.freezable.getasfrozencore#system-
windows-freezable-getasfrozencore\(system-windows-freezable\))| Makes the
instance a frozen clone of the specified
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable)
using base (non-animated) property values.  
(Унаследован от
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable))  
[GetCurrentValueAsFrozen](https://learn.microsoft.com/dotnet/api/system.windows.freezable.getcurrentvalueasfrozen#system-
windows-freezable-getcurrentvalueasfrozen)| Creates a frozen copy of the
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable)
using current property values. Because the copy is frozen, any frozen sub-
objects are copied by reference.  
(Унаследован от
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable))  
[GetCurrentValueAsFrozenCore](https://learn.microsoft.com/dotnet/api/system.windows.freezable.getcurrentvalueasfrozencore#system-
windows-freezable-getcurrentvalueasfrozencore\(system-windows-freezable\))|
Makes the current instance a frozen clone of the specified
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable).
If the object has animated dependency properties, their current animated
values are copied.  
(Унаследован от
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable))  
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
[GetRequiredType](M_Tessa_UI_Behaviors_Behavior_1_GetRequiredType.htm)|  
(Унаследован от [Behavior<T>](T_Tessa_UI_Behaviors_Behavior_1.htm))  
[GetRequiredTypeCount](M_Tessa_UI_Behaviors_Behavior_1_GetRequiredTypeCount.htm)|  
(Унаследован от [Behavior<T>](T_Tessa_UI_Behaviors_Behavior_1.htm))  
[GetValue](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject.getvalue#system-
windows-dependencyobject-getvalue\(system-windows-dependencyproperty\))|
Returns the current effective value of a dependency property on this instance
of a
[DependencyObject](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject).  
(Унаследован от
[DependencyObject](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject))  
[InvalidateProperty](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject.invalidateproperty#system-
windows-dependencyobject-invalidateproperty\(system-windows-
dependencyproperty\))| Re-evaluates the effective value for the specified
dependency property.  
(Унаследован от
[DependencyObject](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject))  
[OnActivated](M_Tessa_UI_Behaviors_ShowInTaskbarWhenDeactivated_OnActivated.htm)|  
(Унаследован от
[ShowInTaskbarWhenDeactivated](T_Tessa_UI_Behaviors_ShowInTaskbarWhenDeactivated.htm))  
[OnAttached](M_Tessa_UI_Behaviors_ShowInTaskbarWhenDeactivated_OnAttached.htm)|  
(Унаследован от
[ShowInTaskbarWhenDeactivated](T_Tessa_UI_Behaviors_ShowInTaskbarWhenDeactivated.htm))  
[OnChanged](https://learn.microsoft.com/dotnet/api/system.windows.freezable.onchanged#system-
windows-freezable-onchanged)| Called when the current
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable)
object is modified.  
(Унаследован от
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable))  
[OnDeactivated](M_Tessa_UI_Behaviors_ShowSplashInTaskbarWhenDeactivated_OnDeactivated.htm)|  
(Переопределяет [ShowInTaskbarWhenDeactivated.OnDeactivated(Object,
EventArgs)](M_Tessa_UI_Behaviors_ShowInTaskbarWhenDeactivated_OnDeactivated.htm))  
[OnDetaching](M_Tessa_UI_Behaviors_ShowInTaskbarWhenDeactivated_OnDetaching.htm)|  
(Унаследован от
[ShowInTaskbarWhenDeactivated](T_Tessa_UI_Behaviors_ShowInTaskbarWhenDeactivated.htm))  
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
##  __См. также
#### Ссылки
[Tessa.UI.Behaviors - пространство имён](N_Tessa_UI_Behaviors.htm)
