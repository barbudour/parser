# WebChartColorPickerViewModel - класс
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Client.Workplaces.WebChart](N_Tessa_Extensions_Default_Client_Workplaces_WebChart.htm)  
 **Сборка:** Tessa.Extensions.Default.Client (в
Tessa.Extensions.Default.Client.dll) Версия: 3.6.0.17
C# __Копировать
     public class WebChartColorPickerViewModel : ViewModel<EmptyModel>
VB __Копировать
     Public Class WebChartColorPickerViewModel
    	Inherits ViewModel(Of EmptyModel)
C++ __Копировать
     public ref class WebChartColorPickerViewModel : public ViewModel<EmptyModel^>
F# __Копировать
     type WebChartColorPickerViewModel = 
        class
            inherit ViewModel<EmptyModel>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[NotificationObject](T_Tessa_Platform_NotificationObject.htm) __[NotificationUIObject](T_Tessa_UI_NotificationUIObject.htm) __[ViewModel](T_Tessa_UI_ViewModel_1.htm)<[EmptyModel](T_Tessa_UI_EmptyModel.htm)> __ WebChartColorPickerViewModel
##  __Конструкторы
[WebChartColorPickerViewModel](M_Tessa_Extensions_Default_Client_Workplaces_WebChart_WebChartColorPickerViewModel__ctor.htm)|
Создаёт экземпляр класса с указанием метаинформации по элементу управления и
модели карточки.  
---|---  
## __Свойства
[ClearColorCommand](P_Tessa_Extensions_Default_Client_Workplaces_WebChart_WebChartColorPickerViewModel_ClearColorCommand.htm)|
Команда, выполняемая при нажатии на кнопку очистки цвета.  
---|---  
[ClearColorCommandClosure](P_Tessa_Extensions_Default_Client_Workplaces_WebChart_WebChartColorPickerViewModel_ClearColorCommandClosure.htm)|
Замыкание для управления командой
[ClearColorCommand](P_Tessa_Extensions_Default_Client_Workplaces_WebChart_WebChartColorPickerViewModel_ClearColorCommand.htm).
Укажите действие, выполняемое при клике по кнопке очистки цвета, через
свойства [Execute](P_Tessa_UI_DelegateCommandClosure_Execute.htm) и
[CanExecute](P_Tessa_UI_DelegateCommandClosure_CanExecute.htm).  
[ClearColorVisibility](P_Tessa_Extensions_Default_Client_Workplaces_WebChart_WebChartColorPickerViewModel_ClearColorVisibility.htm)|
Видимость кнопки очистки цвета. Значение обновляется автоматически, не
рекомендуется изменять его вручную.  
[Color](P_Tessa_Extensions_Default_Client_Workplaces_WebChart_WebChartColorPickerViewModel_Color.htm)|
Выбранный цвет.  
[Focusable](P_Tessa_Extensions_Default_Client_Workplaces_WebChart_WebChartColorPickerViewModel_Focusable.htm)|  
[IsReadOnly](P_Tessa_Extensions_Default_Client_Workplaces_WebChart_WebChartColorPickerViewModel_IsReadOnly.htm)|  
[Model](P_Tessa_UI_ViewModel_1_Model.htm)|  Модель для текущей модели
представления.  
(Унаследован от [ViewModel<TModel>](T_Tessa_UI_ViewModel_1.htm))  
[ParseTextFunc](P_Tessa_Extensions_Default_Client_Workplaces_WebChart_WebChartColorPickerViewModel_ParseTextFunc.htm)|
Функция, вызываемая для получения цвета по введённому пользователем значению.
Получаемое значение не равно null или пустой строке, а оконечные пробелы уже
удалены. Если функция выбрасывает исключение, то ex.Message выводится во
всплывающей подсказке, а значение отображается в красной рамке. По умолчанию
равно null, в этом случае используется стандартный парсинг строки в формате
#AARRGGBB.  
[Scope](P_Tessa_UI_ViewModel_1_Scope.htm)|  
(Унаследован от [ViewModel<TModel>](T_Tessa_UI_ViewModel_1.htm))  
[SelectColorCommand](P_Tessa_Extensions_Default_Client_Workplaces_WebChart_WebChartColorPickerViewModel_SelectColorCommand.htm)|
Команда, выполняемая при нажатии на кнопку выбора цвета.  
[SelectColorCommandClosure](P_Tessa_Extensions_Default_Client_Workplaces_WebChart_WebChartColorPickerViewModel_SelectColorCommandClosure.htm)|
Замыкание для управления командой
[SelectColorCommand](P_Tessa_Extensions_Default_Client_Workplaces_WebChart_WebChartColorPickerViewModel_SelectColorCommand.htm).
Укажите действие, выполняемое при клике по кнопке выбора цвета, через свойства
[Execute](P_Tessa_UI_DelegateCommandClosure_Execute.htm) и
[CanExecute](P_Tessa_UI_DelegateCommandClosure_CanExecute.htm).  
[Text](P_Tessa_Extensions_Default_Client_Workplaces_WebChart_WebChartColorPickerViewModel_Text.htm)|
Текстовое представление выбранного цвета.  
[TextStyle](P_Tessa_Extensions_Default_Client_Workplaces_WebChart_WebChartColorPickerViewModel_TextStyle.htm)|
Стиль текста, который вводится пользователем или выводится для пользователя в
поле с текстовым представлением цвета.  
[UseAllSpace](P_Tessa_Extensions_Default_Client_Workplaces_WebChart_WebChartColorPickerViewModel_UseAllSpace.htm)|
Определяет, должна ли кнопка использовать все свободное пространство  
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
[IsReadOnlyInternal](F_Tessa_Extensions_Default_Client_Workplaces_WebChart_WebChartColorPickerViewModel_IsReadOnlyInternal.htm)|  
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
[Tessa.Extensions.Default.Client.Workplaces.WebChart - пространство
имён](N_Tessa_Extensions_Default_Client_Workplaces_WebChart.htm)
