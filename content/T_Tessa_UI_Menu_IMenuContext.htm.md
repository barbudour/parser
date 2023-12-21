# IMenuContext - интерфейс
Контекст, предоставляющий средства для генерации меню, например, посредством
интерфейса [IContextMenuProvider](T_Tessa_UI_Menu_IContextMenuProvider.htm).
## __Definition
 **Пространство имён:** [Tessa.UI.Menu](N_Tessa_UI_Menu.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IMenuContext : IMenuActionGeneratorProvider, 
    	IUIContextExecutorProvider
VB __Копировать
     Public Interface IMenuContext
    	Inherits IMenuActionGeneratorProvider, IUIContextExecutorProvider
C++ __Копировать
     public interface class IMenuContext : IMenuActionGeneratorProvider, 
    	IUIContextExecutorProvider
F# __Копировать
     type IMenuContext = 
        interface
            interface IMenuActionGeneratorProvider
            interface IUIContextExecutorProvider
        end
Implements
    [IUIContextExecutorProvider](T_Tessa_UI_IUIContextExecutorProvider.htm), [IMenuActionGeneratorProvider](T_Tessa_UI_Menu_IMenuActionGeneratorProvider.htm)
##  __Свойства
[Icons](P_Tessa_UI_Menu_IMenuContext_Icons.htm)|  Возвращает контекстное меню,
доступное для текущей модели представления. Если возвращается null, пустая
коллекция или коллекция из скрытых элементов, то меню при этом не
отображается.  
---|---  
[MenuActionGenerator](P_Tessa_UI_Menu_IMenuActionGeneratorProvider_MenuActionGenerator.htm)|
Используемый объект [Tessa.UI.Menu.IMenuActionGenerator].  
(Унаследован от
[IMenuActionGeneratorProvider](T_Tessa_UI_Menu_IMenuActionGeneratorProvider.htm))  
[UIContextExecutorAsync](P_Tessa_UI_IUIContextExecutorProvider_UIContextExecutorAsync.htm)|
Делегат, выполняющий заданное действие в контексте [Tessa.UI.IUIContext].  
(Унаследован от
[IUIContextExecutorProvider](T_Tessa_UI_IUIContextExecutorProvider.htm))  
##  __См. также
#### Ссылки
[Tessa.UI.Menu - пространство имён](N_Tessa_UI_Menu.htm)
