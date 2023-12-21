# CommandOnEventBehaviorBase - класс
##  __Definition
 **Пространство имён:** [Tessa.UI.Behaviors](N_Tessa_UI_Behaviors.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class CommandOnEventBehaviorBase : Behavior, 
    	ICommandSource
VB __Копировать
     Public MustInherit Class CommandOnEventBehaviorBase
    	Inherits Behavior
    	Implements ICommandSource
C++ __Копировать
     public ref class CommandOnEventBehaviorBase abstract : public Behavior, 
    	ICommandSource
F# __Копировать
     [<AbstractClassAttribute>]
    type CommandOnEventBehaviorBase = 
        class
            inherit Behavior
            interface ICommandSource
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[DispatcherObject](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject) __[DependencyObject](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject) __[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable) __[LinkedFreezable](T_Tessa_UI_LinkedFreezable.htm) __[Behavior](T_Tessa_UI_Behaviors_Behavior.htm) __ CommandOnEventBehaviorBase
Derived
[Tessa.UI.Behaviors.CommandOnContainerEvent](T_Tessa_UI_Behaviors_CommandOnContainerEvent.htm)
[Tessa.UI.Behaviors.CommandOnEvent](T_Tessa_UI_Behaviors_CommandOnEvent.htm)
Implements
    [ICommandSource](https://learn.microsoft.com/dotnet/api/system.windows.input.icommandsource)
##  __Конструкторы
[CommandOnEventBehaviorBase](M_Tessa_UI_Behaviors_CommandOnEventBehaviorBase__ctor.htm)|
Инициализирует новый экземпляр класса CommandOnEventBehaviorBase  
---|---  
##  __Свойства
[AssociatedObject](P_Tessa_UI_Behaviors_CommandOnEventBehaviorBase_AssociatedObject.htm)|  
---|---  
[CanFreeze](https://learn.microsoft.com/dotnet/api/system.windows.freezable.canfreeze#system-
windows-freezable-canfreeze)| Gets a value that indicates whether the object
can be made unmodifiable.  
(Унаследован от
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable))  
[Command](P_Tessa_UI_Behaviors_CommandOnEventBehaviorBase_Command.htm)|  
[CommandParameter](P_Tessa_UI_Behaviors_CommandOnEventBehaviorBase_CommandParameter.htm)|  
[CommandTarget](P_Tessa_UI_Behaviors_CommandOnEventBehaviorBase_CommandTarget.htm)|  
[Delay](P_Tessa_UI_Behaviors_CommandOnEventBehaviorBase_Delay.htm)|  
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
[Event](P_Tessa_UI_Behaviors_CommandOnEventBehaviorBase_Event.htm)|  
[Filter](P_Tessa_UI_Behaviors_CommandOnEventBehaviorBase_Filter.htm)|  
[HandledEventsToo](P_Tessa_UI_Behaviors_CommandOnEventBehaviorBase_HandledEventsToo.htm)|  
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
[CloneCore](M_Tessa_UI_Behaviors_CommandOnEventBehaviorBase_CloneCore.htm)|  
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
[CloneCurrentValueCore](M_Tessa_UI_Behaviors_CommandOnEventBehaviorBase_CloneCurrentValueCore.htm)|  
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
[ExecuteCommand](M_Tessa_UI_Behaviors_CommandOnEventBehaviorBase_ExecuteCommand.htm)|  
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
[GetAsFrozenCore](M_Tessa_UI_Behaviors_CommandOnEventBehaviorBase_GetAsFrozenCore.htm)|  
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
[GetCurrentValueAsFrozenCore](M_Tessa_UI_Behaviors_CommandOnEventBehaviorBase_GetCurrentValueAsFrozenCore.htm)|  
(Переопределяет
[Freezable.GetCurrentValueAsFrozenCore(Freezable)](https://learn.microsoft.com/dotnet/api/system.windows.freezable.getcurrentvalueasfrozencore#system-
windows-freezable-getcurrentvalueasfrozencore\(system-windows-freezable\)))  
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
[GetRequiredType](M_Tessa_UI_Behaviors_CommandOnEventBehaviorBase_GetRequiredType.htm)|  
(Переопределяет
[Behavior.GetRequiredType(Int32)](M_Tessa_UI_Behaviors_Behavior_GetRequiredType.htm))  
[GetRequiredTypeCount](M_Tessa_UI_Behaviors_CommandOnEventBehaviorBase_GetRequiredTypeCount.htm)|  
(Переопределяет
[Behavior.GetRequiredTypeCount()](M_Tessa_UI_Behaviors_Behavior_GetRequiredTypeCount.htm))  
[GetValue](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject.getvalue#system-
windows-dependencyobject-getvalue\(system-windows-dependencyproperty\))|
Returns the current effective value of a dependency property on this instance
of a
[DependencyObject](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject).  
(Унаследован от
[DependencyObject](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject))  
[HandleEvent](M_Tessa_UI_Behaviors_CommandOnEventBehaviorBase_HandleEvent.htm)|  
[InvalidateProperty](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject.invalidateproperty#system-
windows-dependencyobject-invalidateproperty\(system-windows-
dependencyproperty\))| Re-evaluates the effective value for the specified
dependency property.  
(Унаследован от
[DependencyObject](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject))  
[OnAttached](M_Tessa_UI_Behaviors_CommandOnEventBehaviorBase_OnAttached.htm)|  
(Переопределяет
[Behavior.OnAttached()](M_Tessa_UI_Behaviors_Behavior_OnAttached.htm))  
[OnChanged](https://learn.microsoft.com/dotnet/api/system.windows.freezable.onchanged#system-
windows-freezable-onchanged)| Called when the current
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable)
object is modified.  
(Унаследован от
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable))  
[OnDetaching](M_Tessa_UI_Behaviors_CommandOnEventBehaviorBase_OnDetaching.htm)|  
(Переопределяет
[Behavior.OnDetaching()](M_Tessa_UI_Behaviors_Behavior_OnDetaching.htm))  
[OnEvent](M_Tessa_UI_Behaviors_CommandOnEventBehaviorBase_OnEvent.htm)|  
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
[SubscribeToEventCore](M_Tessa_UI_Behaviors_CommandOnEventBehaviorBase_SubscribeToEventCore.htm)|  
[UnsubscribeFromEventCore](M_Tessa_UI_Behaviors_CommandOnEventBehaviorBase_UnsubscribeFromEventCore.htm)|  
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
##  __Поля
[CommandParameterProperty](F_Tessa_UI_Behaviors_CommandOnEventBehaviorBase_CommandParameterProperty.htm)|  
---|---  
[CommandProperty](F_Tessa_UI_Behaviors_CommandOnEventBehaviorBase_CommandProperty.htm)|  
[CommandTargetProperty](F_Tessa_UI_Behaviors_CommandOnEventBehaviorBase_CommandTargetProperty.htm)|  
## __См. также
#### Ссылки
[Tessa.UI.Behaviors - пространство имён](N_Tessa_UI_Behaviors.htm)
