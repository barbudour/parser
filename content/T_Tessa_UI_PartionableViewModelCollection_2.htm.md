# PartionableViewModelCollection<TItemModel, TItemViewModel> \- класс
##  __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class PartionableViewModelCollection<TItemModel, TItemViewModel> : ViewModelCollection<TItemModel, TItemViewModel>
    where TItemModel : class
    where TItemViewModel : ViewModel<TItemModel>
VB __Копировать
     Public MustInherit Class PartionableViewModelCollection(Of TItemModel As Class, TItemViewModel As ViewModel(Of TItemModel))
    	Inherits ViewModelCollection(Of TItemModel, TItemViewModel)
C++ __Копировать
    generic<typename TItemModel, typename TItemViewModel>
    where TItemModel : ref class
    where TItemViewModel : ViewModel<TItemModel>
    public ref class PartionableViewModelCollection abstract : public ViewModelCollection<TItemModel, TItemViewModel>
F# __Копировать
     [<AbstractClassAttribute>]
    type PartionableViewModelCollection<'TItemModel, 'TItemViewModel when 'TItemModel : not struct when 'TItemViewModel : ViewModel<'TItemModel>> = 
        class
            inherit ViewModelCollection<'TItemModel, 'TItemViewModel>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ViewModelCollection](T_Tessa_UI_ViewModelCollection_2.htm)<TItemModel, TItemViewModel> __ PartionableViewModelCollection<TItemModel, TItemViewModel>
