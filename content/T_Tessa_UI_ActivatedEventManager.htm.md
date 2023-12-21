# ActivatedEventManager - класс
The activated event manager.
## __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public class ActivatedEventManager : WeakEventManager<ActivatedEventManager, IActivateMarker>
VB __Копировать
     Public Class ActivatedEventManager
    	Inherits WeakEventManager(Of ActivatedEventManager, IActivateMarker)
C++ __Копировать
     public ref class ActivatedEventManager : public WeakEventManager<ActivatedEventManager^, IActivateMarker^>
F# __Копировать
     type ActivatedEventManager = 
        class
            inherit WeakEventManager<ActivatedEventManager, IActivateMarker>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[DispatcherObject](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject) __[WeakEventManager](https://learn.microsoft.com/dotnet/api/system.windows.weakeventmanager) __[WeakEventManager](T_Tessa_UI_WeakEventManager_2.htm)<ActivatedEventManager, [IActivateMarker](T_Tessa_UI_Views_IActivateMarker.htm)> __ ActivatedEventManager
##  __Свойства
[Dispatcher](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject.dispatcher#system-
windows-threading-dispatcherobject-dispatcher)| Gets the
[Dispatcher](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcher)
this
[DispatcherObject](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject)
is associated with.  
(Унаследован от
[DispatcherObject](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject))  
---|---  
[Item](https://learn.microsoft.com/dotnet/api/system.windows.weakeventmanager.item#system-
windows-weakeventmanager-item\(system-object\))| Gets or sets the data being
stored for the specified source.  
(Унаследован от
[WeakEventManager](https://learn.microsoft.com/dotnet/api/system.windows.weakeventmanager))  
[ReadLock](https://learn.microsoft.com/dotnet/api/system.windows.weakeventmanager.readlock#system-
windows-weakeventmanager-readlock)| Establishes a read-lock on the underlying
data table, and returns an
[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable).  
(Унаследован от
[WeakEventManager](https://learn.microsoft.com/dotnet/api/system.windows.weakeventmanager))  
[WriteLock](https://learn.microsoft.com/dotnet/api/system.windows.weakeventmanager.writelock#system-
windows-weakeventmanager-writelock)| Establishes a write-lock on the
underlying data table, and returns an
[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable).  
(Унаследован от
[WeakEventManager](https://learn.microsoft.com/dotnet/api/system.windows.weakeventmanager))  
##  __Методы
[CheckAccess](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject.checkaccess#system-
windows-threading-dispatcherobject-checkaccess)| Determines whether the
calling thread has access to this
[DispatcherObject](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject).  
(Унаследован от
[DispatcherObject](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject))  
---|---  
[DeliverEvent](https://learn.microsoft.com/dotnet/api/system.windows.weakeventmanager.deliverevent#system-
windows-weakeventmanager-deliverevent\(system-object-system-eventargs\))|
Delivers the event being managed to each listener.  
(Унаследован от
[WeakEventManager](https://learn.microsoft.com/dotnet/api/system.windows.weakeventmanager))  
[DeliverEventToList](https://learn.microsoft.com/dotnet/api/system.windows.weakeventmanager.delivereventtolist#system-
windows-weakeventmanager-delivereventtolist\(system-object-system-eventargs-
system-windows-weakeventmanager-listenerlist\))| Delivers the event being
managed to each listener in the provided list.  
(Унаследован от
[WeakEventManager](https://learn.microsoft.com/dotnet/api/system.windows.weakeventmanager))  
[NewListenerList](https://learn.microsoft.com/dotnet/api/system.windows.weakeventmanager.newlistenerlist#system-
windows-weakeventmanager-newlistenerlist)| Returns a new object to contain
listeners to an event.  
(Унаследован от
[WeakEventManager](https://learn.microsoft.com/dotnet/api/system.windows.weakeventmanager))  
[ProtectedAddHandler](https://learn.microsoft.com/dotnet/api/system.windows.weakeventmanager.protectedaddhandler#system-
windows-weakeventmanager-protectedaddhandler\(system-object-system-
delegate\))| Adds the specified delegate as an event handler of the specified
source.  
(Унаследован от
[WeakEventManager](https://learn.microsoft.com/dotnet/api/system.windows.weakeventmanager))  
[ProtectedAddListener](https://learn.microsoft.com/dotnet/api/system.windows.weakeventmanager.protectedaddlistener#system-
windows-weakeventmanager-protectedaddlistener\(system-object-system-windows-
iweakeventlistener\))| Adds the provided listener to the provided source for
the event being managed.  
(Унаследован от
[WeakEventManager](https://learn.microsoft.com/dotnet/api/system.windows.weakeventmanager))  
[ProtectedRemoveHandler](https://learn.microsoft.com/dotnet/api/system.windows.weakeventmanager.protectedremovehandler#system-
windows-weakeventmanager-protectedremovehandler\(system-object-system-
delegate\))| Removes the previously added handler from the specified source.  
(Унаследован от
[WeakEventManager](https://learn.microsoft.com/dotnet/api/system.windows.weakeventmanager))  
[ProtectedRemoveListener](https://learn.microsoft.com/dotnet/api/system.windows.weakeventmanager.protectedremovelistener#system-
windows-weakeventmanager-protectedremovelistener\(system-object-system-
windows-iweakeventlistener\))| Removes a previously added listener from the
provided source.  
(Унаследован от
[WeakEventManager](https://learn.microsoft.com/dotnet/api/system.windows.weakeventmanager))  
[Purge](https://learn.microsoft.com/dotnet/api/system.windows.weakeventmanager.purge#system-
windows-weakeventmanager-purge\(system-object-system-object-system-boolean\))|
Removes inactive listener entries from the data list for the provided source.
Returns true if some entries were actually removed from the list.  
(Унаследован от
[WeakEventManager](https://learn.microsoft.com/dotnet/api/system.windows.weakeventmanager))  
[Remove](https://learn.microsoft.com/dotnet/api/system.windows.weakeventmanager.remove#system-
windows-weakeventmanager-remove\(system-object\))| Removes all listeners for
the specified source.  
(Унаследован от
[WeakEventManager](https://learn.microsoft.com/dotnet/api/system.windows.weakeventmanager))  
[ScheduleCleanup](https://learn.microsoft.com/dotnet/api/system.windows.weakeventmanager.schedulecleanup#system-
windows-weakeventmanager-schedulecleanup)| Requests that a purge of unused
entries in the underlying listener list be performed on a lower priority
thread.  
(Унаследован от
[WeakEventManager](https://learn.microsoft.com/dotnet/api/system.windows.weakeventmanager))  
[StartListening(IActivateMarker)](M_Tessa_UI_ActivatedEventManager_StartListening.htm)|
Присоединяет обработчик события от текущего объекта для заданного источника.  
(Переопределяет [WeakEventManager<TManager,
TEventSource>.StartListening(TEventSource)](M_Tessa_UI_WeakEventManager_2_StartListening_1.htm))  
[StartListening(Object)](M_Tessa_UI_WeakEventManager_2_StartListening.htm)|
Присоединяет обработчик события от текущего объекта для заданного источника.  
(Унаследован от [WeakEventManager<TManager,
TEventSource>](T_Tessa_UI_WeakEventManager_2.htm))  
[StopListening(IActivateMarker)](M_Tessa_UI_ActivatedEventManager_StopListening.htm)|
Отсоединяет обработчик события от текущего объекта для заданного источника.  
(Переопределяет [WeakEventManager<TManager,
TEventSource>.StopListening(TEventSource)](M_Tessa_UI_WeakEventManager_2_StopListening_1.htm))  
[StopListening(Object)](M_Tessa_UI_WeakEventManager_2_StopListening.htm)|
Отсоединяет обработчик события от текущего объекта для заданного источника.  
(Унаследован от [WeakEventManager<TManager,
TEventSource>](T_Tessa_UI_WeakEventManager_2.htm))  
[VerifyAccess](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject.verifyaccess#system-
windows-threading-dispatcherobject-verifyaccess)| Enforces that the calling
thread has access to this
[DispatcherObject](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject).  
(Унаследован от
[DispatcherObject](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject))  
##  __См. также
#### Ссылки
[Tessa.UI - пространство имён](N_Tessa_UI.htm)
