# CreateMenuContextFunc - делегат
Метод, создающий контекст, предоставляющий средства для генерации меню.
## __Definition
 **Пространство имён:** [Tessa.UI.Menu](N_Tessa_UI_Menu.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public delegate IMenuContext CreateMenuContextFunc(
    	IUIContextExecutorProvider uiContextExecutorProvider
    )
VB __Копировать
     Public Delegate Function CreateMenuContextFunc ( 
    	uiContextExecutorProvider As IUIContextExecutorProvider
    ) As IMenuContext
C++ __Копировать
     public delegate IMenuContext^ CreateMenuContextFunc(
    	IUIContextExecutorProvider^ uiContextExecutorProvider
    )
F# __Копировать
     type CreateMenuContextFunc = 
        delegate of 
            uiContextExecutorProvider : IUIContextExecutorProvider -> IMenuContext
#### Параметры
uiContextExecutorProvider
[IUIContextExecutorProvider](T_Tessa_UI_IUIContextExecutorProvider.htm)
     Объект, предоставляющий доступ к методу, выполняющему заданный метод в контексте [IUIContext](T_Tessa_UI_IUIContext.htm). 
#### Возвращаемое значение
[IMenuContext](T_Tessa_UI_Menu_IMenuContext.htm)  
Контекст, предоставляющий средства для генерации меню.
##  __См. также
#### Ссылки
[Tessa.UI.Menu - пространство имён](N_Tessa_UI_Menu.htm)
