# Tessa.UI.Menu - пространство имён
API для динамического построения меню, в т.ч. контекстных меню.
##  __Классы
[MenuAction](T_Tessa_UI_Menu_MenuAction.htm)|  Действие, используемое в меню.  
---|---  
[MenuActionCollection](T_Tessa_UI_Menu_MenuActionCollection.htm)|  Коллекция
действий [IMenuAction](T_Tessa_UI_Menu_IMenuAction.htm).  
[MenuActionFontWeightConverter](T_Tessa_UI_Menu_MenuActionFontWeightConverter.htm)|
Конвертер, преобразующий толщину шрифта
[MenuActionFontWeight](T_Tessa_UI_Menu_MenuActionFontWeight.htm) в стандартный
тип
[FontWeight](https://learn.microsoft.com/dotnet/api/system.windows.fontweight).
Поддерживается двустороннее преобразование.  
[MenuActionGenerator](T_Tessa_UI_Menu_MenuActionGenerator.htm)|  Создаёт
элементы меню
[MenuItem](https://learn.microsoft.com/dotnet/api/system.windows.controls.menuitem)
для отображения действий [IMenuAction](T_Tessa_UI_Menu_IMenuAction.htm).
Созданные элементы можно использовать в том числе в контекстном меню.  
[MenuContext](T_Tessa_UI_Menu_MenuContext.htm)|  Контекст, предоставляющий
средства для генерации меню, например, посредством интерфейса
[IContextMenuProvider](T_Tessa_UI_Menu_IContextMenuProvider.htm).  
[MenuExtensions](T_Tessa_UI_Menu_MenuExtensions.htm)|  Методы-расширения для
пространства имён Tessa.UI.Menu.  
[MenuManager](T_Tessa_UI_Menu_MenuManager.htm)|  Объект, управляющий жизненным
циклом меню.  
[MenuSeparatorAction](T_Tessa_UI_Menu_MenuSeparatorAction.htm)|  Действие
[IMenuAction](T_Tessa_UI_Menu_IMenuAction.htm), разделяющее другие действия
между собой. Такое действие не содержит бизнес-логики и действительной
информации по внешнему виду. Все свойства, которые должны были бы влиять на
внешний вид, кроме [IsCollapsed](P_Tessa_UI_Menu_IMenuAction_IsCollapsed.htm)
могут изменяться, но в действительности не влияют на отображение.  
## __Интерфейсы
[IContextMenuExtendedProvider](T_Tessa_UI_Menu_IContextMenuExtendedProvider.htm)|
Объект, предоставляющий контекстное меню для текущей модели представления со
всеми его зависимостями, используемыми при генерации.  
---|---  
[IContextMenuProvider](T_Tessa_UI_Menu_IContextMenuProvider.htm)|  Объект,
предоставляющий контекстное меню для текущей модели представления.  
[IMenuAction](T_Tessa_UI_Menu_IMenuAction.htm)|  Действие, используемое в
меню.  
[IMenuActionCollection](T_Tessa_UI_Menu_IMenuActionCollection.htm)|  Коллекция
действий [IMenuAction](T_Tessa_UI_Menu_IMenuAction.htm).  
[IMenuActionCollectionVisual](T_Tessa_UI_Menu_IMenuActionCollectionVisual.htm)|
Коллекция визуальных объектов, которая была сгенерирована посредством
[IMenuActionGenerator](T_Tessa_UI_Menu_IMenuActionGenerator.htm). При выходе
из визуального дерева следует вызывать метод
[Dispose()](https://learn.microsoft.com/dotnet/api/system.idisposable.dispose#system-
idisposable-dispose) для исправления утечек памяти.  
[IMenuActionGenerator](T_Tessa_UI_Menu_IMenuActionGenerator.htm)|  Создаёт
элементы UI для отображения действий
[IMenuAction](T_Tessa_UI_Menu_IMenuAction.htm).  
[IMenuActionGeneratorProvider](T_Tessa_UI_Menu_IMenuActionGeneratorProvider.htm)|
Объект, предоставляющий доступ к объекту
[IMenuActionGenerator](T_Tessa_UI_Menu_IMenuActionGenerator.htm).
## __Заметки
Если модель представления реализует этот интерфейс совместно с
[IContextMenuProvider](T_Tessa_UI_Menu_IContextMenuProvider.htm), то она может
предоставить объект
[IMenuActionGenerator](T_Tessa_UI_Menu_IMenuActionGenerator.htm), отличный от
объекта по умолчанию Default.  
[IMenuActionVisual](T_Tessa_UI_Menu_IMenuActionVisual.htm)|  Визуальный
объект, который был сгенерирован посредством
[IMenuActionGenerator](T_Tessa_UI_Menu_IMenuActionGenerator.htm). При выходе
из визуального дерева следует вызывать метод
[Dispose()](https://learn.microsoft.com/dotnet/api/system.idisposable.dispose#system-
idisposable-dispose) для исправления утечек памяти.  
[IMenuContext](T_Tessa_UI_Menu_IMenuContext.htm)|  Контекст, предоставляющий
средства для генерации меню, например, посредством интерфейса
[IContextMenuProvider](T_Tessa_UI_Menu_IContextMenuProvider.htm).  
## __Делегаты
[CreateMenuContextFunc](T_Tessa_UI_Menu_CreateMenuContextFunc.htm)|  Метод,
создающий контекст, предоставляющий средства для генерации меню.  
---|---  
## __Перечисления
[MenuActionFontWeight](T_Tessa_UI_Menu_MenuActionFontWeight.htm)|  Толщина
шрифта, используемая при выводе заголовков действий
[IMenuAction](T_Tessa_UI_Menu_IMenuAction.htm).  
---|---
