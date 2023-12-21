# ScanDialogView - методы
##  __Методы
[AddChild](https://learn.microsoft.com/dotnet/api/system.windows.controls.contentcontrol.addchild#system-
windows-controls-contentcontrol-addchild\(system-object\))| Adds a specified
object as the child of a
[ContentControl](https://learn.microsoft.com/dotnet/api/system.windows.controls.contentcontrol).  
(Унаследован от
[ContentControl](https://learn.microsoft.com/dotnet/api/system.windows.controls.contentcontrol))  
---|---  
[AddHandler(RoutedEvent,
Delegate)](https://learn.microsoft.com/dotnet/api/system.windows.uielement.addhandler#system-
windows-uielement-addhandler\(system-windows-routedevent-system-delegate\))|
Adds a routed event handler for a specified routed event, adding the handler
to the handler collection on the current element.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[AddHandler(RoutedEvent, Delegate,
Boolean)](https://learn.microsoft.com/dotnet/api/system.windows.uielement.addhandler#system-
windows-uielement-addhandler\(system-windows-routedevent-system-delegate-
system-boolean\))| Adds a routed event handler for a specified routed event,
adding the handler to the handler collection on the current element. Specify
handledEventsToo as true to have the provided handler be invoked for routed
event that had already been marked as handled by another element along the
event route.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[AddLogicalChild](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.addlogicalchild#system-
windows-frameworkelement-addlogicalchild\(system-object\))| Adds the provided
object to the logical tree of this element.  
(Унаследован от
[FrameworkElement](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement))  
[AddText](https://learn.microsoft.com/dotnet/api/system.windows.controls.contentcontrol.addtext#system-
windows-controls-contentcontrol-addtext\(system-string\))| Adds a specified
text string to a
[ContentControl](https://learn.microsoft.com/dotnet/api/system.windows.controls.contentcontrol).  
(Унаследован от
[ContentControl](https://learn.microsoft.com/dotnet/api/system.windows.controls.contentcontrol))  
[AddToEventRoute](https://learn.microsoft.com/dotnet/api/system.windows.uielement.addtoeventroute#system-
windows-uielement-addtoeventroute\(system-windows-eventroute-system-windows-
routedeventargs\))| Adds handlers to the specified
[EventRoute](https://learn.microsoft.com/dotnet/api/system.windows.eventroute)
for the current
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement)
event handler collection.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[AddVisualChild](https://learn.microsoft.com/dotnet/api/system.windows.media.visual.addvisualchild#system-
windows-media-visual-addvisualchild\(system-windows-media-visual\))| Defines
the parent-child relationship between two visuals.  
(Унаследован от
[Visual](https://learn.microsoft.com/dotnet/api/system.windows.media.visual))  
[ApplyAnimationClock(DependencyProperty,
AnimationClock)](https://learn.microsoft.com/dotnet/api/system.windows.uielement.applyanimationclock#system-
windows-uielement-applyanimationclock\(system-windows-dependencyproperty-
system-windows-media-animation-animationclock\))| Applies an animation to a
specified dependency property on this element. Any existing animations are
stopped and replaced with the new animation.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[ApplyAnimationClock(DependencyProperty, AnimationClock,
HandoffBehavior)](https://learn.microsoft.com/dotnet/api/system.windows.uielement.applyanimationclock#system-
windows-uielement-applyanimationclock\(system-windows-dependencyproperty-
system-windows-media-animation-animationclock-system-windows-media-animation-
handoffbehavior\))| Applies an animation to a specified dependency property on
this element, with the ability to specify what happens if the property already
has a running animation.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[ApplyTemplate](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.applytemplate#system-
windows-frameworkelement-applytemplate)| Builds the current template's visual
tree if necessary, and returns a value that indicates whether the visual tree
was rebuilt by this call.  
(Унаследован от
[FrameworkElement](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement))  
[Arrange](https://learn.microsoft.com/dotnet/api/system.windows.uielement.arrange#system-
windows-uielement-arrange\(system-windows-rect\))| Positions child elements
and determines a size for a
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement).
Parent elements call this method from their
[ArrangeCore(Rect)](https://learn.microsoft.com/dotnet/api/system.windows.uielement.arrangecore#system-
windows-uielement-arrangecore\(system-windows-rect\)) implementation (or a WPF
framework-level equivalent) to form a recursive layout update. This method
constitutes the second pass of a layout update.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[ArrangeCore](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.arrangecore#system-
windows-frameworkelement-arrangecore\(system-windows-rect\))| Implements
[ArrangeCore(Rect)](https://learn.microsoft.com/dotnet/api/system.windows.uielement.arrangecore#system-
windows-uielement-arrangecore\(system-windows-rect\)) (defined as virtual in
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))
and seals the implementation.  
(Унаследован от
[FrameworkElement](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement))  
[ArrangeOverride](https://learn.microsoft.com/dotnet/api/system.windows.controls.control.arrangeoverride#system-
windows-controls-control-arrangeoverride\(system-windows-size\))| Called to
arrange and size the content of a
[Control](https://learn.microsoft.com/dotnet/api/system.windows.controls.control)
object.  
(Унаследован от
[Control](https://learn.microsoft.com/dotnet/api/system.windows.controls.control))  
[BeginAnimation(DependencyProperty,
AnimationTimeline)](https://learn.microsoft.com/dotnet/api/system.windows.uielement.beginanimation#system-
windows-uielement-beginanimation\(system-windows-dependencyproperty-system-
windows-media-animation-animationtimeline\))| Starts an animation for a
specified animated property on this element.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[BeginAnimation(DependencyProperty, AnimationTimeline,
HandoffBehavior)](https://learn.microsoft.com/dotnet/api/system.windows.uielement.beginanimation#system-
windows-uielement-beginanimation\(system-windows-dependencyproperty-system-
windows-media-animation-animationtimeline-system-windows-media-animation-
handoffbehavior\))| Starts a specific animation for a specified animated
property on this element, with the option of specifying what happens if the
property already has a running animation.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[BeginInit](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.begininit#system-
windows-frameworkelement-begininit)| Starts the initialization process for
this element.  
(Унаследован от
[FrameworkElement](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement))  
[BeginStoryboard(Storyboard)](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.beginstoryboard#system-
windows-frameworkelement-beginstoryboard\(system-windows-media-animation-
storyboard\))| Begins the sequence of actions that are contained in the
provided storyboard.  
(Унаследован от
[FrameworkElement](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement))  
[BeginStoryboard(Storyboard,
HandoffBehavior)](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.beginstoryboard#system-
windows-frameworkelement-beginstoryboard\(system-windows-media-animation-
storyboard-system-windows-media-animation-handoffbehavior\))| Begins the
sequence of actions contained in the provided storyboard, with options
specified for what should happen if the property is already animated.  
(Унаследован от
[FrameworkElement](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement))  
[BeginStoryboard(Storyboard, HandoffBehavior,
Boolean)](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.beginstoryboard#system-
windows-frameworkelement-beginstoryboard\(system-windows-media-animation-
storyboard-system-windows-media-animation-handoffbehavior-system-boolean\))|
Begins the sequence of actions contained in the provided storyboard, with
specified state for control of the animation after it is started.  
(Унаследован от
[FrameworkElement](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement))  
[BringIntoView()](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.bringintoview#system-
windows-frameworkelement-bringintoview)| Attempts to bring this element into
view, within any scrollable regions it is contained within.  
(Унаследован от
[FrameworkElement](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement))  
[BringIntoView(Rect)](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.bringintoview#system-
windows-frameworkelement-bringintoview\(system-windows-rect\))| Attempts to
bring the provided region size of this element into view, within any
scrollable regions it is contained within.  
(Унаследован от
[FrameworkElement](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement))  
[CaptureMouse](https://learn.microsoft.com/dotnet/api/system.windows.uielement.capturemouse#system-
windows-uielement-capturemouse)| Attempts to force capture of the mouse to
this element.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[CaptureStylus](https://learn.microsoft.com/dotnet/api/system.windows.uielement.capturestylus#system-
windows-uielement-capturestylus)| Attempts to force capture of the stylus to
this element.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[CaptureTouch](https://learn.microsoft.com/dotnet/api/system.windows.uielement.capturetouch#system-
windows-uielement-capturetouch\(system-windows-input-touchdevice\))| Attempts
to force capture of a touch to this element.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[CheckAccess](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject.checkaccess#system-
windows-threading-dispatcherobject-checkaccess)| Determines whether the
calling thread has access to this
[DispatcherObject](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject).  
(Унаследован от
[DispatcherObject](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject))  
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
[EndInit](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.endinit#system-
windows-frameworkelement-endinit)| Indicates that the initialization process
for the element is complete.  
(Унаследован от
[FrameworkElement](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement))  
[Equals](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject.equals#system-
windows-dependencyobject-equals\(system-object\))| Determines whether a
provided
[DependencyObject](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject)
is equivalent to the current
[DependencyObject](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject).  
(Унаследован от
[DependencyObject](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject))  
[FindCommonVisualAncestor](https://learn.microsoft.com/dotnet/api/system.windows.media.visual.findcommonvisualancestor#system-
windows-media-visual-findcommonvisualancestor\(system-windows-
dependencyobject\))| Returns the common ancestor of two visual objects.  
(Унаследован от
[Visual](https://learn.microsoft.com/dotnet/api/system.windows.media.visual))  
[FindName](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.findname#system-
windows-frameworkelement-findname\(system-string\))| Finds an element that has
the provided identifier name.  
(Унаследован от
[FrameworkElement](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement))  
[FindResource](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.findresource#system-
windows-frameworkelement-findresource\(system-object\))| Searches for a
resource with the specified key, and throws an exception if the requested
resource is not found.  
(Унаследован от
[FrameworkElement](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement))  
[Focus](https://learn.microsoft.com/dotnet/api/system.windows.uielement.focus#system-
windows-uielement-focus)| Attempts to set focus to this element.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[GetAnimationBaseValue](https://learn.microsoft.com/dotnet/api/system.windows.uielement.getanimationbasevalue#system-
windows-uielement-getanimationbasevalue\(system-windows-dependencyproperty\))|
Returns the base property value for the specified property on this element,
disregarding any possible animated value from a running or stopped animation.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[GetBindingExpression](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.getbindingexpression#system-
windows-frameworkelement-getbindingexpression\(system-windows-
dependencyproperty\))| Returns the
[BindingExpression](https://learn.microsoft.com/dotnet/api/system.windows.data.bindingexpression)
that represents the binding on the specified property.  
(Унаследован от
[FrameworkElement](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject.gethashcode#system-
windows-dependencyobject-gethashcode)| Gets a hash code for this
[DependencyObject](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject).  
(Унаследован от
[DependencyObject](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject))  
[GetLayoutClip](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.getlayoutclip#system-
windows-frameworkelement-getlayoutclip\(system-windows-size\))| Returns a
geometry for a clipping mask. The mask applies if the layout system attempts
to arrange an element that is larger than the available display space.  
(Унаследован от
[FrameworkElement](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement))  
[GetLocalValueEnumerator](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject.getlocalvalueenumerator#system-
windows-dependencyobject-getlocalvalueenumerator)| Creates a specialized
enumerator for determining which dependency properties have locally set values
on this
[DependencyObject](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject).  
(Унаследован от
[DependencyObject](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject))  
[GetTemplateChild](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.gettemplatechild#system-
windows-frameworkelement-gettemplatechild\(system-string\))| Returns the named
element in the visual tree of an instantiated
[ControlTemplate](https://learn.microsoft.com/dotnet/api/system.windows.controls.controltemplate).  
(Унаследован от
[FrameworkElement](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement))  
[GetUIParentCore](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.getuiparentcore#system-
windows-frameworkelement-getuiparentcore)| Returns an alternative logical
parent for this element if there is no visual parent.  
(Унаследован от
[FrameworkElement](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement))  
[GetValue](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject.getvalue#system-
windows-dependencyobject-getvalue\(system-windows-dependencyproperty\))|
Returns the current effective value of a dependency property on this instance
of a
[DependencyObject](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject).  
(Унаследован от
[DependencyObject](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject))  
[GetVisualChild](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.getvisualchild#system-
windows-frameworkelement-getvisualchild\(system-int32\))| Overrides
[GetVisualChild(Int32)](https://learn.microsoft.com/dotnet/api/system.windows.media.visual.getvisualchild#system-
windows-media-visual-getvisualchild\(system-int32\)), and returns a child at
the specified index from a collection of child elements.  
(Унаследован от
[FrameworkElement](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement))  
[HitTestCore(GeometryHitTestParameters)](https://learn.microsoft.com/dotnet/api/system.windows.uielement.hittestcore#system-
windows-uielement-hittestcore\(system-windows-media-
geometryhittestparameters\))| Implements
[HitTestCore(GeometryHitTestParameters)](https://learn.microsoft.com/dotnet/api/system.windows.media.visual.hittestcore#system-
windows-media-visual-hittestcore\(system-windows-media-
geometryhittestparameters\)) to supply base element hit testing behavior
(returning
[GeometryHitTestResult](https://learn.microsoft.com/dotnet/api/system.windows.media.geometryhittestresult)).  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[HitTestCore(PointHitTestParameters)](https://learn.microsoft.com/dotnet/api/system.windows.uielement.hittestcore#system-
windows-uielement-hittestcore\(system-windows-media-pointhittestparameters\))|
Implements
[HitTestCore(PointHitTestParameters)](https://learn.microsoft.com/dotnet/api/system.windows.media.visual.hittestcore#system-
windows-media-visual-hittestcore\(system-windows-media-
pointhittestparameters\)) to supply base element hit testing behavior
(returning
[HitTestResult](https://learn.microsoft.com/dotnet/api/system.windows.media.hittestresult)).  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[InitializeComponent](M_Tessa_Extensions_Platform_Client_Views_ScanDialogView_InitializeComponent.htm)|
InitializeComponent  
[InputHitTest](https://learn.microsoft.com/dotnet/api/system.windows.uielement.inputhittest#system-
windows-uielement-inputhittest\(system-windows-point\))| Returns the input
element within the current element that is at the specified coordinates,
relative to the current element's origin.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[InvalidateArrange](https://learn.microsoft.com/dotnet/api/system.windows.uielement.invalidatearrange#system-
windows-uielement-invalidatearrange)| Invalidates the arrange state (layout)
for the element. After the invalidation, the element will have its layout
updated, which will occur asynchronously unless subsequently forced by
[UpdateLayout()](https://learn.microsoft.com/dotnet/api/system.windows.uielement.updatelayout#system-
windows-uielement-updatelayout).  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[InvalidateMeasure](https://learn.microsoft.com/dotnet/api/system.windows.uielement.invalidatemeasure#system-
windows-uielement-invalidatemeasure)| Invalidates the measurement state
(layout) for the element.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[InvalidateProperty](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject.invalidateproperty#system-
windows-dependencyobject-invalidateproperty\(system-windows-
dependencyproperty\))| Re-evaluates the effective value for the specified
dependency property.  
(Унаследован от
[DependencyObject](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject))  
[InvalidateVisual](https://learn.microsoft.com/dotnet/api/system.windows.uielement.invalidatevisual#system-
windows-uielement-invalidatevisual)| Invalidates the rendering of the element,
and forces a complete new layout pass.
[OnRender(DrawingContext)](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onrender#system-
windows-uielement-onrender\(system-windows-media-drawingcontext\)) is called
after the layout cycle is completed.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[IsAncestorOf](https://learn.microsoft.com/dotnet/api/system.windows.media.visual.isancestorof#system-
windows-media-visual-isancestorof\(system-windows-dependencyobject\))|
Determines whether the visual object is an ancestor of the descendant visual
object.  
(Унаследован от
[Visual](https://learn.microsoft.com/dotnet/api/system.windows.media.visual))  
[IsDescendantOf](https://learn.microsoft.com/dotnet/api/system.windows.media.visual.isdescendantof#system-
windows-media-visual-isdescendantof\(system-windows-dependencyobject\))|
Determines whether the visual object is a descendant of the ancestor visual
object.  
(Унаследован от
[Visual](https://learn.microsoft.com/dotnet/api/system.windows.media.visual))  
[Measure](https://learn.microsoft.com/dotnet/api/system.windows.uielement.measure#system-
windows-uielement-measure\(system-windows-size\))| Updates the
[DesiredSize](https://learn.microsoft.com/dotnet/api/system.windows.uielement.desiredsize#system-
windows-uielement-desiredsize) of a
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement).
Parent elements call this method from their own
[MeasureCore(Size)](https://learn.microsoft.com/dotnet/api/system.windows.uielement.measurecore#system-
windows-uielement-measurecore\(system-windows-size\)) implementations to form
a recursive layout update. Calling this method constitutes the first pass (the
"Measure" pass) of a layout update.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[MeasureCore](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.measurecore#system-
windows-frameworkelement-measurecore\(system-windows-size\))| Implements basic
measure-pass layout system behavior for
[FrameworkElement](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement).  
(Унаследован от
[FrameworkElement](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement))  
[MeasureOverride](https://learn.microsoft.com/dotnet/api/system.windows.controls.control.measureoverride#system-
windows-controls-control-measureoverride\(system-windows-size\))| Called to
remeasure a control.  
(Унаследован от
[Control](https://learn.microsoft.com/dotnet/api/system.windows.controls.control))  
[MoveFocus](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.movefocus#system-
windows-frameworkelement-movefocus\(system-windows-input-traversalrequest\))|
Moves the keyboard focus away from this element and to another element in a
provided traversal direction.  
(Унаследован от
[FrameworkElement](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement))  
[OnAccessKey](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onaccesskey#system-
windows-uielement-onaccesskey\(system-windows-input-accesskeyeventargs\))|
Provides class handling for when an access key that is meaningful for this
element is invoked.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnApplyTemplate](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.onapplytemplate#system-
windows-frameworkelement-onapplytemplate)| When overridden in a derived class,
is invoked whenever application code or internal processes call
[ApplyTemplate()](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.applytemplate#system-
windows-frameworkelement-applytemplate).  
(Унаследован от
[FrameworkElement](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement))  
[OnChildDesiredSizeChanged](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onchilddesiredsizechanged#system-
windows-uielement-onchilddesiredsizechanged\(system-windows-uielement\))|
Supports layout behavior when a child element is resized.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnContentChanged](https://learn.microsoft.com/dotnet/api/system.windows.controls.contentcontrol.oncontentchanged#system-
windows-controls-contentcontrol-oncontentchanged\(system-object-system-
object\))| Called when the
[Content](https://learn.microsoft.com/dotnet/api/system.windows.controls.contentcontrol.content#system-
windows-controls-contentcontrol-content) property changes.  
(Унаследован от
[ContentControl](https://learn.microsoft.com/dotnet/api/system.windows.controls.contentcontrol))  
[OnContentStringFormatChanged](https://learn.microsoft.com/dotnet/api/system.windows.controls.contentcontrol.oncontentstringformatchanged#system-
windows-controls-contentcontrol-oncontentstringformatchanged\(system-string-
system-string\))| Occurs when the
[ContentStringFormat](https://learn.microsoft.com/dotnet/api/system.windows.controls.contentcontrol.contentstringformat#system-
windows-controls-contentcontrol-contentstringformat) property changes.  
(Унаследован от
[ContentControl](https://learn.microsoft.com/dotnet/api/system.windows.controls.contentcontrol))  
[OnContentTemplateChanged](https://learn.microsoft.com/dotnet/api/system.windows.controls.contentcontrol.oncontenttemplatechanged#system-
windows-controls-contentcontrol-oncontenttemplatechanged\(system-windows-
datatemplate-system-windows-datatemplate\))| Called when the
[ContentTemplate](https://learn.microsoft.com/dotnet/api/system.windows.controls.contentcontrol.contenttemplate#system-
windows-controls-contentcontrol-contenttemplate) property changes.  
(Унаследован от
[ContentControl](https://learn.microsoft.com/dotnet/api/system.windows.controls.contentcontrol))  
[OnContentTemplateSelectorChanged](https://learn.microsoft.com/dotnet/api/system.windows.controls.contentcontrol.oncontenttemplateselectorchanged#system-
windows-controls-contentcontrol-oncontenttemplateselectorchanged\(system-
windows-controls-datatemplateselector-system-windows-controls-
datatemplateselector\))| Called when the
[ContentTemplateSelector](https://learn.microsoft.com/dotnet/api/system.windows.controls.contentcontrol.contenttemplateselector#system-
windows-controls-contentcontrol-contenttemplateselector) property changes.  
(Унаследован от
[ContentControl](https://learn.microsoft.com/dotnet/api/system.windows.controls.contentcontrol))  
[OnContextMenuClosing](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.oncontextmenuclosing#system-
windows-frameworkelement-oncontextmenuclosing\(system-windows-controls-
contextmenueventargs\))| Invoked whenever an unhandled
[ContextMenuClosing](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.contextmenuclosing)
routed event reaches this class in its route. Implement this method to add
class handling for this event.  
(Унаследован от
[FrameworkElement](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement))  
[OnContextMenuOpening](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.oncontextmenuopening#system-
windows-frameworkelement-oncontextmenuopening\(system-windows-controls-
contextmenueventargs\))| Invoked whenever an unhandled
[ContextMenuOpening](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.contextmenuopening)
routed event reaches this class in its route. Implement this method to add
class handling for this event.  
(Унаследован от
[FrameworkElement](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement))  
[OnCreateAutomationPeer](https://learn.microsoft.com/dotnet/api/system.windows.controls.usercontrol.oncreateautomationpeer#system-
windows-controls-usercontrol-oncreateautomationpeer)| Creates and returns an
[AutomationPeer](https://learn.microsoft.com/dotnet/api/system.windows.automation.peers.automationpeer)
for this
[UserControl](https://learn.microsoft.com/dotnet/api/system.windows.controls.usercontrol).  
(Унаследован от
[UserControl](https://learn.microsoft.com/dotnet/api/system.windows.controls.usercontrol))  
[OnDpiChanged](https://learn.microsoft.com/dotnet/api/system.windows.media.visual.ondpichanged#system-
windows-media-visual-ondpichanged\(system-windows-dpiscale-system-windows-
dpiscale\))| Called when the DPI at which this View is rendered changes.  
(Унаследован от
[Visual](https://learn.microsoft.com/dotnet/api/system.windows.media.visual))  
[OnDragEnter](https://learn.microsoft.com/dotnet/api/system.windows.uielement.ondragenter#system-
windows-uielement-ondragenter\(system-windows-drageventargs\))| Invoked when
an unhandled
[DragEnter](https://learn.microsoft.com/dotnet/api/system.windows.dragdrop.dragenter)
attached event reaches an element in its route that is derived from this
class. Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnDragLeave](https://learn.microsoft.com/dotnet/api/system.windows.uielement.ondragleave#system-
windows-uielement-ondragleave\(system-windows-drageventargs\))| Invoked when
an unhandled
[DragLeave](https://learn.microsoft.com/dotnet/api/system.windows.dragdrop.dragleave)
attached event reaches an element in its route that is derived from this
class. Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnDragOver](https://learn.microsoft.com/dotnet/api/system.windows.uielement.ondragover#system-
windows-uielement-ondragover\(system-windows-drageventargs\))| Invoked when an
unhandled
[DragOver](https://learn.microsoft.com/dotnet/api/system.windows.dragdrop.dragover)
attached event reaches an element in its route that is derived from this
class. Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnDrop](https://learn.microsoft.com/dotnet/api/system.windows.uielement.ondrop#system-
windows-uielement-ondrop\(system-windows-drageventargs\))| Invoked when an
unhandled
[DragEnter](https://learn.microsoft.com/dotnet/api/system.windows.dragdrop.dragenter)
attached event reaches an element in its route that is derived from this
class. Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnGiveFeedback](https://learn.microsoft.com/dotnet/api/system.windows.uielement.ongivefeedback#system-
windows-uielement-ongivefeedback\(system-windows-givefeedbackeventargs\))|
Invoked when an unhandled
[GiveFeedback](https://learn.microsoft.com/dotnet/api/system.windows.dragdrop.givefeedback)
attached event reaches an element in its route that is derived from this
class. Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnGotFocus](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.ongotfocus#system-
windows-frameworkelement-ongotfocus\(system-windows-routedeventargs\))|
Invoked whenever an unhandled
[GotFocus](https://learn.microsoft.com/dotnet/api/system.windows.uielement.gotfocus)
event reaches this element in its route.  
(Унаследован от
[FrameworkElement](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement))  
[OnGotKeyboardFocus](https://learn.microsoft.com/dotnet/api/system.windows.uielement.ongotkeyboardfocus#system-
windows-uielement-ongotkeyboardfocus\(system-windows-input-
keyboardfocuschangedeventargs\))| Invoked when an unhandled
[GotKeyboardFocus](https://learn.microsoft.com/dotnet/api/system.windows.input.keyboard.gotkeyboardfocus)
attached event reaches an element in its route that is derived from this
class. Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnGotMouseCapture](https://learn.microsoft.com/dotnet/api/system.windows.uielement.ongotmousecapture#system-
windows-uielement-ongotmousecapture\(system-windows-input-mouseeventargs\))|
Invoked when an unhandled
[GotMouseCapture](https://learn.microsoft.com/dotnet/api/system.windows.input.mouse.gotmousecapture)
attached event reaches an element in its route that is derived from this
class. Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnGotStylusCapture](https://learn.microsoft.com/dotnet/api/system.windows.uielement.ongotstyluscapture#system-
windows-uielement-ongotstyluscapture\(system-windows-input-styluseventargs\))|
Invoked when an unhandled
[GotStylusCapture](https://learn.microsoft.com/dotnet/api/system.windows.input.stylus.gotstyluscapture)
attached event reaches an element in its route that is derived from this
class. Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnGotTouchCapture](https://learn.microsoft.com/dotnet/api/system.windows.uielement.ongottouchcapture#system-
windows-uielement-ongottouchcapture\(system-windows-input-toucheventargs\))|
Provides class handling for the
[GotTouchCapture](https://learn.microsoft.com/dotnet/api/system.windows.uielement.gottouchcapture)
routed event that occurs when a touch is captured to this element.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnInitialized](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.oninitialized#system-
windows-frameworkelement-oninitialized\(system-eventargs\))| Raises the
[Initialized](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.initialized)
event. This method is invoked whenever
[IsInitialized](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.isinitialized#system-
windows-frameworkelement-isinitialized) is set to true internally.  
(Унаследован от
[FrameworkElement](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement))  
[OnIsKeyboardFocusedChanged](https://learn.microsoft.com/dotnet/api/system.windows.uielement.oniskeyboardfocusedchanged#system-
windows-uielement-oniskeyboardfocusedchanged\(system-windows-
dependencypropertychangedeventargs\))| Invoked when an unhandled
[IsKeyboardFocusedChanged](https://learn.microsoft.com/dotnet/api/system.windows.uielement.iskeyboardfocusedchanged)
event is raised on this element. Implement this method to add class handling
for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnIsKeyboardFocusWithinChanged](https://learn.microsoft.com/dotnet/api/system.windows.uielement.oniskeyboardfocuswithinchanged#system-
windows-uielement-oniskeyboardfocuswithinchanged\(system-windows-
dependencypropertychangedeventargs\))| Invoked just before the
[IsKeyboardFocusWithinChanged](https://learn.microsoft.com/dotnet/api/system.windows.uielement.iskeyboardfocuswithinchanged)
event is raised by this element. Implement this method to add class handling
for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnIsMouseCapturedChanged](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onismousecapturedchanged#system-
windows-uielement-onismousecapturedchanged\(system-windows-
dependencypropertychangedeventargs\))| Invoked when an unhandled
[IsMouseCapturedChanged](https://learn.microsoft.com/dotnet/api/system.windows.uielement.ismousecapturedchanged)
event is raised on this element. Implement this method to add class handling
for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnIsMouseCaptureWithinChanged](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onismousecapturewithinchanged#system-
windows-uielement-onismousecapturewithinchanged\(system-windows-
dependencypropertychangedeventargs\))| Invoked when an unhandled
[IsMouseCaptureWithinChanged](https://learn.microsoft.com/dotnet/api/system.windows.uielement.ismousecapturewithinchanged)
event is raised on this element. Implement this method to add class handling
for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnIsMouseDirectlyOverChanged](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onismousedirectlyoverchanged#system-
windows-uielement-onismousedirectlyoverchanged\(system-windows-
dependencypropertychangedeventargs\))| Invoked when an unhandled
[IsMouseDirectlyOverChanged](https://learn.microsoft.com/dotnet/api/system.windows.uielement.ismousedirectlyoverchanged)
event is raised on this element. Implement this method to add class handling
for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnIsStylusCapturedChanged](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onisstyluscapturedchanged#system-
windows-uielement-onisstyluscapturedchanged\(system-windows-
dependencypropertychangedeventargs\))| Invoked when an unhandled
[IsStylusCapturedChanged](https://learn.microsoft.com/dotnet/api/system.windows.uielement.isstyluscapturedchanged)
event is raised on this element. Implement this method to add class handling
for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnIsStylusCaptureWithinChanged](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onisstyluscapturewithinchanged#system-
windows-uielement-onisstyluscapturewithinchanged\(system-windows-
dependencypropertychangedeventargs\))| Invoked when an unhandled
[IsStylusCaptureWithinChanged](https://learn.microsoft.com/dotnet/api/system.windows.uielement.isstyluscapturewithinchanged)
event is raised on this element. Implement this method to add class handling
for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnIsStylusDirectlyOverChanged](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onisstylusdirectlyoverchanged#system-
windows-uielement-onisstylusdirectlyoverchanged\(system-windows-
dependencypropertychangedeventargs\))| Invoked when an unhandled
[IsStylusDirectlyOverChanged](https://learn.microsoft.com/dotnet/api/system.windows.uielement.isstylusdirectlyoverchanged)
event is raised on this element. Implement this method to add class handling
for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnKeyDown](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onkeydown#system-
windows-uielement-onkeydown\(system-windows-input-keyeventargs\))| Invoked
when an unhandled
[KeyDown](https://learn.microsoft.com/dotnet/api/system.windows.input.keyboard.keydown)
attached event reaches an element in its route that is derived from this
class. Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnKeyUp](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onkeyup#system-
windows-uielement-onkeyup\(system-windows-input-keyeventargs\))| Invoked when
an unhandled
[KeyUp](https://learn.microsoft.com/dotnet/api/system.windows.input.keyboard.keyup)
attached event reaches an element in its route that is derived from this
class. Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnLostFocus](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onlostfocus#system-
windows-uielement-onlostfocus\(system-windows-routedeventargs\))| Raises the
[LostFocus](https://learn.microsoft.com/dotnet/api/system.windows.uielement.lostfocus)
routed event by using the event data that is provided.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnLostKeyboardFocus](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onlostkeyboardfocus#system-
windows-uielement-onlostkeyboardfocus\(system-windows-input-
keyboardfocuschangedeventargs\))| Invoked when an unhandled
[LostKeyboardFocus](https://learn.microsoft.com/dotnet/api/system.windows.input.keyboard.lostkeyboardfocus)
attached event reaches an element in its route that is derived from this
class. Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnLostMouseCapture](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onlostmousecapture#system-
windows-uielement-onlostmousecapture\(system-windows-input-mouseeventargs\))|
Invoked when an unhandled
[LostMouseCapture](https://learn.microsoft.com/dotnet/api/system.windows.input.mouse.lostmousecapture)
attached event reaches an element in its route that is derived from this
class. Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnLostStylusCapture](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onloststyluscapture#system-
windows-uielement-onloststyluscapture\(system-windows-input-
styluseventargs\))| Invoked when an unhandled
[LostStylusCapture](https://learn.microsoft.com/dotnet/api/system.windows.input.stylus.loststyluscapture)
attached event reaches an element in its route that is derived from this
class. Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnLostTouchCapture](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onlosttouchcapture#system-
windows-uielement-onlosttouchcapture\(system-windows-input-toucheventargs\))|
Provides class handling for the
[LostTouchCapture](https://learn.microsoft.com/dotnet/api/system.windows.uielement.losttouchcapture)
routed event that occurs when this element loses a touch capture.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnManipulationBoundaryFeedback](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onmanipulationboundaryfeedback#system-
windows-uielement-onmanipulationboundaryfeedback\(system-windows-input-
manipulationboundaryfeedbackeventargs\))| Called when the
[ManipulationBoundaryFeedback](https://learn.microsoft.com/dotnet/api/system.windows.uielement.manipulationboundaryfeedback)
event occurs.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnManipulationCompleted](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onmanipulationcompleted#system-
windows-uielement-onmanipulationcompleted\(system-windows-input-
manipulationcompletedeventargs\))| Called when the
[ManipulationCompleted](https://learn.microsoft.com/dotnet/api/system.windows.uielement.manipulationcompleted)
event occurs.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnManipulationDelta](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onmanipulationdelta#system-
windows-uielement-onmanipulationdelta\(system-windows-input-
manipulationdeltaeventargs\))| Called when the
[ManipulationDelta](https://learn.microsoft.com/dotnet/api/system.windows.uielement.manipulationdelta)
event occurs.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnManipulationInertiaStarting](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onmanipulationinertiastarting#system-
windows-uielement-onmanipulationinertiastarting\(system-windows-input-
manipulationinertiastartingeventargs\))| Called when the
[ManipulationInertiaStarting](https://learn.microsoft.com/dotnet/api/system.windows.uielement.manipulationinertiastarting)
event occurs.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnManipulationStarted](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onmanipulationstarted#system-
windows-uielement-onmanipulationstarted\(system-windows-input-
manipulationstartedeventargs\))| Called when the
[ManipulationStarted](https://learn.microsoft.com/dotnet/api/system.windows.uielement.manipulationstarted)
event occurs.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnManipulationStarting](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onmanipulationstarting#system-
windows-uielement-onmanipulationstarting\(system-windows-input-
manipulationstartingeventargs\))| Provides class handling for the
[ManipulationStarting](https://learn.microsoft.com/dotnet/api/system.windows.uielement.manipulationstarting)
routed event that occurs when the manipulation processor is first created.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnMouseDoubleClick](https://learn.microsoft.com/dotnet/api/system.windows.controls.control.onmousedoubleclick#system-
windows-controls-control-onmousedoubleclick\(system-windows-input-
mousebuttoneventargs\))| Raises the
[MouseDoubleClick](https://learn.microsoft.com/dotnet/api/system.windows.controls.control.mousedoubleclick)
routed event.  
(Унаследован от
[Control](https://learn.microsoft.com/dotnet/api/system.windows.controls.control))  
[OnMouseDown](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onmousedown#system-
windows-uielement-onmousedown\(system-windows-input-mousebuttoneventargs\))|
Invoked when an unhandled
[MouseDown](https://learn.microsoft.com/dotnet/api/system.windows.input.mouse.mousedown)
attached event reaches an element in its route that is derived from this
class. Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnMouseEnter](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onmouseenter#system-
windows-uielement-onmouseenter\(system-windows-input-mouseeventargs\))|
Invoked when an unhandled
[MouseEnter](https://learn.microsoft.com/dotnet/api/system.windows.input.mouse.mouseenter)
attached event is raised on this element. Implement this method to add class
handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnMouseLeave](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onmouseleave#system-
windows-uielement-onmouseleave\(system-windows-input-mouseeventargs\))|
Invoked when an unhandled
[MouseLeave](https://learn.microsoft.com/dotnet/api/system.windows.input.mouse.mouseleave)
attached event is raised on this element. Implement this method to add class
handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnMouseLeftButtonDown](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onmouseleftbuttondown#system-
windows-uielement-onmouseleftbuttondown\(system-windows-input-
mousebuttoneventargs\))| Invoked when an unhandled
[MouseLeftButtonDown](https://learn.microsoft.com/dotnet/api/system.windows.uielement.mouseleftbuttondown)
routed event is raised on this element. Implement this method to add class
handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnMouseLeftButtonUp](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onmouseleftbuttonup#system-
windows-uielement-onmouseleftbuttonup\(system-windows-input-
mousebuttoneventargs\))| Invoked when an unhandled
[MouseLeftButtonUp](https://learn.microsoft.com/dotnet/api/system.windows.uielement.mouseleftbuttonup)
routed event reaches an element in its route that is derived from this class.
Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnMouseMove](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onmousemove#system-
windows-uielement-onmousemove\(system-windows-input-mouseeventargs\))| Invoked
when an unhandled
[MouseMove](https://learn.microsoft.com/dotnet/api/system.windows.input.mouse.mousemove)
attached event reaches an element in its route that is derived from this
class. Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnMouseRightButtonDown](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onmouserightbuttondown#system-
windows-uielement-onmouserightbuttondown\(system-windows-input-
mousebuttoneventargs\))| Invoked when an unhandled
[MouseRightButtonDown](https://learn.microsoft.com/dotnet/api/system.windows.uielement.mouserightbuttondown)
routed event reaches an element in its route that is derived from this class.
Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnMouseRightButtonUp](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onmouserightbuttonup#system-
windows-uielement-onmouserightbuttonup\(system-windows-input-
mousebuttoneventargs\))| Invoked when an unhandled
[MouseRightButtonUp](https://learn.microsoft.com/dotnet/api/system.windows.uielement.mouserightbuttonup)
routed event reaches an element in its route that is derived from this class.
Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnMouseUp](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onmouseup#system-
windows-uielement-onmouseup\(system-windows-input-mousebuttoneventargs\))|
Invoked when an unhandled
[MouseUp](https://learn.microsoft.com/dotnet/api/system.windows.input.mouse.mouseup)
routed event reaches an element in its route that is derived from this class.
Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnMouseWheel](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onmousewheel#system-
windows-uielement-onmousewheel\(system-windows-input-mousewheeleventargs\))|
Invoked when an unhandled
[MouseWheel](https://learn.microsoft.com/dotnet/api/system.windows.input.mouse.mousewheel)
attached event reaches an element in its route that is derived from this
class. Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnPreviewDragEnter](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onpreviewdragenter#system-
windows-uielement-onpreviewdragenter\(system-windows-drageventargs\))| Invoked
when an unhandled
[PreviewDragEnter](https://learn.microsoft.com/dotnet/api/system.windows.dragdrop.previewdragenter)
attached event reaches an element in its route that is derived from this
class. Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnPreviewDragLeave](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onpreviewdragleave#system-
windows-uielement-onpreviewdragleave\(system-windows-drageventargs\))| Invoked
when an unhandled
[PreviewDragLeave](https://learn.microsoft.com/dotnet/api/system.windows.dragdrop.previewdragleave)
attached event reaches an element in its route that is derived from this
class. Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnPreviewDragOver](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onpreviewdragover#system-
windows-uielement-onpreviewdragover\(system-windows-drageventargs\))| Invoked
when an unhandled
[PreviewDragOver](https://learn.microsoft.com/dotnet/api/system.windows.dragdrop.previewdragover)
attached event reaches an element in its route that is derived from this
class. Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnPreviewDrop](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onpreviewdrop#system-
windows-uielement-onpreviewdrop\(system-windows-drageventargs\))| Invoked when
an unhandled
[PreviewDrop](https://learn.microsoft.com/dotnet/api/system.windows.dragdrop.previewdrop)
attached event reaches an element in its route that is derived from this
class. Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnPreviewGiveFeedback](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onpreviewgivefeedback#system-
windows-uielement-onpreviewgivefeedback\(system-windows-
givefeedbackeventargs\))| Invoked when an unhandled
[PreviewGiveFeedback](https://learn.microsoft.com/dotnet/api/system.windows.dragdrop.previewgivefeedback)
attached event reaches an element in its route that is derived from this
class. Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnPreviewGotKeyboardFocus](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onpreviewgotkeyboardfocus#system-
windows-uielement-onpreviewgotkeyboardfocus\(system-windows-input-
keyboardfocuschangedeventargs\))| Invoked when an unhandled
[PreviewGotKeyboardFocus](https://learn.microsoft.com/dotnet/api/system.windows.input.keyboard.previewgotkeyboardfocus)
attached event reaches an element in its route that is derived from this
class. Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnPreviewKeyDown](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onpreviewkeydown#system-
windows-uielement-onpreviewkeydown\(system-windows-input-keyeventargs\))|
Invoked when an unhandled
[PreviewKeyDown](https://learn.microsoft.com/dotnet/api/system.windows.input.keyboard.previewkeydown)
attached event reaches an element in its route that is derived from this
class. Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnPreviewKeyUp](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onpreviewkeyup#system-
windows-uielement-onpreviewkeyup\(system-windows-input-keyeventargs\))|
Invoked when an unhandled
[PreviewKeyUp](https://learn.microsoft.com/dotnet/api/system.windows.input.keyboard.previewkeyup)
attached event reaches an element in its route that is derived from this
class. Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnPreviewLostKeyboardFocus](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onpreviewlostkeyboardfocus#system-
windows-uielement-onpreviewlostkeyboardfocus\(system-windows-input-
keyboardfocuschangedeventargs\))| Invoked when an unhandled
[PreviewKeyDown](https://learn.microsoft.com/dotnet/api/system.windows.input.keyboard.previewkeydown)
attached event reaches an element in its route that is derived from this
class. Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnPreviewMouseDoubleClick](https://learn.microsoft.com/dotnet/api/system.windows.controls.control.onpreviewmousedoubleclick#system-
windows-controls-control-onpreviewmousedoubleclick\(system-windows-input-
mousebuttoneventargs\))| Raises the
[PreviewMouseDoubleClick](https://learn.microsoft.com/dotnet/api/system.windows.controls.control.previewmousedoubleclick)
routed event.  
(Унаследован от
[Control](https://learn.microsoft.com/dotnet/api/system.windows.controls.control))  
[OnPreviewMouseDown](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onpreviewmousedown#system-
windows-uielement-onpreviewmousedown\(system-windows-input-
mousebuttoneventargs\))| Invoked when an unhandled
[PreviewMouseDown](https://learn.microsoft.com/dotnet/api/system.windows.input.mouse.previewmousedown)
attached routed event reaches an element in its route that is derived from
this class. Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnPreviewMouseLeftButtonDown](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onpreviewmouseleftbuttondown#system-
windows-uielement-onpreviewmouseleftbuttondown\(system-windows-input-
mousebuttoneventargs\))| Invoked when an unhandled
[PreviewMouseLeftButtonDown](https://learn.microsoft.com/dotnet/api/system.windows.uielement.previewmouseleftbuttondown)
routed event reaches an element in its route that is derived from this class.
Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnPreviewMouseLeftButtonUp](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onpreviewmouseleftbuttonup#system-
windows-uielement-onpreviewmouseleftbuttonup\(system-windows-input-
mousebuttoneventargs\))| Invoked when an unhandled
[PreviewMouseLeftButtonUp](https://learn.microsoft.com/dotnet/api/system.windows.uielement.previewmouseleftbuttonup)
routed event reaches an element in its route that is derived from this class.
Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnPreviewMouseMove](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onpreviewmousemove#system-
windows-uielement-onpreviewmousemove\(system-windows-input-mouseeventargs\))|
Invoked when an unhandled
[PreviewMouseMove](https://learn.microsoft.com/dotnet/api/system.windows.input.mouse.previewmousemove)
attached event reaches an element in its route that is derived from this
class. Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnPreviewMouseRightButtonDown](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onpreviewmouserightbuttondown#system-
windows-uielement-onpreviewmouserightbuttondown\(system-windows-input-
mousebuttoneventargs\))| Invoked when an unhandled
[PreviewMouseRightButtonDown](https://learn.microsoft.com/dotnet/api/system.windows.uielement.previewmouserightbuttondown)
routed event reaches an element in its route that is derived from this class.
Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnPreviewMouseRightButtonUp](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onpreviewmouserightbuttonup#system-
windows-uielement-onpreviewmouserightbuttonup\(system-windows-input-
mousebuttoneventargs\))| Invoked when an unhandled
[PreviewMouseRightButtonUp](https://learn.microsoft.com/dotnet/api/system.windows.uielement.previewmouserightbuttonup)
routed event reaches an element in its route that is derived from this class.
Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnPreviewMouseUp](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onpreviewmouseup#system-
windows-uielement-onpreviewmouseup\(system-windows-input-
mousebuttoneventargs\))| Invoked when an unhandled
[PreviewMouseUp](https://learn.microsoft.com/dotnet/api/system.windows.input.mouse.previewmouseup)
attached event reaches an element in its route that is derived from this
class. Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnPreviewMouseWheel](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onpreviewmousewheel#system-
windows-uielement-onpreviewmousewheel\(system-windows-input-
mousewheeleventargs\))| Invoked when an unhandled
[PreviewMouseWheel](https://learn.microsoft.com/dotnet/api/system.windows.input.mouse.previewmousewheel)
attached event reaches an element in its route that is derived from this
class. Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnPreviewQueryContinueDrag](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onpreviewquerycontinuedrag#system-
windows-uielement-onpreviewquerycontinuedrag\(system-windows-
querycontinuedrageventargs\))| Invoked when an unhandled
[PreviewQueryContinueDrag](https://learn.microsoft.com/dotnet/api/system.windows.dragdrop.previewquerycontinuedrag)
attached event reaches an element in its route that is derived from this
class. Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnPreviewStylusButtonDown](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onpreviewstylusbuttondown#system-
windows-uielement-onpreviewstylusbuttondown\(system-windows-input-
stylusbuttoneventargs\))| Invoked when an unhandled
[PreviewStylusButtonDown](https://learn.microsoft.com/dotnet/api/system.windows.input.stylus.previewstylusbuttondown)
attached event reaches an element in its route that is derived from this
class. Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnPreviewStylusButtonUp](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onpreviewstylusbuttonup#system-
windows-uielement-onpreviewstylusbuttonup\(system-windows-input-
stylusbuttoneventargs\))| Invoked when an unhandled
[PreviewStylusButtonUp](https://learn.microsoft.com/dotnet/api/system.windows.input.stylus.previewstylusbuttonup)
attached event reaches an element in its route that is derived from this
class. Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnPreviewStylusDown](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onpreviewstylusdown#system-
windows-uielement-onpreviewstylusdown\(system-windows-input-
stylusdowneventargs\))| Invoked when an unhandled
[PreviewStylusDown](https://learn.microsoft.com/dotnet/api/system.windows.input.stylus.previewstylusdown)
attached event reaches an element in its route that is derived from this
class. Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnPreviewStylusInAirMove](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onpreviewstylusinairmove#system-
windows-uielement-onpreviewstylusinairmove\(system-windows-input-
styluseventargs\))| Invoked when an unhandled
[PreviewStylusInAirMove](https://learn.microsoft.com/dotnet/api/system.windows.input.stylus.previewstylusinairmove)
attached event reaches an element in its route that is derived from this
class. Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnPreviewStylusInRange](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onpreviewstylusinrange#system-
windows-uielement-onpreviewstylusinrange\(system-windows-input-
styluseventargs\))| Invoked when an unhandled
[PreviewStylusInRange](https://learn.microsoft.com/dotnet/api/system.windows.input.stylus.previewstylusinrange)
attached event reaches an element in its route that is derived from this
class. Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnPreviewStylusMove](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onpreviewstylusmove#system-
windows-uielement-onpreviewstylusmove\(system-windows-input-
styluseventargs\))| Invoked when an unhandled
[PreviewStylusMove](https://learn.microsoft.com/dotnet/api/system.windows.input.stylus.previewstylusmove)
attached event reaches an element in its route that is derived from this
class. Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnPreviewStylusOutOfRange](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onpreviewstylusoutofrange#system-
windows-uielement-onpreviewstylusoutofrange\(system-windows-input-
styluseventargs\))| Invoked when an unhandled
[PreviewStylusOutOfRange](https://learn.microsoft.com/dotnet/api/system.windows.input.stylus.previewstylusoutofrange)
attached event reaches an element in its route that is derived from this
class. Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnPreviewStylusSystemGesture](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onpreviewstylussystemgesture#system-
windows-uielement-onpreviewstylussystemgesture\(system-windows-input-
stylussystemgestureeventargs\))| Invoked when an unhandled
[PreviewStylusSystemGesture](https://learn.microsoft.com/dotnet/api/system.windows.input.stylus.previewstylussystemgesture)
attached event reaches an element in its route that is derived from this
class. Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnPreviewStylusUp](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onpreviewstylusup#system-
windows-uielement-onpreviewstylusup\(system-windows-input-styluseventargs\))|
Invoked when an unhandled
[PreviewStylusUp](https://learn.microsoft.com/dotnet/api/system.windows.input.stylus.previewstylusup)
attached event reaches an element in its route that is derived from this
class. Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnPreviewTextInput](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onpreviewtextinput#system-
windows-uielement-onpreviewtextinput\(system-windows-input-
textcompositioneventargs\))| Invoked when an unhandled
[PreviewTextInput](https://learn.microsoft.com/dotnet/api/system.windows.input.textcompositionmanager.previewtextinput)
attached event reaches an element in its route that is derived from this
class. Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnPreviewTouchDown](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onpreviewtouchdown#system-
windows-uielement-onpreviewtouchdown\(system-windows-input-toucheventargs\))|
Provides class handling for the
[PreviewTouchDown](https://learn.microsoft.com/dotnet/api/system.windows.uielement.previewtouchdown)
routed event that occurs when a touch presses this element.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnPreviewTouchMove](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onpreviewtouchmove#system-
windows-uielement-onpreviewtouchmove\(system-windows-input-toucheventargs\))|
Provides class handling for the
[PreviewTouchMove](https://learn.microsoft.com/dotnet/api/system.windows.uielement.previewtouchmove)
routed event that occurs when a touch moves while inside this element.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnPreviewTouchUp](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onpreviewtouchup#system-
windows-uielement-onpreviewtouchup\(system-windows-input-toucheventargs\))|
Provides class handling for the
[PreviewTouchUp](https://learn.microsoft.com/dotnet/api/system.windows.uielement.previewtouchup)
routed event that occurs when a touch is released inside this element.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnPropertyChanged](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.onpropertychanged#system-
windows-frameworkelement-onpropertychanged\(system-windows-
dependencypropertychangedeventargs\))| Invoked whenever the effective value of
any dependency property on this
[FrameworkElement](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement)
has been updated. The specific dependency property that changed is reported in
the arguments parameter. Overrides
[OnPropertyChanged(DependencyPropertyChangedEventArgs)](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject.onpropertychanged#system-
windows-dependencyobject-onpropertychanged\(system-windows-
dependencypropertychangedeventargs\)).  
(Унаследован от
[FrameworkElement](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement))  
[OnQueryContinueDrag](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onquerycontinuedrag#system-
windows-uielement-onquerycontinuedrag\(system-windows-
querycontinuedrageventargs\))| Invoked when an unhandled
[QueryContinueDrag](https://learn.microsoft.com/dotnet/api/system.windows.dragdrop.querycontinuedrag)
attached event reaches an element in its route that is derived from this
class. Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnQueryCursor](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onquerycursor#system-
windows-uielement-onquerycursor\(system-windows-input-querycursoreventargs\))|
Invoked when an unhandled
[QueryCursor](https://learn.microsoft.com/dotnet/api/system.windows.input.mouse.querycursor)
attached event reaches an element in its route that is derived from this
class. Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnRender](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onrender#system-
windows-uielement-onrender\(system-windows-media-drawingcontext\))| When
overridden in a derived class, participates in rendering operations that are
directed by the layout system. The rendering instructions for this element are
not used directly when this method is invoked, and are instead preserved for
later asynchronous use by layout and drawing.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnRenderSizeChanged](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.onrendersizechanged#system-
windows-frameworkelement-onrendersizechanged\(system-windows-
sizechangedinfo\))| Raises the
[SizeChanged](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.sizechanged)
event, using the specified information as part of the eventual event data.  
(Унаследован от
[FrameworkElement](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement))  
[OnStyleChanged](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.onstylechanged#system-
windows-frameworkelement-onstylechanged\(system-windows-style-system-windows-
style\))| Invoked when the style in use on this element changes, which will
invalidate the layout.  
(Унаследован от
[FrameworkElement](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement))  
[OnStylusButtonDown](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onstylusbuttondown#system-
windows-uielement-onstylusbuttondown\(system-windows-input-
stylusbuttoneventargs\))| Invoked when an unhandled
[StylusButtonDown](https://learn.microsoft.com/dotnet/api/system.windows.input.stylus.stylusbuttondown)
attached event reaches an element in its route that is derived from this
class. Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnStylusButtonUp](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onstylusbuttonup#system-
windows-uielement-onstylusbuttonup\(system-windows-input-
stylusbuttoneventargs\))| Invoked when an unhandled
[StylusButtonUp](https://learn.microsoft.com/dotnet/api/system.windows.input.stylus.stylusbuttonup)
attached event reaches an element in its route that is derived from this
class. Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnStylusDown](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onstylusdown#system-
windows-uielement-onstylusdown\(system-windows-input-stylusdowneventargs\))|
Invoked when an unhandled
[StylusDown](https://learn.microsoft.com/dotnet/api/system.windows.input.stylus.stylusdown)
attached event reaches an element in its route that is derived from this
class. Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnStylusEnter](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onstylusenter#system-
windows-uielement-onstylusenter\(system-windows-input-styluseventargs\))|
Invoked when an unhandled
[StylusEnter](https://learn.microsoft.com/dotnet/api/system.windows.input.stylus.stylusenter)
attached event is raised by this element. Implement this method to add class
handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnStylusInAirMove](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onstylusinairmove#system-
windows-uielement-onstylusinairmove\(system-windows-input-styluseventargs\))|
Invoked when an unhandled
[StylusInAirMove](https://learn.microsoft.com/dotnet/api/system.windows.input.stylus.stylusinairmove)
attached event reaches an element in its route that is derived from this
class. Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnStylusInRange](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onstylusinrange#system-
windows-uielement-onstylusinrange\(system-windows-input-styluseventargs\))|
Invoked when an unhandled
[StylusInRange](https://learn.microsoft.com/dotnet/api/system.windows.input.stylus.stylusinrange)
attached event reaches an element in its route that is derived from this
class. Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnStylusLeave](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onstylusleave#system-
windows-uielement-onstylusleave\(system-windows-input-styluseventargs\))|
Invoked when an unhandled
[StylusLeave](https://learn.microsoft.com/dotnet/api/system.windows.input.stylus.stylusleave)
attached event is raised by this element. Implement this method to add class
handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnStylusMove](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onstylusmove#system-
windows-uielement-onstylusmove\(system-windows-input-styluseventargs\))|
Invoked when an unhandled
[StylusMove](https://learn.microsoft.com/dotnet/api/system.windows.input.stylus.stylusmove)
attached event reaches an element in its route that is derived from this
class. Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnStylusOutOfRange](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onstylusoutofrange#system-
windows-uielement-onstylusoutofrange\(system-windows-input-styluseventargs\))|
Invoked when an unhandled
[StylusOutOfRange](https://learn.microsoft.com/dotnet/api/system.windows.input.stylus.stylusoutofrange)
attached event reaches an element in its route that is derived from this
class. Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnStylusSystemGesture](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onstylussystemgesture#system-
windows-uielement-onstylussystemgesture\(system-windows-input-
stylussystemgestureeventargs\))| Invoked when an unhandled
[StylusSystemGesture](https://learn.microsoft.com/dotnet/api/system.windows.input.stylus.stylussystemgesture)
attached event reaches an element in its route that is derived from this
class. Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnStylusUp](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onstylusup#system-
windows-uielement-onstylusup\(system-windows-input-styluseventargs\))| Invoked
when an unhandled
[StylusUp](https://learn.microsoft.com/dotnet/api/system.windows.input.stylus.stylusup)
attached event reaches an element in its route that is derived from this
class. Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnTemplateChanged](https://learn.microsoft.com/dotnet/api/system.windows.controls.control.ontemplatechanged#system-
windows-controls-control-ontemplatechanged\(system-windows-controls-
controltemplate-system-windows-controls-controltemplate\))| Called whenever
the control's template changes.  
(Унаследован от
[Control](https://learn.microsoft.com/dotnet/api/system.windows.controls.control))  
[OnTextInput](https://learn.microsoft.com/dotnet/api/system.windows.uielement.ontextinput#system-
windows-uielement-ontextinput\(system-windows-input-
textcompositioneventargs\))| Invoked when an unhandled
[TextInput](https://learn.microsoft.com/dotnet/api/system.windows.input.textcompositionmanager.textinput)
attached event reaches an element in its route that is derived from this
class. Implement this method to add class handling for this event.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnToolTipClosing](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.ontooltipclosing#system-
windows-frameworkelement-ontooltipclosing\(system-windows-controls-
tooltipeventargs\))| Invoked whenever an unhandled
[ToolTipClosing](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.tooltipclosing)
routed event reaches this class in its route. Implement this method to add
class handling for this event.  
(Унаследован от
[FrameworkElement](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement))  
[OnToolTipOpening](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.ontooltipopening#system-
windows-frameworkelement-ontooltipopening\(system-windows-controls-
tooltipeventargs\))| Invoked whenever the
[ToolTipOpening](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.tooltipopening)
routed event reaches this class in its route. Implement this method to add
class handling for this event.  
(Унаследован от
[FrameworkElement](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement))  
[OnTouchDown](https://learn.microsoft.com/dotnet/api/system.windows.uielement.ontouchdown#system-
windows-uielement-ontouchdown\(system-windows-input-toucheventargs\))|
Provides class handling for the
[TouchDown](https://learn.microsoft.com/dotnet/api/system.windows.uielement.touchdown)
routed event that occurs when a touch presses inside this element.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnTouchEnter](https://learn.microsoft.com/dotnet/api/system.windows.uielement.ontouchenter#system-
windows-uielement-ontouchenter\(system-windows-input-toucheventargs\))|
Provides class handling for the
[TouchEnter](https://learn.microsoft.com/dotnet/api/system.windows.uielement.touchenter)
routed event that occurs when a touch moves from outside to inside the bounds
of this element.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnTouchLeave](https://learn.microsoft.com/dotnet/api/system.windows.uielement.ontouchleave#system-
windows-uielement-ontouchleave\(system-windows-input-toucheventargs\))|
Provides class handling for the
[TouchLeave](https://learn.microsoft.com/dotnet/api/system.windows.uielement.touchleave)
routed event that occurs when a touch moves from inside to outside the bounds
of this
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement).  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnTouchMove](https://learn.microsoft.com/dotnet/api/system.windows.uielement.ontouchmove#system-
windows-uielement-ontouchmove\(system-windows-input-toucheventargs\))|
Provides class handling for the
[TouchMove](https://learn.microsoft.com/dotnet/api/system.windows.uielement.touchmove)
routed event that occurs when a touch moves while inside this element.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnTouchUp](https://learn.microsoft.com/dotnet/api/system.windows.uielement.ontouchup#system-
windows-uielement-ontouchup\(system-windows-input-toucheventargs\))| Provides
class handling for the
[TouchUp](https://learn.microsoft.com/dotnet/api/system.windows.uielement.touchup)
routed event that occurs when a touch is released inside this element.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[OnVisualChildrenChanged](https://learn.microsoft.com/dotnet/api/system.windows.media.visual.onvisualchildrenchanged#system-
windows-media-visual-onvisualchildrenchanged\(system-windows-dependencyobject-
system-windows-dependencyobject\))| Called when the
[VisualCollection](https://learn.microsoft.com/dotnet/api/system.windows.media.visualcollection)
of the visual object is modified.  
(Унаследован от
[Visual](https://learn.microsoft.com/dotnet/api/system.windows.media.visual))  
[OnVisualParentChanged](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.onvisualparentchanged#system-
windows-frameworkelement-onvisualparentchanged\(system-windows-
dependencyobject\))| Invoked when the parent of this element in the visual
tree is changed. Overrides
[OnVisualParentChanged(DependencyObject)](https://learn.microsoft.com/dotnet/api/system.windows.uielement.onvisualparentchanged#system-
windows-uielement-onvisualparentchanged\(system-windows-dependencyobject\)).  
(Унаследован от
[FrameworkElement](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement))  
[ParentLayoutInvalidated](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.parentlayoutinvalidated#system-
windows-frameworkelement-parentlayoutinvalidated\(system-windows-uielement\))|
Supports incremental layout implementations in specialized subclasses of
[FrameworkElement](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement).
[ParentLayoutInvalidated(UIElement)](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.parentlayoutinvalidated#system-
windows-frameworkelement-parentlayoutinvalidated\(system-windows-uielement\))
is invoked when a child element has invalidated a property that is marked in
metadata as affecting the parent's measure or arrange passes during layout.  
(Унаследован от
[FrameworkElement](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement))  
[PointFromScreen](https://learn.microsoft.com/dotnet/api/system.windows.media.visual.pointfromscreen#system-
windows-media-visual-pointfromscreen\(system-windows-point\))| Converts a
[Point](https://learn.microsoft.com/dotnet/api/system.windows.point) in screen
coordinates into a
[Point](https://learn.microsoft.com/dotnet/api/system.windows.point) that
represents the current coordinate system of the
[Visual](https://learn.microsoft.com/dotnet/api/system.windows.media.visual).  
(Унаследован от
[Visual](https://learn.microsoft.com/dotnet/api/system.windows.media.visual))  
[PointToScreen](https://learn.microsoft.com/dotnet/api/system.windows.media.visual.pointtoscreen#system-
windows-media-visual-pointtoscreen\(system-windows-point\))| Converts a
[Point](https://learn.microsoft.com/dotnet/api/system.windows.point) that
represents the current coordinate system of the
[Visual](https://learn.microsoft.com/dotnet/api/system.windows.media.visual)
into a [Point](https://learn.microsoft.com/dotnet/api/system.windows.point) in
screen coordinates.  
(Унаследован от
[Visual](https://learn.microsoft.com/dotnet/api/system.windows.media.visual))  
[PredictFocus](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.predictfocus#system-
windows-frameworkelement-predictfocus\(system-windows-input-
focusnavigationdirection\))| Determines the next element that would receive
focus relative to this element for a provided focus movement direction, but
does not actually move the focus.  
(Унаследован от
[FrameworkElement](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement))  
[RaiseEvent](https://learn.microsoft.com/dotnet/api/system.windows.uielement.raiseevent#system-
windows-uielement-raiseevent\(system-windows-routedeventargs\))| Raises a
specific routed event. The
[RoutedEvent](https://learn.microsoft.com/dotnet/api/system.windows.routedevent)
to be raised is identified within the
[RoutedEventArgs](https://learn.microsoft.com/dotnet/api/system.windows.routedeventargs)
instance that is provided (as the
[RoutedEvent](https://learn.microsoft.com/dotnet/api/system.windows.routedeventargs.routedevent#system-
windows-routedeventargs-routedevent) property of that event data).  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[ReadLocalValue](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject.readlocalvalue#system-
windows-dependencyobject-readlocalvalue\(system-windows-dependencyproperty\))|
Returns the local value of a dependency property, if it exists.  
(Унаследован от
[DependencyObject](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject))  
[RegisterName](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.registername#system-
windows-frameworkelement-registername\(system-string-system-object\))|
Provides an accessor that simplifies access to the
[NameScope](https://learn.microsoft.com/dotnet/api/system.windows.namescope)
registration method.  
(Унаследован от
[FrameworkElement](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement))  
[ReleaseAllTouchCaptures](https://learn.microsoft.com/dotnet/api/system.windows.uielement.releasealltouchcaptures#system-
windows-uielement-releasealltouchcaptures)| Releases all captured touch
devices from this element.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[ReleaseMouseCapture](https://learn.microsoft.com/dotnet/api/system.windows.uielement.releasemousecapture#system-
windows-uielement-releasemousecapture)| Releases the mouse capture, if this
element held the capture.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[ReleaseStylusCapture](https://learn.microsoft.com/dotnet/api/system.windows.uielement.releasestyluscapture#system-
windows-uielement-releasestyluscapture)| Releases the stylus device capture,
if this element held the capture.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[ReleaseTouchCapture](https://learn.microsoft.com/dotnet/api/system.windows.uielement.releasetouchcapture#system-
windows-uielement-releasetouchcapture\(system-windows-input-touchdevice\))|
Attempts to release the specified touch device from this element.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[RemoveHandler](https://learn.microsoft.com/dotnet/api/system.windows.uielement.removehandler#system-
windows-uielement-removehandler\(system-windows-routedevent-system-
delegate\))| Removes the specified routed event handler from this element.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[RemoveLogicalChild](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.removelogicalchild#system-
windows-frameworkelement-removelogicalchild\(system-object\))| Removes the
provided object from this element's logical tree.
[FrameworkElement](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement)
updates the affected logical tree parent pointers to keep in sync with this
deletion.  
(Унаследован от
[FrameworkElement](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement))  
[RemoveVisualChild](https://learn.microsoft.com/dotnet/api/system.windows.media.visual.removevisualchild#system-
windows-media-visual-removevisualchild\(system-windows-media-visual\))|
Removes the parent-child relationship between two visuals.  
(Унаследован от
[Visual](https://learn.microsoft.com/dotnet/api/system.windows.media.visual))  
[SetBinding(DependencyProperty,
String)](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.setbinding#system-
windows-frameworkelement-setbinding\(system-windows-dependencyproperty-system-
string\))| Attaches a binding to this element, based on the provided source
property name as a path qualification to the data source.  
(Унаследован от
[FrameworkElement](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement))  
[SetBinding(DependencyProperty,
BindingBase)](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.setbinding#system-
windows-frameworkelement-setbinding\(system-windows-dependencyproperty-system-
windows-data-bindingbase\))| Attaches a binding to this element, based on the
provided binding object.  
(Унаследован от
[FrameworkElement](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement))  
[SetCurrentValue](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject.setcurrentvalue#system-
windows-dependencyobject-setcurrentvalue\(system-windows-dependencyproperty-
system-object\))| Sets the value of a dependency property without changing its
value source.  
(Унаследован от
[DependencyObject](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject))  
[SetResourceReference](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.setresourcereference#system-
windows-frameworkelement-setresourcereference\(system-windows-
dependencyproperty-system-object\))| Searches for a resource with the
specified name and sets up a resource reference to it for the specified
property.  
(Унаследован от
[FrameworkElement](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement))  
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
[ShouldSerializeCommandBindings](https://learn.microsoft.com/dotnet/api/system.windows.uielement.shouldserializecommandbindings#system-
windows-uielement-shouldserializecommandbindings)| Returns whether
serialization processes should serialize the contents of the
[CommandBindings](https://learn.microsoft.com/dotnet/api/system.windows.uielement.commandbindings#system-
windows-uielement-commandbindings) property on instances of this class.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[ShouldSerializeContent](https://learn.microsoft.com/dotnet/api/system.windows.controls.contentcontrol.shouldserializecontent#system-
windows-controls-contentcontrol-shouldserializecontent)| Indicates whether the
[Content](https://learn.microsoft.com/dotnet/api/system.windows.controls.contentcontrol.content#system-
windows-controls-contentcontrol-content) property should be persisted.  
(Унаследован от
[ContentControl](https://learn.microsoft.com/dotnet/api/system.windows.controls.contentcontrol))  
[ShouldSerializeInputBindings](https://learn.microsoft.com/dotnet/api/system.windows.uielement.shouldserializeinputbindings#system-
windows-uielement-shouldserializeinputbindings)| Returns whether serialization
processes should serialize the contents of the
[InputBindings](https://learn.microsoft.com/dotnet/api/system.windows.uielement.inputbindings#system-
windows-uielement-inputbindings) property on instances of this class.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[ShouldSerializeProperty](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject.shouldserializeproperty#system-
windows-dependencyobject-shouldserializeproperty\(system-windows-
dependencyproperty\))| Returns a value that indicates whether serialization
processes should serialize the value for the provided dependency property.  
(Унаследован от
[DependencyObject](https://learn.microsoft.com/dotnet/api/system.windows.dependencyobject))  
[ShouldSerializeResources](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.shouldserializeresources#system-
windows-frameworkelement-shouldserializeresources)| Returns whether
serialization processes should serialize the contents of the
[Resources](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.resources#system-
windows-frameworkelement-resources) property.  
(Унаследован от
[FrameworkElement](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement))  
[ShouldSerializeStyle](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.shouldserializestyle#system-
windows-frameworkelement-shouldserializestyle)| Returns whether serialization
processes should serialize the contents of the
[Style](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.style#system-
windows-frameworkelement-style) property.  
(Унаследован от
[FrameworkElement](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement))  
[ShouldSerializeTriggers](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.shouldserializetriggers#system-
windows-frameworkelement-shouldserializetriggers)| Returns whether
serialization processes should serialize the contents of the
[Triggers](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.triggers#system-
windows-frameworkelement-triggers) property.  
(Унаследован от
[FrameworkElement](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement))  
[ToString](https://learn.microsoft.com/dotnet/api/system.windows.controls.control.tostring#system-
windows-controls-control-tostring)| Returns the string representation of a
[Control](https://learn.microsoft.com/dotnet/api/system.windows.controls.control)
object.  
(Унаследован от
[Control](https://learn.microsoft.com/dotnet/api/system.windows.controls.control))  
[TransformToAncestor(Visual)](https://learn.microsoft.com/dotnet/api/system.windows.media.visual.transformtoancestor#system-
windows-media-visual-transformtoancestor\(system-windows-media-visual\))|
Returns a transform that can be used to transform coordinates from the
[Visual](https://learn.microsoft.com/dotnet/api/system.windows.media.visual)
to the specified
[Visual](https://learn.microsoft.com/dotnet/api/system.windows.media.visual)
ancestor of the visual object.  
(Унаследован от
[Visual](https://learn.microsoft.com/dotnet/api/system.windows.media.visual))  
[TransformToAncestor(Visual3D)](https://learn.microsoft.com/dotnet/api/system.windows.media.visual.transformtoancestor#system-
windows-media-visual-transformtoancestor\(system-windows-media-
media3d-visual3d\))| Returns a transform that can be used to transform
coordinates from the
[Visual](https://learn.microsoft.com/dotnet/api/system.windows.media.visual)
to the specified
[Visual3D](https://learn.microsoft.com/dotnet/api/system.windows.media.media3d.visual3d)
ancestor of the visual object.  
(Унаследован от
[Visual](https://learn.microsoft.com/dotnet/api/system.windows.media.visual))  
[TransformToDescendant](https://learn.microsoft.com/dotnet/api/system.windows.media.visual.transformtodescendant#system-
windows-media-visual-transformtodescendant\(system-windows-media-visual\))|
Returns a transform that can be used to transform coordinates from the
[Visual](https://learn.microsoft.com/dotnet/api/system.windows.media.visual)
to the specified visual object descendant.  
(Унаследован от
[Visual](https://learn.microsoft.com/dotnet/api/system.windows.media.visual))  
[TransformToVisual](https://learn.microsoft.com/dotnet/api/system.windows.media.visual.transformtovisual#system-
windows-media-visual-transformtovisual\(system-windows-media-visual\))|
Returns a transform that can be used to transform coordinates from the
[Visual](https://learn.microsoft.com/dotnet/api/system.windows.media.visual)
to the specified visual object.  
(Унаследован от
[Visual](https://learn.microsoft.com/dotnet/api/system.windows.media.visual))  
[TranslatePoint](https://learn.microsoft.com/dotnet/api/system.windows.uielement.translatepoint#system-
windows-uielement-translatepoint\(system-windows-point-system-windows-
uielement\))| Translates a point relative to this element to coordinates that
are relative to the specified element.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[TryFindResource](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.tryfindresource#system-
windows-frameworkelement-tryfindresource\(system-object\))| Searches for a
resource with the specified key, and returns that resource if found.  
(Унаследован от
[FrameworkElement](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement))  
[UnregisterName](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.unregistername#system-
windows-frameworkelement-unregistername\(system-string\))| Simplifies access
to the
[NameScope](https://learn.microsoft.com/dotnet/api/system.windows.namescope)
de-registration method.  
(Унаследован от
[FrameworkElement](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement))  
[UpdateDefaultStyle](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.updatedefaultstyle#system-
windows-frameworkelement-updatedefaultstyle)| Reapplies the default style to
the current
[FrameworkElement](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement).  
(Унаследован от
[FrameworkElement](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement))  
[UpdateLayout](https://learn.microsoft.com/dotnet/api/system.windows.uielement.updatelayout#system-
windows-uielement-updatelayout)| Ensures that all visual child elements of
this element are properly updated for layout.  
(Унаследован от
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement))  
[VerifyAccess](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject.verifyaccess#system-
windows-threading-dispatcherobject-verifyaccess)| Enforces that the calling
thread has access to this
[DispatcherObject](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject).  
(Унаследован от
[DispatcherObject](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject))  
##  __Методы расширения
[GetVisibleSize](M_Tessa_UI_UIExtensions_GetVisibleSize.htm)|  Возвращает
размер области элемента, который сейчас отображается на экране. В обработчике
события
[SizeChanged](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.sizechanged)
можно получить актуальные отображаемые размеры, которые могут быть меньше
ActualWidth/ActualHeight, например, в случае, если элементу явно указаны
Width/Height, но размеры рабочей области (окна) не позволяют контролу
разместиться полностью, и края контрола "обрезаются". В этом случае свойства
ActualWidth/ActualHeight возвращают размеры контролы без учёта "обрезания", а
этот метод - размеры "после обрезания", т.е. те размеры, которые фактически
видит пользователь.  
(Определяется [UIExtensions](T_Tessa_UI_UIExtensions.htm))  
---|---  
##  __См. также
#### Ссылки
[ScanDialogView -
](T_Tessa_Extensions_Platform_Client_Views_ScanDialogView.htm)
[Tessa.Extensions.Platform.Client.Views - пространство
имён](N_Tessa_Extensions_Platform_Client_Views.htm)
