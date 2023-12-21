# WeakEventManager<TManager, TEventSource> \- класс
Объект, организующий подписку на слабые события.
## __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class WeakEventManager<TManager, TEventSource> : WeakEventManager
    where TManager : WeakEventManager<TManager, TEventSource>
    where TEventSource : class
VB __Копировать
     Public MustInherit Class WeakEventManager(Of TManager As WeakEventManager(Of TManager, TEventSource), TEventSource As Class)
    	Inherits WeakEventManager
C++ __Копировать
    generic<typename TManager, typename TEventSource>
    where TManager : WeakEventManager<TManager, TEventSource>
    where TEventSource : ref class
    public ref class WeakEventManager abstract : public WeakEventManager
F# __Копировать
     [<AbstractClassAttribute>]
    type WeakEventManager<'TManager, 'TEventSource when 'TManager : WeakEventManager<'TManager, 'TEventSource> when 'TEventSource : not struct> = 
        class
            inherit WeakEventManager
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[DispatcherObject](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject) __[WeakEventManager](https://learn.microsoft.com/dotnet/api/system.windows.weakeventmanager) __ WeakEventManager<TManager, TEventSource>
Derived
[Tessa.UI.ActivatedEventManager](T_Tessa_UI_ActivatedEventManager.htm)
[Tessa.UI.AppManager.ApplicationCacheWipedEventManager](T_Tessa_UI_AppManager_ApplicationCacheWipedEventManager.htm)
[Tessa.UI.Cards.Blocks.MultipleColumnBlockRearrangedEventManager](T_Tessa_UI_Cards_Blocks_MultipleColumnBlockRearrangedEventManager.htm)
[Tessa.UI.Cards.Forms.DefaultFormRearrangedEventManager](T_Tessa_UI_Cards_Forms_DefaultFormRearrangedEventManager.htm)
[Tessa.UI.Cards.Views.Controls.LayoutInvalidationRequestedEventManager](T_Tessa_UI_Cards_Views_Controls_LayoutInvalidationRequestedEventManager.htm)
[Tessa.UI.Controls.AutoCompleteCtrl.CommittingChangesWeakEventManager](T_Tessa_UI_Controls_AutoCompleteCtrl_CommittingChangesWeakEventManager.htm)
[Tessa.UI.Controls.AutoCompleteCtrl.PopupButtonClickEventManager](T_Tessa_UI_Controls_AutoCompleteCtrl_PopupButtonClickEventManager.htm)
[Tessa.UI.Controls.AutoCompleteCtrl.PopUpButtonPreviewKeyDownEventManager](T_Tessa_UI_Controls_AutoCompleteCtrl_PopUpButtonPreviewKeyDownEventManager.htm)
[Tessa.UI.Controls.CustomRichTextBoxCtrl.BIRichTextBoxInsertItemEventManager](T_Tessa_UI_Controls_CustomRichTextBoxCtrl_BIRichTextBoxInsertItemEventManager.htm)
[Tessa.UI.Controls.FilePreview.PagingPreviewActionRequestedEventManager](T_Tessa_UI_Controls_FilePreview_PagingPreviewActionRequestedEventManager.htm)
[Tessa.UI.Controls.Scrolling.ScrollingControlDisposedEventManager](T_Tessa_UI_Controls_Scrolling_ScrollingControlDisposedEventManager.htm)
[Tessa.UI.Controls.Scrolling.ScrollToPageSuggestedEventManager](T_Tessa_UI_Controls_Scrolling_ScrollToPageSuggestedEventManager.htm)
[Tessa.UI.Controls.UIElementGotFocusEventManager](T_Tessa_UI_Controls_UIElementGotFocusEventManager.htm)
[Tessa.UI.Files.Controls.FilePreviewResettingEventManager](T_Tessa_UI_Files_Controls_FilePreviewResettingEventManager.htm)
[Tessa.UI.Views.Content.Table.AutoSizeInvalidationEventManager](T_Tessa_UI_Views_Content_Table_AutoSizeInvalidationEventManager.htm)
[Tessa.UI.Views.Filtering.AcceptedWeakEventManager](T_Tessa_UI_Views_Filtering_AcceptedWeakEventManager.htm)
[Tessa.UI.Views.Filtering.ChangedWeakEventManager](T_Tessa_UI_Views_Filtering_ChangedWeakEventManager.htm)
[Tessa.UI.Views.SelectionStateChangedEventManager](T_Tessa_UI_Views_SelectionStateChangedEventManager.htm)
[Tessa.UI.Views.Workplaces.WorkplaceClosingEventManager](T_Tessa_UI_Views_Workplaces_WorkplaceClosingEventManager.htm)
[Tessa.UI.Windows.BackgroundChangedEventManager](T_Tessa_UI_Windows_BackgroundChangedEventManager.htm)
[Tessa.UI.Windows.KeyDownWeakEventManager](T_Tessa_UI_Windows_KeyDownWeakEventManager.htm)
[Tessa.UI.Windows.TessaShellSettingsAppliedEventManager](T_Tessa_UI_Windows_TessaShellSettingsAppliedEventManager.htm)
[Tessa.UI.Windows.WindowActivatedEventManager](T_Tessa_UI_Windows_WindowActivatedEventManager.htm)
[Tessa.UI.Windows.WindowDeactivatedEventManager](T_Tessa_UI_Windows_WindowDeactivatedEventManager.htm)
[Tessa.UI.Windows.WindowLocationChangedEventManager](T_Tessa_UI_Windows_WindowLocationChangedEventManager.htm)
[Tessa.UI.Windows.WorkspaceClosedEventManager](T_Tessa_UI_Windows_WorkspaceClosedEventManager.htm)
Подробнее __Less __
#### Параметры типа
TManager
    Тип текущего объекта. Должен содержать открытый конструктор по умолчанию.
TEventSource
    Ссылочный объект, на событие которого выполняется подписка.
##  __Конструкторы
[WeakEventManager<TManager,
TEventSource>](M_Tessa_UI_WeakEventManager_2__ctor.htm)| Инициализирует новый
экземпляр класса WeakEventManager<TManager, TEventSource>  
---|---  
##  __Свойства
[CurrentManager](P_Tessa_UI_WeakEventManager_2_CurrentManager.htm)|  Текущий
менеджер, организующий подписку на слабые события.  
---|---  
[Dispatcher](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject.dispatcher#system-
windows-threading-dispatcherobject-dispatcher)| Gets the
[Dispatcher](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcher)
this
[DispatcherObject](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject)
is associated with.  
(Унаследован от
[DispatcherObject](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject))  
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
[AddListener](M_Tessa_UI_WeakEventManager_2_AddListener.htm)|  Добавляет
слабую ссылку на подписчика события.  
---|---  
[CheckAccess](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject.checkaccess#system-
windows-threading-dispatcherobject-checkaccess)| Determines whether the
calling thread has access to this
[DispatcherObject](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject).  
(Унаследован от
[DispatcherObject](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject))  
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
[Initialize](M_Tessa_UI_WeakEventManager_2_Initialize.htm)|  
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
[RemoveListener](M_Tessa_UI_WeakEventManager_2_RemoveListener.htm)|  Удаляет
слабую ссылку на подписчика события.  
[ScheduleCleanup](https://learn.microsoft.com/dotnet/api/system.windows.weakeventmanager.schedulecleanup#system-
windows-weakeventmanager-schedulecleanup)| Requests that a purge of unused
entries in the underlying listener list be performed on a lower priority
thread.  
(Унаследован от
[WeakEventManager](https://learn.microsoft.com/dotnet/api/system.windows.weakeventmanager))  
[StartListening(Object)](M_Tessa_UI_WeakEventManager_2_StartListening.htm)|
Присоединяет обработчик события от текущего объекта для заданного источника.  
(Переопределяет
[WeakEventManager.StartListening(Object)](https://learn.microsoft.com/dotnet/api/system.windows.weakeventmanager.startlistening#system-
windows-weakeventmanager-startlistening\(system-object\)))  
[StartListening(TEventSource)](M_Tessa_UI_WeakEventManager_2_StartListening_1.htm)|
Присоединяет обработчик события от текущего объекта для заданного источника.  
[StopListening(Object)](M_Tessa_UI_WeakEventManager_2_StopListening.htm)|
Отсоединяет обработчик события от текущего объекта для заданного источника.  
(Переопределяет
[WeakEventManager.StopListening(Object)](https://learn.microsoft.com/dotnet/api/system.windows.weakeventmanager.stoplistening#system-
windows-weakeventmanager-stoplistening\(system-object\)))  
[StopListening(TEventSource)](M_Tessa_UI_WeakEventManager_2_StopListening_1.htm)|
Отсоединяет обработчик события от текущего объекта для заданного источника.  
[VerifyAccess](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject.verifyaccess#system-
windows-threading-dispatcherobject-verifyaccess)| Enforces that the calling
thread has access to this
[DispatcherObject](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject).  
(Унаследован от
[DispatcherObject](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject))  
##  __См. также
#### Ссылки
[Tessa.UI - пространство имён](N_Tessa_UI.htm)
