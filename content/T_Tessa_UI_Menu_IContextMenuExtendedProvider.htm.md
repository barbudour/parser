# IContextMenuExtendedProvider - интерфейс
Объект, предоставляющий контекстное меню для текущей модели представления со
всеми его зависимостями, используемыми при генерации.
## __Definition
 **Пространство имён:** [Tessa.UI.Menu](N_Tessa_UI_Menu.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IContextMenuExtendedProvider : IContextMenuProvider, 
    	IMenuActionGeneratorProvider, IUIContextExecutorProvider
VB __Копировать
     Public Interface IContextMenuExtendedProvider
    	Inherits IContextMenuProvider, IMenuActionGeneratorProvider, IUIContextExecutorProvider
C++ __Копировать
     public interface class IContextMenuExtendedProvider : IContextMenuProvider, 
    	IMenuActionGeneratorProvider, IUIContextExecutorProvider
F# __Копировать
     type IContextMenuExtendedProvider = 
        interface
            interface IContextMenuProvider
            interface IMenuActionGeneratorProvider
            interface IUIContextExecutorProvider
        end
Implements
    [IUIContextExecutorProvider](T_Tessa_UI_IUIContextExecutorProvider.htm), [IContextMenuProvider](T_Tessa_UI_Menu_IContextMenuProvider.htm), [IMenuActionGeneratorProvider](T_Tessa_UI_Menu_IMenuActionGeneratorProvider.htm)
##  __Свойства
[MenuActionGenerator](P_Tessa_UI_Menu_IMenuActionGeneratorProvider_MenuActionGenerator.htm)|
Используемый объект [Tessa.UI.Menu.IMenuActionGenerator].  
(Унаследован от
[IMenuActionGeneratorProvider](T_Tessa_UI_Menu_IMenuActionGeneratorProvider.htm))  
---|---  
[UIContextExecutorAsync](P_Tessa_UI_IUIContextExecutorProvider_UIContextExecutorAsync.htm)|
Делегат, выполняющий заданное действие в контексте [Tessa.UI.IUIContext].  
(Унаследован от
[IUIContextExecutorProvider](T_Tessa_UI_IUIContextExecutorProvider.htm))  
##  __Методы
[GetContextMenuAsync](M_Tessa_UI_Menu_IContextMenuProvider_GetContextMenuAsync.htm)|
Возвращает контекстное меню, доступное для текущей модели представления. Если
возвращается null, пустая коллекция или коллекция из скрытых элементов, то
меню при этом не отображается.  
(Унаследован от
[IContextMenuProvider](T_Tessa_UI_Menu_IContextMenuProvider.htm))  
---|---  
##  __См. также
#### Ссылки
[Tessa.UI.Menu - пространство имён](N_Tessa_UI_Menu.htm)
