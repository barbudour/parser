# TreeCollectionView - класс
##  __Definition
 **Пространство имён:** [Tessa.UI.Data](N_Tessa_UI_Data.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public class TreeCollectionView : CollectionView, 
    	IEditableCollectionViewAddNewItem, IEditableCollectionView, IItemProperties, IWeakEventListener
VB __Копировать
     Public Class TreeCollectionView
    	Inherits CollectionView
    	Implements IEditableCollectionViewAddNewItem, IEditableCollectionView, IItemProperties, IWeakEventListener
C++ __Копировать
     public ref class TreeCollectionView : public CollectionView, 
    	IEditableCollectionViewAddNewItem, IEditableCollectionView, IItemProperties, IWeakEventListener
F# __Копировать
     type TreeCollectionView = 
        class
            inherit CollectionView
            interface IEditableCollectionViewAddNewItem
            interface IEditableCollectionView
            interface IItemProperties
            interface IWeakEventListener
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[DispatcherObject](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject) __[CollectionView](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview) __ TreeCollectionView
Implements
    [IEditableCollectionView](https://learn.microsoft.com/dotnet/api/system.componentmodel.ieditablecollectionview), [IEditableCollectionViewAddNewItem](https://learn.microsoft.com/dotnet/api/system.componentmodel.ieditablecollectionviewaddnewitem), [IItemProperties](https://learn.microsoft.com/dotnet/api/system.componentmodel.iitemproperties), [IWeakEventListener](https://learn.microsoft.com/dotnet/api/system.windows.iweakeventlistener)
##  __Конструкторы
[TreeCollectionView](M_Tessa_UI_Data_TreeCollectionView__ctor.htm)|
Инициализирует новый экземпляр класса TreeCollectionView  
---|---  
##  __Свойства
[AllowsCrossThreadChanges](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.allowscrossthreadchanges#system-
windows-data-collectionview-allowscrossthreadchanges)| Gets a value that
indicates whether a thread other than the one that created the
[CollectionView](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview)
can change the
[SourceCollection](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.sourcecollection#system-
windows-data-collectionview-sourcecollection).  
(Унаследован от
[CollectionView](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview))  
---|---  
[CanAddNew](P_Tessa_UI_Data_TreeCollectionView_CanAddNew.htm)|  
[CanCancelEdit](P_Tessa_UI_Data_TreeCollectionView_CanCancelEdit.htm)|  
[CanFilter](P_Tessa_UI_Data_TreeCollectionView_CanFilter.htm)|  
(Переопределяет
[CollectionView.CanFilter](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.canfilter#system-
windows-data-collectionview-canfilter))  
[CanGroup](P_Tessa_UI_Data_TreeCollectionView_CanGroup.htm)|  
(Переопределяет
[CollectionView.CanGroup](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.cangroup#system-
windows-data-collectionview-cangroup))  
[CanRemove](P_Tessa_UI_Data_TreeCollectionView_CanRemove.htm)|  
[CanSort](P_Tessa_UI_Data_TreeCollectionView_CanSort.htm)|  
(Переопределяет
[CollectionView.CanSort](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.cansort#system-
windows-data-collectionview-cansort))  
[Comparer](P_Tessa_UI_Data_TreeCollectionView_Comparer.htm)|  
(Переопределяет
[CollectionView.Comparer](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.comparer#system-
windows-data-collectionview-comparer))  
[Count](P_Tessa_UI_Data_TreeCollectionView_Count.htm)|  
(Переопределяет
[CollectionView.Count](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.count#system-
windows-data-collectionview-count))  
[Culture](P_Tessa_UI_Data_TreeCollectionView_Culture.htm)|  
(Переопределяет
[CollectionView.Culture](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.culture#system-
windows-data-collectionview-culture))  
[CurrentAddItem](P_Tessa_UI_Data_TreeCollectionView_CurrentAddItem.htm)|  
[CurrentEditItem](P_Tessa_UI_Data_TreeCollectionView_CurrentEditItem.htm)|  
[CurrentItem](P_Tessa_UI_Data_TreeCollectionView_CurrentItem.htm)|  
(Переопределяет
[CollectionView.CurrentItem](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.currentitem#system-
windows-data-collectionview-currentitem))  
[CurrentPosition](P_Tessa_UI_Data_TreeCollectionView_CurrentPosition.htm)|  
(Переопределяет
[CollectionView.CurrentPosition](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.currentposition#system-
windows-data-collectionview-currentposition))  
[CustomSort](P_Tessa_UI_Data_TreeCollectionView_CustomSort.htm)|  
[Dispatcher](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject.dispatcher#system-
windows-threading-dispatcherobject-dispatcher)| Gets the
[Dispatcher](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcher)
this
[DispatcherObject](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject)
is associated with.  
(Унаследован от
[DispatcherObject](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject))  
[Filter](P_Tessa_UI_Data_TreeCollectionView_Filter.htm)|  
(Переопределяет
[CollectionView.Filter](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.filter#system-
windows-data-collectionview-filter))  
[GroupDescriptions](P_Tessa_UI_Data_TreeCollectionView_GroupDescriptions.htm)|  
(Переопределяет
[CollectionView.GroupDescriptions](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.groupdescriptions#system-
windows-data-collectionview-groupdescriptions))  
[Groups](P_Tessa_UI_Data_TreeCollectionView_Groups.htm)|  
(Переопределяет
[CollectionView.Groups](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.groups#system-
windows-data-collectionview-groups))  
[IsAddingNew](P_Tessa_UI_Data_TreeCollectionView_IsAddingNew.htm)|  
[IsCurrentAfterLast](P_Tessa_UI_Data_TreeCollectionView_IsCurrentAfterLast.htm)|  
(Переопределяет
[CollectionView.IsCurrentAfterLast](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.iscurrentafterlast#system-
windows-data-collectionview-iscurrentafterlast))  
[IsCurrentBeforeFirst](P_Tessa_UI_Data_TreeCollectionView_IsCurrentBeforeFirst.htm)|  
(Переопределяет
[CollectionView.IsCurrentBeforeFirst](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.iscurrentbeforefirst#system-
windows-data-collectionview-iscurrentbeforefirst))  
[IsCurrentInSync](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.iscurrentinsync#system-
windows-data-collectionview-iscurrentinsync)| Gets a value that indicates
whether the
[CurrentItem](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.currentitem#system-
windows-data-collectionview-currentitem) is at the
[CurrentPosition](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.currentposition#system-
windows-data-collectionview-currentposition).  
(Унаследован от
[CollectionView](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview))  
[IsDynamic](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.isdynamic#system-
windows-data-collectionview-isdynamic)| Gets a value that indicates whether
the underlying collection provides change notifications.  
(Унаследован от
[CollectionView](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview))  
[IsEditingItem](P_Tessa_UI_Data_TreeCollectionView_IsEditingItem.htm)|  
[IsEmpty](P_Tessa_UI_Data_TreeCollectionView_IsEmpty.htm)|  
(Переопределяет
[CollectionView.IsEmpty](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.isempty#system-
windows-data-collectionview-isempty))  
[IsInUse](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.isinuse#system-
windows-data-collectionview-isinuse)| Gets a value that indicates whether any
object is subscribing to the events of this
[CollectionView](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview).  
(Унаследован от
[CollectionView](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview))  
[IsRefreshDeferred](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.isrefreshdeferred#system-
windows-data-collectionview-isrefreshdeferred)| Gets a value that indicates
whether there is an outstanding
[DeferRefresh()](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.deferrefresh#system-
windows-data-collectionview-deferrefresh) in use.  
(Унаследован от
[CollectionView](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview))  
[NeedsRefresh](P_Tessa_UI_Data_TreeCollectionView_NeedsRefresh.htm)|  
(Переопределяет
[CollectionView.NeedsRefresh](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.needsrefresh#system-
windows-data-collectionview-needsrefresh))  
[NewItemPlaceholderPosition](P_Tessa_UI_Data_TreeCollectionView_NewItemPlaceholderPosition.htm)|  
[SortDescriptions](P_Tessa_UI_Data_TreeCollectionView_SortDescriptions.htm)|  
(Переопределяет
[CollectionView.SortDescriptions](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.sortdescriptions#system-
windows-data-collectionview-sortdescriptions))  
[SourceCollection](P_Tessa_UI_Data_TreeCollectionView_SourceCollection.htm)|  
(Переопределяет
[CollectionView.SourceCollection](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.sourcecollection#system-
windows-data-collectionview-sourcecollection))  
[UpdatedOutsideDispatcher](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.updatedoutsidedispatcher#system-
windows-data-collectionview-updatedoutsidedispatcher)| Gets a value that
indicates whether it has been necessary to update the change log because a
[CollectionChanged](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.collectionchanged)
notification has been received on a different thread without first entering
the user interface (UI) thread dispatcher.  
(Унаследован от
[CollectionView](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview))  
##  __Методы
[AddNew](M_Tessa_UI_Data_TreeCollectionView_AddNew.htm)|  
---|---  
[CancelEdit](M_Tessa_UI_Data_TreeCollectionView_CancelEdit.htm)|  
[CancelNew](M_Tessa_UI_Data_TreeCollectionView_CancelNew.htm)|  
[CheckAccess](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject.checkaccess#system-
windows-threading-dispatcherobject-checkaccess)| Determines whether the
calling thread has access to this
[DispatcherObject](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject).  
(Унаследован от
[DispatcherObject](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject))  
[ClearChangeLog](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.clearchangelog#system-
windows-data-collectionview-clearchangelog)| Clears any pending changes from
the change log.  
(Унаследован от
[CollectionView](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview))  
Устарело.  
[ClearPendingChanges](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.clearpendingchanges#system-
windows-data-collectionview-clearpendingchanges)| Clears unprocessed changed
to the collection.  
(Унаследован от
[CollectionView](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview))  
[CommitEdit](M_Tessa_UI_Data_TreeCollectionView_CommitEdit.htm)|  
[CommitNew](M_Tessa_UI_Data_TreeCollectionView_CommitNew.htm)|  
[Contains](M_Tessa_UI_Data_TreeCollectionView_Contains.htm)|  
(Переопределяет
[CollectionView.Contains(Object)](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.contains#system-
windows-data-collectionview-contains\(system-object\)))  
[DeferRefresh](M_Tessa_UI_Data_TreeCollectionView_DeferRefresh.htm)|  
(Переопределяет
[CollectionView.DeferRefresh()](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.deferrefresh#system-
windows-data-collectionview-deferrefresh))  
[DetachFromSourceCollection](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.detachfromsourcecollection#system-
windows-data-collectionview-detachfromsourcecollection)| Removes the reference
to the underlying collection from the
[CollectionView](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview).  
(Унаследован от
[CollectionView](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview))  
[EditItem](M_Tessa_UI_Data_TreeCollectionView_EditItem.htm)|  
[GetEnumerator](M_Tessa_UI_Data_TreeCollectionView_GetEnumerator.htm)|  
(Переопределяет
[CollectionView.GetEnumerator()](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.getenumerator#system-
windows-data-collectionview-getenumerator))  
[GetItemAt](M_Tessa_UI_Data_TreeCollectionView_GetItemAt.htm)|  
(Переопределяет
[CollectionView.GetItemAt(Int32)](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.getitemat#system-
windows-data-collectionview-getitemat\(system-int32\)))  
[IndexOf](M_Tessa_UI_Data_TreeCollectionView_IndexOf.htm)|  
(Переопределяет
[CollectionView.IndexOf(Object)](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.indexof#system-
windows-data-collectionview-indexof\(system-object\)))  
[MoveCurrentTo](M_Tessa_UI_Data_TreeCollectionView_MoveCurrentTo.htm)|  
(Переопределяет
[CollectionView.MoveCurrentTo(Object)](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.movecurrentto#system-
windows-data-collectionview-movecurrentto\(system-object\)))  
[MoveCurrentToFirst](M_Tessa_UI_Data_TreeCollectionView_MoveCurrentToFirst.htm)|  
(Переопределяет
[CollectionView.MoveCurrentToFirst()](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.movecurrenttofirst#system-
windows-data-collectionview-movecurrenttofirst))  
[MoveCurrentToLast](M_Tessa_UI_Data_TreeCollectionView_MoveCurrentToLast.htm)|  
(Переопределяет
[CollectionView.MoveCurrentToLast()](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.movecurrenttolast#system-
windows-data-collectionview-movecurrenttolast))  
[MoveCurrentToNext](M_Tessa_UI_Data_TreeCollectionView_MoveCurrentToNext.htm)|  
(Переопределяет
[CollectionView.MoveCurrentToNext()](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.movecurrenttonext#system-
windows-data-collectionview-movecurrenttonext))  
[MoveCurrentToPosition](M_Tessa_UI_Data_TreeCollectionView_MoveCurrentToPosition.htm)|  
(Переопределяет
[CollectionView.MoveCurrentToPosition(Int32)](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.movecurrenttoposition#system-
windows-data-collectionview-movecurrenttoposition\(system-int32\)))  
[MoveCurrentToPrevious](M_Tessa_UI_Data_TreeCollectionView_MoveCurrentToPrevious.htm)|  
(Переопределяет
[CollectionView.MoveCurrentToPrevious()](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.movecurrenttoprevious#system-
windows-data-collectionview-movecurrenttoprevious))  
[OKToChangeCurrent](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.oktochangecurrent#system-
windows-data-collectionview-oktochangecurrent)| Returns a value that indicates
whether the view can change which item is the
[CurrentItem](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.currentitem#system-
windows-data-collectionview-currentitem).  
(Унаследован от
[CollectionView](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview))  
[OnAllowsCrossThreadChangesChanged](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.onallowscrossthreadchangeschanged#system-
windows-data-collectionview-onallowscrossthreadchangeschanged)| Occurs when
the
[AllowsCrossThreadChanges](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.allowscrossthreadchanges#system-
windows-data-collectionview-allowscrossthreadchanges) property changes.  
(Унаследован от
[CollectionView](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview))  
[OnBeginChangeLogging](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.onbeginchangelogging#system-
windows-data-collectionview-onbeginchangelogging\(system-collections-
specialized-notifycollectionchangedeventargs\))| Called by the base class to
notify the derived class that an
[CollectionChanged](https://learn.microsoft.com/dotnet/api/system.collections.specialized.inotifycollectionchanged.collectionchanged)
event has been posted to the message queue.  
(Унаследован от
[CollectionView](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview))  
Устарело.  
[OnCollectionChanged(NotifyCollectionChangedEventArgs)](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.oncollectionchanged#system-
windows-data-collectionview-oncollectionchanged\(system-collections-
specialized-notifycollectionchangedeventargs\))| Raises the
[CollectionChanged](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.collectionchanged)
event.  
(Унаследован от
[CollectionView](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview))  
[OnCollectionChanged(Object,
NotifyCollectionChangedEventArgs)](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.oncollectionchanged#system-
windows-data-collectionview-oncollectionchanged\(system-object-system-
collections-specialized-notifycollectionchangedeventargs\))| Raises the
[CollectionChanged](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.collectionchanged)
event.  
(Унаследован от
[CollectionView](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview))  
[OnCurrentChanged](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.oncurrentchanged#system-
windows-data-collectionview-oncurrentchanged)| Raises the
[CurrentChanged](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.currentchanged)
event.  
(Унаследован от
[CollectionView](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview))  
[OnCurrentChanging()](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.oncurrentchanging#system-
windows-data-collectionview-oncurrentchanging)| Raises a
[CurrentChanging](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.currentchanging)
event that is not cancelable.  
(Унаследован от
[CollectionView](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview))  
[OnCurrentChanging(CurrentChangingEventArgs)](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.oncurrentchanging#system-
windows-data-collectionview-oncurrentchanging\(system-componentmodel-
currentchangingeventargs\))| Raises the
[CurrentChanging](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.currentchanging)
event with the specified arguments.  
(Унаследован от
[CollectionView](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview))  
[OnPropertyChanged](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.onpropertychanged#system-
windows-data-collectionview-onpropertychanged\(system-componentmodel-
propertychangedeventargs\))| Raises the
[PropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged.propertychanged)
event using the specified arguments.  
(Унаследован от
[CollectionView](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview))  
[PassesFilter](M_Tessa_UI_Data_TreeCollectionView_PassesFilter.htm)|  
(Переопределяет
[CollectionView.PassesFilter(Object)](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.passesfilter#system-
windows-data-collectionview-passesfilter\(system-object\)))  
[ProcessCollectionChanged](M_Tessa_UI_Data_TreeCollectionView_ProcessCollectionChanged.htm)|  
(Переопределяет
[CollectionView.ProcessCollectionChanged(NotifyCollectionChangedEventArgs)](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.processcollectionchanged#system-
windows-data-collectionview-processcollectionchanged\(system-collections-
specialized-notifycollectionchangedeventargs\)))  
[ProcessPendingChanges](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.processpendingchanges#system-
windows-data-collectionview-processpendingchanges)| Ensures that all pending
changes to the collection have been committed.  
(Унаследован от
[CollectionView](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview))  
[Refresh](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.refresh#system-
windows-data-collectionview-refresh)| Re-creates the view.  
(Унаследован от
[CollectionView](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview))  
[RefreshOrDefer](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.refreshordefer#system-
windows-data-collectionview-refreshordefer)| Refreshes the view or specifies
that the view needs to be refreshed when the defer cycle completes.  
(Унаследован от
[CollectionView](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview))  
[RefreshOverride](M_Tessa_UI_Data_TreeCollectionView_RefreshOverride.htm)|  
(Переопределяет
[CollectionView.RefreshOverride()](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.refreshoverride#system-
windows-data-collectionview-refreshoverride))  
[Remove](M_Tessa_UI_Data_TreeCollectionView_Remove.htm)|  
[RemoveAt](M_Tessa_UI_Data_TreeCollectionView_RemoveAt.htm)|  
[SetCurrent(Object,
Int32)](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.setcurrent#system-
windows-data-collectionview-setcurrent\(system-object-system-int32\))| Sets
the specified item and index as the values of the
[CurrentItem](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.currentitem#system-
windows-data-collectionview-currentitem) and
[CurrentPosition](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.currentposition#system-
windows-data-collectionview-currentposition) properties.  
(Унаследован от
[CollectionView](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview))  
[SetCurrent(Object, Int32,
Int32)](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.setcurrent#system-
windows-data-collectionview-setcurrent\(system-object-system-int32-system-
int32\))| Sets the specified item and index as the values of the
[CurrentItem](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.currentitem#system-
windows-data-collectionview-currentitem) and
[CurrentPosition](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.currentposition#system-
windows-data-collectionview-currentposition) properties. This method can be
called from a constructor of a derived class.  
(Унаследован от
[CollectionView](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview))  
[VerifyAccess](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject.verifyaccess#system-
windows-threading-dispatcherobject-verifyaccess)| Enforces that the calling
thread has access to this
[DispatcherObject](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject).  
(Унаследован от
[DispatcherObject](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject))  
##  __События
[CollectionChanged](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.collectionchanged)|
Occurs when the view has changed.  
(Унаследован от
[CollectionView](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview))  
---|---  
[CurrentChanged](E_Tessa_UI_Data_TreeCollectionView_CurrentChanged.htm)|  
[CurrentChanging](E_Tessa_UI_Data_TreeCollectionView_CurrentChanging.htm)|  
(Переопределяет
[CollectionView.CurrentChanging](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.currentchanging))  
[PropertyChanged](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview.propertychanged)|
Occurs when a property value has changed.  
(Унаследован от
[CollectionView](https://learn.microsoft.com/dotnet/api/system.windows.data.collectionview))  
##  __См. также
#### Ссылки
[Tessa.UI.Data - пространство имён](N_Tessa_UI_Data.htm)
