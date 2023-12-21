# NotificationObject - класс
Объект, уведомляющий об изменении свойств посредством реализации интерфейса
[INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged).
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class NotificationObject : INotifyPropertyChanged
VB __Копировать
     Public MustInherit Class NotificationObject
    	Implements INotifyPropertyChanged
C++ __Копировать
     public ref class NotificationObject abstract : INotifyPropertyChanged
F# __Копировать
     [<AbstractClassAttribute>]
    type NotificationObject = 
        class
            interface INotifyPropertyChanged
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ NotificationObject
Derived
[Tessa.Cards.CardModelSettings](T_Tessa_Cards_CardModelSettings.htm)
[Tessa.Extensions.Platform.Client.UI.TableViewExtension.MoveButtonBase](T_Tessa_Extensions_Platform_Client_UI_TableViewExtension_MoveButtonBase.htm)
[Tessa.Files.FileContainer](T_Tessa_Files_FileContainer.htm)
[Tessa.Files.FileContainerPermissions](T_Tessa_Files_FileContainerPermissions.htm)
[Tessa.Files.FileContent](T_Tessa_Files_FileContent.htm)
[Tessa.Files.FileEntity](T_Tessa_Files_FileEntity.htm)
[Tessa.Files.FilePermissions](T_Tessa_Files_FilePermissions.htm)
[Tessa.Files.FileSignatureData](T_Tessa_Files_FileSignatureData.htm)
[Tessa.Forums.ForumControlSettings](T_Tessa_Forums_ForumControlSettings.htm)
[Tessa.Themes.ThemeManager](T_Tessa_Themes_ThemeManager.htm)
[Tessa.UI.Cards.Controls.CardFilterViewModel](T_Tessa_UI_Cards_Controls_CardFilterViewModel.htm)
[Tessa.UI.Cards.RowContext](T_Tessa_UI_Cards_RowContext.htm)
[Tessa.UI.Cards.Tasks.TaskColorProvider](T_Tessa_UI_Cards_Tasks_TaskColorProvider.htm)
[Tessa.UI.Cards.Types.LazyDialogFormViewModel](T_Tessa_UI_Cards_Types_LazyDialogFormViewModel.htm)
[Tessa.UI.Controls.Forums.ForumControlLocalSettings](T_Tessa_UI_Controls_Forums_ForumControlLocalSettings.htm)
[Tessa.UI.Files.FileToolTip](T_Tessa_UI_Files_FileToolTip.htm)
[Tessa.UI.Files.PreviewPageOptions](T_Tessa_UI_Files_PreviewPageOptions.htm)
[Tessa.UI.Notifications.NotificationUISettings](T_Tessa_UI_Notifications_NotificationUISettings.htm)
[Tessa.UI.NotificationUIObject](T_Tessa_UI_NotificationUIObject.htm)
[Tessa.UI.Tiles.TilePanelContentSource](T_Tessa_UI_Tiles_TilePanelContentSource.htm)
[Tessa.UI.Tiles.TileSource](T_Tessa_UI_Tiles_TileSource.htm)
[Tessa.UI.Tiles.TileWorkspace](T_Tessa_UI_Tiles_TileWorkspace.htm)
[Tessa.UI.UIButton](T_Tessa_UI_UIButton.htm)
[Tessa.UI.UIElementBase](T_Tessa_UI_UIElementBase.htm)
[Tessa.UI.Windows.TessaShell](T_Tessa_UI_Windows_TessaShell.htm)
[Tessa.UI.Windows.TessaShellControlBase](T_Tessa_UI_Windows_TessaShellControlBase.htm)
[Tessa.UI.Windows.TessaShellPanel](T_Tessa_UI_Windows_TessaShellPanel.htm)
[Tessa.UI.Workflow.Bindings.WorkflowBindingSource](T_Tessa_UI_Workflow_Bindings_WorkflowBindingSource.htm)
[Tessa.UI.WorkflowViewer.Shapes.Annotation](T_Tessa_UI_WorkflowViewer_Shapes_Annotation.htm)
[Tessa.UI.WorkflowViewer.Shapes.Connection](T_Tessa_UI_WorkflowViewer_Shapes_Connection.htm)
[Tessa.UI.WorkflowViewer.Shapes.Node](T_Tessa_UI_WorkflowViewer_Shapes_Node.htm)
Подробнее __Less __
Implements
    [INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged)
##  __Конструкторы
[NotificationObject](M_Tessa_Platform_NotificationObject__ctor.htm)|
Инициализирует новый экземпляр класса NotificationObject  
---|---  
##  __Свойства
[DefaultPropertyChangedAsyncInvocator](P_Tessa_Platform_NotificationObject_DefaultPropertyChangedAsyncInvocator.htm)|
Объект, выполняющий обработку события для приложения по умолчанию. В desktop-
приложении будет обработка будет выполняться в потоке UI.  
---|---  
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
[OnPropertyChanged(String)](M_Tessa_Platform_NotificationObject_OnPropertyChanged_1.htm)|
Уведомляет об изменении свойства с заданным именем у объекта.  
[OnPropertyChangedAsync(PropertyChangedEventArgs,
Boolean)](M_Tessa_Platform_NotificationObject_OnPropertyChangedAsync.htm)|
Уведомляет об изменении свойства с именем, заданным в аргументах события,
асинхронно, в соответствии с принятым для текущего объекта поведением. Если
есть возможность вызвать событие синхронно, то оно вызывается синхронно. Если
объект является моделью представления WPF и текущий поток отличен от потока
диспетчера WPF для приложения (основной поток UI), то выполнение асинхронно
переключается в этот поток. Если это не так, то событие выполняется синхронно.  
[OnPropertyChangedAsync(String,
Boolean)](M_Tessa_Platform_NotificationObject_OnPropertyChangedAsync_1.htm)|
Уведомляет об изменении свойства с заданным именем у объекта асинхронно, в
соответствии с принятым для текущего объекта поведением. Если есть возможность
вызвать событие синхронно, то оно вызывается синхронно. Если объект является
моделью представления WPF и текущий поток отличен от потока диспетчера WPF для
приложения (основной поток UI), то выполнение асинхронно переключается в этот
поток. Если это не так, то событие выполняется синхронно.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __События
[PropertyChanged](E_Tessa_Platform_NotificationObject_PropertyChanged.htm)|
Событие, уведомляющее об изменении свойства с определённым именем у модели
представления.  
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
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
