# SelectableViewModel<TModel> \- класс
##  __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public class SelectableViewModel<TModel> : ViewModel<TModel>, 
    	ISelectableViewModel, IViewModel, INotifyPropertyChanged
VB __Копировать
     Public Class SelectableViewModel(Of TModel)
    	Inherits ViewModel(Of TModel)
    	Implements ISelectableViewModel, IViewModel, INotifyPropertyChanged
C++ __Копировать
    generic<typename TModel>
    public ref class SelectableViewModel : public ViewModel<TModel>, 
    	ISelectableViewModel, IViewModel, INotifyPropertyChanged
F# __Копировать
     type SelectableViewModel<'TModel> = 
        class
            inherit ViewModel<'TModel>
            interface ISelectableViewModel
            interface IViewModel
            interface INotifyPropertyChanged
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[NotificationObject](T_Tessa_Platform_NotificationObject.htm) __[NotificationUIObject](T_Tessa_UI_NotificationUIObject.htm) __[ViewModel](T_Tessa_UI_ViewModel_1.htm)<TModel> __ SelectableViewModel<TModel>
Derived
[Tessa.Extensions.Default.Client.Workplaces.Manager.ManagerWorkplaceTileViewModel](T_Tessa_Extensions_Default_Client_Workplaces_Manager_ManagerWorkplaceTileViewModel.htm)
[Tessa.UI.Cards.CardToolbarItem](T_Tessa_UI_Cards_CardToolbarItem.htm)
[Tessa.UI.Cards.Controls.CardRowViewModel](T_Tessa_UI_Cards_Controls_CardRowViewModel.htm)
[Tessa.UI.Cards.Editors.TabItemEditorViewModel](T_Tessa_UI_Cards_Editors_TabItemEditorViewModel.htm)
[Tessa.UI.Cards.Tasks.TaskHistoryItemViewModel](T_Tessa_UI_Cards_Tasks_TaskHistoryItemViewModel.htm)
[Tessa.UI.Controls.TessaGrid.RowViewModel](T_Tessa_UI_Controls_TessaGrid_RowViewModel.htm)
[Tessa.UI.Controls.TreeItemViewModel<TItemModel,
TItemViewModel>](T_Tessa_UI_Controls_TreeItemViewModel_2.htm)
[Tessa.UI.Files.Controls.FileVersionViewModel](T_Tessa_UI_Files_Controls_FileVersionViewModel.htm)
[Tessa.UI.Files.FileViewModel](T_Tessa_UI_Files_FileViewModel.htm)
[Tessa.UI.Menu.MenuAction](T_Tessa_UI_Menu_MenuAction.htm)
[Tessa.UI.Menu.MenuSeparatorAction](T_Tessa_UI_Menu_MenuSeparatorAction.htm)
[Tessa.UI.Scheme.Legacy.ObjectSelectableViewModel<TModel>](T_Tessa_UI_Scheme_Legacy_ObjectSelectableViewModel_1.htm)
[Tessa.UI.Scheme.ObjectViewModel<TModel>](T_Tessa_UI_Scheme_ObjectViewModel_1.htm)
[Tessa.UI.Views.Charting.Charts.ChartStructure.ChartStructureItem](T_Tessa_UI_Views_Charting_Charts_ChartStructure_ChartStructureItem.htm)
[Tessa.UI.Views.Content.TableCellViewModel](T_Tessa_UI_Views_Content_TableCellViewModel.htm)
[Tessa.UI.Views.TessaListViewHelper.ColumnRowViewModel](T_Tessa_UI_Views_TessaListViewHelper_ColumnRowViewModel.htm)
[Tessa.UI.Views.Workplaces.Tree.TreeItemBase<TTreeItem>](T_Tessa_UI_Views_Workplaces_Tree_TreeItemBase_1.htm)
Подробнее __Less __
Implements
    [INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged), [ISelectableViewModel](T_Tessa_UI_ISelectableViewModel.htm), [IViewModel](T_Tessa_UI_IViewModel.htm)
