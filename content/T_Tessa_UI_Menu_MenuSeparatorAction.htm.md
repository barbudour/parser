# MenuSeparatorAction - класс
Действие [IMenuAction](T_Tessa_UI_Menu_IMenuAction.htm), разделяющее другие
действия между собой. Такое действие не содержит бизнес-логики и
действительной информации по внешнему виду. Все свойства, которые должны были
бы влиять на внешний вид, кроме
[IsCollapsed](P_Tessa_UI_Menu_IMenuAction_IsCollapsed.htm) могут изменяться,
но в действительности не влияют на отображение.
## __Definition
 **Пространство имён:** [Tessa.UI.Menu](N_Tessa_UI_Menu.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class MenuSeparatorAction : SelectableViewModel<EmptyModel>, 
    	IMenuAction, ICloneable, INamedItem, INotifyPropertyChanged
VB __Копировать
     Public NotInheritable Class MenuSeparatorAction
    	Inherits SelectableViewModel(Of EmptyModel)
    	Implements IMenuAction, ICloneable, INamedItem, INotifyPropertyChanged
C++ __Копировать
     public ref class MenuSeparatorAction sealed : public SelectableViewModel<EmptyModel^>, 
    	IMenuAction, ICloneable, INamedItem, INotifyPropertyChanged
F# __Копировать
     [<SealedAttribute>]
    type MenuSeparatorAction = 
        class
            inherit SelectableViewModel<EmptyModel>
            interface IMenuAction
            interface ICloneable
            interface INamedItem
            interface INotifyPropertyChanged
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[NotificationObject](T_Tessa_Platform_NotificationObject.htm) __[NotificationUIObject](T_Tessa_UI_NotificationUIObject.htm) __[ViewModel](T_Tessa_UI_ViewModel_1.htm)<[EmptyModel](T_Tessa_UI_EmptyModel.htm)> __[SelectableViewModel](T_Tessa_UI_SelectableViewModel_1.htm)<[EmptyModel](T_Tessa_UI_EmptyModel.htm)> __ MenuSeparatorAction
Implements
    [INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged), [ICloneable](https://learn.microsoft.com/dotnet/api/system.icloneable), [INamedItem](T_Tessa_Platform_Collections_INamedItem.htm), [IMenuAction](T_Tessa_UI_Menu_IMenuAction.htm)
##  __Конструкторы
[MenuSeparatorAction](M_Tessa_UI_Menu_MenuSeparatorAction__ctor.htm)|  Создаёт
экземпляр класса с указанием значений его свойств.  
---|---  
## __Свойства
[Caption](P_Tessa_UI_Menu_MenuSeparatorAction_Caption.htm)| Заголовок
действия, отображаемый пользователю.  
---|---  
[CaptionFontWeight](P_Tessa_UI_Menu_MenuSeparatorAction_CaptionFontWeight.htm)|
Толщина шрифта, используемая при выводе заголовка
[Tessa.UI.Menu.IMenuAction.Caption].  
[Children](P_Tessa_UI_Menu_MenuSeparatorAction_Children.htm)| Дочерние
действия.  
[Command](P_Tessa_UI_Menu_MenuSeparatorAction_Command.htm)| Команда по
действию.  
[CommandClosure](P_Tessa_UI_Menu_MenuSeparatorAction_CommandClosure.htm)|
Замыкание для команды [Tessa.UI.Menu.IMenuAction.CommandClosure]. Через
свойства этого объекта можно заменить методы Execute и CanExecute для команды.  
[Icon](P_Tessa_UI_Menu_MenuSeparatorAction_Icon.htm)| Заголовок действия,
отображаемый пользователю.  
[Info](P_Tessa_UI_Menu_MenuSeparatorAction_Info.htm)| Информация для
расширений.  
[InputGestureText](P_Tessa_UI_Menu_MenuSeparatorAction_InputGestureText.htm)|
Текст с указанием горячей клавиши, при нажатии которой будет выполнена
команда, привязанная к пункту меню. Указание текста не связывает пункт меню с
командой, а лишь служит визуальной индикацией.  
[IsCollapsed](P_Tessa_UI_Menu_MenuSeparatorAction_IsCollapsed.htm)|  Признак
того, что действие скрыто от пользователя. По умолчанию значение false.  
[IsEnabled](P_Tessa_UI_Menu_MenuSeparatorAction_IsEnabled.htm)|  Признак того,
что действие доступно. По умолчанию значение true.  
[IsSelectable](P_Tessa_UI_SelectableViewModel_1_IsSelectable.htm)|  
(Унаследован от
[SelectableViewModel<TModel>](T_Tessa_UI_SelectableViewModel_1.htm))  
[IsSelected](P_Tessa_UI_SelectableViewModel_1_IsSelected.htm)|  
(Унаследован от
[SelectableViewModel<TModel>](T_Tessa_UI_SelectableViewModel_1.htm))  
[Model](P_Tessa_UI_ViewModel_1_Model.htm)|  Модель для текущей модели
представления.  
(Унаследован от [ViewModel<TModel>](T_Tessa_UI_ViewModel_1.htm))  
[Name](P_Tessa_UI_Menu_MenuSeparatorAction_Name.htm)| Имя объекта, по которому
объект можно идентифицировать в коллекциях.  
[Scope](P_Tessa_UI_ViewModel_1_Scope.htm)|  
(Унаследован от [ViewModel<TModel>](T_Tessa_UI_ViewModel_1.htm))  
[Tooltip](P_Tessa_UI_Menu_MenuSeparatorAction_Tooltip.htm)| Подсказка элемента
меню.  
##  __Методы
[Clone](M_Tessa_UI_Menu_MenuSeparatorAction_Clone.htm)| Создаёт полную копию
действия и его дочерних действий.  
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
[OnIsSelectableChanged](M_Tessa_UI_SelectableViewModel_1_OnIsSelectableChanged.htm)|  
(Унаследован от
[SelectableViewModel<TModel>](T_Tessa_UI_SelectableViewModel_1.htm))  
[OnIsSelectedChanged](M_Tessa_UI_SelectableViewModel_1_OnIsSelectedChanged.htm)|  
(Унаследован от
[SelectableViewModel<TModel>](T_Tessa_UI_SelectableViewModel_1.htm))  
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
##  __Методы расширения
[ExecuteAsync](M_Tessa_UI_Menu_MenuExtensions_ExecuteAsync.htm)|  Выполняет
действие, если оно доступно.  
(Определяется [MenuExtensions](T_Tessa_UI_Menu_MenuExtensions.htm))  
---|---  
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
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
[Tessa.UI.Menu - пространство имён](N_Tessa_UI_Menu.htm)