Derived
[Tessa.UI.FilterableViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_FilterableViewModelCollection_2.htm)
[Tessa.UI.PageableViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_PageableViewModelCollection_2.htm)
#### Параметры типа
TItemModel
TItemViewModel
##  __Конструкторы
[PartionableViewModelCollection<TItemModel,
TItemViewModel>(ViewModelCollection<TItemModel,
TItemViewModel>)](M_Tessa_UI_PartionableViewModelCollection_2__ctor_2.htm)|
Инициализирует новый экземпляр класса
PartionableViewModelCollection<TItemModel, TItemViewModel>  
---|---  
[PartionableViewModelCollection<TItemModel, TItemViewModel>(IList<TItemModel>,
ViewModelScope)](M_Tessa_UI_PartionableViewModelCollection_2__ctor.htm)|
Инициализирует новый экземпляр класса
PartionableViewModelCollection<TItemModel, TItemViewModel>  
[PartionableViewModelCollection<TItemModel,
TItemViewModel>(ViewModelCollection<TItemModel, TItemViewModel>,
Boolean)](M_Tessa_UI_PartionableViewModelCollection_2__ctor_3.htm)|
Инициализирует новый экземпляр класса
PartionableViewModelCollection<TItemModel, TItemViewModel>  
[PartionableViewModelCollection<TItemModel, TItemViewModel>(IList<TItemModel>,
ViewModelScope,
Boolean)](M_Tessa_UI_PartionableViewModelCollection_2__ctor_1.htm)|
Инициализирует новый экземпляр класса
PartionableViewModelCollection<TItemModel, TItemViewModel>  
##  __Свойства
[Count](P_Tessa_UI_ViewModelCollection_2_Count.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
---|---  
[IsInitialized](P_Tessa_UI_ViewModelCollection_2_IsInitialized.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[IsReadOnly](P_Tessa_UI_ViewModelCollection_2_IsReadOnly.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[Item](P_Tessa_UI_ViewModelCollection_2_Item.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[Items](P_Tessa_UI_ViewModelCollection_2_Items.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[Model](P_Tessa_UI_ViewModelCollection_2_Model.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[ParentViewModel](P_Tessa_UI_ViewModelCollection_2_ParentViewModel.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[Scope](P_Tessa_UI_ViewModelCollection_2_Scope.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
##  __Методы
[Add](M_Tessa_UI_ViewModelCollection_2_Add.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
---|---  
[Clear](M_Tessa_UI_ViewModelCollection_2_Clear.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[ClearItems](M_Tessa_UI_ViewModelCollection_2_ClearItems.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[Contains](M_Tessa_UI_ViewModelCollection_2_Contains.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[CopyTo](M_Tessa_UI_ViewModelCollection_2_CopyTo.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
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
[GetEnumerator](M_Tessa_UI_ViewModelCollection_2_GetEnumerator.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetItemModel](M_Tessa_UI_ViewModelCollection_2_GetItemModel.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[GetItemModelCore](M_Tessa_UI_ViewModelCollection_2_GetItemModelCore.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[GetItemViewModel](M_Tessa_UI_ViewModelCollection_2_GetItemViewModel.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[GetItemViewModelCore](M_Tessa_UI_ViewModelCollection_2_GetItemViewModelCore.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[IndexOf](M_Tessa_UI_ViewModelCollection_2_IndexOf.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[Initialize](M_Tessa_UI_ViewModelCollection_2_Initialize.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[Insert](M_Tessa_UI_ViewModelCollection_2_Insert.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[InsertItem](M_Tessa_UI_ViewModelCollection_2_InsertItem.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Move](M_Tessa_UI_ViewModelCollection_2_Move.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[MoveItem](M_Tessa_UI_ViewModelCollection_2_MoveItem.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[OnCollectionChanged](M_Tessa_UI_ViewModelCollection_2_OnCollectionChanged.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[OnItemHidding](M_Tessa_UI_PartionableViewModelCollection_2_OnItemHidding.htm)|  
[OnItemShown](M_Tessa_UI_PartionableViewModelCollection_2_OnItemShown.htm)|  
[OnPropertyChanged(PropertyChangedEventArgs)](M_Tessa_UI_ViewModelCollection_2_OnPropertyChanged.htm)|
Уведомляет об изменении свойства с именем, заданным в аргументах события.  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[OnPropertyChanged(String)](M_Tessa_UI_ViewModelCollection_2_OnPropertyChanged_1.htm)|
Уведомляет об изменении свойства с заданным именем у объекта.  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[OnPropertyChangedAsync(PropertyChangedEventArgs)](M_Tessa_UI_ViewModelCollection_2_OnPropertyChangedAsync.htm)|
Уведомляет об изменении свойства с именем, заданным в аргументах события,
асинхронно, в соответствии с принятым для текущего объекта поведением. Если
есть возможность вызвать событие синхронно, то оно вызывается синхронно. Если
объект является моделью представления WPF и текущий поток отличен от потока
диспетчера WPF для приложения (основной поток UI), то выполнение асинхронно
переключается в этот поток. Если это не так, то событие выполняется синхронно.  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[OnPropertyChangedAsync(String)](M_Tessa_UI_ViewModelCollection_2_OnPropertyChangedAsync_1.htm)|
Уведомляет об изменении свойства с заданным именем у объекта асинхронно, в
соответствии с принятым для текущего объекта поведением. Если есть возможность
вызвать событие синхронно, то оно вызывается синхронно. Если объект является
моделью представления WPF и текущий поток отличен от потока диспетчера WPF для
приложения (основной поток UI), то выполнение асинхронно переключается в этот
поток. Если это не так, то событие выполняется синхронно.  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[OnReceiveWeakEvent](M_Tessa_UI_ViewModelCollection_2_OnReceiveWeakEvent.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[OnSourceItemInserted](M_Tessa_UI_PartionableViewModelCollection_2_OnSourceItemInserted.htm)|  
(Переопределяет [ViewModelCollection<TItemModel,
TItemViewModel>.OnSourceItemInserted(Int32,
TItemViewModel)](M_Tessa_UI_ViewModelCollection_2_OnSourceItemInserted.htm))  
[OnSourceItemMoved](M_Tessa_UI_PartionableViewModelCollection_2_OnSourceItemMoved.htm)|  
(Переопределяет [ViewModelCollection<TItemModel,
TItemViewModel>.OnSourceItemMoved(Int32, Int32,
TItemViewModel)](M_Tessa_UI_ViewModelCollection_2_OnSourceItemMoved.htm))  
[OnSourceItemRemoved](M_Tessa_UI_PartionableViewModelCollection_2_OnSourceItemRemoved.htm)|  
(Переопределяет [ViewModelCollection<TItemModel,
TItemViewModel>.OnSourceItemRemoved(Int32,
TItemViewModel)](M_Tessa_UI_ViewModelCollection_2_OnSourceItemRemoved.htm))  
[OnSourceItemReplaced](M_Tessa_UI_PartionableViewModelCollection_2_OnSourceItemReplaced.htm)|  
(Переопределяет [ViewModelCollection<TItemModel,
TItemViewModel>.OnSourceItemReplaced(Int32, TItemViewModel,
TItemViewModel)](M_Tessa_UI_ViewModelCollection_2_OnSourceItemReplaced.htm))  
[OnSourceItemsResetted](M_Tessa_UI_PartionableViewModelCollection_2_OnSourceItemsResetted.htm)|  
(Переопределяет [ViewModelCollection<TItemModel,
TItemViewModel>.OnSourceItemsResetted()](M_Tessa_UI_ViewModelCollection_2_OnSourceItemsResetted.htm))  
[Remove](M_Tessa_UI_ViewModelCollection_2_Remove.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[RemoveAt](M_Tessa_UI_ViewModelCollection_2_RemoveAt.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[RemoveItem](M_Tessa_UI_ViewModelCollection_2_RemoveItem.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[ReplaceItem](M_Tessa_UI_ViewModelCollection_2_ReplaceItem.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TranslateBaseIndex](M_Tessa_UI_PartionableViewModelCollection_2_TranslateBaseIndex.htm)|  
## __События
[CollectionChanged](E_Tessa_UI_ViewModelCollection_2_CollectionChanged.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
---|---  
[PropertyChanged](E_Tessa_UI_ViewModelCollection_2_PropertyChanged.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.UI - пространство имён](N_Tessa_UI.htm)
