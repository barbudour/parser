# ClientQuickSearchViewModel - класс
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.UI](N_Tessa_Extensions_Platform_Client_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public class ClientQuickSearchViewModel : UIElementBase
VB __Копировать
     Public Class ClientQuickSearchViewModel
    	Inherits UIElementBase
C++ __Копировать
     public ref class ClientQuickSearchViewModel : public UIElementBase
F# __Копировать
     type ClientQuickSearchViewModel = 
        class
            inherit UIElementBase
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[NotificationObject](T_Tessa_Platform_NotificationObject.htm) __[UIElementBase](T_Tessa_UI_UIElementBase.htm) __ ClientQuickSearchViewModel
##  __Конструкторы
[ClientQuickSearchViewModel](M_Tessa_Extensions_Platform_Client_UI_ClientQuickSearchViewModel__ctor.htm)|
Инициализирует новый экземпляр класса ClientQuickSearchViewModel  
---|---  
##  __Свойства
[ClearSearchCommand](P_Tessa_Extensions_Platform_Client_UI_ClientQuickSearchViewModel_ClearSearchCommand.htm)|
Gets Команда очистки строки поиска  
---|---  
[Focusable](P_Tessa_Extensions_Platform_Client_UI_ClientQuickSearchViewModel_Focusable.htm)|
Признак того, что элемент управления может иметь логический фокус.  
(Переопределяет
[UIElementBase.Focusable](P_Tessa_UI_UIElementBase_Focusable.htm))  
[FocusPending](P_Tessa_UI_UIElementBase_FocusPending.htm)|  Признак того, что
элемент управления получит логический фокус, как только станет доступен.  
(Унаследован от [UIElementBase](T_Tessa_UI_UIElementBase.htm))  
[IsEnabled](P_Tessa_UI_UIElementBase_IsEnabled.htm)|  Признак доступности
элемента для взаимодействия  
(Унаследован от [UIElementBase](T_Tessa_UI_UIElementBase.htm))  
[IsFocused](P_Tessa_UI_UIElementBase_IsFocused.htm)|  Признак того, что
элемент управления имеет логический фокус.  
(Унаследован от [UIElementBase](T_Tessa_UI_UIElementBase.htm))  
[IsVisible](P_Tessa_UI_UIElementBase_IsVisible.htm)|  Признак отображения
элемента в пользовательском интерфейса  
(Унаследован от [UIElementBase](T_Tessa_UI_UIElementBase.htm))  
[SearchText](P_Tessa_Extensions_Platform_Client_UI_ClientQuickSearchViewModel_SearchText.htm)|
Gets or sets Текст поиска  
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
(Унаследован от [UIElementBase](T_Tessa_UI_UIElementBase.htm))  
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
[Tessa.Extensions.Platform.Client.UI - пространство
имён](N_Tessa_Extensions_Platform_Client_UI.htm)
