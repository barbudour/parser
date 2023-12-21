# SupportUnloadingViewModel - класс
Базовый класс, реализующий интерфейс
[ISupportUnloading](T_Tessa_UI_ISupportUnloading.htm) и наследуемый от
[ViewModel<TModel>](T_Tessa_UI_ViewModel_1.htm).
## __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class SupportUnloadingViewModel : NotificationUIObject, 
    	ISupportUnloading
VB __Копировать
     Public MustInherit Class SupportUnloadingViewModel
    	Inherits NotificationUIObject
    	Implements ISupportUnloading
C++ __Копировать
     public ref class SupportUnloadingViewModel abstract : public NotificationUIObject, 
    	ISupportUnloading
F# __Копировать
     [<AbstractClassAttribute>]
    type SupportUnloadingViewModel = 
        class
            inherit NotificationUIObject
            interface ISupportUnloading
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[NotificationObject](T_Tessa_Platform_NotificationObject.htm) __[NotificationUIObject](T_Tessa_UI_NotificationUIObject.htm) __ SupportUnloadingViewModel
Derived
[Tessa.UI.Cards.Blocks.BlockViewModelBase](T_Tessa_UI_Cards_Blocks_BlockViewModelBase.htm)
[Tessa.UI.Cards.Controls.ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm)
[Tessa.UI.Cards.Tasks.TaskWorkspaceViewModel](T_Tessa_UI_Cards_Tasks_TaskWorkspaceViewModel.htm)
[Tessa.UI.Controls.AutoCompleteCtrl.AutoCompleteDataSource](T_Tessa_UI_Controls_AutoCompleteCtrl_AutoCompleteDataSource.htm)
[Tessa.UI.Files.FileControl](T_Tessa_UI_Files_FileControl.htm)
Implements
    [ISupportUnloading](T_Tessa_UI_ISupportUnloading.htm)
##  __Конструкторы
[SupportUnloadingViewModel](M_Tessa_UI_SupportUnloadingViewModel__ctor.htm)|
Инициализирует новый экземпляр класса SupportUnloadingViewModel  
---|---  
##  __Свойства
[IsUnloaded](P_Tessa_UI_SupportUnloadingViewModel_IsUnloaded.htm)|  Признак
того, что объект был выгружен и уже не может использоваться в UI. Например,
если объект является контролом карточки, то он становится выгруженным после
закрытия формы редактирования строки или пре рефреше карточки.  
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
[OnUnloadingAsync](M_Tessa_UI_SupportUnloadingViewModel_OnUnloadingAsync.htm)|
Метод вызывается в процессе выгрузки объекта и выполняет некоторую обработку,
например, отписывается от событий и выгружает дочерние объекты (например,
контролы в блоке). Исключения в процесс выполнения метода будут поглощены и
добавлены в лог.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[UnloadAsync](M_Tessa_UI_SupportUnloadingViewModel_UnloadAsync.htm)|
Выполняет выгрузку объекта. Если объект уже был выгружен, то повторная
выгрузка не выполняется.  
## __События
[PropertyChanged](E_Tessa_Platform_NotificationObject_PropertyChanged.htm)|
Событие, уведомляющее об изменении свойства с определённым именем у модели
представления.  
(Унаследован от [NotificationObject](T_Tessa_Platform_NotificationObject.htm))  
---|---  
[Unloaded](E_Tessa_UI_SupportUnloadingViewModel_Unloaded.htm)|  Событие,
возникающее после того, как объект был выгружен и уже не может использоваться
в UI. Если на некоторые свойства объекта, связанные с UI, выполнялась
подписка, то в обработчике события можно выполнить отписку, а также удалить
сам обработчик.  
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
[UnloadAsync](M_Tessa_UI_UIExtensions_UnloadAsync.htm)|  Выполняет выгрузку
объекта. Если объект уже был выгружен, то повторная выгрузка не выполняется.
Возвращает объект, содержащий сообщения, возникшие в процессе выгрузки, в т.ч.
ошибки.  
(Определяется [UIExtensions](T_Tessa_UI_UIExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.UI - пространство имён](N_Tessa_UI.htm)