#### Параметры типа
TModel
##  __Конструкторы
[SelectableViewModel<TModel>()](M_Tessa_UI_SelectableViewModel_1__ctor.htm)|
Инициализирует новый экземпляр класса SelectableViewModel<TModel>  
---|---  
[SelectableViewModel<TModel>(TModel)](M_Tessa_UI_SelectableViewModel_1__ctor_2.htm)|
Инициализирует новый экземпляр класса SelectableViewModel<TModel>  
[SelectableViewModel<TModel>(ViewModelScope)](M_Tessa_UI_SelectableViewModel_1__ctor_1.htm)|
Инициализирует новый экземпляр класса SelectableViewModel<TModel>  
[SelectableViewModel<TModel>(TModel,
ViewModelScope)](M_Tessa_UI_SelectableViewModel_1__ctor_3.htm)| Инициализирует
новый экземпляр класса SelectableViewModel<TModel>  
##  __Свойства
[IsSelectable](P_Tessa_UI_SelectableViewModel_1_IsSelectable.htm)|  
---|---  
[IsSelected](P_Tessa_UI_SelectableViewModel_1_IsSelected.htm)|  
[Model](P_Tessa_UI_ViewModel_1_Model.htm)|  Модель для текущей модели
представления.  
(Унаследован от [ViewModel<TModel>](T_Tessa_UI_ViewModel_1.htm))  
[Scope](P_Tessa_UI_ViewModel_1_Scope.htm)|  
(Унаследован от [ViewModel<TModel>](T_Tessa_UI_ViewModel_1.htm))  
##  __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[OnIsSelectableChanged](M_Tessa_UI_SelectableViewModel_1_OnIsSelectableChanged.htm)|  
[OnIsSelectedChanged](M_Tessa_UI_SelectableViewModel_1_OnIsSelectedChanged.htm)|  
[OnModelPropertyChanged](M_Tessa_UI_ViewModel_1_OnModelPropertyChanged.htm)|  
(Унаследован от [ViewModel<TModel>](T_Tessa_UI_ViewModel_1.htm))  
[OnPropertyChanged(PropertyChangedEventArgs)](M_Tessa_Platform_NotificationObject_OnPropertyChanged.htm)|
Уведомляет об изменении свойства с именем, заданным в аргументах события.  
(Унаследован от [NotificationObject](T_Tessa_Platform_NotificationObject.htm))  
[OnPropertyChanged(String)](M_Tessa_Platform_NotificationObject_OnPropertyChanged_1.htm)|
Уведомляет об изменении свойства с заданным именем у объекта.  
(Унаследован от [NotificationObject](T_Tessa_Platform_NotificationObject.htm))  
[OnPropertyChangedAsync(PropertyChangedEventArgs,
Boolean)](M_Tessa_UI_NotificationUIObject_OnPropertyChangedAsync.htm)|
Уведомляет об изменении свойства с именем, заданным в аргументах события,
асинхронно, в соответствии с принятым для текущего объекта поведением. Если
есть возможность вызвать событие синхронно, то оно вызывается синхронно. Если
объект является моделью представления WPF и текущий поток отличен от потока
диспетчера WPF для приложения (основной поток UI), то выполнение асинхронно
переключается в этот поток. Если это не так, то событие выполняется синхронно.  
(Унаследован от [NotificationUIObject](T_Tessa_UI_NotificationUIObject.htm))  
[OnPropertyChangedAsync(String,
Boolean)](M_Tessa_Platform_NotificationObject_OnPropertyChangedAsync_1.htm)|
Уведомляет об изменении свойства с заданным именем у объекта асинхронно, в
соответствии с принятым для текущего объекта поведением. Если есть возможность
вызвать событие синхронно, то оно вызывается синхронно. Если объект является
моделью представления WPF и текущий поток отличен от потока диспетчера WPF для
приложения (основной поток UI), то выполнение асинхронно переключается в этот
поток. Если это не так, то событие выполняется синхронно.  
(Унаследован от [NotificationObject](T_Tessa_Platform_NotificationObject.htm))  
[OnReceiveWeakEvent](M_Tessa_UI_ViewModel_1_OnReceiveWeakEvent.htm)|  
(Унаследован от [ViewModel<TModel>](T_Tessa_UI_ViewModel_1.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __События
[PropertyChanged](E_Tessa_Platform_NotificationObject_PropertyChanged.htm)|
Событие, уведомляющее об изменении свойства с определённым именем у модели
представления.  
(Унаследован от [NotificationObject](T_Tessa_Platform_NotificationObject.htm))  
---|---  
##  __Поля
[IsSelectableProperty](F_Tessa_UI_SelectableViewModel_1_IsSelectableProperty.htm)|  
---|---  
[IsSelectedProperty](F_Tessa_UI_SelectableViewModel_1_IsSelectedProperty.htm)|  
## __Методы расширения
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
