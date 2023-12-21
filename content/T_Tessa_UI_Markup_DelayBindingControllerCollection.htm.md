# DelayBindingControllerCollection - класс
##  __Definition
 **Пространство имён:** [Tessa.UI.Markup](N_Tessa_UI_Markup.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public class DelayBindingControllerCollection : FreezableCollection<DelayBindingController>
VB __Копировать
     Public Class DelayBindingControllerCollection
    	Inherits FreezableCollection(Of DelayBindingController)
C++ __Копировать
     public ref class DelayBindingControllerCollection : public FreezableCollection<DelayBindingController^>
F# __Копировать
     type DelayBindingControllerCollection = 
        class
            inherit FreezableCollection<DelayBindingController>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[DispatcherObject](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject) __[DependencyObject](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject) __[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable) __[Animatable](https://learn.microsoft.com/dotnet/api/system.windows.media.animation.animatable) __[FreezableCollection](https://learn.microsoft.com/dotnet/api/system.windows.freezablecollection-1)<[DelayBindingController](T_Tessa_UI_Markup_DelayBindingController.htm)> __ DelayBindingControllerCollection
##  __Конструкторы
[DelayBindingControllerCollection](M_Tessa_UI_Markup_DelayBindingControllerCollection__ctor.htm)|
Инициализирует новый экземпляр класса DelayBindingControllerCollection  
---|---  
##  __Свойства
[CanFreeze](https://learn.microsoft.com/dotnet/api/system.windows.freezable.canfreeze#system-
windows-freezable-canfreeze)| Gets a value that indicates whether the object
can be made unmodifiable.  
(Унаследован от
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable))  
---|---  
[Count](https://learn.microsoft.com/dotnet/api/system.windows.freezablecollection-1.count#system-
windows-freezablecollection-1-count)| Gets the number of elements contained by
this
[FreezableCollection<T>](https://learn.microsoft.com/dotnet/api/system.windows.freezablecollection-1).  
(Унаследован от
[FreezableCollection](https://learn.microsoft.com/dotnet/api/system.windows.freezablecollection-1)<[DelayBindingController](T_Tessa_UI_Markup_DelayBindingController.htm)>)  
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
[HasAnimatedProperties](https://learn.microsoft.com/dotnet/api/system.windows.media.animation.animatable.hasanimatedproperties#system-
windows-media-animation-animatable-hasanimatedproperties)| Gets a value that
indicates whether one or more
[AnimationClock](https://learn.microsoft.com/dotnet/api/system.windows.media.animation.animationclock)
objects is associated with any of this object's dependency properties.  
(Унаследован от
[Animatable](https://learn.microsoft.com/dotnet/api/system.windows.media.animation.animatable))  
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
[Item](https://learn.microsoft.com/dotnet/api/system.windows.freezablecollection-1.item#system-
windows-freezablecollection-1-item\(system-int32\))| Gets or sets the element
at the specified index.  
(Унаследован от
[FreezableCollection](https://learn.microsoft.com/dotnet/api/system.windows.freezablecollection-1)<[DelayBindingController](T_Tessa_UI_Markup_DelayBindingController.htm)>)  
##  __Методы
[Add](https://learn.microsoft.com/dotnet/api/system.windows.freezablecollection-1.add#system-
windows-freezablecollection-1-add\(-0\))| Adds the specified object to the end
of the
[FreezableCollection<T>](https://learn.microsoft.com/dotnet/api/system.windows.freezablecollection-1).  
(Унаследован от
[FreezableCollection](https://learn.microsoft.com/dotnet/api/system.windows.freezablecollection-1)<[DelayBindingController](T_Tessa_UI_Markup_DelayBindingController.htm)>)  
---|---  
[ApplyAnimationClock(DependencyProperty,
AnimationClock)](https://learn.microsoft.com/dotnet/api/system.windows.media.animation.animatable.applyanimationclock#system-
windows-media-animation-animatable-applyanimationclock\(system-windows-
dependencyproperty-system-windows-media-animation-animationclock\))| Applies
an
[AnimationClock](https://learn.microsoft.com/dotnet/api/system.windows.media.animation.animationclock)
to the specified
[DependencyProperty](https://learn.microsoft.com/dotnet/api/system.windows.dependencyproperty).
If the property is already animated, the
[SnapshotAndReplace](https://learn.microsoft.com/dotnet/api/system.windows.media.animation.handoffbehavior)
handoff behavior is used.  
(Унаследован от
[Animatable](https://learn.microsoft.com/dotnet/api/system.windows.media.animation.animatable))  
[ApplyAnimationClock(DependencyProperty, AnimationClock,
HandoffBehavior)](https://learn.microsoft.com/dotnet/api/system.windows.media.animation.animatable.applyanimationclock#system-
windows-media-animation-animatable-applyanimationclock\(system-windows-
dependencyproperty-system-windows-media-animation-animationclock-system-
windows-media-animation-handoffbehavior\))| Applies an
[AnimationClock](https://learn.microsoft.com/dotnet/api/system.windows.media.animation.animationclock)
to the specified
[DependencyProperty](https://learn.microsoft.com/dotnet/api/system.windows.dependencyproperty).
If the property is already animated, the specified
[HandoffBehavior](https://learn.microsoft.com/dotnet/api/system.windows.media.animation.handoffbehavior)
is used.  
(Унаследован от
[Animatable](https://learn.microsoft.com/dotnet/api/system.windows.media.animation.animatable))  
[BeginAnimation(DependencyProperty,
AnimationTimeline)](https://learn.microsoft.com/dotnet/api/system.windows.media.animation.animatable.beginanimation#system-
windows-media-animation-animatable-beginanimation\(system-windows-
dependencyproperty-system-windows-media-animation-animationtimeline\))|
Applies an animation to the specified
[DependencyProperty](https://learn.microsoft.com/dotnet/api/system.windows.dependencyproperty).
The animation is started when the next frame is rendered. If the specified
property is already animated, the
[SnapshotAndReplace](https://learn.microsoft.com/dotnet/api/system.windows.media.animation.handoffbehavior)
handoff behavior is used.  
(Унаследован от
[Animatable](https://learn.microsoft.com/dotnet/api/system.windows.media.animation.animatable))  
[BeginAnimation(DependencyProperty, AnimationTimeline,
HandoffBehavior)](https://learn.microsoft.com/dotnet/api/system.windows.media.animation.animatable.beginanimation#system-
windows-media-animation-animatable-beginanimation\(system-windows-
dependencyproperty-system-windows-media-animation-animationtimeline-system-
windows-media-animation-handoffbehavior\))| Applies an animation to the
specified
[DependencyProperty](https://learn.microsoft.com/dotnet/api/system.windows.dependencyproperty).
The animation is started when the next frame is rendered. If the specified
property is already animated, the specified
[HandoffBehavior](https://learn.microsoft.com/dotnet/api/system.windows.media.animation.handoffbehavior)
is used.  
(Унаследован от
[Animatable](https://learn.microsoft.com/dotnet/api/system.windows.media.animation.animatable))  
[CheckAccess](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject.checkaccess#system-
windows-threading-dispatcherobject-checkaccess)| Determines whether the
calling thread has access to this
[DispatcherObject](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject).  
(Унаследован от
[DispatcherObject](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject))  
[Clear](https://learn.microsoft.com/dotnet/api/system.windows.freezablecollection-1.clear#system-
windows-freezablecollection-1-clear)| Removes all elements from the
collection.  
(Унаследован от
[FreezableCollection](https://learn.microsoft.com/dotnet/api/system.windows.freezablecollection-1)<[DelayBindingController](T_Tessa_UI_Markup_DelayBindingController.htm)>)  
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
[Clone](https://learn.microsoft.com/dotnet/api/system.windows.freezablecollection-1.clone#system-
windows-freezablecollection-1-clone)| Creates a modifiable clone of this
[FreezableCollection<T>](https://learn.microsoft.com/dotnet/api/system.windows.freezablecollection-1)
and its contents, making deep copies. If this collection (or its contents) has
animated dependency properties, the property's base value is copied, not its
current animated value.  
(Унаследован от
[FreezableCollection](https://learn.microsoft.com/dotnet/api/system.windows.freezablecollection-1)<[DelayBindingController](T_Tessa_UI_Markup_DelayBindingController.htm)>)  
[CloneCore](https://learn.microsoft.com/dotnet/api/system.windows.freezablecollection-1.clonecore#system-
windows-freezablecollection-1-clonecore\(system-windows-freezable\))| Makes
this instance a clone (deep copy) of the specified
[FreezableCollection<T>](https://learn.microsoft.com/dotnet/api/system.windows.freezablecollection-1)
using base (non-animated) property values.  
(Унаследован от
[FreezableCollection](https://learn.microsoft.com/dotnet/api/system.windows.freezablecollection-1)<[DelayBindingController](T_Tessa_UI_Markup_DelayBindingController.htm)>)  
[CloneCurrentValue](https://learn.microsoft.com/dotnet/api/system.windows.freezablecollection-1.clonecurrentvalue#system-
windows-freezablecollection-1-clonecurrentvalue)| Creates a modifiable copy of
this
[FreezableCollection<T>](https://learn.microsoft.com/dotnet/api/system.windows.freezablecollection-1)
and its contents, making deep copies of this object's current values. If this
object (or the objects it contains) contains animated dependency properties,
their current animated values are copied.  
(Унаследован от
[FreezableCollection](https://learn.microsoft.com/dotnet/api/system.windows.freezablecollection-1)<[DelayBindingController](T_Tessa_UI_Markup_DelayBindingController.htm)>)  
[CloneCurrentValueCore](https://learn.microsoft.com/dotnet/api/system.windows.freezablecollection-1.clonecurrentvaluecore#system-
windows-freezablecollection-1-clonecurrentvaluecore\(system-windows-
freezable\))| Makes this instance a modifiable clone (deep copy) of the
specified
[FreezableCollection<T>](https://learn.microsoft.com/dotnet/api/system.windows.freezablecollection-1)
using current property values.  
(Унаследован от
[FreezableCollection](https://learn.microsoft.com/dotnet/api/system.windows.freezablecollection-1)<[DelayBindingController](T_Tessa_UI_Markup_DelayBindingController.htm)>)  
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
[Contains](https://learn.microsoft.com/dotnet/api/system.windows.freezablecollection-1.contains#system-
windows-freezablecollection-1-contains\(-0\))| Determines whether this
[FreezableCollection<T>](https://learn.microsoft.com/dotnet/api/system.windows.freezablecollection-1)
contains the specified value.  
(Унаследован от
[FreezableCollection](https://learn.microsoft.com/dotnet/api/system.windows.freezablecollection-1)<[DelayBindingController](T_Tessa_UI_Markup_DelayBindingController.htm)>)  
[CopyTo](https://learn.microsoft.com/dotnet/api/system.windows.freezablecollection-1.copyto#system-
windows-freezablecollection-1-copyto\(-0\(\)-system-int32\))| Copies the
entire
[FreezableCollection<T>](https://learn.microsoft.com/dotnet/api/system.windows.freezablecollection-1)
to a compatible one-dimensional array, starting at the specified index of the
target array.  
(Унаследован от
[FreezableCollection](https://learn.microsoft.com/dotnet/api/system.windows.freezablecollection-1)<[DelayBindingController](T_Tessa_UI_Markup_DelayBindingController.htm)>)  
[CreateInstance](https://learn.microsoft.com/dotnet/api/system.windows.freezable.createinstance#system-
windows-freezable-createinstance)| Initializes a new instance of the
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable)
class.  
(Унаследован от
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable))  
[CreateInstanceCore](https://learn.microsoft.com/dotnet/api/system.windows.freezablecollection-1.createinstancecore#system-
windows-freezablecollection-1-createinstancecore)| Creates a new instance of
the
[FreezableCollection<T>](https://learn.microsoft.com/dotnet/api/system.windows.freezablecollection-1).  
(Унаследован от
[FreezableCollection](https://learn.microsoft.com/dotnet/api/system.windows.freezablecollection-1)<[DelayBindingController](T_Tessa_UI_Markup_DelayBindingController.htm)>)  
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
[FreezeCore](https://learn.microsoft.com/dotnet/api/system.windows.freezablecollection-1.freezecore#system-
windows-freezablecollection-1-freezecore\(system-boolean\))| Makes this
[FreezableCollection<T>](https://learn.microsoft.com/dotnet/api/system.windows.freezablecollection-1)
object unmodifiable or determines whether it can be made unmodifiable.  
(Унаследован от
[FreezableCollection](https://learn.microsoft.com/dotnet/api/system.windows.freezablecollection-1)<[DelayBindingController](T_Tessa_UI_Markup_DelayBindingController.htm)>)  
[GetAnimationBaseValue](https://learn.microsoft.com/dotnet/api/system.windows.media.animation.animatable.getanimationbasevalue#system-
windows-media-animation-animatable-getanimationbasevalue\(system-windows-
dependencyproperty\))| Returns the non-animated value of the specified
[DependencyProperty](https://learn.microsoft.com/dotnet/api/system.windows.dependencyproperty).  
(Унаследован от
[Animatable](https://learn.microsoft.com/dotnet/api/system.windows.media.animation.animatable))  
[GetAsFrozen](https://learn.microsoft.com/dotnet/api/system.windows.freezable.getasfrozen#system-
windows-freezable-getasfrozen)| Creates a frozen copy of the
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable),
using base (non-animated) property values. Because the copy is frozen, any
frozen sub-objects are copied by reference.  
(Унаследован от
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable))  
[GetAsFrozenCore](https://learn.microsoft.com/dotnet/api/system.windows.freezablecollection-1.getasfrozencore#system-
windows-freezablecollection-1-getasfrozencore\(system-windows-freezable\))|
Makes this instance a frozen clone of the specified
[FreezableCollection<T>](https://learn.microsoft.com/dotnet/api/system.windows.freezablecollection-1)
using base (non-animated) property values.  
(Унаследован от
[FreezableCollection](https://learn.microsoft.com/dotnet/api/system.windows.freezablecollection-1)<[DelayBindingController](T_Tessa_UI_Markup_DelayBindingController.htm)>)  
[GetCurrentValueAsFrozen](https://learn.microsoft.com/dotnet/api/system.windows.freezable.getcurrentvalueasfrozen#system-
windows-freezable-getcurrentvalueasfrozen)| Creates a frozen copy of the
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable)
using current property values. Because the copy is frozen, any frozen sub-
objects are copied by reference.  
(Унаследован от
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable))  
[GetCurrentValueAsFrozenCore](https://learn.microsoft.com/dotnet/api/system.windows.freezablecollection-1.getcurrentvalueasfrozencore#system-
windows-freezablecollection-1-getcurrentvalueasfrozencore\(system-windows-
freezable\))| Makes this instance a frozen clone of the specified
[Freezable](https://learn.microsoft.com/dotnet/api/system.windows.freezable).
If this object has animated dependency properties, their current animated
values are copied.  
(Унаследован от
[FreezableCollection](https://learn.microsoft.com/dotnet/api/system.windows.freezablecollection-1)<[DelayBindingController](T_Tessa_UI_Markup_DelayBindingController.htm)>)  
[GetEnumerator](https://learn.microsoft.com/dotnet/api/system.windows.freezablecollection-1.getenumerator#system-
windows-freezablecollection-1-getenumerator)| Returns an enumerator for the
entire
[FreezableCollection<T>](https://learn.microsoft.com/dotnet/api/system.windows.freezablecollection-1).  
(Унаследован от
[FreezableCollection](https://learn.microsoft.com/dotnet/api/system.windows.freezablecollection-1)<[DelayBindingController](T_Tessa_UI_Markup_DelayBindingController.htm)>)  
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
[IndexOf](https://learn.microsoft.com/dotnet/api/system.windows.freezablecollection-1.indexof#system-
windows-freezablecollection-1-indexof\(-0\))| Searches for the specified
object and returns the zero-based index of the first occurrence within the
entire
[FreezableCollection<T>](https://learn.microsoft.com/dotnet/api/system.windows.freezablecollection-1).  
(Унаследован от
[FreezableCollection](https://learn.microsoft.com/dotnet/api/system.windows.freezablecollection-1)<[DelayBindingController](T_Tessa_UI_Markup_DelayBindingController.htm)>)  
[Insert](https://learn.microsoft.com/dotnet/api/system.windows.freezablecollection-1.insert#system-
windows-freezablecollection-1-insert\(system-int32-0\))| Inserts the specified
object into the
[FreezableCollection<T>](https://learn.microsoft.com/dotnet/api/system.windows.freezablecollection-1)
at the specified index.  
(Унаследован от
[FreezableCollection](https://learn.microsoft.com/dotnet/api/system.windows.freezablecollection-1)<[DelayBindingController](T_Tessa_UI_Markup_DelayBindingController.htm)>)  
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
[Remove](https://learn.microsoft.com/dotnet/api/system.windows.freezablecollection-1.remove#system-
windows-freezablecollection-1-remove\(-0\))| Removes the first occurrence of
the specified object from the
[FreezableCollection<T>](https://learn.microsoft.com/dotnet/api/system.windows.freezablecollection-1).  
(Унаследован от
[FreezableCollection](https://learn.microsoft.com/dotnet/api/system.windows.freezablecollection-1)<[DelayBindingController](T_Tessa_UI_Markup_DelayBindingController.htm)>)  
[RemoveAt](https://learn.microsoft.com/dotnet/api/system.windows.freezablecollection-1.removeat#system-
windows-freezablecollection-1-removeat\(system-int32\))| Removes the object at
the specified zero-based index of the
[FreezableCollection<T>](https://learn.microsoft.com/dotnet/api/system.windows.freezablecollection-1).  
(Унаследован от
[FreezableCollection](https://learn.microsoft.com/dotnet/api/system.windows.freezablecollection-1)<[DelayBindingController](T_Tessa_UI_Markup_DelayBindingController.htm)>)  
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
[Tessa.UI.Markup - пространство имён](N_Tessa_UI_Markup.htm)
