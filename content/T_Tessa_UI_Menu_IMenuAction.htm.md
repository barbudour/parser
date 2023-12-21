# IMenuAction - интерфейс
Действие, используемое в меню.
## __Definition
 **Пространство имён:** [Tessa.UI.Menu](N_Tessa_UI_Menu.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IMenuAction : ICloneable, 
    	INamedItem, INotifyPropertyChanged
VB __Копировать
     Public Interface IMenuAction
    	Inherits ICloneable, INamedItem, INotifyPropertyChanged
C++ __Копировать
     public interface class IMenuAction : ICloneable, 
    	INamedItem, INotifyPropertyChanged
F# __Копировать
     type IMenuAction = 
        interface
            interface ICloneable
            interface INamedItem
            interface INotifyPropertyChanged
        end
Implements
    [INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged), [ICloneable](https://learn.microsoft.com/dotnet/api/system.icloneable), [INamedItem](T_Tessa_Platform_Collections_INamedItem.htm)
##  __Свойства
[Caption](P_Tessa_UI_Menu_IMenuAction_Caption.htm)| Заголовок действия,
отображаемый пользователю.  
---|---  
[CaptionFontWeight](P_Tessa_UI_Menu_IMenuAction_CaptionFontWeight.htm)|
Толщина шрифта, используемая при выводе заголовка
[Tessa.UI.Menu.IMenuAction.Caption].  
[Children](P_Tessa_UI_Menu_IMenuAction_Children.htm)| Дочерние действия.  
[Command](P_Tessa_UI_Menu_IMenuAction_Command.htm)| Команда по действию.  
[CommandClosure](P_Tessa_UI_Menu_IMenuAction_CommandClosure.htm)|  Замыкание
для команды [Tessa.UI.Menu.IMenuAction.CommandClosure]. Через свойства этого
объекта можно заменить методы Execute и CanExecute для команды.  
[Icon](P_Tessa_UI_Menu_IMenuAction_Icon.htm)| Иконка для действия.  
[Info](P_Tessa_UI_Menu_IMenuAction_Info.htm)| Информация для расширений.  
[InputGestureText](P_Tessa_UI_Menu_IMenuAction_InputGestureText.htm)|  Текст с
указанием горячей клавиши, при нажатии которой будет выполнена команда,
привязанная к пункту меню. Указание текста не связывает пункт меню с командой,
а лишь служит визуальной индикацией.  
[IsCollapsed](P_Tessa_UI_Menu_IMenuAction_IsCollapsed.htm)|  Признак того, что
действие скрыто от пользователя. По умолчанию значение false.  
[IsEnabled](P_Tessa_UI_Menu_IMenuAction_IsEnabled.htm)|  Признак того, что
действие доступно. По умолчанию значение true.  
[IsSelectable](P_Tessa_UI_Menu_IMenuAction_IsSelectable.htm)|  Признак того,
что действие может быть отмечено пользователем при выборе действия или
программно.  
[IsSelected](P_Tessa_UI_Menu_IMenuAction_IsSelected.htm)| Признак того, что
действие было отмечено.  
[Name](P_Tessa_Platform_Collections_INamedItem_Name.htm)| Имя объекта, по
которому объект можно идентифицировать в коллекциях.  
(Унаследован от [INamedItem](T_Tessa_Platform_Collections_INamedItem.htm))  
[Tooltip](P_Tessa_UI_Menu_IMenuAction_Tooltip.htm)| Подсказка элемента меню.  
##  __Методы
[Clone](M_Tessa_UI_Menu_IMenuAction_Clone.htm)| Создаёт полную копию действия
и его дочерних действий.  
---|---  
##  __События
[PropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged.propertychanged)|
Occurs when a property value changes.  
(Унаследован от
[INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged))  
---|---  
##  __Методы расширения
[ExecuteAsync](M_Tessa_UI_Menu_MenuExtensions_ExecuteAsync.htm)|  Выполняет
действие, если оно доступно.  
(Определяется [MenuExtensions](T_Tessa_UI_Menu_MenuExtensions.htm))  
---|---  
##  __См. также
#### Ссылки
[Tessa.UI.Menu - пространство имён](N_Tessa_UI_Menu.htm)
