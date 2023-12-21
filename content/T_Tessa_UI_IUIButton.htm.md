# IUIButton - интерфейс
Модель представления для кнопки диалогового окна
[UIDialog](T_Tessa_UI_UIDialog.htm).
## __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IUIButton : INotifyPropertyChanged
VB __Копировать
     Public Interface IUIButton
    	Inherits INotifyPropertyChanged
C++ __Копировать
     public interface class IUIButton : INotifyPropertyChanged
F# __Копировать
     type IUIButton = 
        interface
            interface INotifyPropertyChanged
        end
Implements
    [INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged)
##  __Свойства
[Caption](P_Tessa_UI_IUIButton_Caption.htm)| Заголовок кнопки.  
---|---  
[Command](P_Tessa_UI_IUIButton_Command.htm)|  Команда, выполняемая при нажатии
на кнопку. Можно изменить значение свойства, но нельзя установить его равным
null.  
[IsCancel](P_Tessa_UI_IUIButton_IsCancel.htm)|  Признак того, что кнопка
реагирует на нажатие Esc, если другой элемент управления не перехватывает
обработку этой кнопки.  
[IsDefault](P_Tessa_UI_IUIButton_IsDefault.htm)|  Признак того, что кнопка
реагирует на нажатие Enter, если другой элемент управления не перехватывает
обработку этой кнопки.  
[Visibility](P_Tessa_UI_IUIButton_Visibility.htm)| Видимость кнопки. Установив
значение свойства, можно скрыть кнопку, не удаляя её из коллекции кнопок.  
##  __Методы
[CloseAsync](M_Tessa_UI_IUIButton_CloseAsync.htm)| Закрывает окно, на котором
размещается кнопка. Метод необходимо вызывать в потоке UI.  
---|---  
##  __События
[CloseRequested](E_Tessa_UI_IUIButton_CloseRequested.htm)| Кнопка запросила
закрытие диалогового окна.  
---|---  
[PropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged.propertychanged)|
Occurs when a property value changes.  
(Унаследован от
[INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged))  
##  __См. также
#### Ссылки
[Tessa.UI - пространство имён](N_Tessa_UI.htm)
