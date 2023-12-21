# NotificationUIObject - класс
Объект, уведомляющий об изменении свойств посредством реализации интерфейса
[INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged),
причём события об изменениях свойств могут асинхронно пробрасываться в поток
UI.
## __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class NotificationUIObject : NotificationObject
VB __Копировать
     Public MustInherit Class NotificationUIObject
    	Inherits NotificationObject
C++ __Копировать
     public ref class NotificationUIObject abstract : public NotificationObject
F# __Копировать
     [<AbstractClassAttribute>]
    type NotificationUIObject = 
        class
            inherit NotificationObject
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[NotificationObject](T_Tessa_Platform_NotificationObject.htm) __ NotificationUIObject
Derived
[Tessa.UI.Cards.CardModel](T_Tessa_UI_Cards_CardModel.htm)
[Tessa.UI.Cards.CardToolbarViewModel](T_Tessa_UI_Cards_CardToolbarViewModel.htm)
[Tessa.UI.Cards.Controls.CardCellViewModel](T_Tessa_UI_Cards_Controls_CardCellViewModel.htm)
[Tessa.UI.Cards.Controls.EditNumeratorDialogViewModel](T_Tessa_UI_Cards_Controls_EditNumeratorDialogViewModel.htm)
[Tessa.UI.Cards.Editors.PropertyGridEnumItem](T_Tessa_UI_Cards_Editors_PropertyGridEnumItem.htm)
[Tessa.UI.Cards.Editors.PropertyGridItemViewModel](T_Tessa_UI_Cards_Editors_PropertyGridItemViewModel.htm)
[Tessa.UI.Cards.EditorViewModelBase](T_Tessa_UI_Cards_EditorViewModelBase.htm)
[Tessa.UI.Cards.Models.CardLibraryModel](T_Tessa_UI_Cards_Models_CardLibraryModel.htm)
[Tessa.UI.Cards.Models.CardStorageViewModel](T_Tessa_UI_Cards_Models_CardStorageViewModel.htm)
[Tessa.UI.Cards.Models.CardTaskNotificationViewModel](T_Tessa_UI_Cards_Models_CardTaskNotificationViewModel.htm)
[Tessa.UI.Cards.Tasks.TaskActionViewModel](T_Tessa_UI_Cards_Tasks_TaskActionViewModel.htm)
[Tessa.UI.Cards.Tasks.TaskAdditionalActionViewModel](T_Tessa_UI_Cards_Tasks_TaskAdditionalActionViewModel.htm)
[Tessa.UI.Cards.Tasks.TaskHistoryTagViewModel](T_Tessa_UI_Cards_Tasks_TaskHistoryTagViewModel.htm)
[Tessa.UI.Cards.Tasks.TaskItemViewModel](T_Tessa_UI_Cards_Tasks_TaskItemViewModel.htm)
[Tessa.UI.Cards.Tasks.TaskLinkViewModel](T_Tessa_UI_Cards_Tasks_TaskLinkViewModel.htm)
[Tessa.UI.Cards.Tasks.TaskSeparatorActionViewModel](T_Tessa_UI_Cards_Tasks_TaskSeparatorActionViewModel.htm)
[Tessa.UI.Cards.Tasks.TaskTagViewModel](T_Tessa_UI_Cards_Tasks_TaskTagViewModel.htm)
[Tessa.UI.Cards.TextStyleViewModel](T_Tessa_UI_Cards_TextStyleViewModel.htm)
[Tessa.UI.IconViewModel](T_Tessa_UI_IconViewModel.htm)
[Tessa.UI.SupportUnloadingViewModel](T_Tessa_UI_SupportUnloadingViewModel.htm)
[Tessa.UI.ViewModel<TModel>](T_Tessa_UI_ViewModel_1.htm)
[Tessa.UI.WorkspaceModel](T_Tessa_UI_WorkspaceModel.htm)
Подробнее __Less __
##  __Конструкторы
[NotificationUIObject](M_Tessa_UI_NotificationUIObject__ctor.htm)|
Инициализирует новый экземпляр класса NotificationUIObject  
---|---  
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
(Переопределяет
[NotificationObject.OnPropertyChangedAsync(PropertyChangedEventArgs,
Boolean)](M_Tessa_Platform_NotificationObject_OnPropertyChangedAsync.htm))  
[OnPropertyChangedAsync(String,
Boolean)](M_Tessa_Platform_NotificationObject_OnPropertyChangedAsync_1.htm)|
Уведомляет об изменении свойства с заданным именем у объекта асинхронно, в
соответствии с принятым для текущего объекта поведением. Если есть возможность
вызвать событие синхронно, то оно вызывается синхронно. Если объект является
моделью представления WPF и текущий поток отличен от потока диспетчера WPF для
приложения (основной поток UI), то выполнение асинхронно переключается в этот
поток. Если это не так, то событие выполняется синхронно.  
(Унаследован от [NotificationObject](T_Tessa_Platform_NotificationObject.htm))  
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
