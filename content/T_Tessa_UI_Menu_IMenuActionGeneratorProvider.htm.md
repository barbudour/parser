# IMenuActionGeneratorProvider - интерфейс
Объект, предоставляющий доступ к объекту
[IMenuActionGenerator](T_Tessa_UI_Menu_IMenuActionGenerator.htm).
## __Заметки
Если модель представления реализует этот интерфейс совместно с
[IContextMenuProvider](T_Tessa_UI_Menu_IContextMenuProvider.htm), то она может
предоставить объект
[IMenuActionGenerator](T_Tessa_UI_Menu_IMenuActionGenerator.htm), отличный от
объекта по умолчанию Default.
## __Definition
 **Пространство имён:** [Tessa.UI.Menu](N_Tessa_UI_Menu.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IMenuActionGeneratorProvider
VB __Копировать
     Public Interface IMenuActionGeneratorProvider
C++ __Копировать
     public interface class IMenuActionGeneratorProvider
F# __Копировать
     type IMenuActionGeneratorProvider = interface end
##  __Свойства
[MenuActionGenerator](P_Tessa_UI_Menu_IMenuActionGeneratorProvider_MenuActionGenerator.htm)|
Используемый объект [Tessa.UI.Menu.IMenuActionGenerator].  
---|---  
## __См. также
#### Ссылки
[Tessa.UI.Menu - пространство имён](N_Tessa_UI_Menu.htm)
