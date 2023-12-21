# SelectFromViewDelegate - делегат
Делегат выборки из контекста представления
## __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public delegate void SelectFromViewDelegate(
    	[NotNullAttribute] ISelectFromViewContext context
    )
VB __Копировать
     Public Delegate Sub SelectFromViewDelegate ( 
    	<NotNullAttribute> context As ISelectFromViewContext
    )
C++ __Копировать
     public delegate void SelectFromViewDelegate(
    	[NotNullAttribute] ISelectFromViewContext^ context
    )
F# __Копировать
     type SelectFromViewDelegate = 
        delegate of 
            [<NotNullAttribute>] context : ISelectFromViewContext -> unit
#### Параметры
context [ISelectFromViewContext](T_Tessa_UI_ISelectFromViewContext.htm)
    Контекст выборки значений из представления
##  __См. также
#### Ссылки
[Tessa.UI - пространство имён](N_Tessa_UI.htm)
