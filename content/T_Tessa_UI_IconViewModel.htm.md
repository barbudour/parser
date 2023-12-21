# IconViewModel - класс
Модель представления для иконки. Может использоваться, например, в тэге
[IFileTagViewModel](T_Tessa_UI_Files_IFileTagViewModel.htm).
## __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class IconViewModel : NotificationUIObject
VB __Копировать
     Public NotInheritable Class IconViewModel
    	Inherits NotificationUIObject
C++ __Копировать
     public ref class IconViewModel sealed : public NotificationUIObject
F# __Копировать
     [<SealedAttribute>]
    type IconViewModel = 
        class
            inherit NotificationUIObject
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[NotificationObject](T_Tessa_Platform_NotificationObject.htm) __[NotificationUIObject](T_Tessa_UI_NotificationUIObject.htm) __ IconViewModel
##  __Конструкторы
[IconViewModel](M_Tessa_UI_IconViewModel__ctor.htm)|  Создаёт экземпляр класса
с указанием значений его свойств.  
---|---  
## __Свойства
[Foreground](P_Tessa_UI_IconViewModel_Foreground.htm)|  Цвет выводимой иконки.
Не должен быть равен null.  
---|---  
[Height](P_Tessa_UI_IconViewModel_Height.htm)|  Ширина иконки. По умолчанию
значение [DefaultHeight](F_Tessa_UI_IconViewModel_DefaultHeight.htm) равное
14.  
[Hover](P_Tessa_UI_IconViewModel_Hover.htm)|  Цвет выводимой иконки при
наведении. Действует только для иконок, отображаемых в тулбаре карточки, во
всех остальных случаях игнорирется.  
[IconContainer](P_Tessa_UI_IconViewModel_IconContainer.htm)|  Контейнер,
предоставляющий доступ к иконкам.  
[Key](P_Tessa_UI_IconViewModel_Key.htm)|  Алиас иконки, например: Thin1
Укажите null, чтобы не выводить геометрию для иконки.  
[Margin](P_Tessa_UI_IconViewModel_Margin.htm)|  Толщина линии при отрисовке
иконки.  
[Stretch](P_Tessa_UI_IconViewModel_Stretch.htm)|  Описывает, как иконка
размещается на доступном пространстве (растяжение по горизонтали и вертикали).
По умолчанию значение
[Uniform](https://learn.microsoft.com/dotnet/api/system.windows.media.stretch).  
[Thickness](P_Tessa_UI_IconViewModel_Thickness.htm)|  Толщина линии при
отрисовке иконки. Должна быть неотрицательным числом.  
[Width](P_Tessa_UI_IconViewModel_Width.htm)|  Ширина иконки. По умолчанию
значение [DefaultWidth](F_Tessa_UI_IconViewModel_DefaultWidth.htm) равное Auto
(double.NaN).  
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
[DefaultHeight](F_Tessa_UI_IconViewModel_DefaultHeight.htm)|  Значение
свойства [Height](P_Tessa_UI_IconViewModel_Height.htm) по умолчанию.  
---|---  
[DefaultWidth](F_Tessa_UI_IconViewModel_DefaultWidth.htm)|  Значение свойства
[Width](P_Tessa_UI_IconViewModel_Width.htm) по умолчанию.  
[ForegroundProperty](F_Tessa_UI_IconViewModel_ForegroundProperty.htm)|  Имя
свойства [Foreground](P_Tessa_UI_IconViewModel_Foreground.htm).  
[HeightProperty](F_Tessa_UI_IconViewModel_HeightProperty.htm)|  Имя свойства
[Height](P_Tessa_UI_IconViewModel_Height.htm).  
[HoverProperty](F_Tessa_UI_IconViewModel_HoverProperty.htm)|  Имя свойства
[Hover](P_Tessa_UI_IconViewModel_Hover.htm).  
[KeyProperty](F_Tessa_UI_IconViewModel_KeyProperty.htm)|  Имя свойства
[Key](P_Tessa_UI_IconViewModel_Key.htm).  
[MarginProperty](F_Tessa_UI_IconViewModel_MarginProperty.htm)|  Имя свойства
[Margin](P_Tessa_UI_IconViewModel_Margin.htm).  
[StretchProperty](F_Tessa_UI_IconViewModel_StretchProperty.htm)|  Имя свойства
[Stretch](P_Tessa_UI_IconViewModel_Stretch.htm).  
[ThicknessProperty](F_Tessa_UI_IconViewModel_ThicknessProperty.htm)|  Имя
свойства [Thickness](P_Tessa_UI_IconViewModel_Thickness.htm).  
[WidthProperty](F_Tessa_UI_IconViewModel_WidthProperty.htm)|  Имя свойства
[Width](P_Tessa_UI_IconViewModel_Width.htm).  
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
