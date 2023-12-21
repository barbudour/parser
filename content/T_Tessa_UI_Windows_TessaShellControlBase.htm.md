# TessaShellControlBase - класс
##  __Definition
 **Пространство имён:** [Tessa.UI.Windows](N_Tessa_UI_Windows.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class TessaShellControlBase : NotificationObject, 
    	ITessaShellControl, IAutomationBase, INotifyPropertyChanged
VB __Копировать
     Public MustInherit Class TessaShellControlBase
    	Inherits NotificationObject
    	Implements ITessaShellControl, IAutomationBase, INotifyPropertyChanged
C++ __Копировать
     public ref class TessaShellControlBase abstract : public NotificationObject, 
    	ITessaShellControl, IAutomationBase, INotifyPropertyChanged
F# __Копировать
     [<AbstractClassAttribute>]
    type TessaShellControlBase = 
        class
            inherit NotificationObject
            interface ITessaShellControl
            interface IAutomationBase
            interface INotifyPropertyChanged
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[NotificationObject](T_Tessa_Platform_NotificationObject.htm) __ TessaShellControlBase
Derived
[Tessa.UI.Windows.TessaShellButton](T_Tessa_UI_Windows_TessaShellButton.htm)
[Tessa.UI.Windows.TessaShellDropDownButton](T_Tessa_UI_Windows_TessaShellDropDownButton.htm)
[Tessa.UI.Windows.TessaShellSeparator](T_Tessa_UI_Windows_TessaShellSeparator.htm)
Implements
    [INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged), [IAutomationBase](T_Tessa_UI_Automation_IAutomationBase.htm), [ITessaShellControl](T_Tessa_UI_Windows_ITessaShellControl.htm)
##  __Конструкторы
[TessaShellControlBase](M_Tessa_UI_Windows_TessaShellControlBase__ctor.htm)|
Инициализирует новый экземпляр класса TessaShellControlBase  
---|---  
##  __Свойства
[AutomationId](P_Tessa_UI_Windows_TessaShellControlBase_AutomationId.htm)|
Уникальный идентификатор для автоматизации.  
---|---  
[AutomationName](P_Tessa_UI_Windows_TessaShellControlBase_AutomationName.htm)|
Имя для автоматизации.  
[IconGeometry](P_Tessa_UI_Windows_TessaShellControlBase_IconGeometry.htm)|  
[IconHeight](P_Tessa_UI_Windows_TessaShellControlBase_IconHeight.htm)|  
[IconWidth](P_Tessa_UI_Windows_TessaShellControlBase_IconWidth.htm)|  
[Padding](P_Tessa_UI_Windows_TessaShellControlBase_Padding.htm)|  
[StrokeThickness](P_Tessa_UI_Windows_TessaShellControlBase_StrokeThickness.htm)|  
[ToolTip](P_Tessa_UI_Windows_TessaShellControlBase_ToolTip.htm)|  
[Visibility](P_Tessa_UI_Windows_TessaShellControlBase_Visibility.htm)|  
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
[Tessa.UI.Windows - пространство имён](N_Tessa_UI_Windows.htm)
