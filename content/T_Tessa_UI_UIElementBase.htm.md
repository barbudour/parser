# UIElementBase - класс
##  __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class UIElementBase : NotificationObject, 
    	IUIElement, INotifyPropertyChanged
VB __Копировать
     Public MustInherit Class UIElementBase
    	Inherits NotificationObject
    	Implements IUIElement, INotifyPropertyChanged
C++ __Копировать
     public ref class UIElementBase abstract : public NotificationObject, 
    	IUIElement, INotifyPropertyChanged
F# __Копировать
     [<AbstractClassAttribute>]
    type UIElementBase = 
        class
            inherit NotificationObject
            interface IUIElement
            interface INotifyPropertyChanged
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[NotificationObject](T_Tessa_Platform_NotificationObject.htm) __ UIElementBase
Derived
[Tessa.Extensions.Platform.Client.UI.ClientQuickSearchViewModel](T_Tessa_Extensions_Platform_Client_UI_ClientQuickSearchViewModel.htm)
[Tessa.UI.Cards.Controls.CommandViewModel<TCommandParameter>](T_Tessa_UI_Cards_Controls_CommandViewModel_1.htm)
[Tessa.UI.Cards.Controls.CurrentPageViewModel](T_Tessa_UI_Cards_Controls_CurrentPageViewModel.htm)
[Tessa.UI.Cards.Controls.FilterPresenter](T_Tessa_UI_Cards_Controls_FilterPresenter.htm)
[Tessa.UI.Cards.Controls.OptionalPagingButton](T_Tessa_UI_Cards_Controls_OptionalPagingButton.htm)
[Tessa.UI.Cards.Controls.QuickSearchViewModel](T_Tessa_UI_Cards_Controls_QuickSearchViewModel.htm)
[Tessa.UI.Cards.Controls.UIElementsViewModel](T_Tessa_UI_Cards_Controls_UIElementsViewModel.htm)
[Tessa.UI.Cards.Controls.ViewControl.ViewControlToolbarButtonViewModel](T_Tessa_UI_Cards_Controls_ViewControl_ViewControlToolbarButtonViewModel.htm)
Подробнее __Less __
Implements
    [INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged), [IUIElement](T_Tessa_UI_IUIElement.htm)
##  __Конструкторы
[UIElementBase](M_Tessa_UI_UIElementBase__ctor.htm)| Инициализирует новый
экземпляр класса UIElementBase  
---|---  
##  __Свойства
[Focusable](P_Tessa_UI_UIElementBase_Focusable.htm)|  Признак того, что
элемент управления может иметь логический фокус.  
---|---  
[FocusPending](P_Tessa_UI_UIElementBase_FocusPending.htm)|  Признак того, что
элемент управления получит логический фокус, как только станет доступен.  
[IsEnabled](P_Tessa_UI_UIElementBase_IsEnabled.htm)|  Признак доступности
элемента для взаимодействия  
[IsFocused](P_Tessa_UI_UIElementBase_IsFocused.htm)|  Признак того, что
элемент управления имеет логический фокус.  
[IsVisible](P_Tessa_UI_UIElementBase_IsVisible.htm)|  Признак отображения
элемента в пользовательском интерфейса  
## __Методы
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
[Focus](M_Tessa_UI_UIElementBase_Focus.htm)|  Устанавливает логический фокус
на элемент.  
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
Boolean)](M_Tessa_Platform_NotificationObject_OnPropertyChangedAsync.htm)|
Уведомляет об изменении свойства с именем, заданным в аргументах события,
асинхронно, в соответствии с принятым для текущего объекта поведением. Если
есть возможность вызвать событие синхронно, то оно вызывается синхронно. Если
объект является моделью представления WPF и текущий поток отличен от потока
диспетчера WPF для приложения (основной поток UI), то выполнение асинхронно
переключается в этот поток. Если это не так, то событие выполняется синхронно.  
(Унаследован от [NotificationObject](T_Tessa_Platform_NotificationObject.htm))  
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
