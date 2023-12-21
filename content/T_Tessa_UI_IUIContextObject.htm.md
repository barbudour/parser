# IUIContextObject - интерфейс
Объект, содержащий информацию об именованном объекте с контекстом
[IUIContext](T_Tessa_UI_IUIContext.htm). Например, может соответствовать
вкладке с карточкой.
## __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IUIContextObject : IUIContextMarker
VB __Копировать
     Public Interface IUIContextObject
    	Inherits IUIContextMarker
C++ __Копировать
     public interface class IUIContextObject : IUIContextMarker
F# __Копировать
     type IUIContextObject = 
        interface
            interface IUIContextMarker
        end
Implements
    [IUIContextMarker](T_Tessa_UI_IUIContextMarker.htm)
##  __Заметки
Объект может содержать прямые ссылки на объекты WPF, поэтому длительное
удержание ссылки на этот объект может привести к утечке памяти.
## __Свойства
[Context](P_Tessa_UI_IUIContextMarker_Context.htm)| Контекст, связанный с
текущим объектом.  
(Унаследован от [IUIContextMarker](T_Tessa_UI_IUIContextMarker.htm))  
---|---  
[ObjectInfo](P_Tessa_UI_IUIContextObject_ObjectInfo.htm)|  Дополнительная
информация по объекту.  
[ObjectInfoToolTip](P_Tessa_UI_IUIContextObject_ObjectInfoToolTip.htm)|
Всплывающая подсказка для
[ObjectInfo](P_Tessa_UI_IUIContextObject_ObjectInfo.htm).  
[ObjectName](P_Tessa_UI_IUIContextObject_ObjectName.htm)|  Имя объекта.  
[ObjectNameToolTip](P_Tessa_UI_IUIContextObject_ObjectNameToolTip.htm)|
Всплывающая подсказка для
[ObjectName](P_Tessa_UI_IUIContextObject_ObjectName.htm).  
## __См. также
#### Ссылки
[Tessa.UI - пространство имён](N_Tessa_UI.htm)
