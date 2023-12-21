# TessaShell - класс
Объект, замещающий окно приложения в контейнере Unity. Не выполняет других
действий. Может использоваться для передачи настроек в метод, возвращаемый
функцией
[TargetProxyFuncAsync](P_Tessa_UI_Windows_TessaShell_TargetProxyFuncAsync.htm).
## __Definition
 **Пространство имён:** [Tessa.UI.Windows](N_Tessa_UI_Windows.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class TessaShell : NotificationObject, 
    	ITessaShell, INotifyPropertyChanged
VB __Копировать
     Public NotInheritable Class TessaShell
    	Inherits NotificationObject
    	Implements ITessaShell, INotifyPropertyChanged
C++ __Копировать
     public ref class TessaShell sealed : public NotificationObject, 
    	ITessaShell, INotifyPropertyChanged
F# __Копировать
     [<SealedAttribute>]
    type TessaShell = 
        class
            inherit NotificationObject
            interface ITessaShell
            interface INotifyPropertyChanged
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[NotificationObject](T_Tessa_Platform_NotificationObject.htm) __ TessaShell
Implements
    [INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged), [ITessaShell](T_Tessa_UI_Windows_ITessaShell.htm)
##  __Конструкторы
[TessaShell](M_Tessa_UI_Windows_TessaShell__ctor.htm)| Инициализирует новый
экземпляр класса TessaShell  
---|---  
##  __Свойства
[SelectedTab](P_Tessa_UI_Windows_TessaShell_SelectedTab.htm)|  Вкладка из
списка [Tessa.UI.Windows.ITessaShell.SelectedTab], активная в настоящий
момент, или null, если активная вкладка отсутствует (обычно в случае, когда
вкладок нет).  
---|---  
[Settings](P_Tessa_UI_Windows_TessaShell_Settings.htm)|  Последние настройки
приложения, которые были применены, или null, если настройки ещё не были
применены.  
[Tabs](P_Tessa_UI_Windows_TessaShell_Tabs.htm)| Вкладки приложения, открытые в
настоящий момент.  
[TargetProxyFuncAsync](P_Tessa_UI_Windows_TessaShell_TargetProxyFuncAsync.htm)|
Асинхронная функция, возвращающая объект, для которого применяются настройки
боковых панелей помимо текущего объекта, или null, если такой объект не задан
(при этом возвращаемая асинхронная задача не равна null). Параметром принимает
объект, посредством которого можно отменить асинхронную задачу.  
## __Методы
[ApplySettingsAsync](M_Tessa_UI_Windows_TessaShell_ApplySettingsAsync.htm)|
Применяет заданные настройки приложения.  
---|---  
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
[SettingsApplied](E_Tessa_UI_Windows_TessaShell_SettingsApplied.htm)| Событие,
возникающее после применения настроек.  
##  __Поля
[SelectedTabProperty](F_Tessa_UI_Windows_TessaShell_SelectedTabProperty.htm)|
Имя свойства [SelectedTab](P_Tessa_UI_Windows_TessaShell_SelectedTab.htm).  
---|---  
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
[Tessa.UI.Windows - пространство имён](N_Tessa_UI_Windows.htm)
