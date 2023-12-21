# TessaDialogDispatcher - перечисление
Указание диспетчера, для которого показывается диалоговое окно.
## __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public enum TessaDialogDispatcher
VB __Копировать
     Public Enumeration TessaDialogDispatcher
C++ __Копировать
     public enum class TessaDialogDispatcher
F# __Копировать
     type TessaDialogDispatcher
##  __Члены
Application| 0|  Для вывода диалоговых окон используется диспетчер приложения.
Если текущий поток отличен от потока UI приложения, то он ожидает завершения
показа диалога.  
---|---|---  
Current| 1|  Для вывода диалоговых окон используется текущий диспетчер. При
этом диспетчер приложения не блокируется до закрытия диалога.  
## __См. также
#### Ссылки
[Tessa.UI - пространство имён](N_Tessa_UI.htm)
